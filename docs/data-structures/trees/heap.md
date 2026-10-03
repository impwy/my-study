# 힙과 우선순위 큐

> 완전 이진 트리에서 부모 우선순위를 유지해 가장 중요한 값을 빠르게 꺼낸다.

- 루트 조회 O(1), 삽입·삭제 O(log n).
- 0-based 자식은 2i+1, 2i+2.
- 힙 배열 전체는 정렬되어 있지 않다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

삽입은 마지막에 값을 넣고 부모와 비교하며 올라간다. 루트 삭제는 마지막 값을 루트로 옮기고 우선순위가 높은 자식과 비교하며 내려간다. 완전 트리라 높이는 로그 규모다. 우선순위 큐는 이 규칙을 사용하는 ADT이며 힙은 대표적인 구현이다.

## Java 예제

```java
import java.util.*;

static void demo() {
    PriorityQueue<Integer> heap = new PriorityQueue<>();
    heap.add(4);
    heap.add(1);
    heap.add(3);
    heap.add(2);
    while (!heap.isEmpty()) System.out.println(heap.remove()); // 1,2,3,4
} // iterator 순회에는 정렬 순서 계약이 없다.
```

## 주의점

Comparator에서 a−b를 반환하면 정수 오버플로가 날 수 있다. 큐 안에 있는 객체의 우선순위 필드를 바꾸면 힙 순서가 자동 복구되지 않는다.

## 꼬리질문

1. 힙의 모든 부모가 자식보다 작아도 배열 전체가 오름차순이 아닌 이유는?
2. remove를 반복한 결과는 정렬되어 있는데 iterator는 왜 그 순서를 보장하지 않을까?
3. 최댓값을 먼저 꺼내려면 비교자를 어떻게 바꿔야 할까?

함께 복습: [큐와 원형 큐](../stack-queue/queue.md) · [다익스트라](../../algorithms/graphs/dijkstra.md)

</details>

## 참고 자료

- [Princeton · Priority Queues](https://algs4.cs.princeton.edu/24pq/) — 힙의 배열 표현과 삽입·삭제 과정을 확인한다.
