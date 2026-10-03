# 제어 흐름과 배열

> 조건·반복으로 실행 경로를 정하고 배열의 길이와 인덱스 경계를 지킨다.

- 배열 인덱스는 0부터 length-1이다.
- 반복문의 초기값·조건·증감을 함께 본다.
- 2차원 배열은 배열 참조의 배열이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

조건문은 boolean 표현식에 따라 분기하고 반복문은 시작 상태·종료 조건·상태 갱신으로 구성된다. Java 배열은 생성 후 길이가 고정되며 기본형 원소는 기본값으로 초기화된다. int[][]는 각 행이 별도 배열이므로 행 길이가 다를 수 있다. 값을 읽기 전에 null과 길이 조건을 확인하고 경계 검사를 불필요하게 서로 다른 규칙으로 섞지 않는다.

## Java 예제

```java
static void demo() {
    int[][] source = {{1, 2}, {3, 4}};
    int[][] shallow = source.clone();
    shallow[0][0] = 9;
    int[][] deep = java.util.Arrays.stream(source).map(int[]::clone).toArray(int[][]::new);
    deep[0][0] = 7;
    System.out.println(source[0][0]); // 9: 얕은 복사는 행을 공유
}
```

## 주의점

배열 변수 복사는 원소 전체의 복사가 아니다. 다차원 배열의 얕은 복사는 내부 행 배열을 공유할 수 있다.

## 꼬리질문

1. int[][]를 복사했는데 한 행 변경이 양쪽에 보이면 어떤 참조가 공유된 것인가?
2. source.clone()이 복사한 것은 정수 값일까, 행 배열의 참조일까?
3. 배열 원소가 가변 객체라면 각 행까지 복사해도 어떤 공유가 남을까?

</details>

## 참고 자료

- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
