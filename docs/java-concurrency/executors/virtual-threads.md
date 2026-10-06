# Virtual Thread와 WebFlux의 선택 기준

> Virtual Thread는 블로킹 I/O 동시 작업의 스레드 비용을 줄이고 WebFlux는 논블로킹 흐름과 백프레셔를 제공한다.

- Virtual Thread는 Java 21에서 정식 도입됐다.
- synchronized 관련 모니터 핀닝 개선은 Java 24의 JEP 491이다.
- CPU·DB 커넥션·외부 API 용량의 한계는 별도로 관리한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

Virtual Thread는 JVM이 관리하는 가벼운 스레드다. 지원되는 블로킹 I/O 대기 중에는 실행을 맡던 플랫폼 스레드를 다른 작업에 사용할 수 있어 많은 동시 요청을 감당하는 데 도움이 된다. 코드를 더 빠르게 실행하는 스레드나 CPU 성능 향상 기능은 아니다.

Java 21에서 정식 도입되었고 Java 24는 synchronized와 관련된 모니터 핀닝을 개선했다. 따라서 Java 25 이전의 모든 도입이 잘못되었다고 단정할 수 없다. 네이티브 호출 등 남은 경로와 실제 라이브러리·부하를 확인한다.

| 선택지 | 검토할 상황 |
| --- | --- |
| Spring MVC와 Virtual Thread | JPA/JDBC 등 블로킹 라이브러리와 명령형 코드가 중심 |
| Spring WebFlux | 논블로킹 호출·스트리밍·백프레셔가 요구되는 흐름 |

WebFlux는 작은 이벤트 루프 집합에서 블로킹하지 않는 실행을 전제한다. Virtual Thread가 있다고 WebFlux가 불필요해지는 것은 아니다. 어느 쪽이든 의존 라이브러리의 실행 방식과 유지보수 비용을 비교한다.

## 주의점

많은 스레드를 생성해도 DB 커넥션과 외부 API 허용량은 늘어나지 않는다. 요청 제한·타임아웃·자원 상한으로 포화를 관리한다. CPU 중심 계산에는 더 많은 동시 작업이 오히려 경합을 늘릴 수 있다. Kotlin Coroutine은 중단 가능한 흐름을 표현하는 별도 도구이며 Virtual Thread와 동일 기능으로 취급하지 않는다.

## 꼬리질문

1. I/O 대기에서 플랫폼 스레드를 놓아 주는 것이 동시 처리량에 도움이 되는 이유는?
2. JPA 기반 API에서 스레드는 늘었지만 DB 커넥션 대기가 증가하면 어떤 자원 상한을 확인할까?
3. CPU 계산·네이티브 호출·스트리밍 요구가 달라지면 Virtual Thread와 WebFlux의 선택을 어떻게 다시 평가할까?

</details>

## 참고 자료

- [Oracle Java 24 · Virtual Threads](https://docs.oracle.com/en/java/javase/24/core/virtual-threads.html) — 실행·대기·핀닝과 적용 한계를 확인한다.
- [Oracle · Significant Changes in JDK 24](https://docs.oracle.com/en/java/javase/24/migrate/significant-changes-jdk-24.html) — Java 24의 synchronized 핀닝 개선을 확인한다.
- [Spring · MVC and WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux/new-framework.html#webflux-framework-choice) — 블로킹 의존성과 논블로킹 요구에 따른 선택을 읽는다.
