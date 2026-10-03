# Cache-aside와 캐시 스탬피드

> 캐시 미스 시 원본을 읽고 채우되 만료 순간 요청이 몰리는 경합과 오래된 값을 관리한다.

- 원본 데이터의 기준을 먼저 정한다.
- TTL·무효화는 허용 가능한 지연과 연결한다.
- single-flight·SWR은 서로 다른 비용을 줄인다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Cache-aside는 캐시를 확인하고 미스면 DB에서 읽은 뒤 값을 채운다. 같은 인기 키가 만료되면 여러 요청이 동시에 DB를 읽는 스탬피드가 생길 수 있다. single-flight는 같은 키의 로딩을 합쳐 원본 부담을 줄인다. stale-while-revalidate는 허용 가능한 오래된 값을 먼저 주고 뒤에서 갱신해 대기 지연을 줄인다. 키에 값이 전혀 없을 때와 갱신 실패 때의 정책도 필요하다.

## Java 예제

Spring Data Redis의 기본 cache-aside 흐름이다. stampede 방지는 아직 포함하지 않는다.

```java
import org.springframework.data.redis.core.StringRedisTemplate;

import java.time.Duration;
import java.util.function.Supplier;

static String get(StringRedisTemplate redis, String key, Supplier<String> loader) {
    String cached = redis.opsForValue().get(key);
    if (cached != null) return cached;
    String value = loader.get();
    if (value != null) redis.opsForValue().set(key, value, Duration.ofSeconds(60));
    return value;
}
```

## 주의점

프로세스 안의 single-flight는 여러 서버 전체의 로딩을 자동 합치지 않는다. TTL만으로 모든 DB·캐시 경쟁이 해결되지는 않는다.

## 꼬리질문

1. single-flight는 DB 부하를 줄여도 왜 첫 요청의 대기 시간을 없애지 못하는가?
2. 캐시가 비어 있을 때 요청 100개가 동시에 오면 loader는 최대 몇 번 호출될 수 있을까?
3. single-flight를 넣어도 로더 장애·타임아웃·캐시 없는 결과를 어떻게 처리해야 할까?

함께 복습: [Redis 복제와 장애 전환](../replication/replication-and-failover.md) · [Redis 원자 연산과 저장소 간 불일치](../failures/atomic-script-and-cross-store.md)

</details>

## 참고 자료

- [Redis · Client-side caching introduction](https://redis.io/docs/latest/develop/clients/client-side-caching/) — 무효화·오래된 값·캐시 일관성의 경계를 확인한다.
- [Redis · Data Types](https://redis.io/docs/latest/develop/data-types/) — 키에 담을 자료형과 지원 연산을 비교한다.
- [Java API 사용 안내](https://docs.spring.io/spring-data/redis/reference/redis/template.html) — Java 템플릿의 값 조회·TTL 저장 연산을 확인한다.
