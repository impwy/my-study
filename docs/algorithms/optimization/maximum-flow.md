# 최대 유량

> 간선 용량과 정점의 흐름 보존을 지키며 시작점에서 끝점까지의 유량을 늘린다.

- 용량을 초과할 수 없다.
- 중간 정점의 유입·유출 합이 같다.
- 잔여 그래프에는 되돌릴 수 있는 역방향도 둔다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

증가 경로를 찾으면 그 경로에서 가장 작은 잔여 용량만큼 유량을 늘린다. 역방향 잔여 간선은 이전 선택을 취소해 다른 경로로 재배치할 수 있게 한다. 더 이상 증가 경로가 없으면 최대 유량과 최소 컷의 연결로 최적성을 설명할 수 있다.

## Java 예제

비음수 용량과 long 범위의 합을 가정하며 입력 잔여 용량 행렬을 직접 변경한다.

```java
import java.util.*;

static long maxFlow(long[][] residual, int s, int t) {
    if (s == t) throw new IllegalArgumentException();
    long total = 0;
    int n = residual.length;
    while (true) {
        int[] p = new int[n];
        Arrays.fill(p, -1);
        p[s] = s;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(s);
        while (!q.isEmpty() && p[t] == -1) {
            int u = q.remove();
            for (int v = 0; v < n; v++)
                if (p[v] == -1 && residual[u][v] > 0) {
                    p[v] = u;
                    q.add(v);
                }
        }
        if (p[t] == -1) return total;
        long f = Long.MAX_VALUE;
        for (int v = t; v != s; v = p[v]) f = Math.min(f, residual[p[v]][v]);
        for (int v = t; v != s; v = p[v]) {
            residual[p[v]][v] -= f;
            residual[v][p[v]] += f;
        }
        total += f;
    }
}
```

## 주의점

역방향 간선 없이 앞선 배치를 고정하면 최대값을 놓칠 수 있다. Ford–Fulkerson의 비용·종료 조건은 용량 자료형과 경로 선택에 따라 다르다.

## 꼬리질문

1. 역방향 잔여 간선은 실제 흐름과 어떤 관계가 있을까?
2. 증가 경로의 최소 잔여 용량이 3이면 경로 전체에 더할 수 있는 흐름은 얼마일까?
3. 이전에 고른 경로가 최종 해를 방해할 때 역방향 용량을 어떻게 활용할까?

</details>

## 참고 자료

- [Princeton · Maximum Flow](https://algs4.cs.princeton.edu/64maxflow/) — 잔여 용량과 증가 경로를 확인한다.
