# 누적합과 투 포인터

> 반복 구간 계산을 전처리하거나 단조롭게 이동하는 두 경계로 중복 탐색을 줄인다.

- 누적합은 정적 구간 합에 맞는다.
- 투 포인터는 이동의 근거가 필요하다.
- 음수·변경·오버플로 조건을 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

길이 n 배열에 prefix[0]=0, prefix[i+1]=prefix[i]+a[i]를 만들면 반열린 구간 [l,r)의 합은 prefix[r]-prefix[l]이다. 값이 바뀌면 단순 누적합의 갱신 비용을 고려한다. 투 포인터는 조건에 따라 경계를 뒤로 되돌리지 않고 움직일 수 있을 때 선형 탐색이 가능하다. 양수 연속 합과 임의 음수 배열은 같은 이동 규칙을 쓰지 못한다.

## Java 예제

```java
static long[] prefix(int[] a) {
    long[] p = new long[a.length + 1];
    for (int i = 0; i < a.length; i++) p[i + 1] = p[i] + a[i];
    return p;
}

static long range(long[] p, int left, int right) {
    return p[right] - p[left];
}
// [left, right); {2,3,4}의 [1,3) 합은 7
```

## 주의점

각 포인터가 한 방향으로 n번 움직인다는 근거가 있어야 O(n)이다. 단지 포인터 두 개가 있다고 선형 알고리즘은 아니다.

## 꼬리질문

1. 음수를 허용하면 합이 크다는 이유로 왼쪽을 줄이는 규칙이 왜 깨질 수 있는가?
2. p[0]=0을 두면 배열 시작부터의 합을 어떤 동일한 식으로 계산할 수 있을까?
3. 누적합의 원소 하나를 바꾸면 뒤쪽 상태를 얼마나 갱신해야 하며 어떤 자료구조가 대안일까?

</details>

## 참고 자료

- [Princeton · Analysis of Algorithms](https://algs4.cs.princeton.edu/14analysis/) — 입력 크기와 연산 횟수를 연결하고 측정과 분석을 구분한다.
