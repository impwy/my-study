# Red–Black Tree와 B-tree

> 높이를 제한하는 균형 규칙과 한 노드의 키 수로 검색 트리의 접근 비용을 관리한다.

- Red–Black Tree는 색 규칙을 가진 BST다.
- B-tree는 여러 키·자식을 한 노드에 둔다.
- B+tree와 B-tree의 저장 방식은 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Red–Black Tree는 색과 경로의 black-height 등 불변식을 회전·재색칠로 유지해 높이를 O(log n)으로 제한한다. B-tree는 다중 키·자식으로 분기 수를 높이고 노드 분할·병합 등으로 균형을 유지한다. 디스크 페이지 접근에서는 높은 분기 수가 트리 높이를 줄이는 데 도움이 된다. B+tree는 데이터 위치와 리프 연결의 특징을 별도로 가진다.

## Java 예제

TreeMap은 B-tree가 아니다. 마지막 계산은 B-tree 분기 수 비교용 모형이다.

```java
import java.util.*;

static void demo() {
    NavigableMap<Integer, String> tree = new TreeMap<>(); // Java 구현은 red-black tree
    tree.put(20, "B");
    tree.put(10, "A");
    tree.put(30, "C");
    System.out.println(tree.subMap(10, true, 30, false)); // {10=A, 20=B}
    int keysPerNode = 127;
    System.out.println(keysPerNode + 1); // B-tree 노드의 최대 자식 수 모형: 128
}
```

## 주의점

AVL·Red–Black·B-tree는 모두 균형 검색에 쓰이지만 동일한 회전·저장 규칙으로 설명하지 않는다. 자료구조 이름만으로 제품의 모든 구현을 단정하지 않는다.

## 꼬리질문

1. 디스크 인덱스에서 한 노드에 많은 키를 두면 어떤 I/O 비용을 줄일 수 있는가?
2. TreeMap의 정렬 조회와 HashMap의 조회 계약은 어떤 점이 다를까?
3. B-tree의 높은 분기 수는 메모리 비교 횟수와 디스크 접근 횟수에 각각 어떤 영향을 줄까?

</details>

## 참고 자료

- [Princeton · Balanced Search Trees](https://algs4.cs.princeton.edu/33balanced/) — 높이 제한과 회전으로 균형을 유지하는 원리를 비교한다.
- [MySQL 8.4 · Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html) — 인덱스 선택·복합 키·쓰기 비용의 관계를 확인한다.
