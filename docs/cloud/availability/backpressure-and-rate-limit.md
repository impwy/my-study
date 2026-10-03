# 백프레셔와 요청 제한

> 처리 가능한 속도에 맞춰 유입·대기·거절을 조정해 과부하가 시스템 전체로 번지는 것을 제한한다.

- 무한 큐는 과부하를 해결하지 않는다.
- 대기실과 사용자별 제한은 목적이 다르다.
- 재시도에도 시간 제한과 분산이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

소비 속도보다 유입이 빠르면 대기열이 증가한다. 유한 큐·동시 실행 제한·요청 제한·대기실을 사용해 허용하는 작업량을 정한다. 대기실은 순번과 전역 진입 속도를 관리하고 사용자별 rate limiter는 특정 주체의 과도한 요청을 제한한다. 토큰 버킷은 지속 보충 속도와 순간 burst 용량을 나누어 설정한다.

## Java 예제

```java
import java.util.concurrent.*;

static class Gate {
    final Semaphore slots = new Semaphore(20);

    void run(Runnable job) {
        if (!slots.tryAcquire()) throw new RejectedExecutionException("overloaded");
        try {
            job.run();
        } finally {
            slots.release();
        }
    }
}
```

## 주의점

모든 클라이언트가 즉시 같은 간격으로 재시도하면 장애 부하를 키운다. 지수 백오프·jitter·재시도 한도를 함께 사용한다.

## 꼬리질문

1. 사용자별 요청 제한이 있어도 전역 유입 제어가 필요할 수 있는 이유는?
2. 이 예제는 초당 요청 수와 동시에 실행 중인 요청 수 중 무엇을 제한할까?
3. 거부를 무조건 즉시 재시도하면 과부하가 커지는 이유와 backoff가 필요한 이유는 무엇일까?

</details>

## 참고 자료

- [Spring Cloud Gateway · RequestRateLimiter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webflux/gatewayfilter-factories/requestratelimiter-factory.html) — 토큰 버킷의 보충 속도·용량·요청 비용을 확인한다.
- [RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 메서드·상태 코드·조건부 요청의 의미를 확인한다.
