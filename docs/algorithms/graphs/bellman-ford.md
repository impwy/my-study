# 벨만–포드

> 모든 간선을 반복 완화해 음수 간선이 있는 최단 경로를 구한다.

- 기본 구현 시간 O(VE).
- V−1회 뒤 추가 완화로 음수 사이클을 확인한다.
- 단일 시작점은 도달 가능한 사이클만 탐지한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

음수 사이클이 없는 최단 단순 경로에는 최대 V−1개의 간선이 있다. 매 회차 모든 간선을 완화하면 그보다 긴 후보 경로까지 점차 반영한다. V−1회 이후에도 개선되면 반복해서 비용을 낮출 수 있는 사이클이 있다는 증거다. 무한대 거리의 정점에서 완화하지 않는다.

## Java 예제

경로 합이 long 범위 안인 입력을 가정한다.

```java
import java.util.*;

record Edge(int from, int to, int weight) {}

static long[] shortest(int n, List<Edge> edges, int start) {
    long[] d = new long[n];
    Arrays.fill(d, Long.MAX_VALUE);
    d[start] = 0;
    for (int pass = 0; pass < n; pass++) {
        boolean changed = false;
        for (Edge e : edges)
            if (d[e.from()] != Long.MAX_VALUE && d[e.from()] + e.weight() < d[e.to()]) {
                d[e.to()] = d[e.from()] + e.weight();
                changed = true;
                if (pass == n - 1)
                    throw new IllegalArgumentException("reachable negative cycle");
            }
        if (!changed) break;
    }
    return d;
}
```

## 주의점

환율 예제의 수학 모델을 실제 무위험 수익 보장으로 해석하지 않는다. 도달 불가능한 사이클 탐지는 별도 시작점 설정이 필요하다.

## 꼬리질문

1. 왜 V−1회 뒤의 개선이 음수 사이클의 단서가 될까?
2. 도달할 수 없는 정점의 거리에서 간선 비용을 더하지 않는 이유는 무엇일까?
3. 시작점에서 도달할 수 없는 음수 사이클도 이 코드가 찾아낼까?

</details>

## 참고 자료

- [Princeton · Shortest Paths](https://algs4.cs.princeton.edu/44sp/) — 가중치 조건에 따른 최단 경로 알고리즘을 비교한다.
