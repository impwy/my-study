# 이진 탐색 트리

> 왼쪽 키는 작고 오른쪽 키는 크다는 규칙으로 후보를 줄인다.

- 탐색 비용은 높이 O(h).
- 중위 순회는 키 순서로 방문한다.
- 균형이 없으면 최악 O(n).

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

현재 키와 목표를 비교해 한쪽 서브트리만 탐색한다. 삭제는 자식 없음·하나·둘로 나눈다. 자식 둘이면 오른쪽의 최솟값 같은 순서상 다음 키로 대체하고 해당 노드를 제거한다. 중복 키는 값 덮어쓰기·개수 저장·한쪽 배치 중 명시적인 정책을 정한다.

## Java 예제

```java
record Node(int key, Node left, Node right) {}

static boolean contains(Node n, int key) {
    while (n != null) {
        if (key == n.key()) return true;
        n = key < n.key() ? n.left() : n.right();
    }
    return false;
}
```

## 주의점

“평균 O(log n)”에는 입력·트리 구성에 대한 가정이 있다. 임의의 BST가 최악 로그 시간을 보장하지 않는다.

## 꼬리질문

1. 정렬된 데이터를 순서대로 넣으면 왜 균형이 깨질 수 있을까?
2. 탐색에서 한쪽 자식을 버릴 수 있는 것은 어떤 불변식 때문일까?
3. 1부터 n까지 순서대로 삽입한 트리에서 마지막 키 탐색 비용은 어떻게 될까?

함께 복습: [AVL 트리](avl-tree.md) · [Red–Black Tree와 B-tree](red-black-and-b-tree.md)

</details>

## 참고 자료

- [Princeton · Binary Search Trees](https://algs4.cs.princeton.edu/32bst/) — 순서 불변식과 삭제의 세 가지 경우를 확인한다.
