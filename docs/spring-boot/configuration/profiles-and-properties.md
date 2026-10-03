# 외부 설정과 프로파일

> 환경별 설정은 코드에서 분리하고 실제 적용된 값의 우선순위를 확인한다.

- 설정은 파일·환경 변수·명령행 등에서 온다.
- 프로파일은 선택한 구성 묶음을 활성화한다.
- 비밀 값은 공개 설정에 넣지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

개발·테스트·운영은 DB 주소·로그 수준 등 설정이 다를 수 있다. 설정을 외부화하면 코드 변경 없이 환경에 맞게 실행할 수 있다. 여러 설정 원천에 같은 키가 있을 때는 Boot의 우선순위 규칙으로 값이 결정된다. 프로파일은 해당 환경에서 사용할 빈·설정 묶음을 고르지만 외부 주입과 우선순위 규칙까지 없어지는 것은 아니다.

## Java 예제

Spring Boot가 필요하다. 비밀 값은 프로파일 파일이나 공개 저장소에 넣지 않는다.

```java
import org.springframework.boot.context.properties.*;
import org.springframework.context.annotation.Configuration;

@ConfigurationProperties(prefix = "app")
record Settings(String endpoint, int timeoutMillis) {}

@Configuration
@EnableConfigurationProperties(Settings.class)
static class Config {}
// app.endpoint와 app.timeout-millis를 타입에 바인딩
```

## 주의점

설정 파일을 나누는 것만으로 비밀이 안전해지는 것은 아니다. Git에 올리지 않는 비밀 관리 수단과 접근 권한을 사용한다.

## 꼬리질문

1. 설정 파일의 DB 주소와 실제 연결 주소가 다르면 어디를 더 확인해야 하는가?
2. 프로파일 파일과 환경 변수에 같은 설정이 있으면 실제 적용값은 어떤 우선순위로 결정될까?
3. 필수 값 누락·음수 timeout을 시작 단계에서 막으려면 어떤 검증을 붙일까?

</details>

## 참고 자료

- [Spring Boot · Externalized Configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html) — 설정 우선순위·프로파일·환경 변수 적용을 확인한다.
