# Actuator 상태와 메트릭

> 서비스의 상태 확인과 성능 관측 정보를 운영에 필요한 범위로 제공한다.

- health와 readiness·liveness의 목적을 구분한다.
- 메트릭은 원인 분석을 위한 관측값이다.
- 엔드포인트 노출·권한을 제한한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

health는 구성된 상태 지표를 모아 응답하며 “업무가 모두 정상”이라는 완전한 증명은 아니다. liveness는 프로세스가 회복 불가능한 상태인지, readiness는 지금 트래픽을 받아도 되는지를 판단하는 데 사용한다. 요청 지연·오류·JVM·커넥션 풀 메트릭을 함께 보면 느려진 구간을 좁힐 수 있다. 필요한 엔드포인트만 노출하고 접근을 제어한다.

## Java 예제

Spring Boot Actuator가 필요하다. 예제의 고정 상태 대신 실제 가벼운 내부 상태를 검사하고 health group을 구성한다.

```java
import org.springframework.boot.actuate.health.*;
import org.springframework.stereotype.Component;

@Component("catalog")
static class CatalogHealth implements HealthIndicator {
    public Health health() {
        return Health.up().withDetail("catalogLoaded", true).build();
    }
}
```

## 주의점

외부 DB의 일시 장애를 liveness 실패로 연결해 모든 인스턴스가 재시작하게 만들지 않는다. 세부 상태·환경 설정을 무차별 공개하지 않는다.

## 꼬리질문

1. readiness와 liveness를 같은 조건으로 만들면 어떤 장애 악순환이 가능한가?
2. 이 indicator가 UP이어도 서비스의 모든 요청이 정상이라고 결론 낼 수 있을까?
3. 외부 DB 장애를 liveness에 넣으면 재시작이 반복될 수 있는데 readiness와 어떻게 나눌까?

</details>

## 참고 자료

- [Spring Boot · Actuator](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html) — 상태·메트릭 엔드포인트와 노출·접근 제어 설정을 확인한다.
