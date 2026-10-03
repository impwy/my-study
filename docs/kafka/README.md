# Kafka

[전체 목록](../../README.md)

## 토픽·파티션

| 문서 | 한 줄 요약 |
| --- | --- |
| [로그·파티션·오프셋](topics/log-partition-offset.md) | Kafka는 토픽의 파티션별 추가 로그에 레코드를 저장하고 오프셋으로 위치를 식별한다. |
| [복제·ISR·High Watermark](topics/replication-and-high-watermark.md) | 리더와 복제본의 로그 진도를 구분하고 소비 가능한 커밋 경계와 장애 시 남는 데이터를 확인한다. |

## 프로듀서

| 문서 | 한 줄 요약 |
| --- | --- |
| [프로듀서 배치·acks·재시도](producers/producer-batch-and-acks.md) | 전송 효율과 확인 수준을 조정하되 재시도·시간 제한·순서에 미치는 영향을 함께 확인한다. |

## 컨슈머·오프셋

| 문서 | 한 줄 요약 |
| --- | --- |
| [poll과 컨슈머 타임아웃](consumers/poll-and-timeouts.md) | 로그를 읽는 주기와 멤버 생존·처리 지연 조건을 나누어 컨슈머 정체를 진단한다. |
| [재시도·DLT·재처리](consumers/retry-dlt-and-replay.md) | 실패한 이벤트의 원인·원문·처리 이력을 보존하고 안전한 재처리와 정합성 확인을 설계한다. |
| [컨슈머 그룹과 리밸런스](consumers/group-and-rebalance.md) | 그룹은 파티션 작업을 나누고 멤버·토픽 조건이 바뀌면 할당을 다시 조정한다. |
| [컨슈머 오프셋과 커밋](consumers/offset-and-commit.md) | 커밋에는 다시 시작할 다음 위치를 기록하고 처리 완료되지 않은 레코드를 건너뛰지 않는다. |

## 전달 보장

| 문서 | 한 줄 요약 |
| --- | --- |
| [Kafka 전달 보장의 범위](delivery/idempotence-and-transactions.md) | 프로듀서 멱등성·Kafka 트랜잭션·컨슈머 처리 정책의 보장 범위를 외부 업무 효과와 구분한다. |

