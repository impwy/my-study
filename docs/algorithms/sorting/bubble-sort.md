# 버블 정렬

> 인접한 원소를 교환해 가장 큰 값을 뒤쪽에 확정한다.

- 한 회차마다 최댓값이 뒤에 놓인다.
- 최악 O(n²), 조기 종료 구현의 최선 O(n).
- 같을 때 교환하지 않으면 안정적이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

왼쪽부터 인접한 두 값을 비교하고 역순일 때 교환한다. 큰 값이 연속 교환으로 오른쪽 끝까지 이동한다. 다음 회차에는 확정된 끝 구간을 제외한다. 한 회차에 교환이 전혀 없었다면 전체가 정렬된 상태이므로 멈출 수 있다.

## Java 예제

```java
static void sort(int[] a) {
    for (int end = a.length - 1; end > 0; end--) {
        boolean swapped = false;
        for (int i = 0; i < end; i++)
            if (a[i] > a[i + 1]) {
                int t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
                swapped = true;
            }
        if (!swapped) break;
    }
}
```

## 주의점

조기 종료를 넣지 않은 구현까지 최선 O(n)이라고 쓰지 않는다. 비교 조건이 >=이면 같은 키의 상대 순서를 바꿀 수 있다.

## 꼬리질문

1. 교환이 없었던 회차가 정렬 완료의 증거가 되는 이유는?
2. 각 회차에서 end 위치에 어떤 값이 확정될까?
3. 비교 조건을 >에서 >=로 바꾸면 중복 키의 안정성과 조기 종료에 어떤 영향이 있을까?

</details>

## 참고 자료

- [Princeton · Elementary Sorts](https://algs4.cs.princeton.edu/21elementary/) — 비교·교환 횟수와 정렬 과정을 그림으로 확인한다.
