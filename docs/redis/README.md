# Redis

[전체 목록](../../README.md)

## 자료형

| 문서 | 한 줄 요약 |
| --- | --- |
| [Redis 자료형과 Sorted Set](types/types-and-sorted-set.md) | 필요한 조회·갱신 연산에 맞춰 자료형을 고르고 Sorted Set은 점수 순으로 멤버를 관리한다. |

## 캐시·TTL

| 문서 | 한 줄 요약 |
| --- | --- |
| [Cache-aside와 캐시 스탬피드](cache/cache-aside-and-stampede.md) | 캐시 미스 시 원본을 읽고 채우되 만료 순간 요청이 몰리는 경합과 오래된 값을 관리한다. |

## 영속성

| 문서 | 한 줄 요약 |
| --- | --- |
| [Redis RDB·AOF와 복구](persistence/rdb-aof-and-recovery.md) | RDB는 시점의 스냅샷을, AOF는 쓰기 명령 기록을 사용해 재시작 후 데이터를 복구한다. |

## 복제

| 문서 | 한 줄 요약 |
| --- | --- |
| [Redis 복제와 장애 전환](replication/replication-and-failover.md) | 복제본은 데이터 사본을 유지하지만 비동기 복제와 장애 전환에는 지연·손실 가능성이 있다. |

## 장애 대응

| 문서 | 한 줄 요약 |
| --- | --- |
| [Redis 원자 연산과 저장소 간 불일치](failures/atomic-script-and-cross-store.md) | Redis 안의 검사·차감을 원자적으로 묶어도 뒤이은 DB 저장·메시지 발행까지 한 번에 확정되지는 않는다. |

