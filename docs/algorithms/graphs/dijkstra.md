# 다익스트라

> 음수가 아닌 가중치에서 가장 가까운 미확정 정점을 차례로 확정한다.

- 모든 간선 가중치가 0 이상이어야 한다.
- relaxation으로 더 짧은 경로를 반영한다.
- 우선순위 큐 구현은 오래된 항목을 건너뛴다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

시작점 거리만 0으로 두고 나머지는 무한대로 초기화한다. 가장 짧은 후보를 꺼내 그 정점의 간선을 완화한다. 음수 간선이 없으므로 아직 보지 않은 경로를 더 붙여 이미 확정한 거리를 줄일 수 없다는 논리를 사용한다. prev를 저장하면 경로를 복원할 수 있다.

## Java 예제

모든 간선 비용은 비음수이고 경로 합은 long 범위 안이라고 가정한다.

```java
import java.util.*;

record Edge(int to, int weight) {}

record State(int v, long cost) {}

static long[] shortest(List<List<Edge>> g, int start) {
    long[] d = new long[g.size()];
    Arrays.fill(d, Long.MAX_VALUE);
    d[start] = 0;
    var q = new PriorityQueue<State>(Comparator.comparingLong(State::cost));
    q.add(new State(start, 0));
    while (!q.isEmpty()) {
        State s = q.remove();
        if (s.cost() != d[s.v()]) continue;
        for (Edge e : g.get(s.v()))
            if (s.cost() + e.weight() < d[e.to()]) {
                d[e.to()] = s.cost() + e.weight();
                q.add(new State(e.to(), d[e.to()]));
            }
    }
    return d;
}
```

## 주의점

음수 간선이 있으면 확정 논리가 깨진다. INF에 가중치를 더해 정수 오버플로가 생기지 않도록 도달 여부와 자료형을 확인한다.

## 꼬리질문

1. 간선 비용이 음수면 “지금 가장 가까운 정점 확정”이 왜 위험할까?
2. 같은 정점의 오래된 State를 큐에서 꺼냈을 때 건너뛰는 이유는 무엇일까?
3. 음수 사이클이 있으면 이 구현의 개선 반복은 어떻게 잘못될 수 있을까?

</details>

## 참고 자료

- [Princeton · Shortest Paths](https://algs4.cs.princeton.edu/44sp/) — 가중치 조건에 따른 최단 경로 알고리즘을 비교한다.
