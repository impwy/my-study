# Outbox와 정합성 대사

> DB 변경과 발송할 이벤트를 함께 기록하고 비동기 전달의 중복·누락을 감지·복구한다.

- DB와 메시지 발행 사이 장애 구간을 찾는다.
- 전달 재시도는 중복 소비를 고려한다.
- 대사는 충분한 진행 유예와 기준이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

주문 DB를 커밋한 뒤 이벤트를 발행하기 전에 종료되면 주문만 남을 수 있다. outbox는 같은 DB 트랜잭션에 업무 변경과 보낼 이벤트를 기록하고 별도 전달기가 읽어 발행하게 한다. 발행 뒤 완료 표시 전에 장애가 나면 중복 발행이 가능하므로 소비자도 멱등성을 가진다. 대사는 저장소 간 현재 상태를 비교하지만 처리 중인 이벤트를 즉시 실패라고 판단해서는 안 된다.

## SQL 예제

orders·outbox 실습 테이블을 가정한다. 같은 DB 트랜잭션에 주문과 전송 의도를 함께 넣는다. 두 INSERT가 성공해야 커밋하며 실패하면 롤백한다. 실제 발행기는 별도로 필요하다.

```sql
BEGIN;
INSERT INTO orders (id) VALUES (42);
INSERT INTO outbox (event_id, aggregate_id, status)
VALUES ('order-42-confirmed', 42, 'NEW');
COMMIT;
```

## 주의점

outbox만으로 모든 외부 효과가 정확히 한 번 실행되는 것은 아니다. 대사 때 단순 수치 차이를 무조건 덮어쓰면 진행 중 요청을 망가뜨릴 수 있다.

## 꼬리질문

1. 이벤트 발행 성공 뒤 완료 표시 전에 장애가 나면 어떤 중복을 처리해야 하는가?
2. 주문과 outbox를 같은 트랜잭션에 넣으면 어느 두 상태의 불일치를 줄일까?
3. relay가 발행 후 상태 갱신 전에 죽으면 중복 전달을 컨슈머가 어떤 식별자로 처리해야 할까?

</details>

## 참고 자료

- [Debezium · Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — outbox 필드·라우팅과 이벤트 전달 구조를 확인한다.
- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
