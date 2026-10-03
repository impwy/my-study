# my-study

짧은 요약과 원문 링크로 남기는 기술 학습 기록.

## 분류

| 카테고리 | 문서 | 소분류 |
| --- | ---: | --- |
| [컴퓨터 구조](docs/computer-architecture/README.md) | 9 | 데이터 표현 · CPU·명령어 · 메모리·캐시 · 입출력 |
| [운영체제](docs/operating-systems/README.md) | 9 | 프로세스·스레드 · 스케줄링 · 동기화·교착상태 · 가상 메모리 |
| [네트워크](docs/network/README.md) | 10 | TCP/IP · TCP·UDP · DNS · HTTP·TLS |
| [데이터베이스](docs/database/README.md) | 11 | 관계형 모델 · SQL · 인덱스 · 트랜잭션·격리 수준 |
| [자료구조](docs/data-structures/README.md) | 17 | 배열·연결 리스트 · 스택·큐 · 해시 · 트리·힙 · 그래프 |
| [알고리즘](docs/algorithms/README.md) | 36 | 복잡도 · 탐색 · 정렬 · 그래프 탐색 · 그리디·동적 계획법 |
| [Java](docs/java/README.md) | 11 | 언어·타입 · 객체지향 · 컬렉션·제네릭 · 예외 · 스트림 · JVM·GC |
| [Java 병렬 프로그래밍](docs/java-concurrency/README.md) | 5 | 스레드 안전성 · 가시성·원자성 · 락 · Executor·Future · 동시성 컬렉션 |
| [Linux](docs/linux/README.md) | 6 | 파일·권한 · 프로세스 · 셸 · 네트워크 명령어 · 서비스·로그 |
| [클라우드](docs/cloud/README.md) | 6 | 가상화 · 컴퓨팅·스토리지 · 네트워크 · 확장성·가용성 |
| [컴퓨터 보안](docs/security/README.md) | 6 | 암호·해시 · 인증·인가 · 웹 취약점 · 접근 제어 |
| [MySQL](docs/mysql/README.md) | 4 | 스키마·SQL · 실행 계획 · InnoDB·인덱스 · MVCC·락 |
| [Redis](docs/redis/README.md) | 5 | 자료형 · 캐시·TTL · 영속성 · 복제 · 장애 대응 |
| [Kafka](docs/kafka/README.md) | 8 | 토픽·파티션 · 프로듀서 · 컨슈머·오프셋 · 전달 보장 |
| [Spring](docs/spring/README.md) | 6 | IoC·DI · 빈 생명주기 · AOP · MVC · 트랜잭션 |
| [Spring Boot](docs/spring-boot/README.md) | 4 | 자동 설정 · 설정·프로파일 · 웹 애플리케이션 · Actuator |
| [JPA](docs/jpa/README.md) | 6 | 엔티티 매핑 · 영속성 컨텍스트 · 연관관계 · 조회·N+1 · 락 |
| [REST API](docs/rest-api/README.md) | 5 | 리소스 설계 · 메서드·상태 코드 · 멱등성 · 페이지네이션·오류 |
| [JavaScript](docs/javascript/README.md) | 6 | 타입·스코프 · 클로저 · 프로토타입 · 비동기·이벤트 루프 |
| [Vue.js](docs/vue/README.md) | 5 | 반응성 · 컴포넌트 · Composition API · 라우팅·상태 관리 |
| [React](docs/react/README.md) | 5 | 렌더링 · props·state · Hooks · 상태 관리·라우팅 |
| [AWS](docs/aws/README.md) | 8 | IAM · VPC · EC2 · S3 · RDS · 로드밸런싱·모니터링 |
| [Git](docs/git/README.md) | 4 | 커밋·브랜치 · merge·rebase · 충돌 해결 · 복구 |
| [GitHub Actions](docs/github-actions/README.md) | 4 | 워크플로 · 이벤트·잡 · 테스트·빌드 · 배포 |
| [DDD](docs/ddd/README.md) | 4 | 도메인 모델 · 바운디드 컨텍스트 · 엔티티·값 객체 · 애그리거트·이벤트 |
| [TDD](docs/tdd/README.md) | 4 | Red–Green–Refactor · 테스트 설계 · 테스트 대역 · 단위·통합 테스트 |
| [데이터 중심 애플리케이션](docs/ddia/README.md) | 5 | 데이터 모델 · 저장 엔진 · 복제·파티셔닝 · 일관성 · 배치·스트림 처리 |
| [디자인 패턴](docs/design-patterns/README.md) | 5 | 설계 원칙 · 생성 패턴 · 구조 패턴 · 행동 패턴 · 적용 조건·트레이드오프 |

## 문서 목록

<details>
<summary>컴퓨터 구조 · 9개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [CPU와 명령어 사이클](docs/computer-architecture/cpu/instruction-cycle.md) | 명령어를 읽고 해석해 연산·메모리 접근·다음 실행 위치를 결정한다. |
| [데이터 경로와 제어 장치](docs/computer-architecture/cpu/control-unit.md) | 제어 신호가 레지스터·ALU·버스의 데이터 흐름을 선택한다. |
| [디지털 논리와 상태](docs/computer-architecture/representation/digital-logic.md) | 논리 게이트로 값을 계산하고 순차 회로로 상태를 기억한다. |
| [메모리 계층과 캐시](docs/computer-architecture/memory/cache.md) | 자주 쓰는 데이터를 가까이 두어 느린 메모리 접근을 줄인다. |
| [명령어 파이프라인](docs/computer-architecture/cpu/pipeline.md) | 여러 명령어의 서로 다른 처리 단계를 겹쳐 처리량을 높인다. |
| [병렬 처리와 메모리 구조](docs/computer-architecture/cpu/parallelism-models.md) | 명령·데이터·프로세서·메모리의 조직으로 병렬성을 구분하고 통신·동기화 비용을 고려한다. |
| [주소 지정 방식](docs/computer-architecture/cpu/addressing-modes.md) | 명령어가 실제 피연산자의 값이나 위치를 찾는 규칙이다. |
| [진법·보수·부동소수점](docs/computer-architecture/representation/number-representation.md) | 비트 패턴은 표현 규칙에 따라 정수·문자·실수가 되며 범위와 정밀도에 제한이 있다. |
| [폴링·인터럽트·DMA](docs/computer-architecture/io/interrupt-dma.md) | CPU와 입출력 장치가 상태를 확인하고 데이터를 옮기는 책임을 나눈다. |

</details>

<details>
<summary>운영체제 · 9개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [CPU 스케줄링](docs/operating-systems/scheduling/cpu-scheduling.md) | 준비된 작업 중 다음 CPU 사용자를 정책에 따라 선택한다. |
| [가상 메모리와 페이지 변환](docs/operating-systems/memory/virtual-memory.md) | 프로세스의 주소를 물리 메모리의 위치로 변환해 격리와 유연한 배치를 제공한다. |
| [교착상태](docs/operating-systems/synchronization/deadlock.md) | 서로 가진 자원을 기다리는 실행들이 더 이상 진행하지 못한다. |
| [디스크 스케줄링](docs/operating-systems/scheduling/disk-scheduling.md) | 저장장치의 접근 요청 순서를 조정해 이동 비용과 공정성을 관리한다. |
| [생산자–소비자](docs/operating-systems/synchronization/producer-consumer.md) | 한정된 버퍼에서 비어 있는 칸과 준비된 항목을 조정한다. |
| [임계 구역과 동기화](docs/operating-systems/synchronization/critical-section.md) | 공유 상태의 불변식이 깨지지 않도록 동시에 들어오는 실행을 제어한다. |
| [페이지 교체와 스래싱](docs/operating-systems/memory/page-replacement.md) | 빈 프레임이 없을 때 내보낼 페이지를 고르고 메모리 부족의 반복 비용을 관리한다. |
| [프로세스 상태와 문맥 교환](docs/operating-systems/processes/context-switch.md) | 실행 가능한 작업을 바꿀 때 실행 위치와 상태를 저장하고 복원한다. |
| [프로세스와 스레드](docs/operating-systems/processes/process-thread.md) | 프로세스는 실행 자원의 경계를, 스레드는 그 안의 실행 흐름을 제공한다. |

</details>

<details>
<summary>네트워크 · 10개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [CIDR와 경로 선택](docs/network/tcp-ip/cidr-and-forwarding.md) | 주소의 네트워크 접두어와 라우팅 테이블의 가장 긴 일치로 다음 홉을 결정한다. |
| [CORS와 브라우저 출처](docs/network/http-tls/cors.md) | CORS는 다른 출처의 응답을 웹 페이지에 공유할 수 있는지 정하며 서버 인증·인가와 별개다. |
| [DNS 이름 해석](docs/network/dns/name-resolution.md) | 리졸버는 캐시와 계층적 권한 서버를 이용해 이름에 해당하는 레코드를 찾는다. |
| [HTTP 메서드와 상태 코드](docs/network/http-tls/http-semantics.md) | HTTP의 메서드·상태 코드는 요청 의도와 결과를 전달하는 공통 계약이다. |
| [TCP 바이트 스트림과 메시지 경계](docs/network/transport/tcp-byte-stream.md) | TCP는 순서 있는 바이트 스트림을 제공하므로 응용 메시지의 경계는 애플리케이션이 정해야 한다. |
| [TCP/IP 계층과 라우팅](docs/network/tcp-ip/layers-and-routing.md) | 주소·경로·전송·응용 규약의 책임을 나누어 데이터가 상대 애플리케이션까지 가는 흐름을 설명한다. |
| [TCP와 UDP 선택](docs/network/transport/tcp-and-udp.md) | TCP의 연결·바이트 스트림과 UDP의 데이터그램을 요구하는 지연·신뢰성·경계 조건으로 비교한다. |
| [TLS와 HTTPS](docs/network/http-tls/tls-handshake.md) | TLS는 상대 인증·키 합의로 만든 보안 채널에 HTTP를 실어 전송 중 데이터를 보호한다. |
| [링크 계층과 오류 검출](docs/network/tcp-ip/ethernet-and-error-control.md) | 같은 링크의 프레임 전달·매체 접근·오류 검출을 종단 간 전송 보장과 구분한다. |
| [흐름 제어와 혼잡 제어](docs/network/transport/flow-and-congestion-control.md) | 수신자가 받을 수 있는 양과 네트워크가 감당할 수 있는 양을 각각 고려해 전송을 조절한다. |

</details>

<details>
<summary>데이터베이스 · 11개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [B+ 트리 인덱스](docs/database/indexes/b-plus-tree.md) | 많은 키를 한 노드에 담아 디스크 접근 깊이를 줄이고 범위 탐색을 연결한다. |
| [PostgreSQL 페이지·튜플과 MVCC](docs/database/transactions/postgresql-page-and-tuple.md) | 행 버전을 페이지에 저장하고 트랜잭션 가시성으로 읽을 버전을 고르며 불필요해진 버전을 정리한다. |
| [SQL 조회·조인·집계](docs/database/sql/select-join-group.md) | 필요한 행을 고르고 관계를 연결한 뒤 집계 조건을 적용한다. |
| [격리 수준과 동시성 이상](docs/database/transactions/isolation.md) | 동시에 실행된 트랜잭션에서 어떤 값을 관찰하고 충돌을 어떻게 처리할지 정한다. |
| [관계형 모델과 키](docs/database/relational/relational-model.md) | 테이블의 행을 구별하고 관계·제약으로 데이터의 의미를 지킨다. |
| [락·직렬 가능성·2PL](docs/database/transactions/concurrency-control.md) | 동시 작업의 순서를 제한해 충돌하는 읽기·쓰기를 조정한다. |
| [로그와 장애 회복](docs/database/transactions/write-ahead-log.md) | 데이터 변경보다 복구 정보를 먼저 기록해 장애 뒤 결과를 재구성한다. |
| [스키마·제약 조건·뷰](docs/database/sql/schema-constraints-and-views.md) | 테이블의 구조와 데이터 규칙을 DB에 선언하고 조회 표현을 뷰로 제공한다. |
| [정규화](docs/database/relational/normalization.md) | 속성 사이의 종속 관계를 분리해 갱신 이상을 줄인다. |
| [트랜잭션과 ACID](docs/database/transactions/acid.md) | 여러 데이터 변경을 하나의 논리적 작업으로 관리한다. |
| [해시와 비트맵 인덱스](docs/database/indexes/hash-and-bitmap-indexes.md) | 동등 비교·범위·집합 조건에 따라 서로 다른 인덱스 표현의 적합성을 판단한다. |

</details>

<details>
<summary>자료구조 · 17개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [AVL 트리](docs/data-structures/trees/avl-tree.md) | 각 노드의 좌우 높이 차를 제한해 BST가 한쪽으로 길어지는 것을 막는다. |
| [Red–Black Tree와 B-tree](docs/data-structures/trees/red-black-and-b-tree.md) | 높이를 제한하는 균형 규칙과 한 노드의 키 수로 검색 트리의 접근 비용을 관리한다. |
| [구간 트리와 Fenwick Tree](docs/data-structures/trees/range-query-trees.md) | 값 갱신과 구간 질의를 함께 처리하려고 부분 구간의 정보를 트리에 저장한다. |
| [그래프의 인접 행렬과 인접 리스트](docs/data-structures/graphs/graph-representation.md) | 정점 사이의 관계를 저장하는 방식에 따라 공간과 탐색 비용이 달라진다. |
| [덱](docs/data-structures/stack-queue/deque.md) | 양쪽 끝에서 넣고 뺄 수 있는 큐를 제공한다. |
| [배열과 행렬의 메모리 표현](docs/data-structures/linear/array-layout.md) | 인덱스를 주소 계산으로 바꾸어 원소에 접근한다. |
| [수식 트리](docs/data-structures/trees/expression-tree.md) | 피연산자를 잎에, 연산자를 내부 노드에 두어 수식 구조를 표현한다. |
| [스레드 이진 트리](docs/data-structures/trees/threaded-binary-tree.md) | 비어 있는 자식 링크를 순회의 이전·다음 노드 연결에 활용한다. |
| [스택](docs/data-structures/stack-queue/stack.md) | 마지막에 넣은 값을 먼저 꺼내는 LIFO 자료형이다. |
| [연결 리스트](docs/data-structures/linear/linked-list.md) | 노드 사이의 연결을 바꾸어 순서를 관리한다. |
| [이진 탐색 트리](docs/data-structures/trees/binary-search-tree.md) | 왼쪽 키는 작고 오른쪽 키는 크다는 규칙으로 후보를 줄인다. |
| [이진 트리와 순회](docs/data-structures/trees/binary-tree.md) | 한 노드의 두 서브트리에 같은 작업을 반복한다. |
| [추상 자료형](docs/data-structures/linear/abstract-data-type.md) | 데이터의 사용 규칙과 연산을 구현 방식에서 분리한다. |
| [큐와 원형 큐](docs/data-structures/stack-queue/queue.md) | 먼저 들어온 값을 먼저 꺼내는 FIFO 자료형이다. |
| [해시 테이블](docs/data-structures/hash/hash-table.md) | 키를 버킷 위치로 바꾸고 충돌을 처리해 탐색을 빠르게 한다. |
| [희소 행렬과 희소 다항식](docs/data-structures/linear/sparse-representation.md) | 대부분이 0인 데이터에서 실제 값이 있는 항만 저장한다. |
| [힙과 우선순위 큐](docs/data-structures/trees/heap.md) | 완전 이진 트리에서 부모 우선순위를 유지해 가장 중요한 값을 빠르게 꺼낸다. |

</details>

<details>
<summary>알고리즘 · 36개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [P·NP·NP-완전](docs/algorithms/complexity/np-completeness.md) | 해를 구하는 비용과 주어진 해를 검증하는 비용을 구분한다. |
| [lower bound와 upper bound](docs/algorithms/search/lower-upper-bound.md) | 정렬된 데이터에서 값의 존재보다 경계 위치를 찾아 중복 구간을 계산한다. |
| [계수 정렬](docs/algorithms/sorting/counting-sort.md) | 키별 개수를 세고 누적 개수로 정렬 위치를 계산한다. |
| [그리디](docs/algorithms/optimization/greedy.md) | 지금의 최선 선택을 반복하되 전체 최적해와 연결되는 근거를 확인한다. |
| [기수 정렬](docs/algorithms/sorting/radix-sort.md) | 각 자리의 안정 정렬을 반복해 전체 키의 순서를 만든다. |
| [깊이 우선 탐색](docs/algorithms/graphs/dfs.md) | 한 경로를 끝까지 내려갔다가 돌아와 다음 후보를 탐색한다. |
| [너비 우선 탐색](docs/algorithms/graphs/bfs.md) | 시작점과 가까운 정점부터 큐로 탐색한다. |
| [누적합과 투 포인터](docs/algorithms/optimization/prefix-sum-and-two-pointers.md) | 반복 구간 계산을 전처리하거나 단조롭게 이동하는 두 경계로 중복 탐색을 줄인다. |
| [다익스트라](docs/algorithms/graphs/dijkstra.md) | 음수가 아닌 가중치에서 가장 가까운 미확정 정점을 차례로 확정한다. |
| [동적 계획법](docs/algorithms/optimization/dynamic-programming.md) | 반복되는 부분 문제의 결과를 저장해 큰 문제를 계산한다. |
| [무손실 압축](docs/algorithms/optimization/data-compression.md) | 반복·빈도·사전을 이용해 원래 데이터를 복원할 수 있는 짧은 표현을 만든다. |
| [문자열 매칭](docs/algorithms/search/string-matching.md) | 패턴의 정보나 해시로 이미 한 비교를 줄이며 문자열에서 위치를 찾는다. |
| [배낭 문제](docs/algorithms/optimization/knapsack.md) | 용량과 사용 가능한 항목 상태를 정의해 최대 가치를 계산한다. |
| [백트래킹](docs/algorithms/optimization/backtracking.md) | 가능한 선택을 시도하고 돌아와 상태를 복원하며 해를 탐색한다. |
| [버블 정렬](docs/algorithms/sorting/bubble-sort.md) | 인접한 원소를 교환해 가장 큰 값을 뒤쪽에 확정한다. |
| [벨만–포드](docs/algorithms/graphs/bellman-ford.md) | 모든 간선을 반복 완화해 음수 간선이 있는 최단 경로를 구한다. |
| [병합 정렬](docs/algorithms/sorting/merge-sort.md) | 배열을 나눠 정렬한 뒤 두 정렬 구간을 비교하며 합친다. |
| [보간 탐색](docs/algorithms/search/interpolation-search.md) | 정렬된 값의 분포로 목표가 있을 위치를 추정한다. |
| [삽입 정렬](docs/algorithms/sorting/insertion-sort.md) | 현재 값을 이미 정렬된 앞 구간의 알맞은 위치에 끼운다. |
| [선택 정렬](docs/algorithms/sorting/selection-sort.md) | 남은 구간의 최솟값을 찾아 현재 자리로 옮긴다. |
| [셸 정렬](docs/algorithms/sorting/shell-sort.md) | 멀리 떨어진 원소를 먼저 정리한 뒤 간격을 줄여 삽입 정렬한다. |
| [순차 탐색](docs/algorithms/search/sequential-search.md) | 앞에서부터 값을 비교해 목표를 찾거나 모든 후보를 확인한다. |
| [슬라이딩 윈도우](docs/algorithms/optimization/sliding-window.md) | 연속 구간을 옮길 때 빠지는 정보와 새로 들어오는 정보만 갱신한다. |
| [연결 요소와 강한 연결 요소](docs/algorithms/graphs/connected-components.md) | 그래프를 서로 연결된 정점 묶음으로 나눈다. |
| [위상 정렬](docs/algorithms/graphs/topological-sort.md) | 선행 조건을 모두 지키는 방향 그래프의 정점 순서를 찾는다. |
| [이진 탐색](docs/algorithms/search/binary-search.md) | 정렬된 배열에서 중간값을 비교해, 정답이 있을 수 없는 절반을 버리는 탐색 방법. |
| [재귀와 호출 스택](docs/algorithms/complexity/recursion.md) | 큰 문제를 더 작은 같은 문제에 맡기고 종료 조건에서 돌아온다. |
| [점근 분석](docs/algorithms/complexity/asymptotic-analysis.md) | 입력 크기가 커질 때 연산 횟수가 어떻게 증가하는지 비교한다. |
| [철근 자르기](docs/algorithms/optimization/rod-cutting.md) | 첫 조각 길이와 남은 길이의 최적 수익을 조합한다. |
| [최대 유량](docs/algorithms/optimization/maximum-flow.md) | 간선 용량과 정점의 흐름 보존을 지키며 시작점에서 끝점까지의 유량을 늘린다. |
| [최소 신장 트리](docs/algorithms/optimization/minimum-spanning-tree.md) | 연결된 무방향 그래프의 모든 정점을 최소 총비용으로 연결한다. |
| [최장 공통 부분 수열](docs/algorithms/optimization/lcs.md) | 순서를 유지하며 건너뛸 수 있는 두 문자열의 가장 긴 공통 수열을 찾는다. |
| [퀵 정렬](docs/algorithms/sorting/quick-sort.md) | 피벗보다 작은 값과 큰 값을 나누고 각 구간을 정렬한다. |
| [큰 정수 표현과 Karatsuba](docs/algorithms/complexity/big-integer-and-karatsuba.md) | 고정 크기 정수 범위를 넘는 수를 자릿수 배열로 표현하고 곱셈의 재귀 구조를 개선한다. |
| [플로이드–워셜](docs/algorithms/graphs/floyd-warshall.md) | 허용하는 중간 정점을 늘려 모든 정점 쌍의 최단거리를 계산한다. |
| [행렬 연쇄 곱셈의 DP](docs/algorithms/optimization/matrix-chain.md) | 곱셈 순서는 유지하면서 괄호 위치를 선택해 전체 스칼라 곱셈 수를 최소화한다. |

</details>

<details>
<summary>Java · 11개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [JDBC 연결과 트랜잭션](docs/java/language/jdbc-boundary.md) | SQL 실행·값 바인딩·결과 처리·트랜잭션·연결 반환의 경계를 관리한다. |
| [JVM 메모리와 GC](docs/java/jvm/jvm-memory-and-gc.md) | GC는 도달할 수 없는 객체의 메모리를 회수하며 애플리케이션 자원 전체를 관리하지 않는다. |
| [NIO의 Buffer와 Channel](docs/java/streams/nio-buffer-channel.md) | 채널을 통해 데이터를 옮기고 버퍼의 position·limit 상태로 읽기·쓰기를 관리한다. |
| [기본형·참조형과 값 전달](docs/java/language/value-and-reference.md) | Java는 기본형 값과 객체 참조 값을 모두 복사해서 메서드에 전달한다. |
| [상속과 다형성](docs/java/oop/inheritance-and-polymorphism.md) | 상위 타입으로 사용하는 객체의 재정의된 인스턴스 메서드는 실제 객체 타입에 따라 실행된다. |
| [스트림 파이프라인](docs/java/streams/stream-pipeline.md) | 스트림은 데이터 저장소가 아니라 원소를 필터링·변환·집계하는 계산 흐름이다. |
| [예외와 자원 정리](docs/java/exceptions/exception-and-resources.md) | 실패를 호출자에게 전달하는 경로와 파일·연결을 닫는 경로를 함께 설계한다. |
| [입출력 스트림과 문자 인코딩](docs/java/streams/io-streams.md) | 바이트 전송과 문자 변환을 구분하고 버퍼·인코딩·종료 책임을 명확히 한다. |
| [제어 흐름과 배열](docs/java/language/control-flow-and-arrays.md) | 조건·반복으로 실행 경로를 정하고 배열의 길이와 인덱스 경계를 지킨다. |
| [컬렉션과 제네릭](docs/java/collections/collections-and-generics.md) | 컬렉션은 저장·탐색 방식으로 고르고, 제네릭으로 원소 타입의 계약을 표현한다. |
| [패키지·라이브러리·모듈](docs/java/language/packages-and-modules.md) | 이름 공간과 배포 묶음, 모듈의 명시적 의존·공개 범위를 구분한다. |

</details>

<details>
<summary>Java 병렬 프로그래밍 · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Executor와 Future](docs/java-concurrency/executors/executor-and-future.md) | 작업 제출과 실행 스레드 관리를 분리하고 Future로 완료·실패·취소 결과를 받는다. |
| [volatile의 가시성과 원자성](docs/java-concurrency/memory-model/volatile.md) | volatile은 해당 변수의 읽기·쓰기에 가시성·순서 보장을 주지만 증가 연산 전체를 원자적으로 만들지 않는다. |
| [동시성 컬렉션의 연산 경계](docs/java-concurrency/collections/concurrent-collections.md) | 동시성 컬렉션은 명시된 개별·복합 API를 안전하게 제공하지만 호출 여러 개를 자동으로 한 작업으로 묶지 않는다. |
| [모니터와 명시적 락](docs/java-concurrency/locks/monitor-and-lock.md) | 락은 같은 상태를 다루는 스레드들의 임계 영역 진입을 조정하고 메모리 가시성을 연결한다. |
| [스레드 안전성과 불변식](docs/java-concurrency/safety/thread-safety.md) | 공유 객체가 여러 스레드의 접근에도 자신의 불변식을 유지하도록 상태와 접근 경계를 설계한다. |

</details>

<details>
<summary>Linux · 6개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [SSH 키와 서버 신원](docs/linux/network/ssh.md) | SSH는 서버 신원 확인과 사용자 인증을 통해 원격 연결을 보호한다. |
| [fork와 exec](docs/linux/processes/fork-and-exec.md) | fork는 자식 프로세스를 만들고 exec는 현재 프로세스의 실행 이미지를 새 프로그램으로 바꾼다. |
| [tmux와 원격 작업 관찰](docs/linux/operations/tmux-and-logs.md) | 원격 접속과 작업 세션을 분리하고 로그·프로세스 상태로 실제 실행을 확인한다. |
| [셸 초기화와 PATH](docs/linux/shell/startup-and-path.md) | 셸 종류·실행 모드에 맞는 설정 파일과 PATH 검색 순서를 확인한다. |
| [파일 권한과 실행 주체](docs/linux/files/permissions.md) | 파일 소유자·그룹·기타 사용자 권한과 실행 프로세스의 주체를 함께 확인한다. |
| [파일 시스템과 버퍼링](docs/linux/files/filesystem-and-buffering.md) | 경로·파일 메타데이터·데이터 블록을 분리하고 메모리 버퍼와 저장 확정의 차이를 이해한다. |

</details>

<details>
<summary>클라우드 · 6개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Kubernetes의 Pod·Deployment·Service](docs/cloud/virtualization/kubernetes-building-blocks.md) | 컨테이너 실행 단위, 원하는 상태 유지, 접근 경로의 책임을 구분한다. |
| [백프레셔와 요청 제한](docs/cloud/availability/backpressure-and-rate-limit.md) | 처리 가능한 속도에 맞춰 유입·대기·거절을 조정해 과부하가 시스템 전체로 번지는 것을 제한한다. |
| [지연·처리량·포화](docs/cloud/availability/latency-throughput-saturation.md) | 부하가 늘 때 처리량·지연 분포·오류·대기열을 함께 보아 병목을 찾는다. |
| [컴퓨팅과 블록·파일·객체 스토리지](docs/cloud/resources/compute-and-storage-boundaries.md) | 애플리케이션의 실행 자원과 데이터 보관 자원을 나누고 접근 방식에 맞는 스토리지를 선택한다. |
| [클라우드 서비스 모델](docs/cloud/virtualization/cloud-service-models.md) | 온디맨드 자원 사용과 IaaS·PaaS·SaaS별 관리 책임의 차이를 설명한다. |
| [클라우드 연결 경로와 아웃바운드 통신](docs/cloud/network/network-path-and-egress.md) | 연결 문제는 DNS·라우팅·접근 제어·서버 대기 상태를 경로 순서대로 확인한다. |

</details>

<details>
<summary>컴퓨터 보안 · 6개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [PKI와 이메일 보안](docs/security/crypto/pki-and-email-security.md) | 공개키의 소유 관계를 신뢰 사슬로 검증하고 이메일의 서명·암호화를 목적별로 적용한다. |
| [SQL Injection·XSS·CSRF](docs/security/web/injection-xss-csrf.md) | 공격이 들어오는 경계와 피해가 발생하는 실행 문맥에 맞춰 웹 취약점을 방어한다. |
| [악성코드와 사고 대응](docs/security/web/malware-and-incident-response.md) | 공격의 유입·실행·확산을 제한하고 증거와 복구 절차를 함께 관리한다. |
| [암호화·해시·전자서명](docs/security/crypto/encryption-hash-signature.md) | 암호화는 기밀성, 해시는 요약, 전자서명은 무결성과 서명자 확인을 위한 서로 다른 도구다. |
| [인증과 인가](docs/security/identity/authentication-authorization.md) | 인증은 주체를 확인하고 인가는 그 주체가 이 자원에서 할 수 있는 행동을 결정한다. |
| [최소 권한과 방어 계층](docs/security/access/least-privilege-defense.md) | 필요한 주체에게 필요한 범위의 권한만 주고 여러 경계에서 실패를 제한한다. |

</details>

<details>
<summary>MySQL · 4개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [InnoDB MVCC와 락](docs/mysql/concurrency/mvcc-and-locks.md) | 스냅샷 읽기와 잠금 읽기를 구분하고 격리 수준·인덱스 조건에 따른 동시 동작을 확인한다. |
| [InnoDB 클러스터드 인덱스](docs/mysql/innodb/clustered-index.md) | InnoDB는 클러스터드 인덱스 리프에 행을 저장하고 보조 인덱스에서 행 식별 키를 이용한다. |
| [MySQL 스키마의 타입·제약·기본값](docs/mysql/sql/schema-types-and-defaults.md) | 테이블은 값의 표현뿐 아니라 누락·중복·범위에 대한 계약을 함께 정의한다. |
| [실행 계획과 복합 인덱스](docs/mysql/plans/explain-and-composite-index.md) | 실제 필터·정렬·조인 조건과 데이터 분포를 기준으로 인덱스의 효과를 검증한다. |

</details>

<details>
<summary>Redis · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Cache-aside와 캐시 스탬피드](docs/redis/cache/cache-aside-and-stampede.md) | 캐시 미스 시 원본을 읽고 채우되 만료 순간 요청이 몰리는 경합과 오래된 값을 관리한다. |
| [Redis RDB·AOF와 복구](docs/redis/persistence/rdb-aof-and-recovery.md) | RDB는 시점의 스냅샷을, AOF는 쓰기 명령 기록을 사용해 재시작 후 데이터를 복구한다. |
| [Redis 복제와 장애 전환](docs/redis/replication/replication-and-failover.md) | 복제본은 데이터 사본을 유지하지만 비동기 복제와 장애 전환에는 지연·손실 가능성이 있다. |
| [Redis 원자 연산과 저장소 간 불일치](docs/redis/failures/atomic-script-and-cross-store.md) | Redis 안의 검사·차감을 원자적으로 묶어도 뒤이은 DB 저장·메시지 발행까지 한 번에 확정되지는 않는다. |
| [Redis 자료형과 Sorted Set](docs/redis/types/types-and-sorted-set.md) | 필요한 조회·갱신 연산에 맞춰 자료형을 고르고 Sorted Set은 점수 순으로 멤버를 관리한다. |

</details>

<details>
<summary>Kafka · 8개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Kafka 전달 보장의 범위](docs/kafka/delivery/idempotence-and-transactions.md) | 프로듀서 멱등성·Kafka 트랜잭션·컨슈머 처리 정책의 보장 범위를 외부 업무 효과와 구분한다. |
| [poll과 컨슈머 타임아웃](docs/kafka/consumers/poll-and-timeouts.md) | 로그를 읽는 주기와 멤버 생존·처리 지연 조건을 나누어 컨슈머 정체를 진단한다. |
| [로그·파티션·오프셋](docs/kafka/topics/log-partition-offset.md) | Kafka는 토픽의 파티션별 추가 로그에 레코드를 저장하고 오프셋으로 위치를 식별한다. |
| [복제·ISR·High Watermark](docs/kafka/topics/replication-and-high-watermark.md) | 리더와 복제본의 로그 진도를 구분하고 소비 가능한 커밋 경계와 장애 시 남는 데이터를 확인한다. |
| [재시도·DLT·재처리](docs/kafka/consumers/retry-dlt-and-replay.md) | 실패한 이벤트의 원인·원문·처리 이력을 보존하고 안전한 재처리와 정합성 확인을 설계한다. |
| [컨슈머 그룹과 리밸런스](docs/kafka/consumers/group-and-rebalance.md) | 그룹은 파티션 작업을 나누고 멤버·토픽 조건이 바뀌면 할당을 다시 조정한다. |
| [컨슈머 오프셋과 커밋](docs/kafka/consumers/offset-and-commit.md) | 커밋에는 다시 시작할 다음 위치를 기록하고 처리 완료되지 않은 레코드를 건너뛰지 않는다. |
| [프로듀서 배치·acks·재시도](docs/kafka/producers/producer-batch-and-acks.md) | 전송 효율과 확인 수준을 조정하되 재시도·시간 제한·순서에 미치는 영향을 함께 확인한다. |

</details>

<details>
<summary>Spring · 6개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [AOP 프록시와 자기 호출](docs/spring/aop/proxy-boundary.md) | Spring의 기본 프록시 방식에서는 프록시를 통과하는 호출에 부가 기능이 적용된다. |
| [IoC와 의존성 주입](docs/spring/di/ioc-and-di.md) | 객체의 생성·연결을 컨테이너에 맡기고 필요한 협력 객체를 외부에서 받는다. |
| [Spring MVC 요청 처리](docs/spring/mvc/request-flow.md) | DispatcherServlet은 요청을 적절한 핸들러에 연결하고 입력·결과 변환과 오류 처리를 조정한다. |
| [Spring 트랜잭션 경계](docs/spring/transactions/transaction-boundary.md) | 하나의 업무에서 함께 성공해야 하는 DB 변경을 명확한 트랜잭션 경계로 묶는다. |
| [빈 생명주기와 싱글턴](docs/spring/lifecycle/bean-lifecycle.md) | 컨테이너는 빈의 생성·주입·초기화·종료를 관리하며 기본 싱글턴은 컨테이너 안에서 공유된다. |
| [트랜잭션 이벤트와 전달 실패](docs/spring/transactions/transaction-events.md) | 이벤트 리스너의 실행 시점과 실행 스레드, 이벤트의 내구성을 각각 설계한다. |

</details>

<details>
<summary>Spring Boot · 4개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Actuator 상태와 메트릭](docs/spring-boot/actuator/health-and-metrics.md) | 서비스의 상태 확인과 성능 관측 정보를 운영에 필요한 범위로 제공한다. |
| [Spring Boot 자동 설정](docs/spring-boot/autoconfiguration/conditional-autoconfiguration.md) | 클래스패스·빈·속성 조건에 맞는 기본 구성을 제공하고 사용자 구성을 존중한다. |
| [Tomcat과 Spring MVC의 역할](docs/spring-boot/web/tomcat-and-servlet.md) | Tomcat은 서블릿 실행 환경을 제공하고 Spring MVC는 요청을 핸들러로 연결해 응답을 조정한다. |
| [외부 설정과 프로파일](docs/spring-boot/configuration/profiles-and-properties.md) | 환경별 설정은 코드에서 분리하고 실제 적용된 값의 우선순위를 확인한다. |

</details>

<details>
<summary>JPA · 6개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [N+1과 조회 설계](docs/jpa/queries/n-plus-one.md) | 필요한 연관 데이터를 개별 추가 쿼리로 읽는 흐름을 관찰하고 화면·업무에 맞는 조회를 설계한다. |
| [flush와 commit](docs/jpa/context/flush-and-commit.md) | flush는 변경을 DB에 동기화하는 과정이고 commit은 트랜잭션을 확정하는 과정이다. |
| [낙관적 락과 비관적 락](docs/jpa/locks/optimistic-and-pessimistic.md) | 동시 변경을 버전 충돌로 감지하거나 DB 락으로 조정해 업무 불변식을 지킨다. |
| [엔티티 식별자와 매핑](docs/jpa/mapping/entity-mapping.md) | JPA 엔티티는 영속 식별자로 구분하며 필드와 테이블의 매핑 규칙을 명시한다. |
| [연관관계의 주인과 양방향 참조](docs/jpa/relationships/owning-side.md) | 외래 키 매핑의 변경 주체와 객체 양쪽의 참조 일관성을 함께 관리한다. |
| [영속성 컨텍스트와 엔티티 상태](docs/jpa/context/persistence-context.md) | 영속성 컨텍스트는 관리 중인 엔티티의 동일성과 변경 추적을 담당한다. |

</details>

<details>
<summary>REST API · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [HTTP 메서드·상태 코드와 재시도 계약](docs/rest-api/http/methods-status-and-retry-contract.md) | 메서드는 작업의 의미를, 상태 코드는 처리 결과를 표현하며 둘을 함께 설계해야 한다. |
| [Problem Details 오류 계약](docs/rest-api/contracts/problem-details.md) | 오류 응답을 공통 구조로 표현하고 업무 오류를 기계가 구분할 수 있게 한다. |
| [REST의 제약과 리소스](docs/rest-api/resources/rest-constraints.md) | REST는 리소스에 대한 통일된 인터페이스와 여러 제약으로 분산 시스템의 상호작용을 설계하는 스타일이다. |
| [멱등 키와 요청 재시도](docs/rest-api/idempotency/idempotency-key.md) | 응답이 유실되어 같은 업무 요청을 재시도해도 결과가 중복 생성되지 않도록 요청의 정체성을 저장한다. |
| [페이지네이션과 안정적인 정렬](docs/rest-api/contracts/pagination.md) | 목록을 나눠 읽을 때 정렬·경계·변경 중 데이터의 일관성을 명확히 한다. |

</details>

<details>
<summary>JavaScript · 6개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [JavaScript 타입과 형 변환](docs/javascript/language/types-and-coercion.md) | 변수의 값 타입은 실행 중 달라질 수 있으며 자동 형 변환과 명시적 변환을 구별해야 한다. |
| [Promise와 async·await](docs/javascript/async/promise-and-await.md) | Promise는 나중의 완료 결과를 표현하고 await는 해당 함수의 후속 실행을 완료 뒤로 이어 준다. |
| [렉시컬 스코프와 TDZ](docs/javascript/language/lexical-scope-and-tdz.md) | 이름을 찾는 범위는 코드가 선언된 위치로 결정되며 let·const는 초기화 전 접근을 허용하지 않는다. |
| [이벤트 루프와 마이크로태스크](docs/javascript/async/event-loop-and-microtasks.md) | 현재 동기 실행이 끝난 뒤 Promise 등의 마이크로태스크를 처리하고 다음 태스크로 진행한다. |
| [클로저와 상태 보존](docs/javascript/closures/captured-environment.md) | 함수는 자신이 만들어진 렉시컬 환경을 참조해 바깥 함수가 종료된 뒤에도 상태를 사용할 수 있다. |
| [프로토타입과 속성 탐색](docs/javascript/objects/prototype-lookup.md) | 객체에 없는 속성은 프로토타입 연결을 따라 찾으며 자기 속성은 상속된 속성을 가릴 수 있다. |

</details>

<details>
<summary>Vue.js · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Composable과 생명주기 정리](docs/vue/composition/composables-and-cleanup.md) | 상태와 생명주기 작업을 함수로 묶어 재사용하고 컴포넌트 종료 때 외부 자원을 정리한다. |
| [Pinia와 공유 상태](docs/vue/state/pinia-shared-state.md) | 여러 컴포넌트가 필요한 상태를 store에 모으고 상태·파생 값·변경 동작의 역할을 나눈다. |
| [Vue Router의 경로와 파라미터](docs/vue/state/router-params-and-navigation.md) | URL을 화면 상태와 연결하고 같은 화면의 파라미터 변경도 새로운 탐색으로 처리한다. |
| [Vue 컴포넌트의 props와 emit](docs/vue/components/props-and-emits.md) | 부모는 props로 값을 전달하고 자식은 이벤트로 변경 의도를 올려 상태의 소유자를 유지한다. |
| [Vue의 ref와 computed](docs/vue/reactivity/ref-and-computed.md) | 반응형 상태를 읽은 계산과 화면을 추적해 상태 변경 시 필요한 결과를 갱신한다. |

</details>

<details>
<summary>React · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [React Router와 URL 상태](docs/react/routing/routes-and-url-state.md) | 라우터는 URL을 화면에 연결하고 파라미터·쿼리·중첩 경로를 탐색 가능한 상태로 다룬다. |
| [React state 스냅샷과 updater](docs/react/state/snapshot-and-updaters.md) | 한 렌더의 state 값은 고정된 스냅샷이며 이전 상태 기반 변경은 updater 함수로 이어 붙인다. |
| [React의 렌더와 커밋](docs/react/rendering/render-and-commit.md) | 렌더는 현재 props·state로 다음 UI를 계산하고 커밋은 필요한 DOM 변경을 적용한다. |
| [useEffect와 cleanup](docs/react/hooks/effects-and-cleanup.md) | Effect는 커밋된 화면을 외부 시스템과 동기화하고 의존성 변경·종료 때 이전 작업을 정리한다. |
| [공유 상태와 reducer](docs/react/routing/shared-state-and-reducer.md) | 여러 화면 조각이 같은 값을 필요로 하면 공통 소유자로 상태를 올리고 변경 규칙을 reducer로 모은다. |

</details>

<details>
<summary>AWS · 8개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [CloudWatch와 CloudTrail](docs/aws/operations/monitoring-and-audit.md) | 운영 지표·로그를 통한 상태 관찰과 AWS API 활동 감사를 구분한다. |
| [EC2·AMI·블록 스토리지](docs/aws/ec2/instance-ami-storage.md) | EC2는 가상 서버를 실행하고 AMI는 시작 이미지, 볼륨은 별도의 저장 수명을 가진다. |
| [IAM 역할과 정책](docs/aws/iam/roles-and-policies.md) | AWS 자원 접근은 주체·정책·조건으로 판단하고 장기 키 대신 적절한 임시 자격 증명을 사용한다. |
| [RDS Multi-AZ와 읽기 복제본](docs/aws/rds/multi-az-and-read-replica.md) | 관리형 DB의 장애 대비와 읽기 확장을 구분하고 실제 배포 방식의 동작을 확인한다. |
| [RTO·RPO와 복구 검증](docs/aws/operations/rto-rpo-and-backup.md) | 허용 중단 시간과 데이터 손실 범위를 정하고 백업에서 실제 복구되는지 확인한다. |
| [S3 객체와 저장소 선택](docs/aws/s3/object-storage.md) | S3는 객체를 키로 저장하며 블록·공유 파일 저장소와 접근 모델이 다르다. |
| [VPC 서브넷·라우팅·보안](docs/aws/vpc/subnets-routes-security.md) | 서브넷의 위치와 경로, 보안 그룹·네트워크 ACL을 구분해 연결 가능성을 판단한다. |
| [로드밸런싱과 Auto Scaling](docs/aws/operations/load-balancing-and-autoscaling.md) | 트래픽 분산과 인스턴스 수 조정을 결합하되 상태·용량·준비 시간을 함께 설계한다. |

</details>

<details>
<summary>Git · 4개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Git restore·reset·revert 선택](docs/git/recovery/restore-reset-revert.md) | 복구 명령은 파일·스테이징·브랜치 이력 중 무엇을 되돌릴지 먼저 정해 선택한다. |
| [merge와 rebase](docs/git/integration/merge-and-rebase.md) | merge는 이력을 합치는 커밋을 만들 수 있고 rebase는 커밋을 새 기반에 다시 적용한다. |
| [충돌 해결과 변경 보존](docs/git/conflicts/conflict-and-recovery.md) | 충돌한 양쪽의 의도를 읽어 통합하고 되돌리기 전에 현재 변경을 보존한다. |
| [커밋·브랜치와 세 작업 영역](docs/git/history/commit-branch-and-areas.md) | 작업 트리·인덱스·커밋을 구분하고 브랜치를 커밋을 가리키는 이름으로 이해한다. |

</details>

<details>
<summary>GitHub Actions · 4개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [CI 캐시와 아티팩트](docs/github-actions/ci/cache-and-artifacts.md) | 재사용 가능한 의존성 캐시와 실행 결과를 전달하는 아티팩트를 목적별로 구분한다. |
| [GitHub Actions 이벤트·잡·행렬](docs/github-actions/jobs/matrix-and-job-dependencies.md) | 이벤트가 워크플로를 시작하고 matrix와 needs가 잡의 실행 조합과 순서를 정한다. |
| [배포 권한·상태 확인·롤백](docs/github-actions/cd/deployment-oidc-and-rollback.md) | 검증한 산출물을 제한된 권한으로 배포하고 실제 상태 확인 뒤 실패를 복구한다. |
| [워크플로·이벤트·잡·스텝](docs/github-actions/workflows/events-jobs-steps.md) | 이벤트가 워크플로를 시작하고 잡이 실행 환경을 가지며 스텝이 순서대로 작업한다. |

</details>

<details>
<summary>DDD · 4개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [도메인 모델과 유비쿼터스 언어](docs/ddd/model/domain-and-language.md) | 업무의 개념·규칙을 팀이 함께 쓰는 언어와 모델로 표현한다. |
| [바운디드 컨텍스트](docs/ddd/contexts/bounded-context.md) | 한 모델과 용어가 일관된 의미를 갖는 경계를 정하고 경계 사이의 번역을 설계한다. |
| [애그리거트와 도메인 이벤트](docs/ddd/aggregates/aggregate-and-events.md) | 일관성 경계의 루트를 통해 규칙을 보호하고 이미 일어난 업무 사실을 이벤트로 전달한다. |
| [엔티티와 값 객체](docs/ddd/identity/entity-value-object.md) | 엔티티는 지속되는 정체성으로, 값 객체는 값과 의미로 구분한다. |

</details>

<details>
<summary>TDD · 4개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Red–Green–Refactor](docs/tdd/cycle/red-green-refactor.md) | 실패하는 작은 테스트로 요구를 드러내고 최소 구현 뒤 설계를 개선한다. |
| [단위·통합·인수 테스트](docs/tdd/levels/unit-and-integration.md) | 작은 규칙의 빠른 검증과 실제 경계 연동·사용자 요구 검증을 목적별로 나눈다. |
| [테스트 대역의 목적](docs/tdd/doubles/test-doubles.md) | 느리거나 통제하기 어려운 협력자를 목적에 맞는 대역으로 바꾸고 실제 연동은 별도로 검증한다. |
| [행동과 경계값 테스트](docs/tdd/design/behavior-and-boundaries.md) | 요구한 결과와 불변식을 검증하고 입력·상태·실패 경계를 대표하는 사례를 선택한다. |

</details>

<details>
<summary>데이터 중심 애플리케이션 · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [LSM 트리와 컴팩션](docs/ddia/storage/lsm-and-compaction.md) | LSM은 쓰기를 메모리에 모아 정렬 파일로 내보내고 병합하면서 읽기·쓰기 비용을 조절한다. |
| [Outbox와 정합성 대사](docs/ddia/consistency/outbox-and-reconciliation.md) | DB 변경과 발송할 이벤트를 함께 기록하고 비동기 전달의 중복·누락을 감지·복구한다. |
| [관계형·문서·그래프 데이터 모델](docs/ddia/models/relational-document-graph-models.md) | 모델 선택은 데이터 모양뿐 아니라 함께 읽고 갱신하는 방식과 관계 탐색으로 결정한다. |
| [배치와 스트림 처리](docs/ddia/processing/batch-and-stream.md) | 유한한 입력 묶음의 처리와 계속 도착하는 이벤트의 처리를 완료·재시작·지연 기준으로 비교한다. |
| [복제와 파티셔닝](docs/ddia/distribution/replication-partitioning.md) | 복제는 사본을 늘리고 파티셔닝은 데이터를 나누며 각각 가용성·용량·운영의 다른 문제를 다룬다. |

</details>

<details>
<summary>디자인 패턴 · 5개</summary>

| 문서 | 한 줄 요약 |
| --- | --- |
| [Factory와 Facade](docs/design-patterns/creational/factory-and-facade.md) | 생성 결정을 모으는 Factory와 여러 협력의 사용 절차를 단순화하는 Facade를 구분한다. |
| [SOLID와 변경 이유](docs/design-patterns/principles/solid.md) | 설계 원칙은 변경과 대체의 비용을 줄이는 판단 기준이며 규칙 이름보다 실제 의존 관계를 본다. |
| [Strategy](docs/design-patterns/behavioral/strategy.md) | 서로 바꿀 수 있는 행동을 같은 계약의 여러 구현으로 분리한다. |
| [디자인 패턴의 적용 조건과 YAGNI](docs/design-patterns/tradeoffs/pattern-selection-and-yagni.md) | 패턴은 실제로 바뀌는 지점을 분리할 때 쓰고 예상만 있는 확장성의 비용을 함께 계산한다. |
| [포트·어댑터와 의존 방향](docs/design-patterns/structural/hexagonal-ports-adapters.md) | 핵심 업무와 외부 기술의 접점을 계약으로 나누어 실행·테스트 환경을 바꿀 수 있게 한다. |

</details>

