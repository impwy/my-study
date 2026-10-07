# Spring Modulith와 애플리케이션 모듈

> Spring Modulith는 Spring Boot 앱 안의 업무 모듈과 공개 경계를 모델링하고 검증하는 도구다.

- **전제:** 업무 책임을 Java 패키지와 공개 계약으로 표현한다.
- **원리:** 모듈 구조를 탐지해 의존성 검증·모듈 통합 테스트·문서화를 지원한다.
- **주의:** 모놀리스는 실행·배포 구조이며 Spring Modulith는 그 구조를 지원하는 라이브러리다.

<details>
<summary>설명과 설정 예제 펼치기</summary>

## 설명

모놀리스는 애플리케이션을 하나의 배포 단위로 구성하는 형태다. 업무별 내부 경계를 유지하면 모듈형 모놀리스라고 부를 수 있다. 하나의 JVM에서 여러 라이브러리를 조립한 앱도 이 형태로 설계할 수 있다.

Spring이 제공하는 제품 이름은 **Spring Modulith**다. 별도로 Spring Monolith라는 도구를 사용하는 것은 아니다. Spring Modulith는 패키지에 기반한 애플리케이션 모듈을 다루며, Gradle 프로젝트 자체를 모듈로 인식하는 도구는 아니다. 따라서 Gradle 멀티모듈 없이도 사용할 수 있다.

기본 탐지는 Spring Boot 실행 클래스 패키지의 직접 하위 패키지를 기준으로 한다. `explicitly-annotated` 전략을 사용하면 `@ApplicationModule`로 표시한 패키지를 모듈로 탐지한다. 단순한 묶음 디렉터리 이름과 탐지되는 Java 패키지는 별도로 확인한다.

## 예제

Spring Modulith 2.1 계열의 `spring-modulith-starter-core`와 테스트용 `spring-modulith-starter-test`를 사용하는 설정 예시다. 검사 대상 클래스와 모든 대상 모듈이 테스트 클래스패스에 있어야 한다.

업무 패키지의 `package-info.java`:

```java
@org.springframework.modulith.ApplicationModule(
    allowedDependencies = "shared"
)
package com.example.member;
```

모듈 탐지 설정:

```yaml
spring:
  modulith:
    detection-strategy: explicitly-annotated
```

구조 검증 테스트:

```java
import org.junit.jupiter.api.Test;
import org.springframework.modulith.core.ApplicationModules;

class ModularityTest {
    @Test
    void verifyModules() {
        ApplicationModules.of(ExampleApplication.class).verify();
    }
}
```

`ExampleApplication`은 `com.example`의 실제 Spring Boot 실행 클래스를 뜻한다. `verify()`는 순환 의존, 내부 패키지 접근, 지정한 허용 의존성 위반을 확인한다. 클래스패스에 없는 모듈과 SQL 수준의 스키마 간 JOIN·FK까지 자동 검증하는 것은 아니다.

## 주의점

`@ApplicationModule`은 Spring Boot 실행 진입점을 생성하거나 모듈을 독립 JVM으로 배포하지 않는다. 기본적으로 모듈 루트 패키지가 공개 API이고 하위 패키지는 내부 구현이다. 하위 패키지 공개가 필요하면 `@NamedInterface`를 검토한다.

모듈 통합 테스트에는 `@ApplicationModuleTest`를 사용할 수 있다. 자체 `@SpringBootTest` 공통 애너테이션과 목적·탐지 범위가 같다고 가정하지 않는다. 실제 HTTP 서버는 별도로 `RANDOM_PORT` 등을 선택해야 한다. 비동기 이벤트 결과를 검증할 때는 `Scenario` 등으로 완료를 기다리고 데이터 정리도 고려한다.

빌드 경계와 업무·배포 경계의 관계는 [바운디드 컨텍스트](../../ddd/contexts/bounded-context.md)에서 비교한다.

## 꼬리질문

1. Spring Modulith의 애플리케이션 모듈과 Gradle 프로젝트는 왜 같은 개념이 아닐까?
2. 업무 코드를 app·domain·in·out 하위 패키지에 둘 때 다른 모듈에 어떤 계약만 공개할까?
3. 구조 검증이 통과해도 다른 모듈의 테이블을 직접 조회하는 문제가 남을 수 있는 이유는?

</details>

## 참고 자료

- [Spring Modulith · Fundamentals](https://docs.spring.io/spring-modulith/reference/fundamentals.html) — 모듈 탐지·공개 인터페이스·허용 의존성을 확인한다.
- [Spring Modulith · Verification](https://docs.spring.io/spring-modulith/reference/verification.html) — verify가 검사하는 경계와 위반을 확인한다.
- [Spring Modulith · Integration Testing](https://docs.spring.io/spring-modulith/reference/testing.html) — 모듈 탐지와 통합 테스트 범위를 확인한다.
