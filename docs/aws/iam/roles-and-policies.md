# IAM 역할과 정책

> AWS 자원 접근은 주체·정책·조건으로 판단하고 장기 키 대신 적절한 임시 자격 증명을 사용한다.

- 사용자·역할·정책의 책임이 다르다.
- 역할은 신뢰 정책과 권한 정책을 가진다.
- 최소 권한과 MFA·감사를 함께 적용한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

정책은 어떤 주체가 어떤 자원에 어떤 행동을 할 수 있는지 정의한다. 역할을 맡을 수 있는 조건은 신뢰 정책이, 맡은 뒤의 접근은 권한 정책이 영향을 준다. 서비스 역할과 작업용 임시 자격 증명을 사용하면 배포 파일에 장기 키를 넣을 필요를 줄인다. 실제 허용 판단은 리소스 정책·상위 제한·명시적 거부 등도 함께 고려한다.

## Java 예제

AWS SDK for Java 2.x의 sts 모듈·리전·자격 증명이 필요하다. 실제 AWS 조회를 수행한다.

```java
import software.amazon.awssdk.services.sts.StsClient;
import software.amazon.awssdk.services.sts.model.GetCallerIdentityRequest;

static String callerArn() {
    try (StsClient sts = StsClient.create()) {
        return sts.getCallerIdentity(GetCallerIdentityRequest.builder().build()).arn();
    }
} // 기본 자격 증명 체인 사용; 장기 키를 코드에 넣지 않음
```

## 주의점

Allow 하나가 있다는 이유로 항상 허용되는 것은 아니다. 명시적 Deny와 조직·세션 등의 제한을 확인한다.

## 꼬리질문

1. 역할의 신뢰 정책과 권한 정책은 각각 어떤 질문에 답하는가?
2. 호출자 ARN을 확인했다고 S3 객체 읽기 권한까지 검증된 것은 왜 아닐까?
3. 환경 변수의 키와 인스턴스 역할이 함께 있을 때 SDK 체인의 우선순위는 어떤 영향을 줄까?

함께 복습: [최소 권한과 방어 계층](../../security/access/least-privilege-defense.md) · [인증과 인가](../../security/identity/authentication-authorization.md)

</details>

## 참고 자료

- [AWS · IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) — 정책·역할·임시 자격 증명과 최소 권한을 확인한다.
- [Java API 사용 안내](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-chain.html) — 자격 증명 공급자 체인의 탐색 순서와 임시 자격 증명 사용을 확인한다.
