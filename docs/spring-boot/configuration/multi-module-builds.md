# Spring Boot 멀티모듈과 의존성 방향

> 멀티모듈은 코드를 여러 빌드 단위로 나누고, 필요한 참조를 의존성으로 명시하는 구성이다.

- **전제:** 하나의 Gradle 빌드에 여러 프로젝트를 등록한다.
- **원리:** 각 모듈은 자신의 소스와 의존성을 사용하며, 실행 앱이 필요한 모듈을 조립한다.
- **주의:** 모듈 수와 JVM·배포 단위의 수는 별개의 결정이다.

<details>
<summary>설명과 구조 예제 펼치기</summary>

## 설명

멀티모듈에서는 라이브러리 모듈마다 컴파일과 테스트 범위를 정할 수 있다. 모듈 A에서 B의 타입을 쓰려면 A에 B 의존성을 선언해야 한다. 같은 저장소에 있거나 같은 JVM에서 실행된다는 이유만으로 모든 타입을 컴파일 시점에 참조할 수 있는 것은 아니다.

Spring Boot 실행 프로젝트와 업무 라이브러리를 나란히 둘 수 있다. `apps`는 실행 프로젝트 자체의 이름일 수도, 여러 실행 프로젝트를 묶는 폴더일 수도 있다. 정해진 이름보다 등록한 Gradle 프로젝트와 의존성 방향이 중요하다.

```text
backend/
├── apps/                 # Spring Boot 실행 프로젝트
├── contexts/
│   ├── member/           # 업무 라이브러리
│   └── lecture/          # 업무 라이브러리
├── global/               # 전역 설정·인프라
├── shared/               # 공유 계약·값 타입
└── test-support/         # 테스트 공통 인프라

apps → member, lecture, global, shared
member, lecture, global → shared
업무 모듈의 테스트 → test-support
```

이 배치는 하나의 구성 예시다. 업무 라이브러리는 일반 JAR로 만들고, 실행 프로젝트의 `bootJar`가 필요한 라이브러리를 포함하면 한 JVM에서 실행할 수 있다. Spring 빈·엔티티·Repository 탐지에는 별도로 클래스패스와 패키지 탐지 범위가 맞아야 한다.

## 주의점

루트의 `src`는 하위 모듈에 자동으로 공유되지 않는다. 루트 `build.gradle.kts`도 파일 전체가 상속되는 것이 아니라 `allprojects`, `subprojects` 또는 공통 플러그인에서 적용한 설정이 공유된다. 루트에만 선언한 `dependencies`가 모든 모듈의 의존성이 되는 것은 아니다.

`shared`에 모든 업무 로직을 모으면 모듈 간 결합이 다시 커진다. 공개 계약과 값 타입 중심으로 작게 유지한다. 빌드 경계와 업무 경계의 차이는 [바운디드 컨텍스트](../../ddd/contexts/bounded-context.md), 등록·의존성 문법은 [Gradle 설정 사용법](gradle-configuration.md)에서 이어서 읽는다.

## 꼬리질문

1. 같은 저장소에 있는 다른 모듈의 타입을 쓰려면 왜 의존성을 선언해야 할까?
2. 실행 앱이 회원·강의 모듈을 한 JAR에 포함할 때 빌드 단위와 실행 단위는 각각 몇 개일까?
3. 모듈을 분리했는데도 shared와 다른 모듈의 내부 타입을 널리 참조하면 어떤 경계가 약해질까?

</details>

## 참고 자료

- [Gradle · Multi-Project Builds](https://docs.gradle.org/current/userguide/multi_project_builds.html) — 프로젝트 등록과 디렉터리 배치를 확인한다.
- [Spring Boot · Packaging Executable Archives](https://docs.spring.io/spring-boot/gradle-plugin/packaging.html) — 실행 JAR이 클래스와 의존성을 포함하는 방식을 확인한다.
- [Gradle · Java Library Plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html) — 라이브러리의 공개 의존성과 내부 의존성 차이를 읽는다.
