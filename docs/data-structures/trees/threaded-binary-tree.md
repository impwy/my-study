# 스레드 이진 트리

> 비어 있는 자식 링크를 순회의 이전·다음 노드 연결에 활용한다.

- 자식과 스레드를 플래그로 구별한다.
- 중위 순회에서 재귀·스택을 줄일 수 있다.
- 삽입·삭제 때 스레드도 유지한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

일반 트리의 null 자식 링크에 중위 순회의 predecessor 또는 successor를 연결한다. 순회는 실제 오른쪽 자식이 있으면 그 서브트리의 가장 왼쪽으로 가고, 없으면 successor 스레드를 따른다. 이 연결은 스레드 실행을 뜻하지 않으며 순회를 위한 추가 정보다.

## Java 예제

오른쪽 스레드만 둔 표현의 후속 노드 탐색이다. left는 실제 자식 링크다.

```java
static class Node {
    int key;
    Node left, right;
    boolean rightThread;
}

static Node leftmost(Node n) {
    while (n != null && n.left != null) n = n.left;
    return n;
}

static Node next(Node n) {
    return n.rightThread ? n.right : leftmost(n.right);
} // 오른쪽 스레드가 있으면 right는 자식 대신 중위 후속 노드
```

## 주의점

플래그 없이 자식 링크와 혼용하면 사이클처럼 끝나지 않을 수 있다. 스레드의 수와 방향은 구현마다 다르다.

## 꼬리질문

1. 스레드 링크를 자식 링크로 잘못 읽으면 어떤 문제가 생길까?
2. 오른쪽 자식이 있을 때 후속 노드가 그 서브트리의 가장 왼쪽 노드인 이유는 무엇일까?
3. 스레드 여부 플래그 없이 일반 재귀 순회를 적용하면 어떤 순환이 생길 수 있을까?

</details>

## 참고 자료

- [Princeton · Binary Search Trees](https://algs4.cs.princeton.edu/32bst/) — 순서 불변식과 삭제의 세 가지 경우를 확인한다.
