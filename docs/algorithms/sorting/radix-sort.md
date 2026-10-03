# 기수 정렬

> 각 자리의 안정 정렬을 반복해 전체 키의 순서를 만든다.

- LSD 방식은 낮은 자리부터 처리한다.
- 각 자리 정렬의 안정성이 필요하다.
- 시간 O(d(n+k)), 자릿수 d와 기수 k를 본다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

낮은 자리 정렬 결과가 다음 자리 정렬에서도 같은 자리값 사이에 유지되어야 한다. 따라서 계수 정렬이나 큐를 이용한 안정적인 배치를 사용한다. 한 번에 전체 숫자를 비교하지 않지만 자리별 순서를 합쳐 전체 순서를 얻는다. 문자열·부호 있는 정수는 길이와 문자·부호 표현에 맞는 규칙이 필요하다.

## Java 예제

```java
static void digitPass(int[] a, long place) {
    int[] count = new int[10], out = new int[a.length];
    for (int x : a) count[(int) (x / place % 10)]++;
    for (int i = 1; i < 10; i++) count[i] += count[i - 1];
    for (int i = a.length - 1; i >= 0; i--) {
        int d = (int) (a[i] / place % 10);
        out[--count[d]] = a[i];
    }
    System.arraycopy(out, 0, a, 0, a.length);
} // 비음수 입력에 place=1, 10, 100 순서로 필요한 자리까지 적용
```

## 주의점

일의 자리 결과를 다음 단계가 뒤섞으면 이미 계산한 정보가 사라진다. 고정 길이 숫자 예제를 모든 문자열에 그대로 적용하지 않는다.

## 꼬리질문

1. 자리별 정렬이 불안정하면 LSD 기수 정렬이 실패하는 이유는?
2. 12와 11의 십의 자리 정렬에서 이전 일의 자리 순서를 유지해야 하는 이유는 무엇일까?
3. 음수를 포함한 입력에 이 코드를 그대로 쓰면 어떤 인덱스 오류가 생길까?

</details>

## 참고 자료

- [Princeton · String Sorts](https://algs4.cs.princeton.edu/51radix/) — key-indexed counting과 기수 정렬의 비용·안정성을 확인한다.
