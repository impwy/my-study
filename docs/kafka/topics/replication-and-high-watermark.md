# 복제·ISR·High Watermark

> 리더와 복제본의 로그 진도를 구분하고 소비 가능한 커밋 경계와 장애 시 남는 데이터를 확인한다.

- 파티션은 리더와 복제본을 가진다.
- ISR은 따라오는 복제본 집합이다.
- 복제 커밋과 컨슈머 오프셋 커밋은 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

프로듀서는 리더에 쓰고 복제본은 로그를 따라온다. 로그 끝 위치와 여러 복제본이 따라온 커밋 경계는 같지 않을 수 있다. High Watermark는 소비자에게 노출되는 복제 커밋 경계를 설명하는 중요한 값이다. 리더 변경 시 epoch·로그 절단 등의 규칙으로 차이를 조정한다. 컨슈머가 어디까지 처리했는지를 저장하는 offset commit과 이 복제 커밋은 목적이 다르다.

## Java 예제

ISR의 공통 복제 위치를 단순화한 모형이다. 실제 HW 갱신은 리더·복제 프로토콜에 따르며 트랜잭션 read_committed에는 LSO도 적용된다.

```java
static long boundary(long[] inSyncReplicaNextOffsets) {
    return java.util.Arrays.stream(inSyncReplicaNextOffsets).min().orElseThrow();
} // ISR의 next offset이 {15,13,14}이면 공통 복제 경계 모형은 13
```

## 주의점

acks=all이 모든 장애에서 손실 불가능을 뜻하지 않는다. 설정·리더 선출·저장 장치·클러스터 실패 조건을 함께 본다.

## 꼬리질문

1. 브로커의 커밋 경계와 컨슈머가 저장한 처리 위치를 혼동하면 어떤 진단 오류가 생기는가?
2. 경계가 13이면 일반적인 HW 의미에서 offset 13 레코드까지 읽을 수 있을까?
3. 브로커의 HW와 컨슈머 커밋 offset을 비교하면 복제 지연과 처리 지연을 어떻게 구분할까?

</details>

## 참고 자료

- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
- [Kafka 4.1 · Producer Configs](https://kafka.apache.org/41/configuration/producer-configs/) — acks·멱등성·배치·타임아웃의 상호 조건을 확인한다.
