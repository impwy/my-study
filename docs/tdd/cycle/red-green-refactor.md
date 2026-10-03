# Red–Green–Refactor

> 실패하는 작은 테스트로 요구를 드러내고 최소 구현 뒤 설계를 개선한다.

- Red에서 올바른 이유로 실패하는지 확인한다.
- Green은 테스트를 통과하는 구현이다.
- Refactor는 행동을 유지하며 구조를 바꾼다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

다음에 필요한 작은 행동을 테스트로 표현한다. 실패가 컴파일·설정 문제인지 요구한 행동의 부재인지 확인한다. 최소 구현으로 통과시킨 뒤 중복·이름·책임을 개선하고 테스트를 다시 실행한다. 리팩터링과 기능 추가를 한 번에 섞으면 실패 원인을 찾기 어려워진다. 이 반복은 충분한 테스트 설계와 요구 이해를 대신하는 자동 보증이 아니다.

## Java 예제

JUnit Jupiter가 필요하다. 현재 코드는 Green 상태의 예제다.

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

static int add(int a, int b) {
    return a + b;
}

@Test
void addsTwoNumbers() {
    assertEquals(5, add(2, 3));
}
// Red: 먼저 add 미구현을 드러내는 테스트 확인
// Green: 최소 구현 / Refactor: 테스트를 유지하며 구조 정리
```

## 주의점

테스트가 이미 구현한 코드를 그대로 재현하면 결함을 함께 복제할 수 있다. 하나의 지나치게 큰 테스트로 시작하지 않는다.

## 꼬리질문

1. Red 단계에서 테스트가 의도한 이유로 실패하는지 확인해야 하는 이유는?
2. 테스트를 구현 뒤에만 실행하면 Red에서 확인하려던 실패 원인을 어떻게 놓칠까?
3. 리팩터링 중 새 동작을 추가하면 Green 상태를 유지하는 작은 단계와 어떻게 구분할까?

함께 복습: [행동과 경계값 테스트](../design/behavior-and-boundaries.md) · [테스트 대역의 목적](../doubles/test-doubles.md)

</details>

## 참고 자료

- [Martin Fowler · Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) — 테스트·구현·리팩터링을 짧은 반복으로 연결하는 이유를 읽는다.
- [JUnit · User Guide](https://docs.junit.org/current/user-guide/) — 단위 테스트·픽스처·실행 구조를 확인한다.
