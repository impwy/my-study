# 그리디

> 지금의 최선 선택을 반복하되 전체 최적해와 연결되는 근거를 확인한다.

- 지역 최선이 전체 최선을 항상 보장하지 않는다.
- 교환 논증 등으로 정당성을 설명한다.
- 문제 조건이 바뀌면 규칙을 다시 검증한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

탐욕 선택은 이미 한 선택을 되돌리지 않는 방식이다. 활동 선택에서는 종료가 가장 빠른 활동을 먼저 골라도 최적해 하나를 유지할 수 있다는 근거가 있다. 하지만 0/1 배낭을 가치/무게 비율 순으로 고르면 남은 공간 때문에 더 좋은 조합을 놓칠 수 있다.

## Java 예제

```java
import java.util.*;

record Meeting(int start, int end) {}

static int maximumMeetings(List<Meeting> input) {
    var meetings = new ArrayList<>(input);
    meetings.sort(Comparator.comparingInt(Meeting::end));
    int end = Integer.MIN_VALUE, count = 0;
    for (Meeting m : meetings)
        if (m.start() >= end) {
            end = m.end();
            count++;
        }
    return count;
}
```

## 주의점

분할 가능한 배낭의 비율 규칙을 0/1 배낭에 그대로 옮기지 않는다. 예제 몇 개 통과는 최적성 증명이 아니다.

## 꼬리질문

1. 그리디 선택을 다른 선택으로 교환해도 최적해가 유지되는지 어떻게 설명할까?
2. 가장 짧은 회의보다 가장 일찍 끝나는 회의를 고르는 이유는 무엇일까?
3. 회의마다 보상이 다르면 개수 최대화의 그리디가 보상 최대화에도 통할까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
