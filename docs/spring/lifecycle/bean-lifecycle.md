# 빈 생명주기와 싱글턴

> 컨테이너는 빈의 생성·주입·초기화·종료를 관리하며 기본 싱글턴은 컨테이너 안에서 공유된다.

- 빈 스코프는 객체 수명과 공유 범위를 정한다.
- 초기화와 종료에서 자원을 관리한다.
- 싱글턴은 스레드 안전성을 보장하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

객체 생성 뒤 의존성이 주입되고 초기화 콜백과 후처리가 수행된다. 일반적으로 호출자는 후처리로 만들어진 프록시를 받을 수도 있다. 컨테이너 종료 시 관리 대상의 종료 콜백을 통해 자원을 정리한다. 기본 singleton 스코프는 같은 빈 정의를 컨테이너에서 공유하므로 여러 HTTP 요청이 같은 서비스 객체에 접근할 수 있다. 요청마다 다른 가변 값을 서비스 필드에 보관하지 않는다.

## Java 예제

Spring Context와 jakarta.annotation API가 필요하다.

```java
import jakarta.annotation.*;

import org.springframework.stereotype.Component;

@Component
static class Client {
    @PostConstruct
    void open() {
        System.out.println("의존성 주입 후 초기화");
    }

    void request() {
        System.out.println("사용");
    }

    @PreDestroy
    void close() {
        System.out.println("컨텍스트 종료 시 정리");
    }
}
```

## 주의점

singleton은 JVM 전체에 단 하나라는 의미가 아니다. prototype 빈의 전체 종료 관리를 singleton과 같다고 가정하지 않는다.

## 꼬리질문

1. 기본 싱글턴 서비스에 요청별 가변 상태를 넣으면 왜 위험한가?
2. 생성자와 PostConstruct는 의존성 주입·사용 가능 시점에서 어떻게 다를까?
3. 프로세스 강제 종료에도 PreDestroy가 항상 실행된다고 가정하면 어떤 자원 복구를 놓칠까?

</details>

## 참고 자료

- [Spring · IoC Container](https://docs.spring.io/spring-framework/reference/core/beans/introduction.html) — 빈·컨테이너·의존성 주입의 기본 역할을 확인한다.
