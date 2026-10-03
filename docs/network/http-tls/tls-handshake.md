# TLS와 HTTPS

> TLS는 상대 인증·키 합의로 만든 보안 채널에 HTTP를 실어 전송 중 데이터를 보호한다.

- 인증서 검증은 서버 신원 확인에 중요하다.
- 세션 키는 대칭 암호화에 사용된다.
- HTTPS는 애플리케이션 권한 검사를 대신하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

TLS 1.3 연결은 지원하는 알고리즘과 키 교환 정보를 협상하고 서버의 인증서·서명 등을 검증하며 공유 키를 만든다. 이후 데이터는 인증된 암호화로 보호된다. 인증서의 신뢰 사슬, 유효 기간, 접속 이름 확인은 다른 서버와 통신하는 실수를 줄인다. HTTP가 이 채널 위에서 전달되는 것이 HTTPS다. 연결 암호화와 사용자 로그인·업무 인가는 서로 다른 층의 책임이다.

## Java 예제

```java
import javax.net.ssl.*;

static void connect(String host, int port) throws java.io.IOException {
    try (SSLSocket socket =
            (SSLSocket) SSLSocketFactory.getDefault().createSocket(host, port)) {
        SSLParameters p = socket.getSSLParameters();
        p.setEndpointIdentificationAlgorithm("HTTPS");
        socket.setSSLParameters(p);
        socket.startHandshake();
        System.out.println(socket.getSession().getProtocol());
    }
}
```

## 주의점

검증을 끄면 암호화를 사용해도 상대 신원을 신뢰할 수 없다. TLS 1.3의 0-RTT는 재전송 위험을 고려해 업무 요청에 적용한다.

## 꼬리질문

1. HTTPS와 API 접근 권한 검사가 동시에 필요한 이유는?
2. 신뢰하는 CA의 인증서 검증 외에 호스트 이름 검증도 필요한 이유는 무엇일까?
3. TLS 연결에 성공한 사용자의 특정 주문 조회 권한은 어느 계층에서 검사해야 할까?

</details>

## 참고 자료

- [RFC 8446 · TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html) — 인증·키 합의·암호화와 핸드셰이크 흐름을 확인한다.
