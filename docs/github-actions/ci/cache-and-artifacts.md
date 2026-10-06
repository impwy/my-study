# CI 캐시와 아티팩트

> CI에서 소스 코드를 테스트·빌드해 산출물을 만들고, 의존성 캐시와 배포용 아티팩트는 목적에 맞게 구분한다.

- **빌드:** 러너가 코드를 가져와 실행 환경을 준비하고 컴파일·테스트·패키징한다.
- **캐시:** 의존성 재사용으로 시간을 줄이되 캐시가 없어도 빌드가 재현되어야 한다.
- **아티팩트:** 테스트 보고서와 검증한 빌드 결과를 보관·전달한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

GitHub Actions의 워크플로는 저장소의 `.github/workflows/` 아래 YAML 파일로 정의한다. 예를 들어 `main`에 push할 때 실행하도록 설정하면 러너가 코드를 checkout하고 JDK·Gradle 환경을 준비해 빌드 명령을 실행한다. GitHub 호스팅 러너를 선택하면 이 작업은 GitHub가 제공하는 작업용 실행 환경에서 진행한다.

Spring Boot·Gradle 프로젝트에서는 프로젝트에 맞는 JDK와 저장소에 포함된 Gradle Wrapper를 사용해 `./gradlew build`를 실행할 수 있다. 기본적인 구성에서는 의존성 다운로드·컴파일·테스트·패키징을 수행하고, `build/libs/`에 JAR를 만든다. Spring Boot 플러그인의 실행 가능한 Boot JAR와 일반 JAR가 함께 생길 수 있으므로 배포할 산출물을 명확히 선택한다. 테스트나 태스크 구성이 다르면 실제 수행 작업도 달라진다.

```text
코드 push → checkout → JDK·Gradle 준비 → 테스트·빌드 → JAR 보관
```

캐시는 lockfile·OS·도구 버전 등으로 키를 정해 의존성 다운로드를 줄일 수 있다. 아티팩트는 테스트 보고서·패키지·이미지 관련 결과를 잡·실행 사이에 전달하거나 보관한다. 캐시 적중 여부가 테스트 성공의 근거가 되어서는 안 되고 오래된 산출물이 검증을 우회하지 않아야 한다. 빌드는 명시된 의존성과 코드로 결과를 만들 수 있어야 한다.

## 주의점

JAR를 빌드하거나 GitHub 아티팩트로 보관하는 단계만으로 EC2의 서비스가 업데이트되지는 않는다. 별도의 전달·실행·상태 확인이 필요하다. 비밀 값을 캐시·아티팩트·로그에 넣지 않는다. 외부 PR이 쓰기 권한이나 신뢰하는 배포 경로를 얻지 않게 한다.

## 꼬리질문

1. 소스 코드를 빌드하는 작업과 빌드한 JAR를 EC2에서 실행하는 작업은 어떤 차이가 있을까?
2. 의존성 파일 해시 외에 OS·JDK 버전이 캐시 키에 필요한 경우는 무엇이며, 캐시가 없어지면 빌드는 어떻게 동작해야 할까?
3. 캐시와 배포용 artifact를 같은 용도로 취급하면 검증·보존·재현성에서 어떤 차이를 놓칠까?

함께 복습: [워크플로·이벤트·잡·스텝](../workflows/events-jobs-steps.md) · [배포 권한·상태 확인·롤백](../cd/deployment-oidc-and-rollback.md)

</details>

## 참고 자료

- [GitHub · Building and testing Java with Gradle](https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-gradle) — checkout·JDK·Gradle 빌드와 JAR 아티팩트 보관 흐름을 확인한다.
- [GitHub · Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) — 캐시 키·복원 범위·접근 조건을 확인한다.
- [GitHub · Store and share data with workflow artifacts](https://docs.github.com/en/actions/tutorials/store-and-share-data) — 빌드 결과와 보고서를 잡 사이에 전달하는 방법을 확인한다.
