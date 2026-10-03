# 배낭 문제

> 용량과 사용 가능한 항목 상태를 정의해 최대 가치를 계산한다.

- 0/1은 각 항목 최대 한 번.
- 무한 배낭은 같은 항목 재사용 가능.
- 1차원 DP에서는 갱신 방향이 중요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

0/1의 선택은 현재 항목을 빼거나 한 번 넣고 이전 항목 상태를 보는 것이다. 무한 배낭은 넣은 뒤 같은 항목을 다시 사용할 수 있다. 용량만 남기는 1차원 최적화에서는 이전 회차를 보존하려면 큰 용량부터, 재사용하려면 작은 용량부터 갱신한다.

## Java 예제

양의 무게, 비음수 가치, 같은 길이의 두 배열과 int 범위의 결과를 가정한다.

```java
static int best(int[] weights, int[] values, int capacity) {
    int[] dp = new int[capacity + 1];
    for (int i = 0; i < weights.length; i++)
        for (int c = capacity; c >= weights[i]; c--)
            dp[c] = Math.max(dp[c], dp[c - weights[i]] + values[i]);
    return dp[capacity];
} // weights={2,3}, values={3,4}, capacity=5 → 7
```

## 주의점

O(NW)는 숫자 용량 W에 비례하는 의사 다항 시간이다. 입력 비트 길이에 대한 다항 시간이라고 표현하지 않는다.

## 꼬리질문

1. 0/1 배낭을 작은 용량부터 갱신하면 같은 항목을 어떻게 재사용하게 될까?
2. 무게 2·가치 3인 물건 하나와 용량 4에서 역순 갱신은 어떤 재사용을 막을까?
3. 모든 물건을 반드시 선택하는 문제라면 dp의 초기값과 불가능 상태를 어떻게 바꿔야 할까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
