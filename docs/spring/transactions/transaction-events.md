# 트랜잭션 이벤트와 전달 실패

> 이벤트 리스너의 실행 시점과 실행 스레드, 이벤트의 내구성을 각각 설계한다.

- 일반 이벤트는 기본적으로 동기 실행된다.
- 트랜잭션 리스너는 커밋 단계에 연결할 수 있다.
- 프로세스 내부 이벤트는 영속 메시지와 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

ApplicationEventPublisher를 사용했다는 이유만으로 리스너가 자동으로 비동기 실행되지는 않는다. @TransactionalEventListener는 BEFORE_COMMIT·AFTER_COMMIT 등 단계에 연결한다. 커밋 후 알림을 보내면 롤백된 주문의 알림을 줄일 수 있지만 커밋 직후 프로세스가 종료되면 알림 전달이 누락될 수 있다. 전달이 중요하면 outbox처럼 DB 상태와 발송할 이벤트를 함께 기록하는 방법을 검토한다.

## 예제

주문 커밋 후 이메일을 보내는 리스너가 실패해도 이미 커밋한 주문은 원래 트랜잭션으로 되돌아가지 않는다. 재시도·실패 기록을 별도로 둔다.

## 주의점

AFTER_COMMIT에서 기존 트랜잭션 자원을 볼 수 있다는 것과 새 변경이 커밋된다는 것은 다르다. 새 DB 쓰기는 적절한 새 경계를 검토한다.

## 복습 질문

커밋 후 이벤트를 사용해도 이벤트 유실이 가능해지는 장애 구간은 어디인가?

자료 구분: **기존 자료** — Spring 강의·이벤트·트랜잭션 노트의 개념. **공식 자료 보완** — 공식 문서의 프록시·실행 시점·롤백 조건.

함께 복습: [Outbox와 정합성 대사](../../ddia/consistency/outbox-and-reconciliation.md) · [애그리거트와 도메인 이벤트](../../ddd/aggregates/aggregate-and-events.md)

</details>

## 참고 자료

- [Spring · Transaction-bound Events](https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html) — 커밋 전·후 리스너의 동작 범위를 확인한다.
