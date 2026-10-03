# 슬라이딩 윈도우

> 연속 구간을 옮길 때 빠지는 정보와 새로 들어오는 정보만 갱신한다.

- 고정 길이 합은 빼기·더하기로 갱신한다.
- 첫 구간을 기준으로 최댓값을 초기화한다.
- 가변 길이는 조건의 단조성을 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

길이 k의 합을 매 구간마다 계산하면 O((n-k+1)k)가 든다. 첫 구간 합을 만든 뒤 왼쪽에서 빠지는 값을 빼고 오른쪽에서 들어오는 값을 더하면 전체를 O(n), 추가 공간 O(1)에 처리한다. 합·빈도·중복 여부 등 어떤 정보를 유지할지 먼저 정한다. 최솟값처럼 빠진 값을 단순히 빼서 복원할 수 없는 집계에는 다른 구조가 필요하다.

## Java 예제

```java
static long maxSum(int[] a, int k) {
    if (k < 1 || k > a.length) throw new IllegalArgumentException();
    long sum = 0;
    for (int i = 0; i < k; i++) sum += a[i];
    long best = sum;
    for (int i = k; i < a.length; i++) {
        sum += (long) a[i] - a[i - k];
        best = Math.max(best, sum);
    }
    return best;
} // {-4,-2,-7}, k=2 → -6
```

## 주의점

0<k<=n 조건을 검증한다. 음수가 있는 가변 구간에서는 합이 커지거나 작아지는 방향이 일정하지 않아 단순 이동 규칙이 깨질 수 있다.

## 꼬리질문

1. 구간 최솟값은 합처럼 빠지는 값을 빼고 새 값을 더할 수 없는 이유는?
2. best를 0으로 초기화하면 모든 값이 음수인 입력에서 왜 틀릴까?
3. 창 크기가 가변이고 합의 상한을 만족해야 한다면 어떤 입력 조건에서 두 포인터가 가능할까?

함께 복습: [누적합과 투 포인터](prefix-sum-and-two-pointers.md) · [덱](../../data-structures/stack-queue/deque.md)

</details>

## 참고 자료

- [Princeton · Analysis of Algorithms](https://algs4.cs.princeton.edu/14analysis/) — 입력 크기와 연산 횟수를 연결하고 측정과 분석을 구분한다.
- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
