# 위상 정렬

> 선행 조건을 모두 지키는 방향 그래프의 정점 순서를 찾는다.

- DAG에서만 전체 순서가 존재한다.
- 진입 차수 0을 큐로 처리할 수 있다.
- 순서는 여러 개일 수 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Kahn 방식은 아직 남아 있는 선행 간선이 없는 정점을 선택한다. 해당 정점의 간선을 제거하면서 이웃의 진입 차수를 줄인다. 모든 정점을 처리하지 못했다면 순환 의존성이 남아 있다. DFS 방식은 종료 순서를 뒤집어 얻되 사이클을 별도로 탐지한다.

## Java 예제

```java
import java.util.*;

static List<Integer> order(List<List<Integer>> g) {
    int[] degree = new int[g.size()];
    for (var nexts : g) for (int v : nexts) degree[v]++;
    Queue<Integer> q = new ArrayDeque<>();
    for (int v = 0; v < degree.length; v++) if (degree[v] == 0) q.add(v);
    List<Integer> out = new ArrayList<>();
    while (!q.isEmpty()) {
        int v = q.remove();
        out.add(v);
        for (int n : g.get(v)) if (--degree[n] == 0) q.add(n);
    }
    if (out.size() != g.size()) throw new IllegalArgumentException("cycle");
    return out;
}
```

## 주의점

일반 정렬처럼 유일한 답이 있는 것이 아니다. DFS 역후위 순서만 구하고 사이클 검사를 빼지 않는다.

## 꼬리질문

1. 처리한 정점 수가 V보다 적으면 왜 사이클을 의심할 수 있을까?
2. 진입 차수가 0인 정점이 동시에 둘이면 위상 순서는 유일할까?
3. 순환 의존성이 있는 빌드 작업을 이 코드로 검사하면 어디에서 실패할까?

</details>

## 참고 자료

- [Princeton · Directed Graphs](https://algs4.cs.princeton.edu/42digraph/) — 위상 순서·사이클·강한 연결 요소를 비교한다.
