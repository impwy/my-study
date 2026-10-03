# 문자열 매칭

> 패턴의 정보나 해시로 이미 한 비교를 줄이며 문자열에서 위치를 찾는다.

- 기본 비교의 최악 비용은 O(nm).
- KMP는 실패 정보로 패턴을 이동한다.
- 해시 일치는 실제 문자열 일치와 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

KMP는 일치했던 prefix와 suffix의 관계를 미리 계산해 텍스트 위치를 불필요하게 되돌리지 않는다. Boyer–Moore는 뒤에서 비교하고 불일치 문자·일치 접미부로 이동량을 정한다. Rabin–Karp는 구간 해시를 빠르게 갱신하되 충돌 가능성을 처리한다.

## Java 예제

아래는 기준이 되는 순진한 탐색이다. KMP·해시 기반 탐색과 비교할 때 사용한다.

```java
static int firstMatch(String text, String pattern) {
    for (int i = 0; i <= text.length() - pattern.length(); i++) {
        int j = 0;
        while (j < pattern.length() && text.charAt(i + j) == pattern.charAt(j)) j++;
        if (j == pattern.length()) return i;
    }
    return -1;
} // firstMatch("ABABAC", "ABAC") == 2
```

## 주의점

문자 인코딩과 길이의 단위를 정한다. Java char 인덱스가 모든 유니코드 문자의 수와 같은 것은 아니다.

## 꼬리질문

1. 해시가 같은 두 구간을 문자열 비교 없이 일치라고 결론 내리면 어떤 문제가 있을까?
2. 예제에서 실패한 접두사를 재사용하면 어떤 문자 비교를 줄일 수 있을까?
3. Java char 기준 위치와 사람이 세는 글자 위치가 달라질 수 있는 입력은 무엇일까?

</details>

## 참고 자료

- [Princeton · Substring Search](https://algs4.cs.princeton.edu/53substring/) — 브루트 포스·KMP·Boyer–Moore·Rabin–Karp를 비교한다.
