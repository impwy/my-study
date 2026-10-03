# PKI와 이메일 보안

> 공개키의 소유 관계를 신뢰 사슬로 검증하고 이메일의 서명·암호화를 목적별로 적용한다.

- 인증서는 공개키와 신원 정보를 연결한다.
- 서명과 암호화의 보장은 다르다.
- 유효 기간·폐기·신뢰 기준이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

공개키가 누구의 키인지 확인하지 못하면 서명을 검증해도 원하는 상대의 진위가 확인되지 않는다. PKI는 인증 기관과 신뢰 사슬·유효성 검사를 통해 이 관계를 다룬다. S/MIME 같은 이메일 보안은 서명으로 변경·서명자를 확인하거나 암호화로 내용을 보호할 수 있다. 전달 채널 TLS와 메시지 자체의 보호도 범위가 다르다.

## Java 예제

```java
import java.security.cert.X509Certificate;

static void inspect(X509Certificate certificate) throws Exception {
    certificate.checkValidity();
    System.out.println(certificate.getSubjectX500Principal());
    System.out.println(certificate.getIssuerX500Principal());
} // 유효 기간 확인만으로 신뢰 체인 검증이 완료되지는 않는다.
```

## 주의점

암호화한 이메일에도 제목·메타데이터 등 보호 범위를 확인한다. 옛 강의의 약한 알고리즘을 신규 설정으로 선택하지 않는다.

## 꼬리질문

1. 이메일 전송 구간 TLS와 메시지 자체 암호화는 어느 경계를 다르게 보호하는가?
2. 인증서 유효 기간이 정상이어도 신뢰하지 않는 발급자라면 무엇을 더 검증해야 할까?
3. 메일 서버 간 TLS만 사용하면 중간 메일 서버가 본문을 읽을 수 있는 이유는 무엇일까?

</details>

## 참고 자료

- [RFC 8551 · S/MIME 4.0](https://www.rfc-editor.org/rfc/rfc8551.html) — 이메일 메시지의 서명·암호화 보장 범위를 확인한다.
- [RFC 8446 · TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html) — 인증·키 합의·암호화와 핸드셰이크 흐름을 확인한다.
