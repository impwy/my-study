# Red–Black Tree와 B-tree

> 높이를 제한하는 균형 규칙과 한 노드의 키 수로 검색 트리의 접근 비용을 관리한다.

- Red–Black Tree는 색 규칙을 가진 BST다.
- B-tree는 여러 키·자식을 한 노드에 둔다.
- B+tree와 B-tree의 저장 방식은 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Red–Black Tree는 색과 경로의 black-height 등 불변식을 회전·재색칠로 유지해 높이를 O(log n)으로 제한한다. B-tree는 다중 키·자식으로 분기 수를 높이고 노드 분할·병합 등으로 균형을 유지한다. 디스크 페이지 접근에서는 높은 분기 수가 트리 높이를 줄이는 데 도움이 된다. B+tree는 데이터 위치와 리프 연결의 특징을 별도로 가진다.

## 예제

메모리의 정렬 Map과 DB 페이지 인덱스는 필요한 연산·저장 단위가 달라 서로 다른 구조를 선택할 수 있다.

## 주의점

AVL·Red–Black·B-tree는 모두 균형 검색에 쓰이지만 동일한 회전·저장 규칙으로 설명하지 않는다. 자료구조 이름만으로 제품의 모든 구현을 단정하지 않는다.

## 복습 질문

디스크 인덱스에서 한 노드에 많은 키를 두면 어떤 I/O 비용을 줄일 수 있는가?

자료 구분: **기존 자료** — 자료구조 노트와 대학 강의의 표현·연산. **공식 자료 보완** — 비용의 전제·균형 조건·표준 API.

</details>

## 참고 자료

- [Princeton · Balanced Search Trees](https://algs4.cs.princeton.edu/33balanced/) — 높이 제한과 회전으로 균형을 유지하는 원리를 비교한다.
- [MySQL 8.4 · Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html) — 인덱스 선택·복합 키·쓰기 비용의 관계를 확인한다.
- [홍정모 연구소](https://honglab.co.kr/) — 기존 학습 노트의 원 강의 출처. 강의의 설명과 실습 맥락을 더 확인한다.
