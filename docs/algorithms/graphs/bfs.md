# 너비 우선 탐색

> 시작점과 가까운 정점부터 큐로 탐색한다.

- 큐에서 발견 순서대로 처리한다.
- 가중치 없는 그래프의 최소 간선 수를 구한다.
- 큐에 넣을 때 방문 표시한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

현재 거리의 정점들을 처리한 뒤 그 다음 거리의 정점을 처리한다. 처음 발견한 경로가 최소 간선 수인 이유는 더 짧은 거리의 후보가 이미 먼저 처리되었기 때문이다. prev를 저장하면 도착점에서 시작점까지 거꾸로 경로를 복원할 수 있다. 인접 리스트에서는 O(V+E)로 순회한다.

## Java 예제

```java
import java.util.*;

static int[] distances(List<List<Integer>> g, int start) {
    int[] d = new int[g.size()];
    Arrays.fill(d, -1);
    Queue<Integer> q = new ArrayDeque<>();
    d[start] = 0;
    q.add(start);
    while (!q.isEmpty()) {
        int v = q.remove();
        for (int next : g.get(v))
            if (d[next] == -1) {
                d[next] = d[v] + 1;
                q.add(next);
            }
    }
    return d;
}
```

## 주의점

꺼낼 때만 방문 표시하면 같은 정점이 여러 번 큐에 들어갈 수 있다. 가중치가 서로 다른 그래프에서는 BFS의 최소 간선 수가 최소 비용이 아닐 수 있다.

## 꼬리질문

1. 왜 큐에 넣는 순간 visited를 표시하는 편이 안전할까?
2. 처음 발견한 정점의 d가 최단 거리가 되는 것은 어떤 간선 비용 전제 때문일까?
3. 간선 비용이 1과 10으로 다르면 같은 FIFO 큐로 구한 값이 왜 틀릴 수 있을까?

</details>

## 참고 자료

- [Princeton · Undirected Graphs](https://algs4.cs.princeton.edu/41graph/) — 인접 리스트와 DFS·BFS의 불변식을 확인한다.
