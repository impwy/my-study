# 연결 리스트

> 노드 사이의 연결을 바꾸어 순서를 관리한다.

- 위치 탐색은 O(n).
- 삽입 위치의 링크를 이미 알면 O(1) 변경이 가능하다.
- 단방향·양방향은 저장 링크와 연산이 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

배열처럼 모든 원소를 옮기지 않고 새 노드를 연결할 수 있다. 하지만 그 위치까지 가는 비용은 따로 든다. 단일 리스트 삭제는 이전 노드의 next를 바꾸어 대상을 건너뛴다. 이중 리스트는 양방향 링크를 함께 맞춰야 앞·뒤 이동이 일관된다. head·tail과 원소 한 개일 때의 경계를 점검한다.

## Java 예제

```java
static class Node {
    int value;
    Node next;

    Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }
}

static void insertAfter(Node previous, int value) {
    previous.next = new Node(value, previous.next);
}

static int get(Node head, int index) {
    for (int i = 0; i < index; i++) {
        if (head == null) throw new IndexOutOfBoundsException();
        head = head.next;
    }
    if (head == null) throw new IndexOutOfBoundsException();
    return head.value;
}
```

## 주의점

“연결 리스트 삽입 O(1)”만 말하면 위치 탐색을 숨길 수 있다. C++의 해제 책임과 Java의 가비지 컬렉션을 구분한다.

## 꼬리질문

1. 인덱스 900번 위치에 삽입할 때 연결 리스트가 항상 배열보다 빠를까?
2. insertAfter가 새 노드의 next를 먼저 연결하는 이유는 무엇일까?
3. 삽입 위치를 이미 아는 경우와 인덱스로 찾아야 하는 경우의 전체 비용은 어떻게 다를까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
