# 운영체제

[전체 목록](../../README.md)

## 프로세스·스레드

| 문서 | 한 줄 요약 |
| --- | --- |
| [프로세스 상태와 문맥 교환](processes/context-switch.md) | 실행 가능한 작업을 바꿀 때 실행 위치와 상태를 저장하고 복원한다. |
| [프로세스와 스레드](processes/process-thread.md) | 프로세스는 실행 자원의 경계를, 스레드는 그 안의 실행 흐름을 제공한다. |

## 스케줄링

| 문서 | 한 줄 요약 |
| --- | --- |
| [CPU 스케줄링](scheduling/cpu-scheduling.md) | 준비된 작업 중 다음 CPU 사용자를 정책에 따라 선택한다. |
| [디스크 스케줄링](scheduling/disk-scheduling.md) | 저장장치의 접근 요청 순서를 조정해 이동 비용과 공정성을 관리한다. |

## 동기화·교착상태

| 문서 | 한 줄 요약 |
| --- | --- |
| [교착상태](synchronization/deadlock.md) | 서로 가진 자원을 기다리는 실행들이 더 이상 진행하지 못한다. |
| [생산자–소비자](synchronization/producer-consumer.md) | 한정된 버퍼에서 비어 있는 칸과 준비된 항목을 조정한다. |
| [임계 구역과 동기화](synchronization/critical-section.md) | 공유 상태의 불변식이 깨지지 않도록 동시에 들어오는 실행을 제어한다. |

## 가상 메모리

| 문서 | 한 줄 요약 |
| --- | --- |
| [가상 메모리와 페이지 변환](memory/virtual-memory.md) | 프로세스의 주소를 물리 메모리의 위치로 변환해 격리와 유연한 배치를 제공한다. |
| [페이지 교체와 스래싱](memory/page-replacement.md) | 빈 프레임이 없을 때 내보낼 페이지를 고르고 메모리 부족의 반복 비용을 관리한다. |

