# Redis Pub/Sub의 전달 보장과 채팅 연동

> Redis Pub/Sub은 현재 구독자에게 메시지를 전달하며, 놓친 메시지를 보관하거나 재전송하지 않는다.

- **보장:** Pub/Sub은 at-most-once 전달이며 연결 단절·처리 실패 후 재전송을 제공하지 않는다.
- **원인:** 메시지 누락의 핵심은 메모리 사용 자체보다 보관·확인·재처리 모델의 부재다.
- **연동:** 채팅 서버 간 전달에 쓰고 각 서버가 자신의 WebSocket 연결로 전달하는 설계를 할 수 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

발행자가 `PUBLISH`하면 Redis가 해당 채널의 현재 구독자들에게 전달한다. 구독 서버가 끊겨 있거나 수신 후 처리하지 못하면 Pub/Sub에서 같은 메시지를 다시 꺼내 읽을 수 없다. Redis가 정상 동작 중이어도 구독자는 메시지를 놓칠 수 있다.

따라서 “Redis는 메모리 기반이라 메시지가 유실된다”보다 “Pub/Sub은 누락을 복구할 로그·ACK·재전송이 없다”가 정확하다. Redis 데이터 영속화를 켜는 것만으로 Pub/Sub이 재생 가능한 로그가 되지는 않는다. 일반 데이터의 복구는 [RDB·AOF](../persistence/rdb-aof-and-recovery.md)와 구분한다.

## 서버 간 전달 예시

다음은 가능한 애플리케이션 설계이며 Spring이 자동으로 구성해 주는 동작은 아니다.

```text
서버 A: 권한 확인·DB 저장 → Redis 채널에 발행
                               ↓
구독 중인 서버 A·B가 각각 수신
                               ↓
각 서버: 로컬 SimpleBroker → 자신에게 연결된 사용자
```

Redis Pub/Sub은 STOMP 브로커가 아니므로 Spring의 `enableStompBrokerRelay()`에 Redis 주소를 넣어 교체하지 않는다. Redis 수신과 `SimpMessagingTemplate` 전송을 잇는 코드가 필요하다. 수신 메시지를 다시 Redis로 발행해 순환하거나, 로컬 직접 전달과 Redis 수신 전달을 겹쳐 중복시키지 않도록 경로를 정한다.

## 주의점

DB에 저장한 메시지를 실시간으로 놓쳤다면 저장된 기록과 실시간 전달 누락을 구분한다. 재접속 시 이력을 조회하고 실시간 도착분과 메시지 ID로 병합할 수 있다.

Redis Streams는 Pub/Sub과 별개의 자료구조로, 기록·재조회·소비 상태 관리 기능을 제공한다. 정확한 전달 보장은 소비·확인·보관 정책을 함께 봐야 한다. Pub/Sub을 쓴다는 이유만으로 Streams의 기능을 기대할 수 없다.

## 꼬리질문

1. Redis 서버가 정상인데도 Pub/Sub 구독자가 메시지를 놓칠 수 있는 이유는 무엇인가?
2. 두 채팅 서버 중 하나가 발행 순간 끊겨 있었다면 DB 이력과 실시간 수신을 어떻게 합칠 수 있는가?
3. 재처리 요구가 추가될 때 Pub/Sub과 Streams 중 어떤 보관·소비 기능을 비교해야 하는가?

</details>

## 참고 자료

- [Redis · Pub/Sub](https://redis.io/docs/latest/develop/pubsub/) — at-most-once 전달과 연결 단절 시의 한계를 확인한다.
- [Spring · External Broker](https://docs.spring.io/spring-framework/reference/web/websocket/stomp/handle-broker-relay.html) — STOMP를 지원하는 외부 브로커에 릴레이하는 조건을 확인한다.
