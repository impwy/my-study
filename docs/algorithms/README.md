# 알고리즘

[전체 목록](../../README.md)

## 복잡도

| 문서 | 한 줄 요약 |
| --- | --- |
| [P·NP·NP-완전](complexity/np-completeness.md) | 해를 구하는 비용과 주어진 해를 검증하는 비용을 구분한다. |
| [재귀와 호출 스택](complexity/recursion.md) | 큰 문제를 더 작은 같은 문제에 맡기고 종료 조건에서 돌아온다. |
| [점근 분석](complexity/asymptotic-analysis.md) | 입력 크기가 커질 때 연산 횟수가 어떻게 증가하는지 비교한다. |
| [큰 정수 표현과 Karatsuba](complexity/big-integer-and-karatsuba.md) | 고정 크기 정수 범위를 넘는 수를 자릿수 배열로 표현하고 곱셈의 재귀 구조를 개선한다. |

## 탐색

| 문서 | 한 줄 요약 |
| --- | --- |
| [lower bound와 upper bound](search/lower-upper-bound.md) | 정렬된 데이터에서 값의 존재보다 경계 위치를 찾아 중복 구간을 계산한다. |
| [문자열 매칭](search/string-matching.md) | 패턴의 정보나 해시로 이미 한 비교를 줄이며 문자열에서 위치를 찾는다. |
| [보간 탐색](search/interpolation-search.md) | 정렬된 값의 분포로 목표가 있을 위치를 추정한다. |
| [순차 탐색](search/sequential-search.md) | 앞에서부터 값을 비교해 목표를 찾거나 모든 후보를 확인한다. |
| [이진 탐색](search/binary-search.md) | 정렬된 배열에서 중간값을 비교해, 정답이 있을 수 없는 절반을 버리는 탐색 방법. |

## 정렬

| 문서 | 한 줄 요약 |
| --- | --- |
| [계수 정렬](sorting/counting-sort.md) | 키별 개수를 세고 누적 개수로 정렬 위치를 계산한다. |
| [기수 정렬](sorting/radix-sort.md) | 각 자리의 안정 정렬을 반복해 전체 키의 순서를 만든다. |
| [버블 정렬](sorting/bubble-sort.md) | 인접한 원소를 교환해 가장 큰 값을 뒤쪽에 확정한다. |
| [병합 정렬](sorting/merge-sort.md) | 배열을 나눠 정렬한 뒤 두 정렬 구간을 비교하며 합친다. |
| [삽입 정렬](sorting/insertion-sort.md) | 현재 값을 이미 정렬된 앞 구간의 알맞은 위치에 끼운다. |
| [선택 정렬](sorting/selection-sort.md) | 남은 구간의 최솟값을 찾아 현재 자리로 옮긴다. |
| [셸 정렬](sorting/shell-sort.md) | 멀리 떨어진 원소를 먼저 정리한 뒤 간격을 줄여 삽입 정렬한다. |
| [퀵 정렬](sorting/quick-sort.md) | 피벗보다 작은 값과 큰 값을 나누고 각 구간을 정렬한다. |

## 그래프 탐색

| 문서 | 한 줄 요약 |
| --- | --- |
| [깊이 우선 탐색](graphs/dfs.md) | 한 경로를 끝까지 내려갔다가 돌아와 다음 후보를 탐색한다. |
| [너비 우선 탐색](graphs/bfs.md) | 시작점과 가까운 정점부터 큐로 탐색한다. |
| [다익스트라](graphs/dijkstra.md) | 음수가 아닌 가중치에서 가장 가까운 미확정 정점을 차례로 확정한다. |
| [벨만–포드](graphs/bellman-ford.md) | 모든 간선을 반복 완화해 음수 간선이 있는 최단 경로를 구한다. |
| [연결 요소와 강한 연결 요소](graphs/connected-components.md) | 그래프를 서로 연결된 정점 묶음으로 나눈다. |
| [위상 정렬](graphs/topological-sort.md) | 선행 조건을 모두 지키는 방향 그래프의 정점 순서를 찾는다. |
| [플로이드–워셜](graphs/floyd-warshall.md) | 허용하는 중간 정점을 늘려 모든 정점 쌍의 최단거리를 계산한다. |

## 그리디·동적 계획법

| 문서 | 한 줄 요약 |
| --- | --- |
| [그리디](optimization/greedy.md) | 지금의 최선 선택을 반복하되 전체 최적해와 연결되는 근거를 확인한다. |
| [누적합과 투 포인터](optimization/prefix-sum-and-two-pointers.md) | 반복 구간 계산을 전처리하거나 단조롭게 이동하는 두 경계로 중복 탐색을 줄인다. |
| [동적 계획법](optimization/dynamic-programming.md) | 반복되는 부분 문제의 결과를 저장해 큰 문제를 계산한다. |
| [무손실 압축](optimization/data-compression.md) | 반복·빈도·사전을 이용해 원래 데이터를 복원할 수 있는 짧은 표현을 만든다. |
| [배낭 문제](optimization/knapsack.md) | 용량과 사용 가능한 항목 상태를 정의해 최대 가치를 계산한다. |
| [백트래킹](optimization/backtracking.md) | 가능한 선택을 시도하고 돌아와 상태를 복원하며 해를 탐색한다. |
| [슬라이딩 윈도우](optimization/sliding-window.md) | 연속 구간을 옮길 때 빠지는 정보와 새로 들어오는 정보만 갱신한다. |
| [철근 자르기](optimization/rod-cutting.md) | 첫 조각 길이와 남은 길이의 최적 수익을 조합한다. |
| [최대 유량](optimization/maximum-flow.md) | 간선 용량과 정점의 흐름 보존을 지키며 시작점에서 끝점까지의 유량을 늘린다. |
| [최소 신장 트리](optimization/minimum-spanning-tree.md) | 연결된 무방향 그래프의 모든 정점을 최소 총비용으로 연결한다. |
| [최장 공통 부분 수열](optimization/lcs.md) | 순서를 유지하며 건너뛸 수 있는 두 문자열의 가장 긴 공통 수열을 찾는다. |
| [행렬 연쇄 곱셈의 DP](optimization/matrix-chain.md) | 곱셈 순서는 유지하면서 괄호 위치를 선택해 전체 스칼라 곱셈 수를 최소화한다. |

