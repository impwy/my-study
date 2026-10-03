# 스택

> 마지막에 넣은 값을 먼저 꺼내는 LIFO 자료형이다.

- push·pop·peek의 역할을 구분한다.
- 재귀 호출·DFS·괄호 검사에 연결된다.
- 빈 스택 접근 규칙을 정한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

아직 처리하지 않은 일을 마지막부터 다시 다뤄야 할 때 적합하다. 함수 호출은 돌아갈 지점을 스택에 쌓는 모델로 이해할 수 있다. 후위 수식 계산에서는 피연산자를 쌓고 연산자가 나오면 두 값을 꺼내 계산한다. 배열 기반과 연결 기반 구현 모두 같은 순서 규칙을 지켜야 한다.

## Java 예제

```java
import java.util.*;

static boolean balanced(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if (c == '(') stack.push(c);
        else if (c == ')' && (stack.isEmpty() || stack.pop() != '(')) return false;
    }
    return stack.isEmpty();
} // "(()())" → true, "())" → false
```

## 주의점

비가환 연산에서 꺼낸 두 값의 순서를 뒤집지 않는다. Java에서는 일반 스택 용도로 ArrayDeque의 메서드 계약을 확인한다.

## 꼬리질문

1. 함수 호출의 반환 순서가 LIFO와 닮은 이유는?
2. 닫는 괄호를 만났을 때 가장 최근 여는 괄호를 확인하는 이유는 무엇일까?
3. 중간 과정은 맞지만 마지막 스택이 비어 있지 않다면 어떤 입력 오류일까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
