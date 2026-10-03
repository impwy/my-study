# 프로듀서 배치·acks·재시도

> 전송 효율과 확인 수준을 조정하되 재시도·시간 제한·순서에 미치는 영향을 함께 확인한다.

- 배치는 파티션 단위로 모인다.
- acks는 브로커 확인 조건을 정한다.
- 처리량과 지연은 측정으로 비교한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

send는 직렬화·파티션 선택·버퍼 적재를 거쳐 전송으로 이어진다. batch.size와 linger.ms는 얼마나 모아 보낼지에 영향을 주며 압축은 네트워크·CPU 비용을 바꾼다. acks=0·1·all은 확인하는 수준이 다르다. 재시도는 일시 장애를 복구할 수 있지만 확인 응답 유실과 중복·순서를 고려해야 한다. 성공 여부는 Future·콜백 등 결과로 확인한다.

## Java 예제

Kafka clients. 설정 조각이며 처리량·지연을 측정해 조정한다.

```java
import org.apache.kafka.clients.producer.ProducerConfig;

import java.util.Properties;

static Properties tuning() {
    Properties p = new Properties();
    p.put(ProducerConfig.ACKS_CONFIG, "all");
    p.put(ProducerConfig.LINGER_MS_CONFIG, 5);
    p.put(ProducerConfig.BATCH_SIZE_CONFIG, 32768);
    return p; // bootstrap.servers·serializer는 별도로 설정
}
```

## 주의점

기본값은 클라이언트 버전에 따라 달라질 수 있다. 슬라이드의 설정 값을 모든 환경의 권장값으로 복사하지 않는다.

## 꼬리질문

1. 배치를 크게 하면 네트워크 효율이 좋아져도 어떤 지연 비용이 늘 수 있는가?
2. linger.ms=5가 배치가 가득 찬 경우에도 반드시 5ms를 기다린다는 뜻일까?
3. acks=all에서 필요한 복제 수 조건은 min.insync.replicas와 ISR 상태에 어떻게 달릴까?

</details>

## 참고 자료

- [Kafka 4.1 · Producer Configs](https://kafka.apache.org/41/configuration/producer-configs/) — acks·멱등성·배치·타임아웃의 상호 조건을 확인한다.
