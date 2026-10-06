# JPA 상속 전략과 물리 테이블

> SINGLE_TABLE·JOINED·TABLE_PER_CLASS는 상속 계층의 저장 방식이며 조회·제약·인덱스 비용으로 비교한다.

- SINGLE_TABLE은 상속 계층을 한 테이블에 저장한다.
- JOINED는 부모·자식 테이블을, TABLE_PER_CLASS는 구체 타입별 테이블을 사용한다.
- 상속 전략과 날짜 인덱스 가능 여부를 혼동하지 않는다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

| 전략 | 물리 구조 | 검토할 비용 |
| --- | --- | --- |
| SINGLE_TABLE | 한 테이블에 계층 전체 저장 | 타입 전용 컬럼의 NULL·제약·행 폭 |
| JOINED | 공통 필드와 하위 타입 필드를 별도 테이블에 저장 | 조회에 필요한 조인·조건 분산 |
| TABLE_PER_CLASS | 구체 타입별 테이블에 필요한 필드 저장 | 다형적 조회의 UNION·중복 컬럼 |

SINGLE_TABLE도 날짜·타입 컬럼에 인덱스를 설계할 수 있다. 부모와 자식의 조건이 다른 테이블에 놓이는 JOINED의 조회 문제를 단일 테이블의 인덱스 불가로 설명하지 않는다. 대표 쿼리와 쓰기 빈도, 제약, 행 폭, 실행 계획을 비교한다.

## 주의점

JPA는 영속성 표준, Hibernate는 구현체, Spring Data JPA는 Repository 추상화다. 실제 SQL·인덱스·락은 DB의 실행과 함께 확인해야 한다. 도메인 모델을 물리 테이블과 항상 일대일로 맞출 필요는 없지만 모델을 분리하면 변환 설계를 책임진다. DTO 프로젝션은 필요한 조회 결과를 만드는 수단이며 여러 엔티티에 일부 컬럼을 임의로 중복 매핑하는 것과 같지 않다. [실행 계획과 복합 인덱스](../../mysql/plans/explain-and-composite-index.md)에서 조회 비용을 이어서 확인한다.

## 꼬리질문

1. 상속 계층의 저장 전략이 SQL의 조인·UNION·NULL 컬럼을 바꾸는 이유는?
2. 하위 타입과 생성일로 조회할 때 SINGLE_TABLE과 JOINED의 인덱스·조건 위치를 어떻게 비교할까?
3. 행 수가 많다는 정보만으로 상속 전략을 확정할 수 없다면 어떤 쿼리·제약·측정이 추가로 필요한가?

</details>

## 참고 자료

- [Hibernate ORM 6.6 · Inheritance](https://docs.hibernate.org/orm/6.6/userguide/html_single/#entity-inheritance) — 상속 전략별 테이블과 생성 SQL을 비교한다.
