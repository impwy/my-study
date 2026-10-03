# 이진 트리와 순회

> 한 노드의 두 서브트리에 같은 작업을 반복한다.

- 노드당 자식은 최대 두 개다.
- 전위·중위·후위는 현재 노드 방문 시점의 차이다.
- 높이와 합은 빈 트리의 기준값을 먼저 정한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

이진 트리는 BST의 정렬 규칙을 반드시 가지는 것은 아니다. 전위는 현재→왼쪽→오른쪽, 중위는 왼쪽→현재→오른쪽, 후위는 왼쪽→오른쪽→현재다. 높이를 노드 수로 세면 빈 트리는 0, 현재 높이는 1+max(왼쪽,오른쪽)이다. 간선 수 기준을 쓰면 기준값이 달라진다.

## Java 예제

```java
record Node(int value, Node left, Node right) {}

static void inorder(Node n) {
    if (n == null) return;
    inorder(n.left());
    System.out.println(n.value());
    inorder(n.right());
} // Node(1, Node(9,null,null), Node(2,null,null)) → 9,1,2
```

## 주의점

일반 이진 트리의 중위 순회가 항상 오름차순은 아니다. 부모보다 자식을 먼저 정리해야 하는 작업은 후위 순회가 자연스럽다.

## 꼬리질문

1. 이진 트리와 이진 탐색 트리의 조건은 무엇이 다를까?
2. 예제의 중위 순회가 오름차순이 아닌 이유는 어떤 조건이 빠져 있기 때문일까?
3. 완전 이진 트리와 포화 이진 트리는 마지막 레벨의 채움 조건이 어떻게 다를까?

</details>

## 참고 자료

- [Princeton · Binary Search Trees](https://algs4.cs.princeton.edu/32bst/) — 순서 불변식과 삭제의 세 가지 경우를 확인한다.
