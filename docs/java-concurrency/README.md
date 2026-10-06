# Java 병렬 프로그래밍

[전체 목록](../../README.md)

## 스레드 안전성

| 문서 | 한 줄 요약 |
| --- | --- |
| [스레드 안전성과 불변식](safety/thread-safety.md) | 공유 객체가 여러 스레드의 접근에도 자신의 불변식을 유지하도록 상태와 접근 경계를 설계한다. |

## 가시성·원자성

| 문서 | 한 줄 요약 |
| --- | --- |
| [volatile의 가시성과 원자성](memory-model/volatile.md) | volatile은 해당 변수의 읽기·쓰기에 가시성·순서 보장을 주지만 증가 연산 전체를 원자적으로 만들지 않는다. |

## 락

| 문서 | 한 줄 요약 |
| --- | --- |
| [모니터와 명시적 락](locks/monitor-and-lock.md) | 락은 같은 상태를 다루는 스레드들의 임계 영역 진입을 조정하고 메모리 가시성을 연결한다. |

## Executor·Future

| 문서 | 한 줄 요약 |
| --- | --- |
| [Executor와 Future](executors/executor-and-future.md) | 작업 제출과 실행 스레드 관리를 분리하고 Future로 완료·실패·취소 결과를 받는다. |
| [Virtual Thread와 WebFlux의 선택 기준](executors/virtual-threads.md) | Virtual Thread는 블로킹 I/O 동시 작업의 스레드 비용을 줄이고 WebFlux는 논블로킹 흐름과 백프레셔를 제공한다. |

## 동시성 컬렉션

| 문서 | 한 줄 요약 |
| --- | --- |
| [동시성 컬렉션의 연산 경계](collections/concurrent-collections.md) | 동시성 컬렉션은 명시된 개별·복합 API를 안전하게 제공하지만 호출 여러 개를 자동으로 한 작업으로 묶지 않는다. |

