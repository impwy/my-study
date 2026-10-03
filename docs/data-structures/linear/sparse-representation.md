# 희소 행렬과 희소 다항식

> 대부분이 0인 데이터에서 실제 값이 있는 항만 저장한다.

- 행렬은 행·열·값의 튜플로 표현할 수 있다.
- 다항식은 지수·계수의 쌍을 저장한다.
- 메모리 절감과 조회 비용을 교환한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

모든 좌표나 모든 차수의 계수를 저장하면 빈 값이 대부분인 데이터에서 낭비가 크다. 존재하는 값만 저장하면 공간은 값의 개수에 비례한다. 대신 임의 위치를 찾을 때 인덱스나 탐색이 필요하다. 같은 좌표의 중복과 0으로 사라진 항을 어떻게 정리할지도 정의한다.

## Java 예제

```java
import java.util.Map;

record Cell(int row, int column) {}

static int valueAt(Map<Cell, Integer> sparse, int row, int column) {
    return sparse.getOrDefault(new Cell(row, column), 0);
} // Map.of(new Cell(2,5), 9): (2,5)=9, 나머지 좌표=0
```

## 주의점

희소 표현은 작은 밀집 행렬보다 느리거나 더 복잡할 수 있다. 좌표·포인터를 저장하는 부가 비용도 계산한다.

## 꼬리질문

1. 값이 빽빽한 데이터에서 희소 표현의 장점이 사라지는 이유는?
2. 0을 저장하지 않는 표현에서 실제 값 0의 갱신은 어떤 삭제 연산으로 바꿀 수 있을까?
3. 객체·해시 엔트리 비용까지 포함하면 어떤 밀도에서 배열이 더 경제적일까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
