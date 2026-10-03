# Redis 자료형과 Sorted Set

> 필요한 조회·갱신 연산에 맞춰 자료형을 고르고 Sorted Set은 점수 순으로 멤버를 관리한다.

- String·Hash·List·Set·Sorted Set의 의미가 다르다.
- Sorted Set 멤버는 중복되지 않고 점수로 정렬된다.
- 조회 비용에는 결과 크기도 포함한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

단일 값은 String, 필드 묶음은 Hash, 중복 없는 멤버는 Set으로 표현할 수 있다. Sorted Set은 멤버마다 score를 두어 순위·범위 조회에 사용한다. 점수 갱신은 순서를 바꿀 수 있고 같은 점수의 정렬 규칙도 확인해야 한다. 삽입 O(log N) 같은 기본 연산과 M개의 결과를 반환하는 O(log N + M) 범위 조회를 구분한다.

## 예제

상품별 집계 점수를 ZINCRBY로 갱신하고 상위 목록을 조회할 수 있다. 시간이 점수인 대기열은 동점과 순서 정책을 별도로 정한다.

## 주의점

Redis 명령 하나의 원자성이 DB·Kafka를 포함한 전체 업무의 원자성은 아니다. 모든 명령이 같은 시간복잡도를 가진다고 쓰지 않는다.

## 복습 질문

상위 10개 조회와 전체 100만 개 조회를 둘 다 O(log N)이라고 부르면 무엇을 빠뜨리는가?

자료 구분: **기존 자료** — 캐시·집계·쿠폰 동시성 자료의 원리. **공식 자료 보완** — Redis 명령 비용·원자성·장애 조건.

</details>

## 참고 자료

- [Redis · Data Types](https://redis.io/docs/latest/develop/data-types/) — 키에 담을 자료형과 지원 연산을 비교한다.
- [Redis · Sorted Sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/) — 점수·멤버·범위 조회 및 명령 비용을 확인한다.
