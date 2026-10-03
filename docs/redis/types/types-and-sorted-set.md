# Redis 자료형과 Sorted Set

> 필요한 조회·갱신 연산에 맞춰 자료형을 고르고 Sorted Set은 점수 순으로 멤버를 관리한다.

- String·Hash·List·Set·Sorted Set의 의미가 다르다.
- Sorted Set 멤버는 중복되지 않고 점수로 정렬된다.
- 조회 비용에는 결과 크기도 포함한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

단일 값은 String, 필드 묶음은 Hash, 중복 없는 멤버는 Set으로 표현할 수 있다. Sorted Set은 멤버마다 score를 두어 순위·범위 조회에 사용한다. 점수 갱신은 순서를 바꿀 수 있고 같은 점수의 정렬 규칙도 확인해야 한다. 삽입 O(log N) 같은 기본 연산과 M개의 결과를 반환하는 O(log N + M) 범위 조회를 구분한다.

## Java 예제

Spring Data Redis와 구성된 StringRedisTemplate이 필요하다. 실습 Redis의 ranking을 갱신한다.

```java
import org.springframework.data.redis.core.StringRedisTemplate;

import java.util.Set;

static Set<String> top(StringRedisTemplate redis) {
    redis.opsForZSet().incrementScore("ranking", "user:42", 1);
    return redis.opsForZSet().reverseRange("ranking", 0, 9);
}
```

## 주의점

Redis 명령 하나의 원자성이 DB·Kafka를 포함한 전체 업무의 원자성은 아니다. 모든 명령이 같은 시간복잡도를 가진다고 쓰지 않는다.

## 꼬리질문

1. 상위 10개 조회와 전체 100만 개 조회를 둘 다 O(log N)이라고 부르면 무엇을 빠뜨리는가?
2. 같은 점수의 member 정렬과 상위 10개 반환은 어떤 비용·순서 계약을 확인해야 할까?
3. 매 호출에서 점수를 증가시키는 이 함수를 재시도하면 어떤 중복 효과가 생길까?

</details>

## 참고 자료

- [Redis · Data Types](https://redis.io/docs/latest/develop/data-types/) — 키에 담을 자료형과 지원 연산을 비교한다.
- [Redis · Sorted Sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/) — 점수·멤버·범위 조회 및 명령 비용을 확인한다.
- [Java API 사용 안내](https://docs.spring.io/spring-data/redis/reference/redis/template.html) — Redis 자료형을 Java 연산 인터페이스로 사용하는 방식을 확인한다.
