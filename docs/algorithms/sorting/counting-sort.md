# 계수 정렬

> 키별 개수를 세고 누적 개수로 정렬 위치를 계산한다.

- 작은 정수 키 범위가 전제다.
- 시간 O(n+k), 추가 공간은 구현에 따라 O(n+k).
- 안정 구현은 누적합과 배치 방향을 맞춘다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

비교 대신 각 키가 몇 번 나왔는지를 저장한다. 누적합은 해당 키 이하 원소의 총수를 나타내므로 마지막 배치 위치를 계산할 수 있다. 입력을 뒤에서부터 순회하며 해당 키의 누적값을 하나 줄여 결과 위치로 쓰면 같은 키의 순서가 보존된다. k가 입력 크기보다 지나치게 크면 비용이 커진다.

## Java 예제

```java
static int[] sort(int[] a, int max) {
    int[] count = new int[max + 1], out = new int[a.length];
    for (int x : a) count[x]++; // 0 <= x <= max
    for (int i = 1; i < count.length; i++) count[i] += count[i - 1];
    for (int i = a.length - 1; i >= 0; i--) out[--count[a[i]]] = a[i];
    return out;
}
```

## 주의점

음수 키는 오프셋 처리 등이 필요하다. 계수 정렬의 O(n)을 주장할 때 키 범위 k를 생략하지 않는다.

## 꼬리질문

1. 누적 개수와 “해당 키의 개수”는 어떻게 다를까?
2. 누적 개수에서 1을 먼저 뺀 값을 출력 인덱스로 쓰는 이유는 무엇일까?
3. 원소는 10개인데 최댓값이 10억이면 시간·공간 면에서 어떤 정렬을 선택할까?

</details>

## 참고 자료

- [Princeton · String Sorts](https://algs4.cs.princeton.edu/51radix/) — key-indexed counting과 기수 정렬의 비용·안정성을 확인한다.
