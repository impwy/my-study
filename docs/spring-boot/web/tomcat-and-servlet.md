# Tomcat과 Spring MVC의 역할

> Tomcat은 서블릿 실행 환경을 제공하고 Spring MVC는 요청을 핸들러로 연결해 응답을 조정한다.

- 서블릿 컨테이너와 Spring은 다르다.
- 내장 서버와 외부 WAR 배포를 구분한다.
- Connector·Servlet·Bean 설정의 층이 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Servlet 기반 요청은 Tomcat의 수신 처리와 필터·서블릿 흐름을 거쳐 DispatcherServlet으로 전달된다. Spring MVC는 핸들러를 찾고 입력 처리·메서드 실행·결과 변환을 조정한다. Boot의 내장 Tomcat도 서블릿 컨테이너 역할을 한다. 외부 server.xml, 웹 앱 web.xml, Spring XML·@Configuration은 서로 다른 대상을 설정하므로 실제 읽는 설정과 실행 방식을 확인한다.

## Java 예제

Spring Boot 3.x의 Tomcat 웹 애플리케이션 설정 클래스 안에 두는 예제다. 처리량은 스레드 수만으로 결정되지 않는다.

```java
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.context.annotation.Bean;

@Bean
WebServerFactoryCustomizer<TomcatServletWebServerFactory> tomcat() {
    return factory ->
            factory.addConnectorCustomizers(
                    connector -> connector.setProperty("maxThreads", "100"));
}
```

## 주의점

이 흐름은 Spring MVC 기준이다. WebFlux의 실행 모델을 같은 설명으로 일반화하지 않는다. 설정 파일을 생성했다는 사실만으로 앱에 로드되지는 않는다.

## 꼬리질문

1. Tomcat의 Connector 설정과 Spring Bean 설정은 각각 어떤 동작을 바꾸는가?
2. Tomcat 처리 스레드를 100개로 설정해도 DB 커넥션 풀이 10개면 어느 곳에서 대기가 생길까?
3. Servlet 필터와 Spring MVC 인터셉터는 요청 처리 흐름의 어느 위치에 있을까?

</details>

## 참고 자료

- [Apache Tomcat · Introduction](https://tomcat.apache.org/tomcat-11.0-doc/introduction.html) — 서블릿 컨테이너의 역할과 지원 범위를 확인한다.
- [Spring · Web MVC](https://docs.spring.io/spring-framework/reference/web/webmvc.html) — 요청 매핑·검증·예외 처리가 실행되는 흐름을 확인한다.
