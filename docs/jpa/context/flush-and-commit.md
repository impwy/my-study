# flush와 commit

> flush는 변경을 DB에 동기화하는 과정이고 commit은 트랜잭션을 확정하는 과정이다.

- flush 뒤에도 롤백할 수 있다.
- 쿼리 전 자동 flush가 일어날 수 있다.
- SQL 실행과 트랜잭션 완료를 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

관리 엔티티의 변경을 감지한 SQL은 flush 시 DB로 전달된다. 제약 조건 오류가 이 시점에 드러날 수 있지만 DB 트랜잭션은 아직 확정되지 않았다. commit은 성공한 변경을 확정한다. flush 모드와 조회 종류·제공자에 따라 쿼리 실행 전 동기화가 발생할 수 있으므로 “SQL은 항상 commit 때만 실행”이라고 외우지 않는다.

## 예제

persist 뒤 flush로 INSERT가 실행되어도 이후 예외로 롤백되면 행이 확정되지 않는다. 식별자 생성 전략에 따라 INSERT 시점이 더 빠를 수도 있다.

## 주의점

flush는 캐시 비우기와 다르다. clear로 관리 객체를 분리하기 전에 필요한 변경을 동기화하지 않으면 반영되지 않을 수 있다.

## 복습 질문

로그에 INSERT가 보였는데 트랜잭션 후 행이 없는 상황을 어떻게 설명할까?

자료 구분: **기존 자료** — JPA 가이드·워크북·강의의 매핑·조회 개념. **공식 자료 보완** — Hibernate 6.6과 Spring의 정확한 동작 경계.

함께 복습: [영속성 컨텍스트와 엔티티 상태](persistence-context.md) · [Spring 트랜잭션 경계](../../spring/transactions/transaction-boundary.md)

</details>

## 참고 자료

- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
- [Spring · @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) — 프록시 경계·롤백 조건·트랜잭션 속성을 확인한다.
