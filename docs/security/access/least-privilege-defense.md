# 최소 권한과 방어 계층

> 필요한 주체에게 필요한 범위의 권한만 주고 여러 경계에서 실패를 제한한다.

- 기본 거부에서 필요한 권한을 열어 간다.
- 예방·탐지·대응은 역할이 다르다.
- 보안 로그와 권한 변경을 추적한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파일 ACL·서비스 계정·방화벽·애플리케이션 인가를 각 경계에 맞게 설정한다. 방화벽은 트래픽을 제한하지만 허용된 요청의 업무 권한까지 판단하지 않는다. IDS는 이상 징후를 탐지하며 IPS는 차단 기능을 포함할 수 있다. 한 방어가 실패했을 때 피해가 모든 데이터와 계정으로 번지지 않도록 권한과 네트워크·서비스 경계를 나눈다.

## Java 예제

애플리케이션의 기본 거부 모형이다. 실제 IAM·DB 권한 판정 전체를 구현하지 않는다.

```java
enum Action {
    READ_ORDER,
    DELETE_USER
}

static void require(java.util.Set<Action> allowed, Action requested) {
    if (!allowed.contains(requested)) throw new SecurityException("denied");
}
// require(Set.of(Action.READ_ORDER), Action.DELETE_USER) → 거부
```

## 주의점

탐지 제품 설치만으로 대응이 완성되지 않는다. 오탐·알림 처리·로그 보존·사고 후 복구 정책도 함께 정한다.

## 꼬리질문

1. 애플리케이션 계정이 탈취되었을 때 최소 권한이 피해 범위를 어떻게 줄이는가?
2. 조회만 필요한 서비스에 삭제 권한까지 주면 침해 시 피해 범위가 어떻게 넓어질까?
3. 애플리케이션 검사가 우회되더라도 DB·네트워크 계층 제한이 남아야 하는 이유는 무엇일까?

</details>

## 참고 자료

- [OWASP · Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 인증·인가·암호·입력 처리에 맞는 방어 지침을 찾아 읽는다.
- [AWS · IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) — 정책·역할·임시 자격 증명과 최소 권한을 확인한다.
