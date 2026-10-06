# Outbox와 정합성 대사

> 원본 변경과 전송 의도를 함께 기록하고 비동기 전달의 중복·지연·누락을 감지해 복구한다.

- Outbox는 업무 변경과 발행할 이벤트를 같은 DB 트랜잭션에 기록한다.
- CDC는 DB 변화를 운반하지만 도메인 사건의 의미를 자동으로 정하지 않는다.
- 전달 재시도·소비 멱등성·대사·복구를 별도로 설계한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

주문 DB 커밋 뒤 이벤트 발행 전에 종료되면 주문만 남는다. Outbox는 원본 변경과 전송 의도를 함께 저장하고 별도 전달기가 발행하도록 한다. 발행 성공 후 완료 표시 전에 장애가 나면 중복 발행이 가능하므로 이벤트 ID와 소비자 멱등성도 필요하다.

## SQL 예제

orders·outbox 실습 테이블과 같은 DB 트랜잭션을 가정한다. 두 INSERT가 성공해야 커밋하며 실패하면 롤백한다. 실제 발행기는 별도로 필요하다.

```sql
BEGIN;
INSERT INTO orders (id) VALUES (42);
INSERT INTO outbox (event_id, aggregate_id, status)
VALUES ('order-42-confirmed', 42, 'NEW');
COMMIT;
```

## 복제 방식을 선택할 때

직접 조회는 복제·동기화 부담을 줄이지만 대상 서비스의 지연·장애에 의존한다. 이벤트 기반 읽기 모델은 필요한 정보를 별도로 보관하지만 허용 지연과 재처리를 책임진다. CDC(Change Data Capture)는 DB 변경을 추출하는 기술이며 Outbox 이벤트의 전달 경로로도 활용할 수 있다.

원본 소유자, 이벤트 식별자·버전, 삭제 반영, 역전 이벤트 처리, 실패 메시지 보관과 재처리, 원본 대사 기준을 정한다. 대사는 상태를 비교하되 처리 중인 이벤트의 지연을 곧바로 실패로 판단하지 않는다.

## 주의점

Spring 애플리케이션 이벤트의 발행·커밋 후 리스너 실행만으로 DB 커밋과 Kafka 발행의 원자성이나 내구성 있는 재시도가 보장되지 않는다. Outbox도 모든 외부 효과를 정확히 한 번 실행하게 만들지는 않는다. 단순 수치 차이를 무조건 덮어쓰는 대사는 진행 중 요청을 망가뜨릴 수 있다.

## 꼬리질문

1. 원본 변경과 이벤트 발행 사이의 장애 구간을 Outbox가 어떻게 줄이는가?
2. 회원 삭제 이벤트가 늦거나 순서가 역전되면 읽기 모델은 어떤 버전·재처리 기준을 가져야 할까?
3. 발행 후 완료 기록 전에 장애가 발생하거나 대사 중 요청이 진행되고 있다면 무엇을 조심해야 할까?

</details>

## 참고 자료

- [Debezium · Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — 이벤트 식별자와 Outbox 라우팅 구성을 확인한다.
- [Spring · Transaction-bound Events](https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html) — 이벤트의 트랜잭션 실행 시점과 보장 범위를 확인한다.
- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 전달 보장과 외부 저장소 효과의 경계를 확인한다.
