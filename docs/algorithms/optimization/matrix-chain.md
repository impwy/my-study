# 행렬 연쇄 곱셈의 DP

> 곱셈 순서는 유지하면서 괄호 위치를 선택해 전체 스칼라 곱셈 수를 최소화한다.

- 행렬 차원이 각 곱셈 비용을 정한다.
- 부분 구간의 최소 비용을 상태로 둔다.
- 모든 분할 지점을 비교한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

A_i의 크기를 p_(i-1)×p_i라고 두면 m[i,j]는 i부터 j까지 곱할 최소 비용이다. 분할 k에 대해 m[i,k]+m[k+1,j]+p_(i-1)p_kp_j를 비교한다. 길이가 짧은 구간부터 채워야 필요한 부분 결과가 준비된다. 연산 순서의 수는 많지만 O(n²) 상태와 O(n) 분할을 사용해 기본 알고리즘은 O(n³)이다.

## Java 예제

양의 차원과 long 범위 안의 계산 비용을 가정한다.

```java
static long minimumCost(int[] p) { // 행렬 i의 크기: p[i] × p[i+1]
    int n = p.length - 1;
    long[][] dp = new long[n][n];
    for (int len = 2; len <= n; len++)
        for (int i = 0; i + len <= n; i++) {
            int j = i + len - 1;
            dp[i][j] = Long.MAX_VALUE;
            for (int k = i; k < j; k++)
                dp[i][j] =
                        Math.min(
                                dp[i][j],
                                dp[i][k] + dp[k + 1][j] + (long) p[i] * p[k + 1] * p[j + 1]);
        }
    return n == 0 ? 0 : dp[0][n - 1];
} // {10,30,5,60} → 4500
```

## 주의점

행렬의 순서를 마음대로 바꾸는 문제가 아니다. 실제 수치 오차·병렬 장치 비용은 이 기본 비용 모델과 별개다.

## 꼬리질문

1. 같은 세 행렬인데 괄호 위치에 따라 비용이 달라지는 이유는?
2. 분할 위치 k에서 마지막 곱셈의 세 차원이 p[i], p[k+1], p[j+1]인 이유는 무엇일까?
3. 최소 비용과 함께 괄호 배치도 출력하려면 어떤 선택을 저장해야 할까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
