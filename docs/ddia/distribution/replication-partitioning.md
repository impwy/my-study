# 복제와 파티셔닝

> 복제는 사본을 늘리고 파티셔닝은 데이터를 나누며 각각 가용성·용량·운영의 다른 문제를 다룬다.

- 복제와 샤딩은 다르다.
- 복제 지연과 핫 파티션을 고려한다.
- 분할 키는 조회·쓰기 패턴에 영향을 준다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

복제는 같은 데이터를 여러 노드에 두어 장애 대비·읽기 분산 등에 사용한다. 파티셔닝은 데이터나 로그를 키·범위 등으로 나누어 저장·처리한다. 같은 설계에 두 방법을 함께 사용할 수 있다. 특정 키에 요청이 몰리면 분할해도 하나의 파티션이 병목이 되며, 복제본에 최신 값이 바로 보이지 않는다면 쓰기 직후 읽기 요구를 따로 해결해야 한다.

## Java 예제

단순 해시 분할 모형이다. 운영 저장소는 정해진 해시·가상 노드·데이터 이동 절차를 사용한다.

```java
static int partition(String key, int count) {
    if (count < 1) throw new IllegalArgumentException();
    return Math.floorMod(key.hashCode(), count);
} // 분할 위치만 결정; 복제본 수는 별도 설정
```

## 주의점

이 내용은 Kafka·DB 강의에서 확인한 원리를 교차 정리한 것이다. 제목만 있는 DDIA 독서 기록을 읽은 것으로 취급하지 않는다.

## 꼬리질문

1. 파티션을 늘리는 것과 복제 수를 늘리는 것이 처리·장애에 각각 어떤 영향을 주는가?
2. count를 바꾸면 기존 키의 위치가 얼마나 바뀔 수 있으며 재배치가 왜 필요할까?
3. 한 고객 키에 요청이 몰리면 파티션 수를 늘려도 핫스폿이 남는 이유는 무엇일까?

</details>

## 참고 자료

- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
- [Redis · Replication](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/) — 비동기 복제와 읽기 지연·장애 시 손실 가능성을 확인한다.
