# 컨슈머 그룹과 리밸런스

> 그룹은 파티션 작업을 나누고 멤버·토픽 조건이 바뀌면 할당을 다시 조정한다.

- 한 그룹의 파티션은 한 멤버에 할당된다.
- 그룹이 다르면 독립적으로 소비한다.
- 리밸런스 중 처리·커밋 경계를 관리한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

subscribe를 사용한 그룹 소비에서는 코디네이션으로 파티션이 할당된다. 멤버가 추가·제거되거나 구독 파티션이 달라지면 할당이 바뀔 수 있다. 멤버가 파티션 수보다 많으면 일부는 유휴 상태다. 리밸런스에서 넘겨주는 파티션의 미완료 작업·오프셋을 어떻게 처리할지 정해야 한다. static membership과 cooperative 방식은 이동·중단 비용을 줄이는 선택지이며 버전·설정 조건을 확인한다.

## Java 예제

Kafka clients와 구성된 consumer가 필요하다. 콜백 로깅만 보여 주며 실제 오프셋·진행 중 작업 처리는 별도로 구현한다.

```java
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.TopicPartition;

import java.util.*;

static void subscribe(KafkaConsumer<String, String> consumer) {
    consumer.subscribe(
            List.of("orders"),
            new ConsumerRebalanceListener() {
                public void onPartitionsRevoked(Collection<TopicPartition> p) {
                    System.out.println("revoked=" + p);
                }

                public void onPartitionsAssigned(Collection<TopicPartition> p) {
                    System.out.println("assigned=" + p);
                }
            });
}
```

## 주의점

다중 작업 스레드 사용이 KafkaConsumer 객체의 스레드 안전성을 뜻하지 않는다. 파티션별 처리 순서와 커밋 위치를 별도로 관리한다.

## 꼬리질문

1. 컨슈머 수를 계속 늘려도 처리량이 증가하지 않는 파티션 조건은?
2. 파티션 3개인 그룹에 컨슈머 5개가 있으면 동시에 담당할 수 있는 컨슈머 수는 얼마일까?
3. 파티션을 잃을 때 진행 중 작업과 커밋을 처리하지 않으면 어떤 중복·순서 문제가 생길까?

</details>

## 참고 자료

- [Kafka 4.1 · Consumer Configs](https://kafka.apache.org/41/configuration/consumer-configs/) — 그룹 프로토콜·poll·커밋·타임아웃 옵션을 확인한다.
- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
