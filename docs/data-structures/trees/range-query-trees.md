# 구간 트리와 Fenwick Tree

> 값 갱신과 구간 질의를 함께 처리하려고 부분 구간의 정보를 트리에 저장한다.

- 정적 합은 누적합부터 고려한다.
- Segment Tree는 합·최솟값 등 집계를 지원한다.
- Fenwick Tree는 누적 합 갱신에 간결하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

값이 자주 바뀌는데 매번 누적합을 다시 만들면 갱신 비용이 커진다. Segment Tree는 구간을 나누고 각 노드에 집계값을 저장해 한 점 갱신·구간 질의를 O(log n)으로 처리할 수 있다. Fenwick Tree는 인덱스 비트를 이용해 누적 합의 일부를 묶고 갱신·prefix 질의를 O(log n)에 수행한다. 집계의 결합 규칙과 단위값을 명확히 한다.

## Java 예제

유효한 범위 인덱스를 전달한다고 가정한 Fenwick tree다.

```java
static class Fenwick {
    final long[] tree;

    Fenwick(int size) {
        tree = new long[size + 1];
    }

    void add(int index, long delta) { // 0-based 외부 인덱스
        for (int i = index + 1; i < tree.length; i += i & -i) tree[i] += delta;
    }

    long prefix(int end) { // [0,end)
        long sum = 0;
        for (int i = end; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    long range(int left, int right) {
        return prefix(right) - prefix(left);
    }
}
```

## 주의점

최솟값을 일반적인 합 Fenwick Tree처럼 빼서 구간 결과로 만들 수는 없다. 인덱스 0·1 기반과 빈 구간 규칙을 통일한다.

## 꼬리질문

1. 누적합은 질의가 O(1)인데도 값 변경이 많으면 트리를 선택하는 이유는?
2. i & -i가 나타내는 구간 길이는 i=12에서 얼마일까?
3. 구간 합 대신 구간 최솟값을 구하려면 같은 뺄셈 방식이 가능한지 설명할 수 있을까?

</details>

## 참고 자료

- [Peter Fenwick · Cumulative Frequency Tables](https://doi.org/10.1002/spe.4380240306) — 누적 빈도 트리의 원래 설계와 비용을 확인한다.
- [Princeton · SegmentTree source](https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/SegmentTree.java.html) — 구간 분할·조회·갱신의 실제 구현을 확인한다.
