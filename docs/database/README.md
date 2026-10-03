# 데이터베이스

[전체 목록](../../README.md)

## 관계형 모델

| 문서 | 한 줄 요약 |
| --- | --- |
| [관계형 모델과 키](relational/relational-model.md) | 테이블의 행을 구별하고 관계·제약으로 데이터의 의미를 지킨다. |
| [정규화](relational/normalization.md) | 속성 사이의 종속 관계를 분리해 갱신 이상을 줄인다. |

## SQL

| 문서 | 한 줄 요약 |
| --- | --- |
| [SQL 조회·조인·집계](sql/select-join-group.md) | 필요한 행을 고르고 관계를 연결한 뒤 집계 조건을 적용한다. |
| [스키마·제약 조건·뷰](sql/schema-constraints-and-views.md) | 테이블의 구조와 데이터 규칙을 DB에 선언하고 조회 표현을 뷰로 제공한다. |

## 인덱스

| 문서 | 한 줄 요약 |
| --- | --- |
| [B+ 트리 인덱스](indexes/b-plus-tree.md) | 많은 키를 한 노드에 담아 디스크 접근 깊이를 줄이고 범위 탐색을 연결한다. |
| [해시와 비트맵 인덱스](indexes/hash-and-bitmap-indexes.md) | 동등 비교·범위·집합 조건에 따라 서로 다른 인덱스 표현의 적합성을 판단한다. |

## 트랜잭션·격리 수준

| 문서 | 한 줄 요약 |
| --- | --- |
| [PostgreSQL 페이지·튜플과 MVCC](transactions/postgresql-page-and-tuple.md) | 행 버전을 페이지에 저장하고 트랜잭션 가시성으로 읽을 버전을 고르며 불필요해진 버전을 정리한다. |
| [격리 수준과 동시성 이상](transactions/isolation.md) | 동시에 실행된 트랜잭션에서 어떤 값을 관찰하고 충돌을 어떻게 처리할지 정한다. |
| [락·직렬 가능성·2PL](transactions/concurrency-control.md) | 동시 작업의 순서를 제한해 충돌하는 읽기·쓰기를 조정한다. |
| [로그와 장애 회복](transactions/write-ahead-log.md) | 데이터 변경보다 복구 정보를 먼저 기록해 장애 뒤 결과를 재구성한다. |
| [트랜잭션과 ACID](transactions/acid.md) | 여러 데이터 변경을 하나의 논리적 작업으로 관리한다. |

