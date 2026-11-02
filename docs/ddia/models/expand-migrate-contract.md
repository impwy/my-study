# Expand–Migrate–Contract와 데이터 호환성

> 구조 확장, 데이터 이관, 구 구조 제거를 서로 다른 단계로 나눠 신·구 애플리케이션의 공존과 롤백 가능성을 유지한다.

- **전제:** 롤링 중에는 N과 N-1 애플리케이션이 같은 데이터에 접근한다.
- **원리:** 추가 → 호환 쓰기·이관·읽기 전환 → 의존성 제거 확인 후 삭제 순서를 지킨다.
- **주의:** 스키마 호환성은 DDL 잠금, 저장소 간 일관성, 백업·복구 가능성까지 자동으로 보장하지 않는다.

<details>
<summary>변경 단계·저장소별 정책·백업의 한계 펼치기</summary>

## PostgreSQL의 세 단계

애플리케이션 패치에 PostgreSQL·MongoDB·Kafka·Redis 재시작을 묶지 않는 것을 이 사례의 운영 원칙으로 삼는다. 데이터 변경도 한 번에 끝내기보다 다음처럼 분리한다.

| 단계 | 수행 내용 | 다음 단계로 넘어갈 조건 |
| --- | --- | --- |
| **Expand** | nullable 컬럼·새 테이블 등 기존 코드와 공존하는 구조 추가. 즉시 rename/drop/필수값 강제를 피함 | 이전 애플리케이션도 확장된 스키마에서 정상 동작 |
| **Migrate** | 호환 코드 배포, 신·구 필드 쓰기 동기화, 재실행 가능한 소규모 backfill, 읽기 전환 | 누락·불일치와 동시 쓰기 경합 검증 완료 |
| **Contract** | 구 필드 의존 코드부터 제거하고 이후 릴리스에서 컬럼·임시 경로 삭제 | 롤백 기간 종료, 구 코드·배치·소비자의 참조가 모두 사라짐 |

**새 필드 우선 읽기 + 없으면 구 필드 fallback에는 조건이 있다.** 구버전이 구 필드만 갱신하면 이미 채워진 새 필드는 낡은 값이 될 수 있다. 동기화가 보장되기 전에는 구 필드를 기준으로 읽거나, 구버전 쓰기까지 반영하는 동기화 경로를 마련한다. backfill도 동시 갱신을 덮어쓰지 않도록 설계한다. 읽기 전환은 데이터 복사 완료만으로 결정하지 않는다.

## Migration Job과 잠금

제공된 운영 기록에는 배포 전 단일 migration Job과 트랜잭션·advisory lock 사용이 있다. 실제 구현은 이번 문서에서 재점검하지 않았다.

- 단일 Job도 재시도될 수 있으므로 실행 이력과 재실행 안전성을 관리한다. [Advisory lock](https://www.postgresql.org/docs/current/explicit-locking.html#ADVISORY-LOCKS)은 같은 키·규칙을 사용하는 실행자 사이의 협조적 잠금이다.
- nullable 컬럼 추가도 잠금은 필요하다. `ADD COLUMN`은 일반적으로 `ACCESS EXCLUSIVE` 잠금을 요구하므로, 전체 재작성이 없다고 무조건 지연이 없는 것은 아니다. 잠금 대기 제한과 사전 검증을 둔다.
- 대량 backfill은 배포 트랜잭션에 넣지 않고 재실행 가능한 별도 Job으로 나눈다. 짧은 트랜잭션·진행 위치·재시도·검증을 설계한다.
- `CREATE INDEX CONCURRENTLY`는 쓰기 차단을 줄이지만 트랜잭션 블록 안에서 실행할 수 없다. 트랜잭션 기반 migration과 실행 경로를 분리하고, 실패 후 invalid 인덱스도 점검한다.

## 저장소·이벤트별 호환 정책

| 대상 | 이 사례의 정책 | 확인할 조건 |
| --- | --- | --- |
| MongoDB | 새 필드는 optional로 도입하고 구·신 문서 모두 읽기 | 누락 필드 처리와 컬렉션 validator도 함께 호환되어야 함 |
| Kafka | optional/default를 고려한 추가 변경 우선. 비호환 변경은 `*.v2` 토픽과 호환 소비자 준비 | 필드 추가만으로 호환이 보장되지 않음. 직렬화·역직렬화·업무 코드를 양방향 검증 |
| Redis | `key:v1:*`, `key:v2:*`로 캐시 표현 분리 | 구 키의 재생성·두 버전 무효화·TTL 정책 유지. 이 사례에서는 캐시로 사용하고 원본은 별도 저장소에 둠 |

이는 제품이 자동으로 보장하는 정책이 아니라 애플리케이션 설계다. [MongoDB validator](https://www.mongodb.com/docs/manual/core/schema-validation/)와 [이벤트 스키마 호환성 방향](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)을 확인한다. 기본 BACKWARD 설정만으로 구 소비자가 새 이벤트를 읽을 수 있다고 판단하면 안 된다. v2 도입 후에는 토픽뿐 아니라 **구 소비자가 읽을 수 있는 이벤트 공급·재처리 경로**를 롤백 기간 동안 유지한다.

캐시 일반 원리는 [Cache-aside와 스탬피드](../../redis/cache/cache-aside-and-stampede.md), 비동기 정합성은 [Outbox와 대사](../consistency/outbox-and-reconciliation.md)에서 복습한다.

## 백업과 롤백의 경계

원문에는 API·Worker를 멈춘 뒤 PostgreSQL·MongoDB를 백업하는 구현이 설명되어 있다. 이 방식은 무중단 패치의 필수 선행 단계로 사용할 수 없다. 또한 두 프로세스 중지만으로 모든 쓰기·진행 중 작업이 정지했는지까지 입증되지는 않는다.

[pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)는 동시 읽기·쓰기를 허용하면서 단일 PostgreSQL DB의 일관된 덤프를 만들 수 있다. 하지만 별도 MongoDB 백업과 같은 업무 시점의 공동 스냅샷을 자동으로 만들지는 않는다. [MongoDB 백업 방식](https://www.mongodb.com/docs/manual/core/backups/)도 구성별 전제가 다르다.

일상 패치는 최근 **복구 시험을 거친 백업**과 호환 migration을 사용한다. 파괴적 변경은 유지보수 시간을 확보하거나, PostgreSQL PITR·MongoDB의 적합한 백업/oplog 복구 체계와 저장소 간 복구·대사를 먼저 검증한다. replica set 구성만으로 임의 시점 복구가 완성되는 것은 아니다.

애플리케이션 롤백은 확장된 스키마를 유지한 채 수행한다. 자동 down migration을 실행하지 않고 후속 forward migration을 검토한다. 단, 이미 삭제·손상된 데이터가 forward migration만으로 복원되는 것은 아니다.

## 꼬리질문

1. 구조 추가와 구 구조 제거를 같은 배포에서 수행하면 왜 롤백 가능성이 줄어드는가?
2. backfill 도중 구버전 API가 기존 필드를 갱신할 때, 새 필드 우선 읽기에서 어떤 오류가 생길 수 있을까?
3. PostgreSQL과 MongoDB 각각의 백업이 성공해도 서비스 전체의 일관된 복구를 보장하지 못하는 이유는 무엇인가?

함께 복습: [롤링 배포의 조건](../../cloud/availability/kubernetes-rolling-update.md) · [API·WebSocket 호환성](../../rest-api/contracts/rolling-deployment-compatibility.md)

</details>

## 참고 자료

- [GitLab · Avoiding downtime in migrations](https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/) — 여러 릴리스에 걸쳐 컬럼·코드 변경을 분리하는 실제 운영 원칙을 확인한다.
- [PostgreSQL · ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) — 컬럼·제약 변경의 잠금과 재작성 조건을 확인한다. 실제 운영 버전의 문서도 대조한다.
- [PostgreSQL · CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) — 동시 인덱스 생성의 트랜잭션 제약과 실패 후 점검 사항을 확인한다.
