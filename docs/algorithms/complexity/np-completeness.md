# P·NP·NP-완전

> 해를 구하는 비용과 주어진 해를 검증하는 비용을 구분한다.

- NP는 판정 문제의 검증 관점이다.
- NP-hard는 모든 NP 문제의 환원 관계로 정의한다.
- NP-완전은 NP이면서 NP-hard다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

NP를 “다항 시간에 절대 못 푼다”로 정의하지 않는다. 어떤 문제의 해 후보가 주어졌을 때 다항 시간에 검증할 수 있다는 관점이 중요하다. 다항 환원은 한 문제를 다른 문제의 입력으로 바꾸어 난이도 관계를 설명한다. P=NP인지 여부는 해결되지 않은 문제다.

## Java 예제

```java
static boolean verifiesSubset(int[] values, boolean[] chosen, long target) {
    if (values.length != chosen.length) return false;
    long sum = 0;
    for (int i = 0; i < values.length; i++) if (chosen[i]) sum += values[i];
    return sum == target;
} // {3, 5, 8}, {true, true, false}, 8 → true
```

## 주의점

근사 알고리즘의 보장은 문제의 조건에 의존한다. 특정 탐욕 휴리스틱이 모든 경우에 최적해를 준다고 쓰지 않는다.

## 꼬리질문

1. NP에 속한다는 사실만으로 NP-완전이라고 말할 수 없는 이유는?
2. 예제의 후보 검증과 모든 부분집합에서 후보를 찾는 작업은 비용이 어떻게 다를까?
3. 입력 수치가 큰 경우 O(n·target) DP가 입력 비트 수에 대한 다항 시간이라고 할 수 있을까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
