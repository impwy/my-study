# lower bound와 upper bound

> 정렬된 데이터에서 값의 존재보다 경계 위치를 찾아 중복 구간을 계산한다.

- lower: 처음으로 target 이상인 위치.
- upper: 처음으로 target보다 큰 위치.
- 반열린 구간 [left, right)을 유지한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

경계를 찾으면 없는 값의 삽입 위치와 같은 값의 개수도 표현할 수 있다. lower bound는 mid 값이 target보다 작으면 왼쪽을 버리고, 그렇지 않으면 mid를 포함한 왼쪽 구간을 남긴다. 오른쪽 초기값을 n으로 두면 결과가 n일 수도 있다. upper bound는 버리는 조건에 같음을 포함한다.

## Java 예제

```java
static int bound(int[] a, int x, boolean upper) {
    int lo = 0, hi = a.length; // [lo, hi)
    while (lo < hi) {
        int m = lo + (hi - lo) / 2;
        if (a[m] < x || (upper && a[m] == x)) lo = m + 1;
        else hi = m;
    }
    return lo;
} // [1, 2, 2, 4]에서 lower(2)=1, upper(2)=3
```

## 주의점

일반 이진 탐색의 “찾으면 반환”을 쓰면 경계를 보장하지 않는다. 배열 길이 n을 결과로 받았을 때 바로 인덱싱하지 않는다.

## 꼬리질문

1. 같은 값의 개수를 upper−lower로 구할 수 있는 이유는 무엇일까?
2. 예제에서 x가 3일 때 두 경계는 각각 어디를 가리킬까?
3. hi를 배열 길이로 두어도 a[hi]에 접근하지 않는 이유는 무엇일까?

</details>

## 참고 자료

- [Princeton · Analysis of Algorithms](https://algs4.cs.princeton.edu/14analysis/) — 입력 크기와 연산 횟수를 연결하고 측정과 분석을 구분한다.
