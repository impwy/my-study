# 병합 정렬

> 배열을 나눠 정렬한 뒤 두 정렬 구간을 비교하며 합친다.

- 분할 정복 구조.
- 시간 Θ(n log n), 배열 구현의 보조 공간 O(n).
- 동률에서 왼쪽을 먼저 고르면 안정적이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

나누기만으로 정렬되는 것이 아니라 병합 단계가 순서를 만든다. 두 구간의 맨 앞 중 작은 값을 결과에 넣고 그 구간의 포인터만 이동한다. 한 단계에서 전체 원소를 훑고 단계 수가 log n이므로 n log n 비용이 된다. 재귀 대신 작은 구간부터 합치는 bottom-up 방식도 있다.

## Java 예제

```java
import java.util.Arrays;

static int[] sort(int[] a) {
    if (a.length < 2) return a.clone();
    int m = a.length / 2;
    int[] l = sort(Arrays.copyOfRange(a, 0, m)), r = sort(Arrays.copyOfRange(a, m, a.length));
    int[] out = new int[a.length];
    int i = 0, j = 0;
    for (int k = 0; k < out.length; k++)
        out[k] = j == r.length || (i < l.length && l[i] <= r[j]) ? l[i++] : r[j++];
    return out;
}
```

## 주의점

일반 배열 병합은 보조 배열을 사용한다. 연결 리스트 구현이나 특수 in-place 구현의 공간 비용과 혼동하지 않는다.

## 꼬리질문

1. 정렬되지 않은 두 구간에도 같은 병합 절차를 쓰면 왜 실패할까?
2. 병합 비교에서 <=를 쓰면 왼쪽과 오른쪽의 같은 키 중 무엇이 먼저 나올까?
3. 이 구현이 생성하는 임시 배열과 재귀 스택의 최대 동시 공간을 어떻게 구분할까?

</details>

## 참고 자료

- [Princeton · Mergesort](https://algs4.cs.princeton.edu/22mergesort/) — 분할·병합 과정과 보조 배열 비용을 확인한다.
