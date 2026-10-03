# AVL 트리

> 각 노드의 좌우 높이 차를 제한해 BST가 한쪽으로 길어지는 것을 막는다.

- 균형 인수는 왼쪽 높이−오른쪽 높이.
- 모든 노드에서 절댓값이 1 이하.
- 회전은 키 순서를 보존한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

삽입·삭제 후 경로를 되짚으며 높이와 균형을 갱신한다. LL·RR은 한 번, LR·RL은 두 번 회전해 구조를 고친다. 회전은 서브트리의 연결만 바꾸며 중위 키 순서를 유지한다. 높이를 로그 규모로 제한하므로 탐색·삽입·삭제의 최악 비용도 O(log n)이 된다.

## Java 예제

LL 불균형의 단일 회전이다. 삽입·삭제 전체 구현에는 높이 검사와 나머지 회전 경우도 필요하다.

```java
static class Node {
    int key;
    Node left, right;
    int height = 1;

    Node(int key) {
        this.key = key;
    }
}

static int h(Node n) {
    return n == null ? 0 : n.height;
}

static void update(Node n) {
    n.height = 1 + Math.max(h(n.left), h(n.right));
}

static Node rotateRight(Node y) {
    Node x = y.left, middle = x.right;
    x.right = y;
    y.left = middle;
    update(y);
    update(x);
    return x;
}
```

## 주의점

회전 뒤 옛 루트와 새 루트의 높이를 맞는 순서로 갱신한다. AVL과 red-black은 같은 균형 규칙을 쓰지 않는다.

## 꼬리질문

1. 회전으로 노드 위치를 바꿔도 BST의 키 순서가 유지되는 이유는?
2. 오른쪽 회전 전후에 middle 서브트리의 키는 어떤 두 키 사이에 있어야 할까?
3. 왼쪽 자식의 오른쪽 가지가 무거운 경우 단일 오른쪽 회전만으로 균형을 복구할 수 있을까?

</details>

## 참고 자료

- [Princeton · Balanced Search Trees](https://algs4.cs.princeton.edu/33balanced/) — 높이 제한과 회전으로 균형을 유지하는 원리를 비교한다.
