# 보간 탐색

> 정렬된 값의 분포로 목표가 있을 위치를 추정한다.

- 값 분포가 고른 데이터에서 유리하다.
- 최악 O(n)까지 악화될 수 있다.
- 분모 0·범위 밖·오버플로를 처리한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

이진 탐색이 가운데 인덱스를 고르는 데 비해 보간 탐색은 양 끝 값과 목표값의 비율을 이용한다. 추정이 좋으면 비교를 줄이지만 값이 치우쳐 있으면 한쪽으로 조금씩만 이동할 수 있다. 정렬 조건은 여전히 필요하며 추정 위치가 현재 구간 안에 있는지도 확인한다.

## Java 예제

```java
static int find(int[] a, int x) {
    int lo = 0, hi = a.length - 1;
    while (lo <= hi && x >= a[lo] && x <= a[hi]) {
        if (a[lo] == a[hi]) return a[lo] == x ? lo : -1;
        int p = lo + (int) (((long) x - a[lo]) * (hi - lo) / ((long) a[hi] - a[lo]));
        if (a[p] == x) return p;
        if (a[p] < x) lo = p + 1;
        else hi = p - 1;
    }
    return -1;
}
```

## 주의점

a[left]==a[right]일 때 나눗셈을 수행하지 않는다. 평균 O(log log n)은 분포 가정이 있는 결과다.

## 꼬리질문

1. 큰 값 몇 개가 몰려 있으면 위치 추정이 왜 부정확해질까?
2. 모든 원소가 5인 배열에서 분모가 0이 되는 문제를 어떤 분기가 막을까?
3. 분포가 치우친 입력에서 이진 탐색으로 전환하는 기준을 무엇으로 잡을까?

</details>

## 참고 자료

- [Princeton · Analysis of Algorithms](https://algs4.cs.princeton.edu/14analysis/) — 입력 크기와 연산 횟수를 연결하고 측정과 분석을 구분한다.
