# 채팅의 브로커 선택과 메시지 전달

> 참여자 수·서버 수·메시지 보관·순서 요구를 나누어 SimpleBroker, Redis Pub/Sub, RabbitMQ, Kafka를 비교한다.

- **규모:** 단체방과 다중 서버는 별개이며, 1:1 채팅도 연결이 서버마다 나뉘면 중계가 필요하다.
- **전달:** 같은 브로커를 사용해도 구독·큐·컨슈머 그룹 구성에 따라 전체 전달 또는 작업 분산이 된다.
- **신뢰성:** 브로커의 수락·소비 확인·DB 저장·클라이언트 수신·읽음은 서로 다른 성공 단계다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

연결·프로토콜은 [WebSocket과 STOMP](../../network/http-tls/websocket-and-stomp.md), 서버 안의 목적지 처리는 [Spring STOMP 라우팅](../../spring/mvc/stomp-message-routing.md)에서 확인한다.

1:1 채팅에서 방과 참여자를 DB로 확인한 뒤 회원 ID로 전달하는 방식은 가능하다. 단체방도 같은 방식으로 참여자에게 각각 보내거나 방별 목적지를 구독하게 할 수 있다. DB의 참여 권한과 현재 연결의 구독 상태는 별도로 관리한다.

서버 A에 발신자가, 서버 B에 수신자가 연결되면 서버 사이 전달이 필요하다. 외부 브로커를 사용해도 WebSocket 연결·송신 버퍼·인증 상태는 각 서버에 남는다. 같은 물리 서버에서 프로세스만 분리한다고 전체 메모리 부담이 자동으로 줄지는 않는다.

| 선택지 | 채팅에서의 역할과 조건 |
| --- | --- |
| [SimpleBroker](../../spring/mvc/stomp-message-routing.md) | 한 서버의 구독자를 관리한다. 단체방도 가능하지만 영속 이력·서버 간 중계는 별도다. |
| [Redis Pub/Sub](../../redis/failures/pub-sub-delivery-semantics.md) | 현재 구독 서버들에 전달하고 각 서버가 로컬 연결로 보낼 수 있다. 보관·재전송은 없다. |
| RabbitMQ | STOMP 플러그인을 켜면 Spring Broker Relay로 연결할 수 있다. 큐·구독·영속성 정책을 정한다. |
| [Kafka](../../kafka/topics/log-partition-offset.md) | 보관된 로그를 소비한다. 소비 코드와 WebSocket 전송을 잇고 그룹·라우팅을 설계한다. |

## RabbitMQ의 큐와 전체 전달

기본 AMQP 0-9-1 모델은 `Producer → Exchange → Binding → Queue → Consumer`다. Exchange가 바인딩 규칙으로 큐를 선택한다. 한 큐의 여러 소비자는 메시지를 나눠 받고, 여러 큐로 복제하면 각 큐가 독립적으로 받을 수 있다.

STOMP 플러그인의 `/queue/...`는 같은 큐의 구독자에게 작업을 분산한다. `/topic/...`는 매칭되는 구독자들에게 전달하며 기본 구독 큐는 비영속·자동 삭제다. 오프라인 보관이 필요하면 durable 구독과 큐 수명도 구성해야 한다. Spring의 접두사만 바꿔 RabbitMQ의 목적지 규칙을 바꿀 수는 없다.

RabbitMQ도 durable queue, persistent message, publisher confirm, consumer ACK, 복제 큐를 조합해 신뢰성을 높일 수 있다. Publisher confirm은 발행 구간, consumer ACK는 소비 구간을 확인한다. STOMP에서는 persistent SEND에 대한 RECEIPT 등 해당 플러그인의 확인 방식을 따로 확인한다. 어느 확인도 사람의 읽음을 자동으로 뜻하지 않는다. RabbitMQ의 다음 단계가 항상 Kafka인 것은 아니다.

## 주의점

FIFO 큐나 Kafka 파티션은 전체 시스템의 처리·화면 순서를 자동 보장하지 않는다. 다중 발행자·병렬 처리·재전달·WebSocket 송신 단계까지 확인한다. 방 순번은 업무상 기준 순서를 정의하는 수단이며 Kafka에서는 같은 방의 키·파티션 정책도 필요하다.

DB 커밋 후 발행 전에 프로세스가 종료되는 간격은 브로커 교체만으로 없어지지 않는다. [Outbox와 정합성 대사](../consistency/outbox-and-reconciliation.md)로 이어서 공부한다. Kafka의 전체 전달과 작업 분산은 [컨슈머 그룹](../../kafka/consumers/group-and-rebalance.md), 외부 효과의 exactly-once 한계는 [전달 보장의 범위](../../kafka/delivery/idempotence-and-transactions.md)를 참고한다.

## 꼬리질문

1. 같은 큐의 소비자 여러 명과, 각각 큐를 가진 구독자 여러 명은 전달 결과가 어떻게 다른가?
2. 수신자의 연결이 다른 서버에 있다면 어떤 중계·로컬 전달 경로가 필요한가?
3. 브로커가 메시지를 수락한 뒤에도 DB·클라이언트·읽음 관점에서 어떤 실패와 순서 문제가 남는가?

</details>

## 참고 자료

- [RabbitMQ · STOMP Plugin](https://www.rabbitmq.com/docs/stomp) — 목적지·구독 큐 수명·메시지 영속성과 STOMP 확인 방식을 읽는다.
- [RabbitMQ · Reliability Guide](https://www.rabbitmq.com/docs/reliability) — 발행자·브로커·소비자가 나눠 책임지는 전달 신뢰성을 확인한다.
- [RabbitMQ · Queues](https://www.rabbitmq.com/docs/queues) — FIFO·동시 소비·재전달과 순서의 조건을 확인한다.
