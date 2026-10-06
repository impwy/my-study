# JPA

[전체 목록](../../README.md)

## 엔티티 매핑

| 문서 | 한 줄 요약 |
| --- | --- |
| [JPA 상속 전략과 물리 테이블](mapping/inheritance-strategies.md) | SINGLE_TABLE·JOINED·TABLE_PER_CLASS는 상속 계층의 저장 방식이며 조회·제약·인덱스 비용으로 비교한다. |
| [엔티티 식별자와 매핑](mapping/entity-mapping.md) | JPA 엔티티는 영속 식별자로 구분하며 필드와 테이블의 매핑 규칙을 명시한다. |

## 영속성 컨텍스트

| 문서 | 한 줄 요약 |
| --- | --- |
| [flush와 commit](context/flush-and-commit.md) | flush는 변경을 DB에 동기화하는 과정이고 commit은 트랜잭션을 확정하는 과정이다. |
| [영속성 컨텍스트와 엔티티 상태](context/persistence-context.md) | 영속성 컨텍스트는 관리 중인 엔티티의 동일성과 변경 추적을 담당한다. |

## 연관관계

| 문서 | 한 줄 요약 |
| --- | --- |
| [연관관계의 주인과 양방향 참조](relationships/owning-side.md) | 외래 키 매핑의 변경 주체와 객체 양쪽의 참조 일관성을 함께 관리한다. |

## 조회·N+1

| 문서 | 한 줄 요약 |
| --- | --- |
| [N+1과 조회 설계](queries/n-plus-one.md) | 필요한 연관 데이터를 개별 추가 쿼리로 읽는 흐름을 관찰하고 화면·업무에 맞는 조회를 설계한다. |

## 락

| 문서 | 한 줄 요약 |
| --- | --- |
| [낙관적 락과 비관적 락](locks/optimistic-and-pessimistic.md) | 동시 변경을 버전 충돌로 감지하거나 DB 락으로 조정해 업무 불변식을 지킨다. |

