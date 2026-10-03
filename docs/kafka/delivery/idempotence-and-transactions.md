# Kafka 전달 보장의 범위

> 프로듀서 멱등성·Kafka 트랜잭션·컨슈머 처리 정책의 보장 범위를 외부 업무 효과와 구분한다.

- 프로듀서 멱등성은 전송 재시도 중복을 줄인다.
- Kafka 트랜잭션은 Kafka 기록·오프셋을 묶을 수 있다.
- 외부 DB·결제는 별도의 중복 방어가 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

레코드를 보낸 뒤 응답이 유실되면 재시도 중복이 생길 수 있다. 멱등 프로듀서는 해당 프로듀서 세션의 전송을 식별해 로그 중복을 제한한다. consume-process-produce를 Kafka 트랜잭션으로 묶고 적절한 격리 소비를 사용하면 Kafka 범위의 정확히 한 번 처리 의미를 구성할 수 있다. 컨슈머의 외부 DB INSERT나 결제 호출은 자동으로 이 트랜잭션에 포함되지 않는다.

## 예제

DB 저장 뒤 커밋 전에 장애가 나면 같은 이벤트를 다시 읽을 수 있다. 이벤트 ID UNIQUE와 동일 DB 트랜잭션으로 처리 기록·업무 변경을 묶어 중복 효과를 제한한다.

## 주의점

자동 커밋 여부만으로 at-most-once·at-least-once를 단정하지 않는다. 실제 처리 완료와 커밋의 순서가 핵심이다.

## 복습 질문

멱등 프로듀서를 사용해도 컨슈머 결제가 두 번 실행될 수 있는 이유는?

자료 구분: **기존 자료** — Kafka 강의와 이벤트 처리 노트의 흐름. **공식 자료 보완** — Kafka 4.1 설정·복제·커밋 보장 범위.

함께 복습: [컨슈머 오프셋과 커밋](../consumers/offset-and-commit.md) · [멱등 키와 요청 재시도](../../rest-api/idempotency/idempotency-key.md)

</details>

## 참고 자료

- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
- [Kafka 4.1 · Producer Configs](https://kafka.apache.org/41/configuration/producer-configs/) — acks·멱등성·배치·타임아웃의 상호 조건을 확인한다.
