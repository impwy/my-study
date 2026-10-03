# MySQL

[전체 목록](../../README.md)

## 스키마·SQL

| 문서 | 한 줄 요약 |
| --- | --- |
| [MySQL 스키마의 타입·제약·기본값](sql/schema-types-and-defaults.md) | 테이블은 값의 표현뿐 아니라 누락·중복·범위에 대한 계약을 함께 정의한다. |

## 실행 계획

| 문서 | 한 줄 요약 |
| --- | --- |
| [실행 계획과 복합 인덱스](plans/explain-and-composite-index.md) | 실제 필터·정렬·조인 조건과 데이터 분포를 기준으로 인덱스의 효과를 검증한다. |

## InnoDB·인덱스

| 문서 | 한 줄 요약 |
| --- | --- |
| [InnoDB 클러스터드 인덱스](innodb/clustered-index.md) | InnoDB는 클러스터드 인덱스 리프에 행을 저장하고 보조 인덱스에서 행 식별 키를 이용한다. |

## MVCC·락

| 문서 | 한 줄 요약 |
| --- | --- |
| [InnoDB MVCC와 락](concurrency/mvcc-and-locks.md) | 스냅샷 읽기와 잠금 읽기를 구분하고 격리 수준·인덱스 조건에 따른 동시 동작을 확인한다. |

