# 배포 권한·상태 확인·롤백

> 검증한 산출물을 제한된 권한으로 실행 서버에 전달하고, 실제 서비스 상태를 확인한 뒤 실패를 복구한다.

- **단계:** CI 성공과 배포 성공을 구분한다.
- **권한:** OIDC는 신뢰 조건에 따른 임시 자격 증명을 사용한다.
- **운영:** 동시 배포와 상태 확인·롤백 기준을 정한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

테스트·빌드 뒤 어느 커밋의 산출물을 배포하는지 고정한다. Spring Boot의 JAR 배포를 예로 들면 GitHub Actions에서 검증한 실행 가능한 JAR를 EC2로 전달하고, 새 버전으로 실행하거나 재시작한 뒤 상태 확인 API를 호출한다. 구체적인 전달·프로세스 관리 방법은 선택한 배포 도구에 따라 달라진다.

```text
GitHub Actions: 테스트·빌드
    → 검증한 JAR 전달
    → EC2: 새 버전 실행
    → 서비스 상태 확인
```

S3를 배포 산출물의 중간 저장소로 사용하는 구조도 가능하다. 예를 들어 CodeDeploy는 S3에 저장한 애플리케이션 리비전을 EC2 배포에 사용할 수 있다. 이때 S3 업로드와 EC2에서의 다운로드·실행은 서로 다른 작업이며, S3가 JAR를 실행하는 것은 아니다. 파일을 직접 전달하는 방식을 선택하면 배포용 S3는 필수가 아니다.

VPC는 EC2가 사용하는 네트워크와 배포 통신 경로를 구성한다. 프라이빗 EC2에 GitHub 호스팅 러너가 직접 접속하려면 별도의 도달 경로가 필요하다. IAM으로 AWS API 호출이 허용되어도 네트워크 접속이나 SSH 로그인이 자동으로 허용되지는 않는다.

클라우드 인증은 저장한 장기 키 대신 OIDC 기반 역할을 검토하며 저장소·브랜치·환경 등 신뢰 조건을 제한한다. 배포 명령 성공 뒤 readiness·대표 요청·오류 지표를 확인한다. 실패 시 어떤 이전 버전으로 돌아가며 DB 변경이 호환되는지까지 계획한다.

## 주의점

컨테이너 이미지만 되돌려도 호환되지 않는 DB 마이그레이션은 되돌아가지 않는다. OIDC를 쓴다고 모든 브랜치를 신뢰해도 되는 것은 아니다. 단일 서버의 프로세스를 재시작하는 배포는 중단이 발생할 수 있으므로 상태 확인과 서비스 전환 방법을 함께 고려한다.

## 꼬리질문

1. 빌드한 파일을 S3에 올리는 것과 EC2에서 새 서비스를 실행하는 것은 왜 별개의 단계일까?
2. 배포 명령이 성공해도 readiness 확인이 실패하면 어떤 상태로 배포를 판단해야 할까?
3. 이전 버전으로 롤백하기 전에 DB 스키마 호환성을 확인하고, 대표 요청·오류 지표·롤백 조건을 함께 정해야 하는 이유는 무엇일까?

함께 복습: [워크플로·이벤트·잡·스텝](../workflows/events-jobs-steps.md) · [CI 캐시와 아티팩트](../ci/cache-and-artifacts.md) · [EC2·AMI·블록 스토리지](../../aws/ec2/instance-ami-storage.md) · [Actuator 상태와 메트릭](../../spring-boot/actuator/health-and-metrics.md)

</details>

## 참고 자료

- [GitHub · Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — 이벤트·잡·스텝·권한·의존 관계의 정확한 문법을 확인한다.
- [GitHub · OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect) — OIDC 토큰과 클라우드 신뢰 조건을 확인한다.
- [AWS · Upload an application revision to S3](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-wordpress-upload-application.html) — S3에 보관한 산출물을 CodeDeploy 배포에서 사용하는 구조를 확인한다.
