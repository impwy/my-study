# B+ 트리 인덱스

> 많은 키를 한 노드에 담아 디스크 접근 깊이를 줄이고 범위 탐색을 연결한다.

- 균형된 다진 탐색 구조다.
- 리프 연결이 범위 조회를 돕는다.
- 삽입·삭제 때 분할·병합 비용이 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

메모리의 이진 탐색 트리와 달리 DB 페이지에 여러 키를 담으면 적은 페이지 접근으로 큰 데이터를 찾을 수 있다. 내부 노드는 갈 방향을 고르고 리프에서 실제 키를 찾는다. 인덱스는 읽기를 빠르게 하지만 모든 변경에서 유지 비용과 추가 공간을 요구한다.

## Java 예제

정렬된 키의 범위 조회를 보여 준다. TreeMap은 B+ tree가 아니며 리프 페이지 연결을 구현하지 않는다.

```java
import java.util.*;

static void rangeModel() {
    NavigableMap<Integer, String> ordered = new TreeMap<>();
    ordered.put(10, "A");
    ordered.put(20, "B");
    ordered.put(30, "C");
    System.out.println(ordered.subMap(10, true, 30, false)); // 10·20 조회
}
```

## 주의점

인덱스를 쓴다는 사실만으로 최적 계획이라고 결론 내리지 않는다. 많은 행을 읽어야 하면 전체 스캔이 더 나을 수 있다.

## 꼬리질문

1. DB 인덱스가 이진 트리보다 분기 수를 크게 잡는 이유는?
2. 시작 키를 찾은 뒤 리프를 순서대로 읽는 방식은 범위 조회에서 어떤 장점이 있을까?
3. 리프에 키만 있고 실제 행은 다른 페이지에 있다면 어떤 추가 I/O가 생길까?

</details>

## 참고 자료

- [MySQL 8.4 · Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html) — 인덱스 선택·복합 키·쓰기 비용의 관계를 확인한다.
