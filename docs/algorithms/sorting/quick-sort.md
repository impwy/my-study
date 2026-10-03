# 퀵 정렬

> 피벗보다 작은 값과 큰 값을 나누고 각 구간을 정렬한다.

- 분할 규칙과 재귀 구간을 맞춘다.
- 평균·기대 O(n log n), 최악 O(n²).
- 일반 in-place 구현은 안정적이지 않다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

피벗 기준 분할은 병합 없이 구간 사이의 순서를 정한다. 각 구간 내부만 다시 정렬하면 된다. 편향된 피벗이 계속 선택되면 한쪽 크기만 1씩 줄어 비용이 제곱으로 커진다. 무작위 피벗과 같은 키를 모으는 3-way 분할은 특정 입력의 편향을 줄인다.

## Java 예제

```java
static void sort(int[] a, int lo, int hi) {
    if (lo >= hi) return;
    int pivot = a[lo], lt = lo, i = lo + 1, gt = hi;
    while (i <= gt) {
        if (a[i] < pivot) swap(a, lt++, i++);
        else if (a[i] > pivot) swap(a, i, gt--);
        else i++;
    }
    sort(a, lo, lt - 1);
    sort(a, gt + 1, hi);
}

static void swap(int[] a, int i, int j) {
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
}
```

## 주의점

Hoare와 Lomuto 분할은 반환값과 다음 재귀 범위가 다르다. “반환된 인덱스는 항상 피벗 최종 위치”라고 가정하지 않는다.

## 꼬리질문

1. 모든 값이 같은 배열에서 3-way 분할은 어떤 중복 작업을 줄일까?
2. gt와 교환한 뒤 i를 바로 증가시키지 않는 이유는 무엇일까?
3. 이미 정렬된 서로 다른 값에서 첫 원소 피벗의 재귀 깊이를 줄이려면 어떻게 바꿀까?

</details>

## 참고 자료

- [Princeton · Quicksort](https://algs4.cs.princeton.edu/23quicksort/) — 분할 불변식과 중복 키 처리 방법을 확인한다.
