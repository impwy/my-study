# 지연·처리량·포화

> 부하가 늘 때 처리량·지연 분포·오류·대기열을 함께 보아 병목을 찾는다.

- 평균과 p95·p99는 다른 모습을 보여준다.
- 성공 처리량과 요청 발생량을 구분한다.
- 포화 뒤에는 대기와 실패가 늘 수 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

처리량은 단위 시간에 완료한 작업 수이고 지연은 한 작업에 걸린 시간이다. p95는 관측값의 약 95%가 그 이하인 경계를 나타낸다. 한 자원이 포화되면 요청을 더 넣어도 완료량이 비례해서 늘지 않고 큐·지연·오류가 증가할 수 있다. CPU·DB 연결·락·외부 API 같은 후보의 사용률과 대기 시간을 함께 관찰한다.

## Java 예제

작은 표본의 nearest-rank 계산이다. 운영 메트릭의 집계·히스토그램 오차와 표본 수를 따로 확인한다.

```java
import java.util.Arrays;

static long nearestRankP99(long[] millis) {
    if (millis.length == 0) throw new IllegalArgumentException();
    long[] sorted = millis.clone();
    Arrays.sort(sorted);
    return sorted[(int) Math.ceil(sorted.length * 0.99) - 1];
}
```

## 주의점

응답을 큐 적재 직후 반환하면 API 지연은 줄어도 업무 완료 지연은 남는다. 오류를 제외한 빠른 요청만으로 성능을 평가하지 않는다.

## 꼬리질문

1. API p99가 줄었는데 최종 저장 완료는 늦어지는 구조를 어떻게 설명할까?
2. 평균이 낮아도 p99가 높다면 어떤 사용자 경험이 숨겨질 수 있을까?
3. 비동기 처리에서 API 응답 시간만 측정하면 큐 대기와 최종 완료 지연을 어떻게 놓칠까?

함께 복습: [백프레셔와 요청 제한](backpressure-and-rate-limit.md) · [JDBC 연결과 트랜잭션](../../java/language/jdbc-boundary.md)

</details>

## 참고 자료

- [AWS · Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — 가용성·보안·성능·운영의 설계 기준을 확인한다.
- [Java SE 21 · ExecutorService](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/ExecutorService.html) — 작업 제출·종료·Future와 메모리 가시성 계약을 확인한다.
