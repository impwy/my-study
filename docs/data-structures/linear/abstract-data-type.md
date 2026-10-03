# 추상 자료형

> 데이터의 사용 규칙과 연산을 구현 방식에서 분리한다.

- ADT는 연산의 계약이다.
- 같은 ADT를 배열·연결 구조로 구현할 수 있다.
- 계약과 연산 비용을 함께 본다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

스택은 “마지막에 넣은 값을 먼저 꺼낸다”라는 규칙과 push·pop 연산으로 정의할 수 있다. 배열과 연결 리스트는 그 규칙을 구현하는 서로 다른 방법이다. 사용자는 내부 포인터보다 제공된 계약에 의존한다. 구현을 바꾸더라도 동작은 유지되어야 하지만 메모리·성능 특성은 달라질 수 있다.

## Java 예제

```java
import java.util.*;

interface IntStack {
    void push(int value);

    int pop();
}

static class ArrayStack implements IntStack {
    private final Deque<Integer> values = new ArrayDeque<>();

    public void push(int value) {
        values.push(value);
    }

    public int pop() {
        return values.pop();
    }
}

static int last() {
    IntStack s = new ArrayStack();
    s.push(1);
    s.push(2);
    return s.pop();
}
```

## 주의점

이름이 같은 API라고 동시성·null·예외 계약까지 같지는 않다. 구현을 감춘다는 이유로 비용까지 무시하지 않는다.

## 꼬리질문

1. 스택이 배열인지 연결 리스트인지 모른 채 사용할 수 있는 이유는?
2. ArrayStack을 연결 리스트 구현으로 바꿀 때 사용 코드가 유지되려면 어떤 계약이 같아야 할까?
3. 빈 스택의 pop 처리도 ADT 계약에 포함해야 하는 이유는 무엇일까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
