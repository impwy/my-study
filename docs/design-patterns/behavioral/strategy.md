# Strategy

> 서로 바꿀 수 있는 행동을 같은 계약의 여러 구현으로 분리한다.

- 호출자는 공통 계약을 사용한다.
- 전략 선택과 전략 실행을 나눈다.
- 변경하는 축이 있을 때 도입한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

여러 할인·검증·결제 알고리즘이 같은 목적을 달성하지만 구현이 다르면 계약을 만들고 각 전략으로 분리할 수 있다. 호출자는 조건 분기 전체를 알고 있지 않아도 주입된 전략을 실행한다. 선택은 조립·팩토리·레지스트리 등의 별도 책임으로 둘 수 있다. 타입이 한 개이고 변경 가능성이 낮다면 단순 메서드가 더 명확할 수 있다.

## Java 예제

작은 비음수 가격의 전략 예제다. 실제 금액 계산에는 범위·반올림 규칙이 필요하다.

```java
interface Discount {
    int apply(int price);
}

record Checkout(Discount discount) {
    int total(int price) {
        return discount.apply(price);
    }
}

static void demo() {
    Discount tenPercent = price -> price * 90 / 100;
    System.out.println(new Checkout(tenPercent).total(1000)); // 900
}
```

## 주의점

전략마다 서로 다른 의미를 같은 이름으로 억지로 묶지 않는다. 선택 분기가 다른 곳으로 옮겨 갔다는 이유만으로 변경 비용이 사라진 것은 아니다.

## 꼬리질문

1. 전략 객체가 생기면 기존 조건 분기 중 어떤 책임은 여전히 남는가?
2. 할인 전략을 교체할 수 있어도 어떤 고객에게 어떤 전략을 적용할지는 어디에서 결정할까?
3. 정수 비율 계산에 반올림·오버플로·중복 할인 정책이 추가되면 전략 계약을 어떻게 명시할까?

</details>

## 참고 자료

- [Head First Design Patterns · Strategy example](https://github.com/bethrobson/Head-First-Design-Patterns/tree/master/src/headfirst/designpatterns/strategy) — 교재 저자의 코드로 교체 가능한 행동 구조를 확인한다.
