# CORS와 브라우저 출처

> CORS는 다른 출처의 응답을 웹 페이지에 공유할 수 있는지 정하며 서버 인증·인가와 별개다.

- 출처는 스킴·호스트·포트로 구분한다.
- 일부 요청은 OPTIONS 프리플라이트를 보낸다.
- 허용 메서드 설정은 엔드포인트를 만들지 않는다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

브라우저는 웹 페이지가 다른 출처로 보내는 요청의 응답 접근을 CORS 규칙으로 제한한다. 필요한 요청은 먼저 허용 출처·메서드·헤더를 확인하는 프리플라이트를 한다. 서버의 Controller 요청 매핑과 CORS 정책, 보안 인가는 서로 다른 판단이다. 쿠키 등 자격 증명을 포함하는 경우에는 허용 출처·credentials 조합과 보안 필터 연동을 확인한다.

## 주의점

CORS는 비브라우저 클라이언트의 접근을 막는 일반 인증 장치가 아니다. 임의 Origin을 자격 증명과 함께 신뢰하지 않는다.

## 꼬리질문

1. curl은 성공하는데 브라우저에서 실패하면 어떤 정책 차이를 확인해야 하는가?
2. 허용되지 않은 Origin에 헤더를 안 주어도 curl 요청 자체를 막는 것은 왜 아닐까?
3. 쿠키를 포함하는 요청을 허용하려면 와일드카드 Origin 대신 어떤 추가 계약이 필요할까?

함께 복습: [인증과 인가](../../security/identity/authentication-authorization.md) · [Spring MVC 요청 처리](../../spring/mvc/request-flow.md)

</details>

## 참고 자료

- [Spring MVC · CORS](https://docs.spring.io/spring-framework/reference/web/webmvc-cors.html) — 출처·프리플라이트·허용 설정의 적용 방식을 확인한다.
- [OWASP · Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 인증·인가·암호·입력 처리에 맞는 방어 지침을 찾아 읽는다.
