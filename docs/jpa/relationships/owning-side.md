# 연관관계의 주인과 양방향 참조

> 외래 키 매핑의 변경 주체와 객체 양쪽의 참조 일관성을 함께 관리한다.

- mappedBy는 반대편 주인을 가리킨다.
- 주인 쪽 변경이 관계 저장에 반영된다.
- 편의 메서드로 양쪽 객체를 맞춘다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

양방향 관계는 두 객체의 참조와 하나의 DB 외래 키로 표현될 수 있다. 일반적인 양방향 일대다·다대일 매핑에서는 외래 키를 가진 다대일 쪽이 주인이다. 반대편 컬렉션만 변경하면 DB 관계에 반영되지 않을 수 있다. 주인 쪽 외래 키 관계를 설정하면서 반대편 컬렉션도 함께 맞추어 같은 트랜잭션의 객체 그래프를 일관되게 만든다.

## Java 예제

Jakarta Persistence. ID는 별도로 부여하며 add는 양쪽 자바 참조를 일관되게 유지한다.

```java
import jakarta.persistence.*;

import java.util.*;

@Entity
static class Purchase {
    @Id Long id;

    @OneToMany(mappedBy = "purchase")
    List<Line> lines = new ArrayList<>();

    void add(Line line) {
        lines.add(line);
        line.purchase = this;
    }
}

@Entity
static class Line {
    @Id Long id;

    @ManyToOne
    @JoinColumn(name = "purchase_id")
    Purchase purchase;
}
```

## 주의점

cascade는 작업 전파이고 fetch는 로딩 전략이다. orphanRemoval은 부모에서 제거된 자식의 삭제 의미로 공유 객체에는 신중히 사용한다.

## 꼬리질문

1. 부모의 컬렉션에만 자식을 추가했는데 외래 키가 설정되지 않는 이유는?
2. purchase.lines만 수정하고 line.purchase를 설정하지 않으면 외래키 변경이 왜 누락될까?
3. 연관관계 주인과 애그리거트의 업무상 소유자가 같은 개념이라고 볼 수 있을까?

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
