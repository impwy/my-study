# 암호화·해시·전자서명

> 암호화는 기밀성, 해시는 요약, 전자서명은 무결성과 서명자 확인을 위한 서로 다른 도구다.

- 대칭 암호는 공유 키를 사용한다.
- 비대칭 암호는 공개키·개인키 관계를 이용한다.
- 해시는 복호화하는 암호가 아니다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

대칭 키는 대량 데이터 암호화에 쓰며 상대와 안전하게 키를 공유해야 한다. 공개키 방식은 키 합의·서명 등 목적에 따라 사용한다. 해시는 입력의 고정 길이 요약을 만들며, 안전한 해시에는 역상·충돌 저항성 같은 요구가 있다. 서명은 개인키로 만들고 공개키로 검증한다. 실제 암호는 검증된 라이브러리와 안전한 모드·nonce 관리로 사용한다.

## Java 예제

GCM은 인증 태그를 포함한다. nonce는 복호화에 함께 필요하고 키와 조합해 재사용하면 안 된다. 키 생성·보관 정책은 별도로 정한다.

```java
import java.security.SecureRandom;

import javax.crypto.*;
import javax.crypto.spec.GCMParameterSpec;

static byte[] encrypt(byte[] message, SecretKey key, byte[] nonce) throws Exception {
    Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
    cipher.init(Cipher.ENCRYPT_MODE, key, new GCMParameterSpec(128, nonce));
    return cipher.doFinal(message);
}

static byte[] nonce() {
    byte[] n = new byte[12];
    new SecureRandom().nextBytes(n);
    return n;
}
```

## 주의점

DES·MD5 같은 역사적 알고리즘 설명을 신규 시스템의 선택지로 그대로 옮기지 않는다. 단순 SHA 해시만으로 비밀번호를 저장하지 않는다.

## 꼬리질문

1. 파일 해시 일치와 신뢰하는 공개키로 검증한 서명은 무엇을 다르게 보장하는가?
2. 같은 키와 nonce를 다시 쓰면 GCM의 기밀성·무결성에 어떤 위험이 생길까?
3. 공유 비밀키 기반 인증과 공개키 서명은 검증자·부인 방지 조건이 어떻게 다를까?

</details>

## 참고 자료

- [OWASP · Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 인증·인가·암호·입력 처리에 맞는 방어 지침을 찾아 읽는다.
- [RFC 8446 · TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html) — 인증·키 합의·암호화와 핸드셰이크 흐름을 확인한다.
