# SQL Injection·XSS·CSRF

> 공격이 들어오는 경계와 피해가 발생하는 실행 문맥에 맞춰 웹 취약점을 방어한다.

- SQL에는 값 바인딩을 사용한다.
- 출력 인코딩은 HTML·속성·스크립트 문맥에 맞춘다.
- 쿠키 인증의 상태 변경 요청은 CSRF 방어를 검토한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

SQL Injection은 입력이 쿼리 문법으로 해석될 때 생기므로 파라미터 바인딩으로 값과 명령을 분리한다. XSS는 공격자의 내용이 사용자 브라우저에서 실행되는 문제로 안전한 출력 처리와 위험한 HTML 삽입 제한이 필요하다. CSRF는 브라우저가 자동 첨부하는 인증 정보로 사용자가 의도하지 않은 요청을 보내는 공격이다. 토큰·Origin 검사·SameSite 등 방어의 적용 조건을 확인한다.

## Java 예제

```java
import java.sql.*;

static void search(Connection c, String name) throws SQLException {
    try (PreparedStatement p = c.prepareStatement("SELECT id FROM users WHERE name = ?")) {
        p.setString(1, name);
        try (ResultSet r = p.executeQuery()) {
            while (r.next()) System.out.println(r.getLong(1));
        }
    }
} // name을 SQL 문장에 문자열 연결하지 않는다.
```

## 주의점

파라미터 바인딩은 동적으로 만든 테이블명·정렬 문법까지 자동 보호하지 않는다. HTTPS가 이 세 취약점을 자동 해결하지 않는다.

## 꼬리질문

1. SQL 값 바인딩과 HTML 출력 인코딩을 서로 대체할 수 없는 이유는?
2. name에 SQL 구문이 포함되어도 바인딩하면 값으로 취급되는 이유는 무엇일까?
3. 이 값이 HTML로 출력되거나 쿠키 기반 변경 요청에 쓰이면 XSS·CSRF는 각각 어떻게 따로 방어할까?

</details>

## 참고 자료

- [OWASP · Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 인증·인가·암호·입력 처리에 맞는 방어 지침을 찾아 읽는다.
