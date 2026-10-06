# 로그·파티션·오프셋

> Kafka는 파티션별 순서 있는 이벤트 로그에 레코드를 보관하고 소비자는 오프셋으로 읽기 위치를 관리한다.

- 순서와 오프셋은 파티션 안에서 정의된다.
- 소비했다고 레코드가 즉시 삭제되지는 않는다.
- 보존 로그와 소비 위치를 분리해 여러 소비와 재처리를 지원한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

토픽은 파티션으로 나뉘고 각 파티션은 순서 있는 로그를 가진다. 같은 키를 같은 파티션에 보내면 그 범위의 순서를 활용할 수 있지만 여러 파티션의 전역 순서를 당연히 얻지는 못한다. 보존 기간·크기·컴팩션 정책은 소비자의 위치와 별개다. 서로 다른 컨슈머 그룹이 같은 데이터를 각자의 목적과 속도로 읽을 수 있다.

“Kafka log”의 log는 레코드를 추가하는 저장 구조를 가리킬 수 있다. 애플리케이션 오류 메시지를 Kafka로 전송하는 경우의 로그 데이터와 구분해야 한다. [관측 도구의 로그](../../cloud/availability/observability-lgtm.md)는 발생 사건을 분석하는 자료라는 관점이다.

## Java 예제

Kafka clients 라이브러리가 필요하다. 위치 자료구조의 예시이며 브로커를 호출하지 않는다. 메서드는 클래스 안에 둔다.

```java
import org.apache.kafka.common.TopicPartition;
import java.util.HashMap;
import java.util.Map;

static void positions() {
    Map<TopicPartition, Long> next = new HashMap<>();
    next.put(new TopicPartition("orders", 0), 12L);
    next.put(new TopicPartition("orders", 1), 7L);
    System.out.println(next);
}
```

## 주의점

offset 12와 다른 파티션의 offset 7로 전체 시간 순서를 판단할 수 없다. 재처리하려는 오래된 데이터는 보존 정책으로 없어졌을 수 있다. 파티션 수 변경과 파티셔닝 정책도 같은 키의 배치와 순서 요구에 영향을 준다. 개발용 단일 브로커 구성은 가능하며 운영 브로커 수는 복제·장애 목표로 정한다. “항상 최소 3대”가 모든 Kafka 사용의 필수 조건은 아니다.

## 꼬리질문

1. 보존 정책과 소비 위치를 분리하면 여러 컨슈머가 무엇을 독립적으로 할 수 있는가?
2. 두 파티션의 offset 숫자가 다를 때 먼저 발생한 사건을 알아내려면 어떤 추가 정보가 필요한가?
3. 파티션 수를 늘리거나 보존 기간을 줄이면 기존 순서·재처리의 어떤 가정을 다시 확인해야 할까?

</details>

## 참고 자료

- [Apache Kafka 4.1 · Introduction](https://kafka.apache.org/41/getting-started/introduction/) — 토픽·파티션·키·이벤트 보존의 기본 관계를 읽는다.
- [Apache Kafka 4.1 · Quick Start](https://kafka.apache.org/41/getting-started/quickstart/) — 단일 개발 구성으로 생산·소비를 확인하는 흐름을 읽는다.
