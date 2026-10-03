# Redis 원자 연산과 저장소 간 불일치

> Redis 안의 검사·차감을 원자적으로 묶어도 뒤이은 DB 저장·메시지 발행까지 한 번에 확정되지는 않는다.

- 단일 명령·스크립트의 경계를 명확히 한다.
- 재시도는 중복과 누락을 함께 고려한다.
- 대사·복구 정책으로 저장소 차이를 관리한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Lua 스크립트로 중복 검사와 재고 차감을 한 실행 범위에 묶을 수 있다. 하지만 Redis 성공 뒤 Kafka 발행이나 DB 저장이 실패하면 저장소 간 상태가 갈라진다. 이벤트의 식별자·재처리·최종 DB 제약·예약 만료 또는 보상·대사를 설계해야 한다. 분산 락 역시 수명·소유권·장애·갱신 조건을 확인해야 하며 이름만으로 모든 실패를 막지 못한다.

## Java 예제

Spring Data Redis. 한 Redis 키의 검사·차감만 묶으며 요청 중복 방지와 DB 확정은 별도다. 실제 앱에서는 스크립트 빈을 재사용한다.

```java
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.script.DefaultRedisScript;

import java.util.List;

static Long reserve(StringRedisTemplate redis, String stockKey) {
    var script =
            new DefaultRedisScript<Long>(
                    """
                    local n=tonumber(redis.call('GET',KEYS[1]) or '0')
                    if n <= 0 then return 0 end
                    redis.call('DECR',KEYS[1])
                    return 1
                    """,
                    Long.class);
    return redis.execute(script, List.of(stockKey));
}
```

## 주의점

스크립트는 실패한 이전 명령을 DB 트랜잭션처럼 자동 롤백하지 않는다. Cluster의 여러 키를 사용하는 스크립트는 키 배치 제약도 확인한다.

## 꼬리질문

1. Redis 차감 성공 뒤 프로세스가 종료되면 어떤 상태를 근거로 복구해야 하는가?
2. 검사와 차감을 원자적으로 묶어도 같은 요청의 재시도는 재고를 다시 차감할 수 있을까?
3. Redis 성공 뒤 DB 기록 전에 종료되면 요청 식별자·예약 기록·대사가 어떤 복구 근거를 제공해야 할까?

</details>

## 참고 자료

- [Redis · Scripting](https://redis.io/docs/latest/develop/programmability/eval-intro/) — 스크립트 실행 경계·제약과 실패 동작을 확인한다.
- [Redis · Replication](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/) — 비동기 복제와 읽기 지연·장애 시 손실 가능성을 확인한다.
- [Java API 사용 안내](https://docs.spring.io/spring-data/redis/reference/redis/scripting.html) — Java에서 Lua 스크립트를 실행하고 재사용하는 방법을 확인한다.
