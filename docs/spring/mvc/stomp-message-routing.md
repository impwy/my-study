# Spring STOMP 메시지 라우팅과 SimpleBroker

> 연결 주소·업무 목적지·구독 목적지를 구분하고, Spring의 설정이 메시지를 처리기와 브로커로 나누는 과정을 추적한다.

- **역할:** spring-websocket은 연결·전송을, spring-messaging은 메시지·채널·메시징 처리를 지원한다.
- **라우팅:** `/pub`은 설정한 업무 접두사이고 `/user`는 변경 가능한 Spring 사용자별 목적지 기본 접두사다.
- **브로커:** SimpleBroker는 현재 서버의 구독 상태를 메모리에 관리하며 영속적인 채팅 기록 저장소는 아니다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

`@EnableWebSocketMessageBroker`를 사용하면 STOMP 메시지를 업무 처리기 또는 브로커로 전달하는 구성이 만들어진다. `@MessageMapping`은 들어오는 업무 메시지를 처리하고, `SimpMessagingTemplate`은 서버 코드에서 메시지를 발행한다.

수신은 `clientInboundChannel`, 서버 코드의 브로커 발행은 `brokerChannel`, 클라이언트 송신은 `clientOutboundChannel`을 거친다. 이 채널들은 애플리케이션 내부 전달 경로다.

## 설정 예제

spring-websocket·spring-messaging을 사용하는 Servlet 기반 Spring 설정 클래스의 메서드 일부다. 클래스에는 `@Configuration`·`@EnableWebSocketMessageBroker`와 `WebSocketMessageBrokerConfigurer` 구현이 필요하다. 업무 처리기·인증·저장 로직은 별도이며 실행 결과를 검증한 완성 애플리케이션은 아니다.

```java
@Override
public void registerStompEndpoints(StompEndpointRegistry registry) {
    registry.addEndpoint("/ws");
}

@Override
public void configureMessageBroker(MessageBrokerRegistry registry) {
    registry.setApplicationDestinationPrefixes("/pub");
    registry.enableSimpleBroker("/queue", "/topic");
    registry.setUserDestinationPrefix("/user");
}
```

| 주소 예시 | 의미 |
| --- | --- |
| `wss://서버/ws` | 연결을 여는 WebSocket 엔드포인트 |
| `/pub/rooms/42/messages` | SEND 프레임에 넣는 업무 목적지 |
| `/user/queue/messages` | 사용자별 메시지를 받는 구독 목적지 |
| `/topic/rooms/42` | 방별 구독에 사용할 수 있는 브로커 목적지 |

`/pub/rooms/42/messages`는 `/pub`을 제거한 뒤 `@MessageMapping("/rooms/{roomId}/messages")`에 매핑된다. 프론트는 열린 연결 안에서 이 목적지를 지정한다. 목적지마다 새 HTTP 요청을 보내는 구조가 아니다.

`convertAndSendToUser(principalName, "/queue/messages", payload)`는 사용자별 전송이다. 클라이언트는 `/user/queue/messages`를 구독하며 Spring이 세션별 목적지로 변환한다. 해당 목적지를 구독한 같은 사용자의 여러 세션이 기본 수신 대상이 될 수 있다. 회원 ID를 이름으로 쓰려면 인증된 `Principal.getName()`도 그 값과 대응해야 한다.

## 주의점

`/pub`은 개발자가 정한 이름이고 `/user`도 설정으로 바꿀 수 있다. SimpleBroker에서 `/queue`와 `/topic`은 등록한 접두사일 뿐, 이름에 따라 작업 분산·영속 큐 기능이 생기지는 않는다. 둘 다 일치하는 구독자에게 전달한다.

SimpleBroker는 ACK·RECEIPT를 지원하지 않고 서버 간 구독 상태를 공유하지 않는다. 단체방도 한 서버 안에서는 구현할 수 있으며, 1:1 채팅도 여러 서버에 연결이 나뉘면 서버 사이 전달이 필요하다.

DB의 참여 권한과 브로커의 구독 상태는 다르다. SEND·SUBSCRIBE 권한을 검증하고 퇴장 후 수신도 막아야 한다. 외부 브로커 연동은 [채팅 브로커 선택](../../ddia/processing/chat-message-brokers.md)에서 이어진다.

## 꼬리질문

1. `/ws`, `/pub`, `/user/queue`는 각각 어느 단계에서 사용되는가?
2. `/pub`을 `/app`으로 바꾸면 프론트 목적지와 `@MessageMapping` 중 무엇을 함께 확인해야 하는가?
3. 사용자가 방을 나갔는데 구독이 남아 있다면 방별 전달과 회원별 전달은 각각 어떤 검증이 필요한가?

</details>

## 참고 자료

- [Spring · Flow of Messages](https://docs.spring.io/spring-framework/reference/web/websocket/stomp/message-flow.html) — 모듈·채널·컨트롤러·브로커 사이의 전달 경로를 확인한다.
- [Spring · User Destinations](https://docs.spring.io/spring-framework/reference/web/websocket/stomp/user-destination.html) — 사용자 이름과 세션별 목적지 변환을 확인한다.
- [Spring · External Broker](https://docs.spring.io/spring-framework/reference/web/websocket/stomp/handle-broker-relay.html) — SimpleBroker의 한계와 STOMP 릴레이의 차이를 읽는다.
