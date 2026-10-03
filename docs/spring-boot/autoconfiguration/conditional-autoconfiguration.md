# Spring Boot 자동 설정

> 클래스패스·빈·속성 조건에 맞는 기본 구성을 제공하고 사용자 구성을 존중한다.

- starter는 관련 의존성을 묶는다.
- 자동 설정은 조건에 따라 적용된다.
- 적용 결과는 조건 보고서로 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Boot는 필요한 라이브러리의 존재와 빈·설정 값 등을 보고 구성을 활성화한다. 사용자가 특정 빈을 제공하면 해당 기본 빈 구성은 물러나는 경우가 많다. 따라서 starter를 추가했는데 원하는 기능이 켜지지 않으면 단순히 “자동”이라고 추측하지 말고 조건·사용자 빈·프로파일을 확인한다. @SpringBootApplication은 구성·컴포넌트 검색·자동 설정과 연결된다.

## Java 예제

Spring Boot의 조건부 빈 예제다. 실제 자동 설정 클래스 등록 전체를 구현하지 않는다.

```java
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.context.annotation.*;

interface Greeting {
    String text();
}

@Configuration
static class Defaults {
    @Bean
    @ConditionalOnMissingBean(Greeting.class)
    Greeting greeting() {
        return () -> "default";
    }
}
```

## 주의점

모든 자동 설정이 같은 조건을 쓰는 것은 아니다. 라이브러리 추가만으로 보안·연결·업무 설정까지 완성되었다고 보지 않는다.

## 꼬리질문

1. 같은 starter를 넣은 두 프로젝트의 빈 구성이 달라질 수 있는 이유는?
2. 사용자 Greeting 빈이 등록되어 있으면 기본 빈 조건은 어떻게 평가될까?
3. 이 설정을 starter의 자동 설정으로 배포하려면 클래스패스 조건·등록 방식·평가 순서를 왜 더 확인해야 할까?

</details>

## 참고 자료

- [Spring Boot · Auto-configuration](https://docs.spring.io/spring-boot/reference/using/auto-configuration.html) — 조건에 따른 자동 구성과 사용자 설정의 우선순위를 확인한다.
