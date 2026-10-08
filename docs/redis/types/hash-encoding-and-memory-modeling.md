# Redis Hash 인코딩과 메모리 모델링

> Hash의 메모리 절약은 작은 객체의 인코딩과 키 오버헤드 감소에서 나오며, 묶는 크기는 TTL·조회·분산 요구로 정한다.

- **원리:** 작은 Hash는 `listpack`으로 저장할 수 있지만 크기 조건을 넘으면 일반 인코딩으로 전환된다.
- **비교:** 키 100만 개와 Hash 필드 100만 개는 단일 조회가 모두 평균 O(1)이어도 메모리·운영 단위가 다르다.
- **판단:** 메모리 계측과 함께 독립 만료, 큰 키의 영향, Cluster 분산을 평가한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

`user:100`에 `name="Alen"`, `age="33"`, `city="Suwon"`을 Hash로 저장하면 필드별 String 키보다 최상위 키·객체 오버헤드를 줄일 수 있다. Redis 7.x의 작은 Hash는 `listpack`이라는 연속된 메모리 표현을 사용할 수 있다. 일반적인 문자열 압축과는 다르며, 메모리를 아끼는 내부 인코딩이다.

Redis 7.4 기본 설정은 `hash-max-listpack-entries=512`, `hash-max-listpack-value=64`이다. 필드 수와 필드명·값의 크기가 조건을 넘으면 `hashtable`로 전환된다. 작은 `listpack`은 필드를 순차 탐색하지만 크기를 제한하므로, 명령 문서의 [HGET](https://redis.io/docs/latest/commands/hget/)은 O(1)로 표기한다. 제한을 크게 올리면 CPU 비용과 전환 지연을 다시 측정해야 한다. 실제 인코딩은 버전·설정·사용 기능에 따라 확인한다.

같은 필드·값 100만 쌍을 개별 String 키와 하나의 Hash로 비교하면, 큰 Hash는 기본 설정에서 `listpack` 절약을 유지하지 못한다. 그래도 최상위 키 오버헤드 감소로 메모리가 줄 수 있지만 절약량과 조회 지연은 측정해야 한다. `GET`과 `HGET` 단일 조회의 평균 복잡도는 같아도 실제 지연이 같다는 뜻은 아니다. [HGETALL](https://redis.io/docs/latest/commands/hgetall/)로 100만 필드를 읽으면 O(N)이며 응답도 커진다.

## 비교 실습 설계

실측 결과가 아닌 재현을 위한 비교 조건이다. 독립된 실습 인스턴스에서 동일한 사용자 10만 명·3개 필드를 준비하고 A·B·C를 각각 새 인스턴스에 적재한다. Redis 버전·설정·값 길이·TTL·영속성·클라이언트 동시성·파이프라인 조건을 맞춘다.

| 방식 | 사용자 100의 저장 예 | 전체 규모 |
| --- | --- | --- |
| A: 필드마다 String | `user:100:name` → `Alen` 등 | 30만 키 |
| B: 객체마다 Hash | `user:100` → `name`, `age`, `city` | 10만 키·각 3필드 |
| C: 여러 객체를 한 Hash | `users` → `100:name`, `100:age`, `100:city` | 1키·30만 필드 |

C는 JSON으로 바꾸지 않고 B와 같은 필드·값을 저장한다. 추가로 100명씩 묶는 버킷 Hash도 비교하면 키 감소와 작은 인코딩을 함께 평가할 수 있다. 이때 버킷당 300필드지만 각 필드명·값의 바이트 길이 조건도 충족해야 한다.

적재된 실습 인스턴스에서 `redis-cli`로 실행한다. `users`는 C에서, `user:100`은 B에서 확인한다.

```sh
redis-cli INFO server
redis-cli CONFIG GET 'hash-max-listpack-*'
redis-cli INFO memory
redis-cli MEMORY USAGE user:100
redis-cli OBJECT ENCODING user:100
redis-cli MEMORY USAGE users
redis-cli OBJECT ENCODING users
```

[MEMORY USAGE](https://redis.io/docs/latest/commands/memory-usage/)는 키와 값의 할당·관리 비용을 보여 준다. A의 사용자 한 명은 세 키의 값을 합쳐 비교한다. 큰 Hash는 기본 5개 샘플로 추정하며, `SAMPLES 0`은 전체 샘플링이라 실습에서만 신중히 사용한다.

[INFO MEMORY](https://redis.io/docs/latest/commands/info/)의 `used_memory`·`used_memory_dataset`을 적재 전후로 비교하고, OS 관점의 `used_memory_rss`도 따로 기록한다. 키별 메모리 합과 인스턴스 전체 메모리는 같지 않다. 조회는 단일 필드와 사용자 전체를 분리해 같은 요청량·반환 데이터에서 처리량·p50·p95·p99를 비교한다. B·C의 우열을 미리 정하지 않는다.

## 주의점

- **Hash가 모든 데이터에 적합하지는 않다.** 값은 문자열이며 다른 자료구조를 직접 중첩하지 않는다. 순위·범위 조회에는 Sorted Set 등의 연산이 필요하다. 메모리 관리는 String·Set 등 모든 자료형에 적용한다.
- **TTL은 버전을 구분한다.** `EXPIRE users`는 Hash 전체를 만료시킨다. Redis 7.4부터는 [HEXPIRE](https://redis.io/docs/latest/commands/hexpire/)로 필드별 TTL을 지정할 수 있다. C에서 사용자 단위 만료는 관련 세 필드의 TTL을 함께 관리해야 하며, `HSET`으로 덮어쓴 필드의 TTL은 제거된다.
- **삭제·퇴거·분산 단위는 여전히 키다.** 큰 Hash의 삭제나 메모리 정책에 따른 키 퇴거는 묶인 데이터에 영향을 준다. Cluster는 키를 16,384개 슬롯에 배치하고 한 Hash의 필드를 여러 샤드로 나누지 않는다. 큰 Hash는 한 샤드에 메모리·요청을 집중시킬 수 있다. 노드 장애는 그 노드의 다른 키에도 영향을 주므로, 큰 키의 영향 범위와 노드 장애의 범위를 구분한다.

## 꼬리질문

1. 작은 Hash의 메모리 절약은 어디서 나오며, 평균 O(1)인 `HGET`을 지원하면서 `listpack`이 순차 탐색할 수 있는 이유는 무엇인가?
2. 키 100만 개와 하나의 Hash에 필드 100만 개를 저장했을 때 인코딩·총메모리·단일 조회·전체 조회를 어떻게 비교할까?
3. 데이터를 묶은 상태에서 사용자별 TTL, 일부 데이터 삭제·퇴거의 영향, Cluster 분산을 동시에 만족하려면 묶는 단위를 어떻게 정해야 할까?

</details>

## 참고 자료

- [Redis · Memory optimization](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/) — 작은 Hash의 인코딩 조건과 메모리·CPU 절충을 읽는다. 본문의 필드 TTL 불가 설명은 과거 설명이므로 아래 최신 Hash 문서와 대조한다.
- [Redis · Hashes](https://redis.io/docs/latest/develop/data-types/hashes/) — 필드 조회·갱신과 Redis 7.4 이후 필드별 만료를 확인한다.
- [Redis · Cluster specification](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/) — 키별 슬롯 배치와 hash tag에 따른 분산 조건을 확인한다.
