# Actuator 상태와 메트릭

> 서비스의 상태 확인과 성능 관측 정보를 운영에 필요한 범위로 제공한다.

- health와 readiness·liveness의 목적을 구분한다.
- 메트릭은 원인 분석을 위한 관측값이다.
- 엔드포인트 노출·권한을 제한한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

health는 구성된 상태 지표를 모아 응답하며 “업무가 모두 정상”이라는 완전한 증명은 아니다. liveness는 프로세스가 회복 불가능한 상태인지, readiness는 지금 트래픽을 받아도 되는지를 판단하는 데 사용한다. 요청 지연·오류·JVM·커넥션 풀 메트릭을 함께 보면 느려진 구간을 좁힐 수 있다. 필요한 엔드포인트만 노출하고 접근을 제어한다.

## 예제

배포 후 readiness가 준비되기 전에 로드밸런서가 요청을 보내면 초기 오류가 늘 수 있다. health 성공만 보지 말고 대표 요청과 오류·지연도 확인한다.

## 주의점

외부 DB의 일시 장애를 liveness 실패로 연결해 모든 인스턴스가 재시작하게 만들지 않는다. 세부 상태·환경 설정을 무차별 공개하지 않는다.

## 복습 질문

readiness와 liveness를 같은 조건으로 만들면 어떤 장애 악순환이 가능한가?

자료 구분: **기존 자료** — Boot·Tomcat·설정 학습 자료의 흐름. **공식 자료 보완** — 자동 구성·설정·상태 노출 조건.

</details>

## 참고 자료

- [Spring Boot · Actuator](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html) — 상태·메트릭 엔드포인트와 노출·접근 제어 설정을 확인한다.
