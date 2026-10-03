# 동적 계획법

> 반복되는 부분 문제의 결과를 저장해 큰 문제를 계산한다.

- 상태의 의미를 한 문장으로 정의한다.
- 점화식·초기값·계산 순서를 정한다.
- 메모이제이션과 표 채우기를 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

같은 부분 문제를 매번 다시 풀면 중복 비용이 커진다. DP는 결과를 저장하고 다시 사용한다. 최적화 문제에서는 작은 문제의 최적해를 이용해 전체 최적해를 만들 수 있는지 확인한다. 재귀에 저장을 붙인 top-down과 필요한 작은 상태부터 채우는 bottom-up이 있다.

## Java 예제

```java
static long ways(int n) { // 한 번에 1칸 또는 2칸
    if (n < 0 || n > 91) throw new IllegalArgumentException();
    long[] dp = new long[Math.max(2, n + 1)];
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];
    return dp[n];
} // ways(4) == 5
```

## 주의점

재귀를 쓴다고 자동으로 DP가 아니다. 상태에 필요한 정보를 빠뜨리면 서로 다른 부분 문제를 같은 것으로 취급한다.

## 꼬리질문

1. DP를 시작할 때 코드보다 상태의 의미를 먼저 적는 이유는?
2. dp[0]=1은 실제 이동 횟수가 0인 경우를 어떻게 해석한 값일까?
3. 직전 두 상태만 필요하다면 저장 공간을 O(1)로 줄일 수 있을까?

함께 복습: [배낭 문제](knapsack.md) · [최장 공통 부분 수열](lcs.md)

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
