# WebSocket과 STOMP의 역할

> WebSocket은 양방향 연결과 전송을, STOMP는 그 위에서 사용하는 명령·구독·목적지를 정의한다.

- **연결:** WebSocket 연결 하나로 클라이언트와 서버가 양방향 메시지를 주고받는다.
- **메시징:** STOMP의 SEND·SUBSCRIBE·MESSAGE로 전송과 수신 규칙을 표현한다.
- **경계:** 두 프로토콜만으로 채팅 기록 저장·오프라인 복구·읽음 처리가 완성되지는 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

WebSocket은 연결을 유지하며 텍스트·바이너리 메시지를 교환한다. HTTP/1.1 환경에서는 HTTP Upgrade 핸드셰이크로 시작하며, `wss://`는 TLS로 보호되는 연결이다. WebSocket 자체가 채팅방·참여 권한·DB 저장을 정의하지는 않는다.

STOMP는 WebSocket 위에서 사용할 수 있는 메시징 프로토콜이다. 명령, 헤더, 본문으로 구성된 프레임을 사용한다. STOMP 없이 WebSocket에 JSON을 보내는 설계도 가능하지만 메시지 종류와 라우팅 규칙을 직접 정해야 한다. STOMP는 WebSocket 전용이 아니며 TCP 위에서도 사용할 수 있다.

## 프레임 예제

STOMP 1.2의 형태를 보여 주는 예시다. `<NUL>`은 실제 전송 시 프레임 끝을 나타내는 널 바이트다.

```text
SUBSCRIBE
id:chat-subscription
destination:/user/queue/messages

<NUL>

SEND
destination:/pub/rooms/42/messages
content-type:application/json

{"content":"안녕하세요"}
<NUL>
```

| 명령 | 역할 |
| --- | --- |
| CONNECT / CONNECTED | STOMP 연결 협상 |
| SEND | 목적지로 메시지 전송 |
| SUBSCRIBE / UNSUBSCRIBE | 구독 시작·해제 |
| MESSAGE | 구독한 클라이언트에 메시지 전달 |
| ACK / NACK | 수신 메시지의 처리 확인·부정 확인 |
| RECEIPT | 요청한 프레임의 서버 처리 확인 |

## 주의점

STOMP는 `destination` 헤더를 정의하지만 목적지 문자열의 문법·의미는 서버에 맡긴다. `/topic`과 `/queue`는 모든 STOMP 서버가 동일하게 처리해야 하는 표준 키워드가 아니다.

프로토콜이 ACK를 정의해도 사용 중인 브로커가 지원하는지 확인해야 한다. RECEIPT나 TCP 전달 성공은 DB 커밋·상대방의 읽음을 자동으로 증명하지 않는다. Spring에서의 실제 라우팅은 [Spring STOMP 메시지 라우팅](../../spring/mvc/stomp-message-routing.md)을 참고한다.

## 꼬리질문

1. WebSocket이 연결과 전송을 제공하는데도 STOMP 같은 메시징 규칙을 추가하는 이유는 무엇인가?
2. `/ws`에 연결한 클라이언트가 `/pub/rooms/42/messages`로 보낼 때 새 HTTP 연결이 필요한가?
3. 연결이 끊긴 동안의 메시지와 읽음 상태를 복구하려면 프로토콜 밖에서 무엇을 설계해야 하는가?

</details>

## 참고 자료

- [RFC 6455 · The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455) — 핸드셰이크·프레임·서브프로토콜의 책임을 확인한다.
- [STOMP 1.2 Specification](https://stomp.github.io/stomp-specification-1.2.html) — 명령·목적지·ACK·RECEIPT의 정확한 의미를 읽는다.
- [Spring · STOMP Overview](https://docs.spring.io/spring-framework/reference/web/websocket/stomp/overview.html) — WebSocket 위의 STOMP와 목적지 이름의 관례를 연결해 본다.
