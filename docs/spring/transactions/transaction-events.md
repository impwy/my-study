# 트랜잭션 이벤트와 전달 실패

> 이벤트 리스너의 실행 시점과 실행 스레드, 이벤트의 내구성을 각각 설계한다.

- 일반 이벤트는 기본적으로 동기 실행된다.
- 트랜잭션 리스너는 커밋 단계에 연결할 수 있다.
- 프로세스 내부 이벤트는 영속 메시지와 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

ApplicationEventPublisher를 사용했다는 이유만으로 리스너가 자동으로 비동기 실행되지는 않는다. @TransactionalEventListener는 BEFORE_COMMIT·AFTER_COMMIT 등 단계에 연결한다. 커밋 후 알림을 보내면 롤백된 주문의 알림을 줄일 수 있지만 커밋 직후 프로세스가 종료되면 알림 전달이 누락될 수 있다. 전달이 중요하면 outbox처럼 DB 상태와 발송할 이벤트를 함께 기록하는 방법을 검토한다.

## Java 예제

Spring 빈·트랜잭션 관리가 필요하다. 이벤트는 DB 저장 이후 발행한다고 가정한 흐름 예제이며 영속 메시지 전달을 보장하지 않는다.

```java
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.event.*;

record OrderCreated(long id) {}

static class Events {
    final ApplicationEventPublisher publisher;

    Events(ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }

    @Transactional
    public void create(long id) {
        publisher.publishEvent(new OrderCreated(id));
    }

    @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
    public void after(OrderCreated event) {
        System.out.println(event.id());
    }
}
```

## 주의점

AFTER_COMMIT에서 기존 트랜잭션 자원을 볼 수 있다는 것과 새 변경이 커밋된다는 것은 다르다. 새 DB 쓰기는 적절한 새 경계를 검토한다.

## 꼬리질문

1. 커밋 후 이벤트를 사용해도 이벤트 유실이 가능해지는 장애 구간은 어디인가?
2. 트랜잭션이 롤백되면 AFTER_COMMIT 리스너는 실행될까?
3. 커밋 후 리스너 실행 전 프로세스가 종료되면 outbox가 어떤 누락을 줄일 수 있을까?

함께 복습: [Outbox와 정합성 대사](../../ddia/consistency/outbox-and-reconciliation.md) · [애그리거트와 도메인 이벤트](../../ddd/aggregates/aggregate-and-events.md)

</details>

## 참고 자료

- [Spring · Transaction-bound Events](https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html) — 커밋 전·후 리스너의 동작 범위를 확인한다.
