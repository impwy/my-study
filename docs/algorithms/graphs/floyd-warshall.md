# 플로이드–워셜

> 허용하는 중간 정점을 늘려 모든 정점 쌍의 최단거리를 계산한다.

- dist[i][j]는 i에서 j로 가는 비용이다.
- k를 바깥 반복으로 둔다.
- 시간 O(V³), 공간 O(V²).

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

중간 정점 k를 새롭게 허용할 때 기존 경로와 i→k→j 경로를 비교한다. dist[i][k]+dist[k][j]가 더 작으면 값을 갱신한다. 초기 대각선은 0이며 여러 직접 간선 중 최솟값을 넣는다. 음수 사이클을 거치는 경로는 유한한 최단 비용으로 해석할 수 없다.

## Java 예제

inf는 도달 불가 표식이며 유한한 경로 비용의 합은 long 범위 안이라고 가정한다.

```java
static void shortest(long[][] d, long inf) {
    for (int k = 0; k < d.length; k++)
        for (int i = 0; i < d.length; i++)
            for (int j = 0; j < d.length; j++)
                if (d[i][k] != inf && d[k][j] != inf)
                    d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
} // 초기화: d[i][i]=0, 직접 간선 비용, 나머지는 inf
```

## 주의점

직접 간선과 이미 계산한 경로를 혼동하지 않는다. predecessor를 복원할 때 k가 항상 j의 직전 정점인 것은 아니다.

## 꼬리질문

1. 벨만–포드의 간선 완화와 이 알고리즘의 “중간 정점 허용”은 무엇이 다를까?
2. k 반복문을 가장 바깥에 두어야 유지되는 상태의 의미는 무엇일까?
3. 계산 뒤 d[i][i]가 음수라면 어떤 경로 조건을 확인해야 할까?

</details>

## 참고 자료

- [Princeton · Shortest Paths](https://algs4.cs.princeton.edu/44sp/) — 가중치 조건에 따른 최단 경로 알고리즘을 비교한다.
