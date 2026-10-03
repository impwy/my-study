# 큰 정수 표현과 Karatsuba

> 고정 크기 정수 범위를 넘는 수를 자릿수 배열로 표현하고 곱셈의 재귀 구조를 개선한다.

- 자릿수 순서와 carry를 명확히 한다.
- 기본 곱셈은 자릿수별 곱을 누적한다.
- Karatsuba는 부분 곱 수를 줄인다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

큰 정수 덧셈은 각 자릿수와 carry를 합쳐 다음 자리로 넘긴다. 곱셈은 모든 자리 쌍의 곱을 누적하는 방식에서 시작한다. 두 수를 상·하위 두 부분으로 나누면 일반 분할 곱셈은 네 부분 곱을 요구한다. Karatsuba는 합의 곱을 이용해 세 부분 곱으로 줄여 충분히 큰 입력에서 점근 비용을 개선한다. 작은 입력에는 재귀·배열 비용이 더 클 수 있다.

## Java 예제

양의 정수와 bits > 0을 가정한 한 단계 분할이다. BigInteger 내부 알고리즘을 고정한다고 가정하지 않는다.

```java
import java.math.BigInteger;

static BigInteger threeProducts(BigInteger a, BigInteger b, int bits) {
    BigInteger ah = a.shiftRight(bits), al = a.subtract(ah.shiftLeft(bits));
    BigInteger bh = b.shiftRight(bits), bl = b.subtract(bh.shiftLeft(bits));
    BigInteger high = ah.multiply(bh), low = al.multiply(bl);
    BigInteger cross = ah.add(al).multiply(bh.add(bl)).subtract(high).subtract(low);
    return high.shiftLeft(2 * bits).add(cross.shiftLeft(bits)).add(low);
} // threeProducts(BigInteger.valueOf(123), BigInteger.valueOf(45), 4) = 5535
```

## 주의점

자릿수 수와 실제 정수 값을 복잡도 변수로 혼동하지 않는다. 문자열 순서만으로 숫자 대소를 비교하면 길이·부호 조건을 놓친다.

## 꼬리질문

1. 부분 곱을 줄였어도 작은 입력에서 기본 곱셈이 빠를 수 있는 이유는?
2. cross를 세 번의 곱셈으로 구할 때 빼는 high와 low는 각각 무엇일까?
3. 이 예제가 완전한 재귀 Karatsuba 구현이 되려면 분할·종료 조건을 어디에 추가해야 할까?

</details>

## 참고 자료

- [Java · BigInteger](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigInteger.html) — 임의 정밀도 정수 연산과 API 계약을 확인한다.
- [MIT · Algorithms Lecture Notes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/lecture-notes/) — 분할 정복·점화식 분석의 강의 자료를 찾아 읽는다.
