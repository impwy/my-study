# Redis 자료형과 Sorted Set

> 주어진 조회 패턴과 데이터 규모에서 Redis 자료구조를 어떻게 모델링할 것인가가 설계의 출발점이다.

- **조회:** 단일 키 조회와 조건에 맞는 객체 탐색을 구분한다.
- **자료형:** String·Hash·List·Set·Sorted Set은 지원하는 연산과 의미가 다르다.
- **비용:** 명령의 시간 복잡도뿐 아니라 결과 크기와 인덱스 유지 비용도 고려한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Redis는 키에 자료형을 가진 값을 연결한다. [GET](https://redis.io/docs/latest/commands/get/)은 String 값 조회에 사용하는 명령이며 평균 O(1)이다. 여기서 기준은 키 개수다. `product:1`과 `product:detail:1`의 콜론은 이름 규칙이며, 계층이나 검색 인덱스를 자동 생성하지 않는다. 두 키의 조회 복잡도는 같지만 **키 길이의 영향까지 없는 것은 아니다.** 긴 이름은 메모리·전송량과 해싱·비교 비용을 늘릴 수 있고, 큰 값의 응답 전송에도 시간이 든다.

| 접근 패턴 | 자료형·모델링 예 |
| --- | --- |
| 단일 값·직렬화된 객체 조회 | String: `product:1` |
| 객체 필드 일부 조회·갱신 | Hash: `user:100`의 `name`, `age`, `city` |
| 순서 있는 원소의 양 끝 처리 | List |
| 카테고리별 상품·사용자별 추천 후보 | Set: 상품 ID를 중복 없이 저장 |
| 추천 점수·가격·순위로 범위 조회 | Sorted Set: 상품 ID와 score 저장 |

예를 들어 `category:10:products`에 상품 ID `1`, `2`를 Set으로 저장하면, 해당 카테고리의 ID를 얻은 뒤 `product:1`, `product:2`를 읽는다. 이것은 애플리케이션이 관리하는 인덱스다. 상품의 카테고리 변경·삭제 시 인덱스도 갱신해야 한다. 원본 키에 TTL을 설정해도 다른 Set의 ID가 자동 제거되지는 않는다.

Sorted Set의 member는 중복되지 않으며 score로 정렬된다. 같은 score에서는 member의 사전식 순서를 사용한다. 삽입은 O(log N), 기본적인 순위 범위 조회는 O(log N + M)이며 N은 멤버 수, M은 반환 수다. 전체 결과를 반환하는 비용을 무시하면 안 된다.

## Java 예제

Spring Data Redis와 구성된 `StringRedisTemplate`이 필요하다. 실습 Redis의 `ranking`을 갱신한다. [ZSetOperations API](https://docs.spring.io/spring-data/redis/docs/current/api/org/springframework/data/redis/core/ZSetOperations.html) 기준이며 여기서 실행한 결과는 아니다. 메서드는 클래스 안에 둔다.

```java
import org.springframework.data.redis.core.StringRedisTemplate;
import java.util.Set;

static Set<String> top(StringRedisTemplate redis) {
    redis.opsForZSet().incrementScore("ranking", "user:42", 1);
    return redis.opsForZSet().reverseRange("ranking", 0, 9);
}
```

## 주의점

`KEYS`는 전체 키 탐색 동안 서버를 오래 점유할 수 있어 일반 요청 경로에 넣지 않는다. [SCAN](https://redis.io/docs/latest/commands/scan/)은 탐색을 나누지만 전체 순회는 O(N)이다. 중복 반환과 순회 중 변경을 고려해야 하며, `MATCH`가 조건 검색 인덱스를 만드는 것은 아니다. 빈 결과여도 커서가 0이 될 때까지 진행한다. 반복적인 서비스 조회에는 필요한 Set·Sorted Set 인덱스를 설계한다.

위 Java 함수는 호출마다 점수를 증가시킨다. 재시도하면 중복 증가할 수 있고, 증가와 조회는 서로 다른 명령이어서 사이에 다른 요청이 실행될 수 있다. Redis 명령 하나의 원자성이 DB·Kafka를 포함한 전체 업무의 원자성을 보장하지는 않는다.

객체를 얼마나 묶을지는 [Hash 인코딩과 메모리 모델링](hash-encoding-and-memory-modeling.md)의 TTL·분산 조건과 함께 판단한다.

## 꼬리질문

1. `GET`의 평균 O(1)과 Sorted Set의 O(log N + M)에서 각각 어떤 데이터 규모를 기준으로 삼는가?
2. 카테고리별 상품 목록과 사용자별 추천 상위 10개를 만들 때 Set·Sorted Set 중 무엇을 고르고, 상품 변경 시 어떤 인덱스를 갱신해야 할까?
3. 목록이 100만 건이거나 점수가 같고 재시도가 발생한다면 반환량·정렬 계약·중복 갱신을 어떻게 관리할까?

</details>

## 참고 자료

- [Redis · Keys and values](https://redis.io/docs/latest/develop/using-commands/keyspace/) — 키 이름, 만료, 키 탐색의 의미와 주의점을 확인한다.
- [Redis · Data types](https://redis.io/docs/latest/develop/data-types/) — 조회·갱신 요구에 맞는 자료형을 비교한다.
- [Redis · Sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/) — score·member 정렬과 범위 조회 비용을 확인한다.
