# SOLID와 변경 이유

> 설계 원칙은 변경과 대체의 비용을 줄이는 판단 기준이며 규칙 이름보다 실제 의존 관계를 본다.

- 책임은 함께 바뀌는 이유로 구분한다.
- 대체는 상위 계약을 유지해야 한다.
- 추상화는 필요한 경계를 보호한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

SRP는 하나의 변경 이유, OCP는 확장 시 기존 핵심 변경을 줄이는 구조, LSP는 하위 타입의 대체 가능성, ISP는 사용하지 않는 계약 의존을 줄이기, DIP는 핵심 정책이 구체 기술에 매이지 않게 하기와 관련된다. 모든 클래스를 인터페이스로 감싸거나 아주 작은 파일로 쪼개는 것이 목표는 아니다. 실제 변경 시나리오와 테스트 가능성으로 설계를 평가한다.

## Java 예제

```java
interface PaymentGateway {
    void pay(int amount);
}

record Checkout(PaymentGateway gateway) {
    void complete(int amount) {
        gateway.pay(amount);
    }
}

static void demo() {
    Checkout checkout = new Checkout(amount -> System.out.println("paid=" + amount));
    checkout.complete(100);
}
```

## 주의점

추상화 수를 늘리면 이해 비용도 증가한다. 구체적인 변경 이유와 보호하려는 계약 없이 패턴을 추가하지 않는다.

## 꼬리질문

1. 인터페이스가 존재해도 핵심이 기술 세부에 의존할 수 있는 구조는?
2. Checkout이 구체 결제 SDK 대신 PaymentGateway에 의존하면 어떤 변경 이유를 분리할까?
3. 인터페이스에 사용하지 않는 결제·배송·알림 메서드를 모두 넣으면 어떤 원칙의 이점이 줄어들까?

</details>

## 참고 자료

- [Alistair Cockburn · Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — 포트·어댑터로 외부 기술을 분리하는 원래 의도를 읽는다.
- [Eric Evans · DDD Reference](https://www.domainlanguage.com/ddd/reference/) — 엔티티·값 객체·애그리거트·컨텍스트의 원래 정의를 확인한다.
