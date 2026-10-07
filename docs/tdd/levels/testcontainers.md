# Testcontainers와 통합 테스트 DB

> Testcontainers는 테스트에서 실제 DB 등의 서비스를 컨테이너로 실행하고 연결 정보를 제공한다.

- **전제:** Docker 호환 런타임과 테스트 대상 이미지에 접근할 수 있어야 한다.
- **원리:** 임시 PostgreSQL에 연결해 SQL·매핑·제약 등 실제 연동을 검증한다.
- **주의:** 컨테이너 공유와 테스트 데이터 격리는 서로 다른 문제다.

<details>
<summary>설명과 설정 예제 펼치기</summary>

## 설명

H2를 PostgreSQL 대신 사용하면 방언과 일부 기능의 차이를 놓칠 수 있다. Testcontainers로 대상 DB를 실행하면 수동으로 고정 테스트 DB를 준비할 필요가 줄어든다. 실제 DB를 쓴다는 사실만으로 운영과 같은 스키마·데이터·권한까지 검증되는 것은 아니다.

| 관리 방식 | 공유·종료 기준 |
| --- | --- |
| 수동 static 싱글턴 | 같은 테스트 JVM·클래스로더에서 공유; 기본 Ryuk 정리 사용 |
| Spring의 컨테이너 빈 | 캐시된 Spring 컨텍스트에서 공유; 컨텍스트 종료 시 정리 |
| JUnit의 static @Container | 테스트 클래스 단위로 시작·종료 |

Gradle의 서로 다른 모듈 테스트 작업은 별도 테스트 JVM을 사용한다. 같은 설정 클래스를 의존해도 모든 모듈이 컨테이너 하나를 공유하는 것은 아니다.

## 예제

아래는 Spring Boot 4.1 계열과 Testcontainers 2 계열의 수동 싱글턴 설정 예시다. `testcontainers-postgresql`, PostgreSQL JDBC 드라이버와 Spring 테스트 의존성이 필요하다. 버전은 사용하는 Spring Boot BOM으로 관리한다.

```java
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.test.context.DynamicPropertyRegistrar;
import org.testcontainers.postgresql.PostgreSQLContainer;

@TestConfiguration(proxyBeanMethods = false)
public class PostgresTestConfig {
    private static final PostgreSQLContainer DB =
            new PostgreSQLContainer("postgres:18");

    static {
        DB.start();
    }

    @Bean
    DynamicPropertyRegistrar databaseProperties() {
        return registry -> {
            registry.add("spring.datasource.url", DB::getJdbcUrl);
            registry.add("spring.datasource.username", DB::getUsername);
            registry.add("spring.datasource.password", DB::getPassword);
            registry.add("spring.jpa.hibernate.ddl-auto", () -> "create-drop");
        };
    }
}
```

테스트에서 이 설정을 `@Import`한다. Repository 테스트에는 `@DataJpaTest`와 필요한 테스트 부트 설정을 사용하고, `@AutoConfigureTestDatabase(replace = Replace.NONE)`으로 DB 교체를 막을 수 있다. 직접 만든 Repository 어댑터는 추가로 import한다.

Spring 관리 방식으로 바꾸려면 컨테이너를 `@Bean`으로 제공하고 `@ServiceConnection`을 붙인다. 이때 `spring-boot-testcontainers`가 필요하며 직접 `start()`나 JDBC 연결 속성 등록을 대신할 수 있다. 설정 클래스가 공통 테스트 모듈의 `src/main`에 있다면 필요한 의존성도 그 모듈의 주 소스 컴파일 범위에 둔다.

## 주의점

`@DataJpaTest`는 기본 롤백하지만 `@SpringBootTest` 전체 통합 테스트는 자동 롤백하지 않는다. 실제 HTTP 서버에서 처리한 요청은 테스트와 별도 트랜잭션이므로 테스트에 붙인 `@Transactional`만으로 서버 데이터를 정리할 수 없다. `create-drop`은 컨텍스트 생명주기에 연결되며 테스트 메서드마다 DB를 초기화하는 옵션이 아니다.

저장 매핑은 반환 객체만 확인하지 말고 필요한 경우 flush·clear 후 DB에서 다시 읽는다. 모듈별 스키마는 초기화 SQL이나 실제 마이그레이션으로 준비한다. 같은 DB를 쓰는 비동기 테스트에서는 처리가 끝난 뒤 정리해야 한다. 수동 싱글턴과 JUnit 종료 관리를 무심코 섞지 않는다. 테스트 범위는 [단위·통합·인수 테스트](unit-and-integration.md)에서 확인한다.

## 꼬리질문

1. PostgreSQL 컨테이너를 사용하면 H2 테스트와 비교해 어떤 연동 문제를 확인할 수 있을까?
2. 여러 테스트 클래스가 DB를 공유할 때 컨테이너는 유지하면서 데이터는 어떻게 격리할까?
3. HTTP 요청이나 커밋 후 비동기 이벤트가 데이터를 변경하면 자동 롤백만으로 충분하지 않은 이유는?

</details>

## 참고 자료

- [Testcontainers · Manual Lifecycle Control](https://java.testcontainers.org/test_framework_integration/manual_lifecycle_control/) — 싱글턴의 시작과 정리 범위를 확인한다.
- [Spring Boot · Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html) — 컨테이너 빈과 ServiceConnection의 연결·수명주기를 확인한다.
- [Spring Boot · Testing Spring Boot Applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — JPA 테스트와 HTTP 테스트의 트랜잭션 차이를 읽는다.
