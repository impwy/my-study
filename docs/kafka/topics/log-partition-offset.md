# 로그·파티션·오프셋

> Kafka는 토픽의 파티션별 추가 로그에 레코드를 저장하고 오프셋으로 위치를 식별한다.

- 순서는 파티션 안에서 정의된다.
- 오프셋은 파티션별 위치다.
- 소비했다고 레코드가 즉시 삭제되지는 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

토픽은 여러 파티션으로 나뉘며 각 파티션은 순서 있는 로그를 가진다. 같은 키의 레코드를 같은 파티션에 보내면 그 범위의 순서를 활용할 수 있다. 파티션이 다르면 하나의 전역 순서를 당연히 얻지 못한다. 데이터 보존은 시간·크기·압축 정책으로 정하며 컨슈머의 읽기 위치와 별개다. 컨슈머 그룹이 다르면 같은 로그를 다른 목적과 속도로 읽을 수 있다.

## Java 예제

Kafka clients 라이브러리가 필요하다. 위치 자료구조를 보여 주며 브로커 호출은 하지 않는다.

```java
import org.apache.kafka.common.TopicPartition;

import java.util.*;

static void positions() {
    Map<TopicPartition, Long> next = new HashMap<>();
    next.put(new TopicPartition("orders", 0), 12L);
    next.put(new TopicPartition("orders", 1), 7L);
    System.out.println(next); // offset은 파티션별로 따로 관리
}
```

## 주의점

파티션 오프셋은 토픽 전체의 전역 일련번호가 아니다. 오래된 오프셋의 데이터는 보존 정책으로 이미 지워졌을 수 있다.

## 꼬리질문

1. 같은 토픽의 두 레코드가 서로 다른 파티션에 있으면 순서를 어떻게 판단해야 하는가?
2. 파티션 0의 offset 12와 파티션 1의 offset 7로 전체 토픽의 시간 순서를 판단할 수 있을까?
3. 같은 키의 이벤트 순서를 유지하려면 파티션 선택과 파티션 수 변경에서 무엇을 고려해야 할까?

</details>

## 참고 자료

- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
