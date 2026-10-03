# 재시도·DLT·재처리

> 실패한 이벤트의 원인·원문·처리 이력을 보존하고 안전한 재처리와 정합성 확인을 설계한다.

- 일시 장애와 영구 실패를 구분한다.
- 재처리는 중복 실행에 안전해야 한다.
- DLT 이동이 업무 성공을 뜻하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

일시적인 DB 연결 실패는 제한된 재시도로 복구될 수 있지만 잘못된 형식·권한·영구 제약 실패를 무한 재시도하면 파티션이 막힌다. 정해진 정책 뒤 실패 이벤트를 별도 토픽에 기록하고 원인 해결 후 선택적으로 재처리한다. 발행 성공과 최종 DB 반영 성공을 구분하고 추적 식별자로 결과를 확인한다. 중복 방어와 정합성 대사는 함께 필요하다.

## Java 예제

Kafka clients. 전송 확인 후 원본 offset 처리가 따로 필요하다. 오류 이유·횟수·업무 식별자는 공개 가능한 형태로 함께 기록한다.

```java
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.producer.*;

import java.nio.charset.StandardCharsets;

static void deadLetter(
        KafkaProducer<String, String> producer, ConsumerRecord<String, String> failed)
        throws Exception {
    var out =
            new ProducerRecord<String, String>(
                    failed.topic() + ".DLT", failed.key(), failed.value());
    out.headers()
            .add(
                    "source-offset",
                    Long.toString(failed.offset()).getBytes(StandardCharsets.UTF_8));
    out.headers()
            .add(
                    "source-partition",
                    Integer.toString(failed.partition()).getBytes(StandardCharsets.UTF_8));
    producer.send(out).get();
}
```

## 주의점

오류를 catch하고 정상 반환하면 프레임워크가 성공으로 판단할 수 있다. DLT 전달·원본 커밋의 실패 정책도 확인한다.

## 꼬리질문

1. 재발행 성공과 업무 복구 완료를 서로 다른 상태로 두는 이유는?
2. DLT 전송 성공 뒤 원본 커밋 전에 종료되면 어떤 중복이 다시 생길까?
3. DLT 재발행이 성공한 것과 실제 업무 복구가 완료된 것을 어떤 식별자·상태로 구분할까?

</details>

## 참고 자료

- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
- [Kafka 4.1 · Consumer Configs](https://kafka.apache.org/41/configuration/consumer-configs/) — 그룹 프로토콜·poll·커밋·타임아웃 옵션을 확인한다.
