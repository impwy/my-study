# 철근 자르기

> 첫 조각 길이와 남은 길이의 최적 수익을 조합한다.

- dp[length]는 그 길이의 최대 수익.
- 모든 첫 절단 길이를 비교한다.
- 선택을 저장하면 절단 방법을 복원한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

길이 n의 수익은 price[cut]+dp[n−cut] 중 최댓값이다. 길이 0의 수익은 0으로 둔다. 같은 남은 길이를 여러 번 계산하므로 DP로 재사용한다. 작은 길이부터 표를 채우면 기본 시간은 O(n²)이다.

## Java 예제

```java
static int revenue(int[] price, int n) { // price[i]: 길이 i 가격, price[0]=0
    int[] dp = new int[n + 1];
    for (int len = 1; len <= n; len++) {
        int best = Integer.MIN_VALUE;
        for (int first = 1; first <= len; first++)
            best = Math.max(best, price[first] + dp[len - first]);
        dp[len] = best;
    }
    return dp[n];
}
```

## 주의점

절단 비용이 있으면 점화식에 포함해야 한다. 최대 수익만 저장하면 실제 절단 방법을 바로 복원하지 못한다.

## 꼬리질문

1. 처음 자르는 길이를 모두 비교해야 하는 이유는?
2. 길이 1·2·3의 가격이 1·5·6이면 길이 3의 최대 수익은 얼마일까?
3. 절단마다 비용이 발생하면 자르지 않는 경우와 자르는 경우의 점화식을 어떻게 구분할까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
