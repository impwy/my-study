# flush와 commit

> flush는 변경을 DB에 동기화하는 과정이고 commit은 트랜잭션을 확정하는 과정이다.

- flush 뒤에도 롤백할 수 있다.
- 쿼리 전 자동 flush가 일어날 수 있다.
- SQL 실행과 트랜잭션 완료를 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

관리 엔티티의 변경을 감지한 SQL은 flush 시 DB로 전달된다. 제약 조건 오류가 이 시점에 드러날 수 있지만 DB 트랜잭션은 아직 확정되지 않았다. commit은 성공한 변경을 확정한다. flush 모드와 조회 종류·제공자에 따라 쿼리 실행 전 동기화가 발생할 수 있으므로 “SQL은 항상 commit 때만 실행”이라고 외우지 않는다.

## Java 예제

RESOURCE_LOCAL EntityManager와 신규 엔티티를 가정한다. JTA·Spring 트랜잭션에서는 관리자 API를 사용한다.

```java
import jakarta.persistence.*;

static void flushThenRollback(EntityManager em, Object entity) {
    EntityTransaction tx = em.getTransaction();
    tx.begin();
    try {
        em.persist(entity);
        em.flush();
        tx.rollback();
    } catch (RuntimeException e) {
        if (tx.isActive()) tx.rollback();
        throw e;
    }
} // SQL이 DB로 전달되어도 커밋되지 않은 저장은 롤백될 수 있음
```

## 주의점

flush는 캐시 비우기와 다르다. clear로 관리 객체를 분리하기 전에 필요한 변경을 동기화하지 않으면 반영되지 않을 수 있다.

## 꼬리질문

1. 로그에 INSERT가 보였는데 트랜잭션 후 행이 없는 상황을 어떻게 설명할까?
2. flush 직후 다른 트랜잭션이 변경을 볼 수 있는지는 어떤 DB 조건에 달릴까?
3. rollback 뒤 수정된 자바 객체가 자동으로 이전 필드 값으로 되돌아가지 않는다면 재사용을 어떻게 판단할까?

함께 복습: [영속성 컨텍스트와 엔티티 상태](persistence-context.md) · [Spring 트랜잭션 경계](../../spring/transactions/transaction-boundary.md)

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
- [Spring · @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) — 프록시 경계·롤백 조건·트랜잭션 속성을 확인한다.
