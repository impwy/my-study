# 낙관적 락과 비관적 락

> 동시 변경을 버전 충돌로 감지하거나 DB 락으로 조정해 업무 불변식을 지킨다.

- @Version은 오래된 상태의 갱신을 감지한다.
- 비관적 락은 획득·대기·해제 비용이 있다.
- 재시도는 업무 전체의 안전성을 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

낙관적 락은 읽기 동안 배타 락을 유지하지 않고 갱신할 때 버전 조건으로 충돌을 검출한다. 비관적 락은 DB가 제공하는 락을 획득해 경합을 조정한다. 재고 1개를 두 요청이 차감하는 상황에서 검사와 변경을 올바른 경계로 묶어야 한다. 충돌 빈도·트랜잭션 길이·DB 동작에 따라 방식을 고르고 unique·check 제약도 최종 방어로 둔다.

## Java 예제

Jakarta Persistence와 활성 트랜잭션이 필요하다. 두 락 방식을 한꺼번에 사용해야 한다는 뜻은 아니다.

```java
import jakarta.persistence.*;

@Entity
static class Inventory {
    @Id Long id;
    @Version Long version;
    int stock;
}

static Inventory lock(EntityManager em, long id) {
    return em.find(Inventory.class, id, LockModeType.PESSIMISTIC_WRITE);
} // 활성 트랜잭션 안에서 호출; @Version은 낙관적 충돌 검출에 사용
```

## 주의점

이미 실행한 외부 결제까지 무조건 반복하지 않는다. 락 없는 일반 SELECT가 항상 비관적 락 요청을 기다린다고 단정하지 않는다.

## 꼬리질문

1. 낙관적 락 오류가 났을 때 수정된 객체를 그대로 저장만 다시 하면 왜 부족한가?
2. 동일 version을 읽은 두 트랜잭션이 갱신할 때 낙관적 락은 어느 변경을 거절할까?
3. 충돌 뒤에는 새 트랜잭션으로 최신 상태를 읽고 업무 조건까지 다시 판단해야 하는 이유는 무엇일까?

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
- [MySQL 8.4 · InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) — 일관 읽기·격리 수준·락의 제품별 동작을 확인한다.
