# 진법·보수·부동소수점

> 비트 패턴은 표현 규칙에 따라 정수·문자·실수가 되며 범위와 정밀도에 제한이 있다.

- 비트 수는 표현 가능한 경우의 수를 제한한다.
- 2의 보수 정수의 범위는 비대칭이다.
- 부동소수점은 많은 실수를 근사한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

같은 비트도 부호 없는 수와 2의 보수 해석에서 다르게 읽힌다. n비트 2의 보수 정수는 -2^(n-1)부터 2^(n-1)-1까지 나타낸다. 실수는 부호·지수·유효 숫자 등으로 표현해 넓은 범위를 얻지만 유한 비트로 모든 값을 정확하게 저장하지 못한다. 연산에서 넘침·반올림·오차 누적을 따로 고려한다.

## Java 예제

```java
static void demo() {
    byte bits = (byte) 0b11111111;
    System.out.println(bits); // signed: -1
    System.out.println(Byte.toUnsignedInt(bits)); // unsigned 해석: 255
    System.out.println(0.1 + 0.2 == 0.3); // false
}
```

## 주의점

작은 자료형의 덧셈 결과와 언어의 승격·오버플로 규칙을 구분한다. 화폐는 요구에 맞는 정수 단위·십진 표현을 검토한다.

## 꼬리질문

1. 같은 비트가 두 가지 숫자가 되는 이유와 0.1+0.2 비교의 오차는 각각 어떤 표현 문제인가?
2. 8비트 11111111의 부호 있는 해석과 부호 없는 해석은 왜 다를까?
3. 금액의 소수 계산을 정확하게 하려면 double 대신 어떤 표현과 반올림 정책을 선택할까?

</details>

## 참고 자료

- [MIT OCW · Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — 논리 회로에서 CPU·메모리까지 강의와 도식을 따라 확인한다.
- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
