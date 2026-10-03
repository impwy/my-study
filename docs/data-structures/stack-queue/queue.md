# 큐와 원형 큐

> 먼저 들어온 값을 먼저 꺼내는 FIFO 자료형이다.

- enqueue·dequeue·front를 구분한다.
- 원형 배열은 인덱스를 나머지 연산으로 되돌린다.
- 가득 참과 비어 있음의 구별이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

큐는 도착 순서대로 일을 처리하거나 BFS의 다음 방문을 관리한다. 원형 큐는 앞에서 꺼낸 빈 공간을 다시 이용하므로 매번 배열을 당기지 않는다. front와 rear만 같으면 빈 상태인지 꽉 찬 상태인지 모호할 수 있다. 원소 수를 별도로 저장하거나 한 칸을 비워 두는 규칙으로 해결한다.

## Java 예제

```java
import java.util.*;

static void demo() {
    Queue<String> q = new ArrayDeque<>();
    q.offer("first");
    q.offer("second");
    System.out.println(q.poll()); // first
    System.out.println(q.poll()); // second
    System.out.println(q.poll()); // null
}
```

## 주의점

인덱스 이동 공식만 맞아도 큐가 완성되는 것은 아니다. 삽입 전 용량과 삭제 전 비어 있음 검사가 필요하다.

## 꼬리질문

1. front==rear만으로 빈 큐와 가득 찬 큐를 어떻게 구분할까?
2. 빈 큐에서 poll과 remove의 계약은 어떻게 다를까?
3. 원형 배열 큐에서 size를 따로 유지하면 어떤 두 상태를 구별할 수 있을까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
