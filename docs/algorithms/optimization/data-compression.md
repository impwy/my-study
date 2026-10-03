# 무손실 압축

> 반복·빈도·사전을 이용해 원래 데이터를 복원할 수 있는 짧은 표현을 만든다.

- RLE는 연속 반복을 센다.
- Huffman은 빈도에 따라 prefix-free 코드를 만든다.
- 압축률은 데이터 특성에 의존한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

RLE는 AAAA를 문자 A와 횟수 4로 표현한다. Huffman은 낮은 빈도 둘을 반복 결합해 트리를 만들고 경로 비트로 문자를 표현한다. LZ 계열은 이전에 등장한 구간을 위치와 길이로 참조한다. 디코더가 사용할 메타데이터까지 전체 크기에 포함해야 한다.

## Java 예제

연속 반복을 이용하는 RLE 예제다. Huffman 코딩처럼 빈도로 부호 길이를 정하는 방식과 비교한다.

```java
static String encode(String s) { // 문자와 횟수를 구분하는 간단한 RLE
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < s.length(); ) {
        int j = i + 1;
        while (j < s.length() && s.charAt(j) == s.charAt(i)) j++;
        out.append((int) s.charAt(i)).append(':').append(j - i).append(';');
        i = j;
    }
    return out.toString();
} // "AAAB" → "65:3;66:1;"
```

## 주의점

기존 문자열 “압축” 예제 중 전체 문자 개수를 세거나 정렬해 세는 방식은 원래 순서를 복원하지 못할 수 있다. RLE와 구분한다.

## 꼬리질문

1. 문자별 전체 빈도만 저장하면 원래 문자열을 복원할 수 있을까?
2. 문자 코드와 개수를 구분하는 구분자를 빼면 복원 과정에 어떤 모호함이 생길까?
3. 반복이 거의 없는 입력에서는 이 RLE 결과가 원본보다 커지는 이유는 무엇일까?

</details>

## 참고 자료

- [Princeton · Data Compression](https://algs4.cs.princeton.edu/55compression/) — RLE·Huffman·사전 기반 압축의 조건을 비교한다.
