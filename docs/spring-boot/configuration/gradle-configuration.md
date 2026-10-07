# Spring Boot 멀티모듈의 Gradle 설정 사용법

> settings는 프로젝트 구성을, build는 플러그인·의존성·작업을 정의한다.

- **구조:** settings.gradle.kts의 include와 projectDir로 프로젝트와 실제 폴더를 연결한다.
- **공통 설정:** allprojects와 subprojects는 적용 범위가 다르며 루트 설정 전체가 상속되는 것은 아니다.
- **의존성:** implementation·api·testImplementation은 사용·노출 범위를 구분한다.

<details>
<summary>설명과 Kotlin DSL 예제 펼치기</summary>

## 설명

`settings.gradle.kts`는 Gradle 프로젝트 이름과 위치를 정한다. 각 `build.gradle.kts`는 해당 프로젝트에 적용할 플러그인과 의존성·작업을 정한다. Kotlin DSL의 `.kts`와 Groovy DSL의 `.gradle`은 같은 역할의 서로 다른 문법이다.

루트의 `allprojects { }`는 루트와 하위 프로젝트를, `subprojects { }`는 하위 프로젝트만 설정한다. 루트 블록 밖의 `dependencies { }`는 루트 프로젝트의 의존성이다. 하위 프로젝트에 자동 복제되지 않는다. `apply false`는 플러그인을 현재 프로젝트에 적용하지 않고 다른 프로젝트에서 적용할 준비를 하는 표현이다.

## 예제

Gradle 9 계열의 Java Library 플러그인을 사용하는 Kotlin DSL 예시다. 실제 디렉터리와 Wrapper가 준비되어 있어야 한다.

`settings.gradle.kts`:

```kotlin
rootProject.name = "backend"
include(":apps", ":member", ":shared", ":test-support")
project(":member").projectDir = file("contexts/member")
```

등록한 프로젝트는 `:member`이고 실제 위치는 `contexts/member`다. 묶음 폴더인 `contexts`를 별도 프로젝트로 만들 필요는 없다.

루트 `build.gradle.kts`의 공통 설정 예시:

```kotlin
allprojects {
    repositories { mavenCentral() }
}

subprojects {
    apply(plugin = "java-library")
    tasks.withType<Test>().configureEach {
        useJUnitPlatform()
    }
}
```

업무 모듈 `build.gradle.kts`의 의존성 예시:

```kotlin
dependencies {
    implementation(project(":shared"))
    testImplementation(project(":test-support"))
}
```

| 구성 | 필요한 상황 |
| --- | --- |
| implementation | 모듈 구현이 사용하는 의존성; 소비자의 컴파일 클래스패스에는 재노출하지 않음 |
| api | 공개 메서드·타입에 노출되는 의존성을 소비자에게도 제공 |
| testImplementation | 해당 모듈의 테스트 컴파일·실행 의존성 |
| runtimeOnly | 실행에만 필요한 의존성, 예: JDBC 드라이버 |
| compileOnly / annotationProcessor | 컴파일 시 타입 / 애너테이션 처리, 예: Lombok |

위 코드는 설정 조각이며 완전한 Spring Boot 빌드는 아니다. 실행 프로젝트에 Boot 플러그인을 적용하고, Java toolchain과 Boot·Modulith BOM을 맞추는 구성은 별도로 필요하다. BOM은 버전을 관리하며 라이브러리를 저절로 추가하지 않는다.

Wrapper로 구조와 클래스패스를 확인한다.

```bash
./gradlew projects
./gradlew :member:test
./gradlew :member:dependencies --configuration testRuntimeClasspath
./gradlew :apps:bootJar
```

## 주의점

`implementation`은 소비자의 컴파일 클래스패스 노출을 줄이며, 런타임 의존성까지 없애는 설정은 아니다. 테스트 공통 코드가 `test-support/src/main`에 있다면 그 코드를 컴파일하는 의존성은 test-support의 `implementation` 또는 `api`에 있어야 한다. 테스트 공통 JAR의 소비자는 이를 `testImplementation`으로 참조한다.

공통 설정이 커지면 convention plugin으로 옮기는 방법을 검토한다. 공통 test-support를 모든 모듈에 추가할 때 자기 자신을 의존하지 않도록 제외한다. 빌드 파일 위치와 Java 패키지 위치도 별개다. 관련 구조는 [멀티모듈 구성](multi-module-builds.md)에서 확인한다.

## 꼬리질문

1. settings의 프로젝트 등록과 build의 의존성 선언은 왜 서로 다른 역할일까?
2. contexts/member 폴더를 :member로 등록하고 테스트 전용 공통 모듈을 사용하려면 어디에 무엇을 선언할까?
3. implementation을 api로 넓히거나 공통 설정을 모든 프로젝트에 적용하면 어떤 결합이 증가할까?

</details>

## 참고 자료

- [Gradle · Multi-Project Builds](https://docs.gradle.org/current/userguide/multi_project_builds.html) — include와 projectDir의 의미를 확인한다.
- [Gradle · Project DSL](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html) — allprojects와 subprojects의 적용 범위를 확인한다.
- [Gradle · Java Library Plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html) — api와 implementation의 컴파일·실행 범위를 확인한다.
