# 큰 정수 표현과 Karatsuba

> 고정 크기 정수 범위를 넘는 수를 자릿수 배열로 표현하고 곱셈의 재귀 구조를 개선한다.

- 자릿수 순서와 carry를 명확히 한다.
- 기본 곱셈은 자릿수별 곱을 누적한다.
- Karatsuba는 부분 곱 수를 줄인다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

큰 정수 덧셈은 각 자릿수와 carry를 합쳐 다음 자리로 넘긴다. 곱셈은 모든 자리 쌍의 곱을 누적하는 방식에서 시작한다. 두 수를 상·하위 두 부분으로 나누면 일반 분할 곱셈은 네 부분 곱을 요구한다. Karatsuba는 합의 곱을 이용해 세 부분 곱으로 줄여 충분히 큰 입력에서 점근 비용을 개선한다. 작은 입력에는 재귀·배열 비용이 더 클 수 있다.

## 예제

123+89를 낮은 자리부터 계산하면 3+9=12에서 2를 남기고 carry 1을 전달한다. Java 업무 코드에서는 직접 구현보다 BigInteger의 계약을 먼저 검토한다.

## 주의점

자릿수 수와 실제 정수 값을 복잡도 변수로 혼동하지 않는다. 문자열 순서만으로 숫자 대소를 비교하면 길이·부호 조건을 놓친다.

## 복습 질문

부분 곱을 줄였어도 작은 입력에서 기본 곱셈이 빠를 수 있는 이유는?

자료 구분: **기존 자료** — 알고리즘·자료구조 노트와 대학 강의의 원리·예제. **공식 자료 보완** — 복잡도 전제·경계 조건·Java 계약.

</details>

## 참고 자료

- [Java · BigInteger](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigInteger.html) — 임의 정밀도 정수 연산과 API 계약을 확인한다.
- [MIT · Algorithms Lecture Notes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/lecture-notes/) — 분할 정복·점화식 분석의 강의 자료를 찾아 읽는다.
- [홍정모 연구소](https://honglab.co.kr/) — 기존 학습 노트의 원 강의 출처. 강의의 설명과 실습 맥락을 더 확인한다.
