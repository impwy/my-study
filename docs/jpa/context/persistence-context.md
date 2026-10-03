# 영속성 컨텍스트와 엔티티 상태

> 영속성 컨텍스트는 관리 중인 엔티티의 동일성과 변경 추적을 담당한다.

- new·managed·detached·removed 상태를 구분한다.
- 같은 컨텍스트에서 동일 식별자는 같은 관리 객체다.
- merge는 전달 객체를 그대로 관리하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

persist는 새 엔티티를 관리 상태로 연결하며 실제 SQL 실행 시점은 flush와 전략에 영향을 받는다. 관리 객체의 변경은 변경 감지 대상이다. detach·clear·컨텍스트 종료 뒤 객체는 관리되지 않으므로 단순 필드 변경이 자동 반영되지 않는다. merge는 전달한 상태를 관리 객체로 복사하고 그 관리 객체를 반환한다. 호출자가 넘긴 detached 객체 자체가 관리 상태로 바뀌는 것은 아니다.

## Java 예제

type은 매핑된 엔티티이며 해당 ID가 존재한다고 가정한다.

```java
import jakarta.persistence.EntityManager;

static <T> void identity(EntityManager em, Class<T> type, Object id) {
    T first = em.find(type, id), second = em.find(type, id);
    System.out.println(first == second); // 같은 컨텍스트·같은 엔티티 식별자
    em.clear();
    System.out.println(em.contains(first)); // false: 분리 상태
}
```

## 주의점

1차 캐시는 전역 공유 캐시가 아니다. 장시간 대량 데이터를 관리하면 메모리와 변경 감지 비용이 커질 수 있다.

## 꼬리질문

1. merge 호출 후 원래 객체와 반환 객체의 관리 상태가 다른 이유는?
2. 같은 영속성 컨텍스트에서 find를 반복하면 객체 동일성이 어떻게 유지될까?
3. clear 뒤 기존 객체의 필드를 바꿔도 dirty checking 대상이 아닌 이유는 무엇일까?

함께 복습: [flush와 commit](flush-and-commit.md) · [연관관계의 주인과 양방향 참조](../relationships/owning-side.md)

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
