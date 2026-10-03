# Redis RDB·AOF와 복구

> RDB는 시점의 스냅샷을, AOF는 쓰기 명령 기록을 사용해 재시작 후 데이터를 복구한다.

- RDB 저장 주기 사이의 변경은 복구 파일에 없을 수 있다.
- AOF의 fsync 정책은 성능과 데이터 손실 가능성에 영향을 준다.
- 영속성 설정과 실제 복원 가능성은 따로 검증한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

RDB는 특정 시점의 메모리 데이터를 파일로 저장한다. 백업·이동에 편하지만 마지막 저장 이후의 변경은 사라질 수 있다. AOF는 데이터를 변경하는 명령을 기록하고 재시작 시 재생한다. appendfsync always·everysec·no는 디스크 동기화 시점을 달리한다. everysec은 일반적으로 약 1초 분량의 쓰기 손실 가능성을 고려하는 설정이며 장애 조건 전체에 대한 절대 상한으로 받아들이지 않는다.

AOF rewrite는 같은 최종 상태를 복원할 수 있도록 기록을 재구성한다. RDB와 AOF를 함께 켠 경우 Redis는 보통 더 완전한 AOF로 복원한다. 설정 파일뿐 아니라 최근 저장·쓰기 상태와 백업 복원 절차도 확인한다.

## Java 예제

```java
static void inspect(org.springframework.data.redis.core.StringRedisTemplate redis) {
    java.util.Properties info =
            redis.execute(
                    (org.springframework.data.redis.core.RedisCallback<java.util.Properties>)
                            connection -> connection.serverCommands().info("persistence"));
    if (info == null) throw new IllegalStateException("INFO 결과 없음");
    System.out.println("RDB: " + info.getProperty("rdb_last_bgsave_status"));
    System.out.println("AOF enabled: " + info.getProperty("aof_enabled"));
    System.out.println("AOF write: " + info.getProperty("aof_last_write_status"));
}
```

## 주의점

Spring Data Redis 의존성과 연결 설정이 필요하며 INFO 권한이 제한될 수 있다. 상태가 ok여도 별도 백업이나 복원 테스트를 대신하지 않는다. 복제는 실수로 삭제한 명령도 전파할 수 있다.

## 꼬리질문

1. 마지막 RDB 저장 직후 쓰기가 성공하고 서버가 종료되면 어떤 변경이 사라질 수 있을까?
2. AOF everysec에서 응답 성공과 디스크 동기화 완료를 동일하게 볼 수 있을까?
3. 복제본이 있어도 별도 백업과 복원 테스트가 필요한 이유는 무엇일까?

</details>

## 참고 자료

- [Redis · 영속성](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/) — RDB·AOF·fsync·rewrite·백업의 장단점을 비교한다.
