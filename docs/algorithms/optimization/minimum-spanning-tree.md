# 최소 신장 트리

> 연결된 무방향 그래프의 모든 정점을 최소 총비용으로 연결한다.

- 연결 그래프의 트리는 V−1개 간선을 갖는다.
- Kruskal은 작은 간선부터 사이클을 피한다.
- Prim은 현재 트리 밖으로 나가는 작은 간선을 고른다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

최단 경로는 시작점에서의 이동 비용을 최소화하지만 MST는 모든 정점을 연결하는 간선 비용의 합을 최소화한다. Kruskal은 Union-Find로 이미 연결된 두 정점의 간선을 제외한다. Prim은 현재 집합과 바깥을 잇는 후보를 관리한다. 비연결 그래프에서는 신장 숲이 된다.

## Java 예제

정점이 하나 이상인 무방향 그래프의 Kruskal 예제다.

```java
import java.util.*;

record Edge(int u, int v, int weight) {}

static int root(int[] p, int v) {
    return p[v] == v ? v : (p[v] = root(p, p[v]));
}

static long cost(int n, List<Edge> input) {
    int[] p = new int[n];
    for (int i = 0; i < n; i++) p[i] = i;
    var edges = new ArrayList<>(input);
    edges.sort(Comparator.comparingInt(Edge::weight));
    long cost = 0;
    int used = 0;
    for (Edge e : edges) {
        int a = root(p, e.u()), b = root(p, e.v());
        if (a != b) {
            p[a] = b;
            cost += e.weight();
            used++;
        }
    }
    if (used != n - 1) throw new IllegalArgumentException("disconnected");
    return cost;
}
```

## 주의점

MST 위의 두 점 경로가 원래 그래프의 최단 경로라는 보장은 없다. 음수 간선은 MST 자체의 금지 조건이 아니다.

## 꼬리질문

1. MST와 최단 경로 트리의 최소화 대상은 어떻게 다를까?
2. 두 끝점의 대표가 같으면 그 간선은 왜 사이클을 만들까?
3. 음수 간선은 MST에도 문제가 될까, 아니면 최단 경로 문제와 조건이 다를까?

</details>

## 참고 자료

- [Princeton · Minimum Spanning Trees](https://algs4.cs.princeton.edu/43mst/) — 컷 성질과 Prim·Kruskal의 선택 기준을 확인한다.
