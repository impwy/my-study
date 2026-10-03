# 자료구조

[전체 목록](../../README.md)

## 배열·연결 리스트

| 문서 | 한 줄 요약 |
| --- | --- |
| [배열과 행렬의 메모리 표현](linear/array-layout.md) | 인덱스를 주소 계산으로 바꾸어 원소에 접근한다. |
| [연결 리스트](linear/linked-list.md) | 노드 사이의 연결을 바꾸어 순서를 관리한다. |
| [추상 자료형](linear/abstract-data-type.md) | 데이터의 사용 규칙과 연산을 구현 방식에서 분리한다. |
| [희소 행렬과 희소 다항식](linear/sparse-representation.md) | 대부분이 0인 데이터에서 실제 값이 있는 항만 저장한다. |

## 스택·큐

| 문서 | 한 줄 요약 |
| --- | --- |
| [덱](stack-queue/deque.md) | 양쪽 끝에서 넣고 뺄 수 있는 큐를 제공한다. |
| [스택](stack-queue/stack.md) | 마지막에 넣은 값을 먼저 꺼내는 LIFO 자료형이다. |
| [큐와 원형 큐](stack-queue/queue.md) | 먼저 들어온 값을 먼저 꺼내는 FIFO 자료형이다. |

## 해시

| 문서 | 한 줄 요약 |
| --- | --- |
| [해시 테이블](hash/hash-table.md) | 키를 버킷 위치로 바꾸고 충돌을 처리해 탐색을 빠르게 한다. |

## 트리·힙

| 문서 | 한 줄 요약 |
| --- | --- |
| [AVL 트리](trees/avl-tree.md) | 각 노드의 좌우 높이 차를 제한해 BST가 한쪽으로 길어지는 것을 막는다. |
| [Red–Black Tree와 B-tree](trees/red-black-and-b-tree.md) | 높이를 제한하는 균형 규칙과 한 노드의 키 수로 검색 트리의 접근 비용을 관리한다. |
| [구간 트리와 Fenwick Tree](trees/range-query-trees.md) | 값 갱신과 구간 질의를 함께 처리하려고 부분 구간의 정보를 트리에 저장한다. |
| [수식 트리](trees/expression-tree.md) | 피연산자를 잎에, 연산자를 내부 노드에 두어 수식 구조를 표현한다. |
| [스레드 이진 트리](trees/threaded-binary-tree.md) | 비어 있는 자식 링크를 순회의 이전·다음 노드 연결에 활용한다. |
| [이진 탐색 트리](trees/binary-search-tree.md) | 왼쪽 키는 작고 오른쪽 키는 크다는 규칙으로 후보를 줄인다. |
| [이진 트리와 순회](trees/binary-tree.md) | 한 노드의 두 서브트리에 같은 작업을 반복한다. |
| [힙과 우선순위 큐](trees/heap.md) | 완전 이진 트리에서 부모 우선순위를 유지해 가장 중요한 값을 빠르게 꺼낸다. |

## 그래프

| 문서 | 한 줄 요약 |
| --- | --- |
| [그래프의 인접 행렬과 인접 리스트](graphs/graph-representation.md) | 정점 사이의 관계를 저장하는 방식에 따라 공간과 탐색 비용이 달라진다. |

