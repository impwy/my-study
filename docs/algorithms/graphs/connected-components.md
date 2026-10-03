# 연결 요소와 강한 연결 요소

> 그래프를 서로 연결된 정점 묶음으로 나눈다.

- 무방향 연결과 방향의 양방향 도달은 다르다.
- 각 탐색에서 같은 component ID를 준다.
- SCC는 서로 왕복 도달할 수 있는 묶음이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

무방향 그래프에서 아직 방문하지 않은 정점마다 DFS·BFS를 시작하면 연결 요소가 나뉜다. 방향 그래프에서 한 번 도달한다는 사실만으로 같은 SCC가 되지는 않는다. Kosaraju는 역방향 그래프의 종료 순서를 이용해 원래 그래프의 묶음을 찾는다.

## Java 예제

```java
import java.util.List;

static int count(List<List<Integer>> g) { // 무방향 그래프
    boolean[] seen = new boolean[g.size()];
    int count = 0;
    for (int v = 0; v < g.size(); v++)
        if (!seen[v]) {
            visit(g, v, seen);
            count++;
        }
    return count;
}

static void visit(List<List<Integer>> g, int v, boolean[] seen) {
    seen[v] = true;
    for (int next : g.get(v)) if (!seen[next]) visit(g, next, seen);
}
```

## 주의점

방향 그래프를 무방향처럼 처리하면 의존 관계나 도달 가능성의 의미가 달라진다.

## 꼬리질문

1. A에서 B로 갈 수 있는데 B에서 A로 못 가면 같은 SCC일까?
2. 간선 없는 정점 하나도 연결 요소로 세어야 하는 이유는 무엇일까?
3. 방향 그래프의 SCC를 찾으려면 한 방향 방문 가능성에 어떤 조건을 더해야 할까?

</details>

## 참고 자료

- [Princeton · Directed Graphs](https://algs4.cs.princeton.edu/42digraph/) — 위상 순서·사이클·강한 연결 요소를 비교한다.
