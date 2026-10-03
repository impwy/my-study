# 깊이 우선 탐색

> 한 경로를 끝까지 내려갔다가 돌아와 다음 후보를 탐색한다.

- 재귀 또는 명시적 스택을 사용한다.
- visited로 반복 방문을 막는다.
- 인접 리스트 전체 순회 O(V+E).

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

방문한 정점에서 아직 방문하지 않은 이웃으로 계속 이동한다. 경로가 막히면 이전 정점으로 돌아온다. 미로·연결 요소·사이클 탐지 같은 문제에 상태를 더해 활용한다. 방문 순서는 이웃의 나열 순서에도 의존한다. 재귀 구현의 호출 깊이는 최악 V까지 커질 수 있다.

## Java 예제

```java
import java.util.List;

static void dfs(List<List<Integer>> g, int v, boolean[] seen) {
    seen[v] = true;
    System.out.println(v);
    for (int next : g.get(v)) if (!seen[next]) dfs(g, next, seen);
}
```

## 주의점

방향 그래프 사이클은 visited만으로 부족할 수 있어 현재 경로에 있는지 확인한다. 반복 스택의 push 순서가 재귀 순서와 다를 수 있다.

## 꼬리질문

1. 무방향 그래프에서 부모로 되돌아가는 간선을 사이클로 오인하지 않으려면?
2. seen 표시를 재귀 호출 뒤에 하면 사이클에서 어떤 일이 생길까?
3. 정점이 일렬로 10만 개 연결되어 있으면 재귀 대신 어떤 자료구조를 사용할까?

</details>

## 참고 자료

- [Princeton · Undirected Graphs](https://algs4.cs.princeton.edu/41graph/) — 인접 리스트와 DFS·BFS의 불변식을 확인한다.
