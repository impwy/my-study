# 최장 공통 부분 수열

> 순서를 유지하며 건너뛸 수 있는 두 문자열의 가장 긴 공통 수열을 찾는다.

- 부분 수열은 연속일 필요가 없다.
- dp[i][j]는 두 prefix의 LCS 길이다.
- 길이 표와 문자열 인덱스를 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

끝 문자가 같으면 앞 prefix의 LCS에 1을 더한다. 다르면 한쪽 끝 문자를 제외한 두 상태 중 큰 값을 선택한다. i,j는 문자 개수이므로 실제 문자 접근은 i−1,j−1이다. 값이 어느 상태에서 왔는지 추적하면 실제 수열도 복원할 수 있다.

## Java 예제

```java
static int length(String a, String b) {
    int[][] dp = new int[a.length() + 1][b.length() + 1];
    for (int i = 1; i <= a.length(); i++)
        for (int j = 1; j <= b.length(); j++)
            dp[i][j] =
                    a.charAt(i - 1) == b.charAt(j - 1)
                            ? dp[i - 1][j - 1] + 1
                            : Math.max(dp[i - 1][j], dp[i][j - 1]);
    return dp[a.length()][b.length()];
} // length("ABC", "AC") == 2
```

## 주의점

LCS와 최장 공통 부분 문자열을 혼동하지 않는다. 동률 경로가 여러 개면 복원된 수열도 여러 개일 수 있다.

## 꼬리질문

1. 두 끝 문자가 다를 때 왜 위쪽·왼쪽 상태 중 최댓값을 볼까?
2. LCS와 연속된 공통 부분 문자열의 차이가 점화식에 어떻게 드러날까?
3. 길이 대신 실제 수열을 반환하려면 어떤 경로를 역추적해야 할까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
