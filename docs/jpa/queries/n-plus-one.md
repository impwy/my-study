# N+1과 조회 설계

> 필요한 연관 데이터를 개별 추가 쿼리로 읽는 흐름을 관찰하고 화면·업무에 맞는 조회를 설계한다.

- SQL 수와 실행 시점을 측정한다.
- fetch join·DTO·배치 조회를 상황별로 고른다.
- 컬렉션 fetch join과 페이지네이션은 주의한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

목록 한 번을 읽고 각 원소의 연관 객체를 접근할 때 추가 쿼리가 반복되면 N+1이 된다. 지연 로딩은 불필요한 조회를 줄이지만 접근 방식에 따라 반복 조회가 생긴다. 필요한 연관을 한 번에 가져오는 fetch join, 필요한 필드만 선택하는 DTO 조회, 배치 조회 등을 비교한다. 단일 쿼리도 너무 큰 곱집합을 만들면 비용이 커진다.

## Java 예제

Jakarta Persistence. 실제 쿼리 수·결과 행 수는 구현체와 실행 계획으로 확인한다.

```java
import jakarta.persistence.*;

import java.util.*;

@Entity
static class Purchase {
    @Id Long id;

    @OneToMany(mappedBy = "purchase")
    List<Line> lines = new ArrayList<>();
}

@Entity
static class Line {
    @Id Long id;
    @ManyToOne Purchase purchase;
}

static List<Purchase> fetch(EntityManager em) {
    return em.createQuery(
                    "select distinct p from Purchase p left join fetch p.lines", Purchase.class)
            .getResultList();
}
```

## 주의점

EAGER는 모든 N+1을 해결하지 않는다. 컬렉션 fetch join에 limit를 단순 적용하면 페이지 의미가 깨지거나 메모리 페이징이 발생할 수 있다.

## 꼬리질문

1. 쿼리 수를 줄인 뒤에도 응답이 더 느려질 수 있는 데이터 형태는?
2. 일반 조회 후 각 purchase.lines를 접근할 때 어떤 추가 질의가 N번 실행될 수 있을까?
3. 컬렉션 fetch join에 페이지네이션을 추가하면 행 증폭과 제한 처리에서 어떤 문제가 생길까?

함께 복습: [실행 계획과 복합 인덱스](../../mysql/plans/explain-and-composite-index.md) · [페이지네이션과 안정적인 정렬](../../rest-api/contracts/pagination.md)

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
