# 백프레셔와 요청 제한

> 처리 가능한 속도에 맞춰 유입·대기·거절을 조정해 과부하가 시스템 전체로 번지는 것을 제한한다.

- 무한 큐는 과부하를 해결하지 않는다.
- 대기실과 사용자별 제한은 목적이 다르다.
- 재시도에도 시간 제한과 분산이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

소비 속도보다 유입이 빠르면 대기열이 증가한다. 유한 큐·동시 실행 제한·요청 제한·대기실을 사용해 허용하는 작업량을 정한다. 대기실은 순번과 전역 진입 속도를 관리하고 사용자별 rate limiter는 특정 주체의 과도한 요청을 제한한다. 토큰 버킷은 지속 보충 속도와 순간 burst 용량을 나누어 설정한다.

## 예제

한 사용자에게 초당 한도를 정하고 초과하면 429를 반환한다. 여러 서버의 전역 대기실은 서버 수가 늘어도 합계 배출 속도가 목표를 넘지 않게 조정한다.

## 주의점

모든 클라이언트가 즉시 같은 간격으로 재시도하면 장애 부하를 키운다. 지수 백오프·jitter·재시도 한도를 함께 사용한다.

## 복습 질문

사용자별 요청 제한이 있어도 전역 유입 제어가 필요할 수 있는 이유는?

자료 구분: **기존 자료** — 클라우드 강의·부하 실험 가이드·Kubernetes 학습 글의 개념. **공식 자료 보완** — 정의·운영 조건·측정 해석.

</details>

## 참고 자료

- [Spring Cloud Gateway · RequestRateLimiter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webflux/gatewayfilter-factories/requestratelimiter-factory.html) — 토큰 버킷의 보충 속도·용량·요청 비용을 확인한다.
- [RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 메서드·상태 코드·조건부 요청의 의미를 확인한다.
