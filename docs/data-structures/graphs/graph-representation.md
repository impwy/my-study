# 그래프의 인접 행렬과 인접 리스트

> 정점 사이의 관계를 저장하는 방식에 따라 공간과 탐색 비용이 달라진다.

- 행렬 공간 O(V²), 연결 확인 O(1).
- 리스트 공간 O(V+E), 이웃만 순회.
- 방향·가중치·중복 간선 규칙을 정한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

행렬은 정점 쌍마다 한 칸을 두고 연결 여부나 가중치를 저장한다. 리스트는 정점마다 실제 이웃만 저장하므로 희소 그래프에 유리하다. 무방향 간선은 보통 양쪽 이웃 목록에 기록한다. 탐색의 복잡도는 알고리즘 이름뿐 아니라 이 표현을 기준으로 계산해야 한다.

## Java 예제

```java
import java.util.*;

static List<List<Integer>> graph(int n, int[][] edges) {
    List<List<Integer>> g = new ArrayList<>();
    for (int i = 0; i < n; i++) g.add(new ArrayList<>());
    for (int[] e : edges) {
        g.get(e[0]).add(e[1]);
        g.get(e[1]).add(e[0]);
    }
    return g;
} // 무방향 간선 하나는 양쪽 인접 리스트에 저장
```

## 주의점

가중치 0인 간선이 가능하면 숫자 0을 “간선 없음”으로 쓰면 안 된다. 비연결 그래프 전체 순회는 시작점을 추가해야 한다.

## 꼬리질문

1. 희소 그래프의 BFS가 행렬에서는 O(V²)이 되는 이유는?
2. 무방향 간선을 두 번 저장해도 공간이 O(V+E)인 이유는 무엇일까?
3. 두 정점 사이 간선 존재를 아주 자주 검사한다면 인접 행렬과 리스트를 어떻게 비교할까?

</details>

## 참고 자료

- [Princeton · Undirected Graphs](https://algs4.cs.princeton.edu/41graph/) — 인접 리스트와 DFS·BFS의 불변식을 확인한다.
