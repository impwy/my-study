# Problem Details 오류 계약

> 오류 응답을 공통 구조로 표현하고 업무 오류를 기계가 구분할 수 있게 한다.

- 상태 코드와 오류 본문을 일치시킨다.
- 오류 타입·발생 위치·확장 필드를 구분한다.
- 내부 구현·민감 정보는 숨긴다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

서버의 오류를 클라이언트가 일관되게 해석하려면 자유로운 문자열만 반환하는 방식보다 공통 계약이 필요하다. Problem Details는 type·title·status·detail·instance 같은 필드를 정의하고 추가 업무 코드도 확장할 수 있다. 같은 오류 타입의 title은 안정적으로 쓰고 구체적인 이번 실패는 detail에 담는다. HTTP 상태와 본문의 status를 모순되게 만들지 않는다.

## 예제

재고 소진이면 409와 `application/problem+json` 응답으로 현재 상태 충돌을 나타내고, 별도의 안정적인 `code`로 SOLD_OUT을 표현할 수 있다.

## 주의점

스택 트레이스·SQL·비밀번호·토큰을 detail에 넣지 않는다. 클라이언트 로직은 사람이 읽는 번역 문자열의 완전 일치에 의존하지 않는다.

## 복습 질문

사용자용 오류 메시지와 프로그램이 분기하는 오류 코드를 구분하는 이유는?

자료 구분: **기존 자료** — 네트워크 워크북과 API 학습 자료의 설계 원리. **공식 자료 보완** — 논문·RFC·조회 계약.

</details>

## 참고 자료

- [RFC 9457 · Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) — 오류 필드와 확장 항목의 표준 의미를 확인한다.
- [RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 메서드·상태 코드·조건부 요청의 의미를 확인한다.
