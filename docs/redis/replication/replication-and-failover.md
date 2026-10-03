# Redis 복제와 장애 전환

> 복제본은 데이터 사본을 유지하지만 비동기 복제와 장애 전환에는 지연·손실 가능성이 있다.

- 복제 성공과 영속 기록을 구분한다.
- 복제본 읽기는 늦은 값을 볼 수 있다.
- 장애 전환은 데이터 복구와 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

주 서버의 변경이 복제본에 전달되는 데 시간이 걸릴 수 있다. 주 서버가 성공 응답한 직후 장애가 나고 해당 변경을 받지 못한 복제본이 승격되면 확인받은 쓰기도 유실될 수 있다. 가용성 높은 구성과 RDB·AOF 같은 영속성, 백업·복구는 서로 보완하는 별도 장치다. 중요한 재고·업무 효과는 이 실패 가능성을 포함해 정합성·대사 절차를 설계한다.

## Java 예제

Spring Data Redis. INFO 접근 권한이 필요하며 실습용으로 복제 상태를 조회한다.

```java
import org.springframework.data.redis.core.RedisCallback;
import org.springframework.data.redis.core.StringRedisTemplate;

import java.util.Properties;

static Properties replication(StringRedisTemplate redis) {
    return redis.execute(
            (RedisCallback<Properties>)
                    connection -> connection.serverCommands().info("replication"));
}
```

## 주의점

Redis 복제를 강한 일관성과 동일시하지 않는다. replica가 있다고 백업이 필요 없는 것도 아니다.

## 꼬리질문

1. 주 서버가 성공 응답한 쓰기가 장애 전환 뒤 없어질 수 있는 시간 구간은?
2. 조회한 복제 offset과 연결 상태가 정상이어도 최근 쓰기 유실이 불가능하다고 말할 수 있을까?
3. 복제 lag와 장애 전환 시간을 함께 관측하면 RPO·가용성 판단에 어떤 도움이 될까?

</details>

## 참고 자료

- [Redis · Replication](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/) — 비동기 복제와 읽기 지연·장애 시 손실 가능성을 확인한다.
- [Redis · Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/) — RDB·AOF의 복구 범위와 비용을 확인한다.
- [Java API 사용 안내](https://docs.spring.io/spring-data/redis/reference/redis/template.html) — 템플릿의 연결 콜백과 저수준 명령 접근 방식을 확인한다.
