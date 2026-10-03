# 스트림 파이프라인

> 스트림은 데이터 저장소가 아니라 원소를 필터링·변환·집계하는 계산 흐름이다.

- 중간 연산은 대체로 지연 실행된다.
- 최종 연산이 파이프라인을 소비한다.
- 공유 상태를 바꾸는 람다는 피한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

컬렉션에서 스트림을 만들고 filter·map 같은 중간 연산을 연결한 뒤 collect·reduce 같은 최종 연산으로 결과를 얻는다. 중간 연산 선언만으로 모든 원소가 처리되는 것은 아니다. 최종 연산과 단축 평가에 따라 실제 처리 범위가 달라진다. 같은 스트림을 최종 연산 뒤 다시 사용하는 것은 지원되지 않는다. 반복문보다 항상 빠르다는 기준으로 선택하지 않는다.

## Java 예제

```java
import java.util.List;

static void demo() {
    var stream = List.of(1, 2, 3).stream().filter(x -> x > 1).map(x -> x * 10);
    System.out.println(stream.toList()); // [20,30]: 최종 연산 때 평가
    // stream.count()를 이어서 호출하면 이미 사용한 스트림이므로 실패
}
```

## 주의점

parallelStream이 공유 ArrayList를 안전하게 만들어 주지 않는다. 병렬 처리의 비용·순서·블로킹 작업을 따로 고려한다.

## 꼬리질문

1. filter와 map만 연결하고 최종 연산을 하지 않으면 왜 결과가 없는가?
2. filter와 map의 순서를 바꾸면 결과와 처리 비용은 항상 같을까?
3. 공유 가변 상태를 수정하는 map을 parallel stream에서 실행하면 어떤 위험이 있을까?

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
