# 엔티티 식별자와 매핑

> JPA 엔티티는 영속 식별자로 구분하며 필드와 테이블의 매핑 규칙을 명시한다.

- 기본 생성자·식별자 등 엔티티 요구사항을 확인한다.
- 값 객체는 생명주기·식별 필요로 구분한다.
- 도메인 모델과 DB 제약을 함께 설계한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

@Entity와 @Id는 영속 타입과 식별자를 나타낸다. 생성 전략과 컬럼·접근 방식은 DB와 제공자 조건에 맞게 선택한다. 값 객체를 @Embeddable로 표현하면 엔티티에 속한 값 묶음을 매핑할 수 있다. 메모리의 equals와 영속 식별자 정책은 신규 상태·프록시·식별자 생성 시점까지 고려한다. 도메인의 필수 조건은 코드뿐 아니라 DB 제약으로도 보호한다.

## Java 예제

Jakarta Persistence와 JPA 구현체가 필요하다. 매핑 선언만으로 운영 스키마 변경을 가정하지 않는다.

```java
import jakarta.persistence.*;

@Entity
static class Member {
    @Id @GeneratedValue Long id;

    @Column(nullable = false, unique = true)
    String email;

    protected Member() {}

    Member(String email) {
        this.email = email;
    }
}
```

## 주의점

record를 일반적인 JPA 엔티티로 바로 사용한다고 가정하지 않는다. 엔티티를 public setter 모음으로 만들면 불변식을 우회하기 쉽다.

## 꼬리질문

1. 업무 식별자와 DB 생성 식별자를 선택할 때 equals에서 어떤 시점을 고려해야 하는가?
2. id가 저장 전에는 null일 수 있다면 equals·hashCode에 생성 ID를 쓰는 설계에서 무엇을 조심해야 할까?
3. unique 매핑과 운영 DB의 실제 UNIQUE 제약이 일치하는지 어떻게 확인할까?

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
