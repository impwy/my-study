# 컨슈머 오프셋과 커밋

> 커밋에는 다시 시작할 다음 위치를 기록하고 처리 완료되지 않은 레코드를 건너뛰지 않는다.

- 읽기 위치와 커밋 위치는 다르다.
- 커밋 값은 다음에 읽을 오프셋이다.
- 처리 후 커밋에도 재처리 가능성이 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

poll로 레코드를 가져오면 읽기 위치는 앞서갈 수 있지만 업무가 완료되었다는 뜻은 아니다. 오프셋 10까지 처리했다면 재개 위치 11을 커밋한다. DB 처리 후 커밋 전에 장애가 나면 재처리되어 중복 가능성이 남는다. 비동기 작업에서 뒤 레코드가 먼저 끝났다고 높은 위치를 커밋하면 앞의 미완료 레코드를 영구히 건너뛸 수 있다.

## Java 예제

Kafka clients. 해당 파티션을 담당하며 이전 레코드가 모두 처리됐다고 가정한다. 자동 커밋은 끄고 consumer 호출은 담당 스레드에서 수행한다.

```java
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.TopicPartition;

import java.util.Map;

static void commitProcessed(
        KafkaConsumer<String, String> consumer,
        String topic,
        int partition,
        long lastProcessed) {
    consumer.commitSync(
            Map.of(
                    new TopicPartition(topic, partition),
                    new OffsetAndMetadata(lastProcessed + 1)));
} // 10,11,12가 모두 성공하면 다음 읽기 위치 13을 커밋
```

## 주의점

auto.offset.reset은 모든 시작 위치를 매번 덮어쓰는 설정이 아니다. 유효한 커밋이 없거나 범위를 벗어난 경우의 정책으로 이해한다.

## 꼬리질문

1. 12가 끝났어도 11이 끝나지 않았을 때 커밋 위치를 어떻게 결정해야 하는가?
2. 11이 실패하고 12만 완료된 상태에서 13을 커밋하면 재시작 후 무엇을 놓칠까?
3. 업무 저장 성공 뒤 커밋 전에 종료되면 재처리에 필요한 멱등성은 어디에서 보장해야 할까?

함께 복습: [재시도·DLT·재처리](retry-dlt-and-replay.md) · [컨슈머 그룹과 리밸런스](group-and-rebalance.md)

</details>

## 참고 자료

- [Kafka 4.1 · Consumer Configs](https://kafka.apache.org/41/configuration/consumer-configs/) — 그룹 프로토콜·poll·커밋·타임아웃 옵션을 확인한다.
- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
