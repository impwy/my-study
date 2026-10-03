# 수식 트리

> 피연산자를 잎에, 연산자를 내부 노드에 두어 수식 구조를 표현한다.

- 구조가 우선순위를 표현한다.
- 후위 순회로 계산할 수 있다.
- 중위 출력에는 괄호가 필요할 수 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

수식의 문자열 순서보다 어떤 부분이 먼저 결합하는지가 중요하다. 내부 노드는 두 서브트리를 먼저 계산한 뒤 연산을 적용한다. 후위식으로 만들 때 피연산자 노드를 스택에 넣고, 연산자에서 오른쪽·왼쪽 노드를 꺼내 새 트리로 묶는다. 그 트리를 다시 스택에 넣는다.

## Java 예제

```java
sealed interface Expr permits Num, Sub {}

record Num(int value) implements Expr {}

record Sub(Expr left, Expr right) implements Expr {}

static int eval(Expr e) {
    if (e instanceof Num n) return n.value();
    Sub s = (Sub) e;
    return eval(s.left()) - eval(s.right());
} // eval(new Sub(new Num(8), new Num(3))) == 5
```

## 주의점

괄호 없이 중위 출력하면 원래 결합 순서가 사라질 수 있다. 단항 연산자와 함수는 자식 개수에 맞는 추가 규칙이 필요하다.

## 꼬리질문

1. 후위식에서 먼저 꺼낸 노드가 오른쪽 자식인 이유는?
2. 뺄셈 트리에서 왼쪽·오른쪽 자식을 바꾸면 결과가 어떻게 달라질까?
3. 후위식 8 3 -를 읽을 때 두 번 pop한 순서로 자식을 붙이면 어떤 오류가 생길까?

</details>

## 참고 자료

- [Princeton · Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) — 추상 자료형과 배열·연결 구현의 차이를 확인한다.
