# 배열과 행렬의 메모리 표현

> 인덱스를 주소 계산으로 바꾸어 원소에 접근한다.

- 고정 크기 배열 인덱싱은 O(1).
- 중간 삽입·삭제는 이동 비용이 든다.
- 행 우선 1차원 표현은 r×cols+c를 쓴다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

같은 크기의 원소를 연속 배치하면 시작점과 인덱스로 위치를 계산할 수 있다. 행렬도 한 배열에 펼쳐 좌표를 인덱스로 바꿀 수 있다. Java int[][]는 행 배열에 대한 참조 배열이므로 행 길이가 달라도 된다. 평탄한 int[]와 동일한 메모리 배치라고 가정하지 않는다.

## Java 예제

```java
static int at(int[] flat, int columns, int row, int column) {
    return flat[row * columns + column];
}

static void demo() {
    int[] flat = {1, 2, 3, 4, 5, 6};
    int[][] jagged = {{1}, {2, 3}};
    System.out.println(at(flat, 3, 1, 2)); // 6
    System.out.println(jagged[0].length != jagged[1].length); // true
}
```

## 주의점

행·열 경계와 r×cols의 정수 오버플로를 점검한다. 물리 배치가 좋다고 모든 실제 성능이 자동 개선되는 것은 아니다.

## 꼬리질문

1. int[][]에서 각 행의 길이가 다를 수 있는 이유는 무엇일까?
2. 행 우선 평탄화에서 다음 행의 시작 인덱스는 어떻게 계산할까?
3. Java의 int[][]가 하나의 연속 2차원 저장 공간이라는 가정은 왜 위험할까?

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
