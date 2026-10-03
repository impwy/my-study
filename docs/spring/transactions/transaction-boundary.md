# Spring 트랜잭션 경계

> 하나의 업무에서 함께 성공해야 하는 DB 변경을 명확한 트랜잭션 경계로 묶는다.

- 기본 프록시 호출 경계를 확인한다.
- 기본 롤백 규칙과 전파 속성을 구분한다.
- 외부 시스템은 같은 DB 롤백 범위에 들지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

@Transactional은 지정한 트랜잭션 관리자와 전파 규칙으로 실행 경계를 만든다. 기본 설정에서는 RuntimeException·Error가 롤백 대상이고 checked 예외에는 별도 규칙이 필요할 수 있다. REQUIRED는 기존 트랜잭션에 참여하고 REQUIRES_NEW는 별도의 트랜잭션을 시작한다. 내부 메서드 호출·예외를 잡아 정상 반환하는 흐름까지 함께 보아야 실제 결과를 이해할 수 있다.

## Java 예제

Spring 빈으로 등록한 서비스를 프록시를 통해 호출하고 동일 DB의 트랜잭션 관리자를 구성한다. 유효한 금액·잔액 규칙은 별도 검증한다.

```java
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.transaction.annotation.Transactional;

static class TransferService {
    final JdbcTemplate db;

    TransferService(JdbcTemplate db) {
        this.db = db;
    }

    @Transactional
    public void move(long from, long to, int amount) {
        if (db.update("UPDATE accounts SET balance=balance-? WHERE id=?", amount, from) != 1)
            throw new IllegalStateException();
        if (db.update("UPDATE accounts SET balance=balance+? WHERE id=?", amount, to) != 1)
            throw new IllegalStateException();
    }
}
```

## 주의점

readOnly는 최적화 힌트와 제품별 동작이 있으며 일반적인 쓰기 금지 장치로 믿지 않는다. 외부 호출을 긴 DB 트랜잭션 안에 두면 연결·락 점유가 길어진다.

## 꼬리질문

1. 결제 성공 뒤 DB 저장이 실패하면 DB 트랜잭션만으로 해결되지 않는 부분은?
2. 두 번째 UPDATE에서 런타임 예외가 발생하면 첫 변경은 어떤 경계에서 롤백될까?
3. checked 예외·내부 호출·다른 스레드 작업을 추가하면 기본 트랜잭션 정책에서 무엇을 다시 확인해야 할까?

함께 복습: [AOP 프록시와 자기 호출](../aop/proxy-boundary.md) · [트랜잭션 이벤트와 전달 실패](transaction-events.md)

</details>

## 참고 자료

- [Spring · @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) — 프록시 경계·롤백 조건·트랜잭션 속성을 확인한다.
- [Spring · Transaction-bound Events](https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html) — 커밋 전·후 리스너의 동작 범위를 확인한다.
