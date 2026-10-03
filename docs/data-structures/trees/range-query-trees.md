# 구간 트리와 Fenwick Tree

> 값 갱신과 구간 질의를 함께 처리하려고 부분 구간의 정보를 트리에 저장한다.

- 정적 합은 누적합부터 고려한다.
- Segment Tree는 합·최솟값 등 집계를 지원한다.
- Fenwick Tree는 누적 합 갱신에 간결하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

값이 자주 바뀌는데 매번 누적합을 다시 만들면 갱신 비용이 커진다. Segment Tree는 구간을 나누고 각 노드에 집계값을 저장해 한 점 갱신·구간 질의를 O(log n)으로 처리할 수 있다. Fenwick Tree는 인덱스 비트를 이용해 누적 합의 일부를 묶고 갱신·prefix 질의를 O(log n)에 수행한다. 집계의 결합 규칙과 단위값을 명확히 한다.

## 예제

판매량을 자주 수정하면서 날짜 범위 합을 묻는 경우 갱신 가능한 트리를 검토한다. 고정 데이터의 합만 묻는다면 누적합이 더 단순하다.

## 주의점

최솟값을 일반적인 합 Fenwick Tree처럼 빼서 구간 결과로 만들 수는 없다. 인덱스 0·1 기반과 빈 구간 규칙을 통일한다.

## 복습 질문

누적합은 질의가 O(1)인데도 값 변경이 많으면 트리를 선택하는 이유는?

자료 구분: **기존 자료** — 자료구조 노트와 대학 강의의 표현·연산. **공식 자료 보완** — 비용의 전제·균형 조건·표준 API.

</details>

## 참고 자료

- [Peter Fenwick · Cumulative Frequency Tables](https://doi.org/10.1002/spe.4380240306) — 누적 빈도 트리의 원래 설계와 비용을 확인한다.
- [Princeton · SegmentTree source](https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/SegmentTree.java.html) — 구간 분할·조회·갱신의 실제 구현을 확인한다.
- [홍정모 연구소](https://honglab.co.kr/) — 기존 학습 노트의 원 강의 출처. 강의의 설명과 실습 맥락을 더 확인한다.
