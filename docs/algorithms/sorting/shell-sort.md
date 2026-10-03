# 셸 정렬

> 멀리 떨어진 원소를 먼저 정리한 뒤 간격을 줄여 삽입 정렬한다.

- gap별 부분 수열을 정렬한다.
- 마지막 gap은 1이다.
- 비용은 gap 수열에 따라 달라진다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

인접 이동만 하는 삽입 정렬의 먼 거리 이동 비용을 줄이려는 방법이다. gap이 4라면 0,4,8과 1,5,9처럼 같은 나머지 위치를 묶어 정렬한다. 간격을 줄여 반복하면 마지막 삽입 정렬은 이미 어느 정도 정리된 데이터를 받는다.

## Java 예제

```java
static void sort(int[] a) {
    for (int gap = a.length / 2; gap > 0; gap /= 2)
        for (int i = gap; i < a.length; i++) {
            int value = a[i], j = i;
            while (j >= gap && a[j - gap] > value) {
                a[j] = a[j - gap];
                j -= gap;
            }
            a[j] = value;
        }
}
```

## 주의점

모든 gap 수열에 같은 시간 복잡도를 주장하지 않는다. 멀리 있는 값의 교환은 같은 키의 상대 순서를 바꿀 수 있다.

## 꼬리질문

1. 마지막 gap이 1이 아니면 정렬 완료를 보장할 수 있을까?
2. gap=2일 때 [4, 3, 2, 1]은 어떤 두 부분 수열로 나뉠까?
3. 간격 수열을 바꾸면 최악 시간 복잡도도 같은 값이라고 말할 수 있을까?

</details>

## 참고 자료

- [Princeton · Elementary Sorts](https://algs4.cs.princeton.edu/21elementary/) — 비교·교환 횟수와 정렬 과정을 그림으로 확인한다.
