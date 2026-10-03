# 덱

> 양쪽 끝에서 넣고 뺄 수 있는 큐를 제공한다.

- 앞·뒤 삽입과 삭제 네 연산.
- 스택과 큐의 용도로 모두 쓸 수 있다.
- 중간 임의 접근과는 다른 계약이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

덱은 한쪽 끝만 허용하는 스택·큐보다 선택 범위가 넓다. ArrayDeque 같은 원형 배열 구현은 끝 연산을 효율적으로 처리한다. 슬라이딩 윈도우에서는 후보의 인덱스를 저장하고 쓸모없는 후보를 뒤에서 제거하는 데 활용할 수 있다. 어떤 끝이 입력과 출력인지 API 이름을 일관되게 선택한다.

## Java 예제

```java
import java.util.*;

static void demo() {
    Deque<Integer> d = new ArrayDeque<>();
    d.addLast(1);
    d.addLast(2);
    d.addFirst(0);
    System.out.println(d.removeFirst()); // 0
    System.out.println(d.removeLast()); // 2
}
```

## 주의점

offer·poll의 실패 반환과 add·remove의 예외 차이를 확인한다. 일반 덱이 자동으로 스레드 안전한 것은 아니다.

## 꼬리질문

1. 같은 덱을 FIFO와 LIFO로 쓰려면 어떤 끝 연산을 골라야 할까?
2. addLast와 removeFirst를 조합하면 어느 원소가 먼저 빠질까?
3. 여러 스레드가 공유하는 덱에 ArrayDeque를 그대로 쓰면 어떤 보장이 부족할까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
