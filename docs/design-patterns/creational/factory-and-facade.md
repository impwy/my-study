# Factory와 Facade

> 생성 결정을 모으는 Factory와 여러 협력의 사용 절차를 단순화하는 Facade를 구분한다.

- Factory는 생성 책임을 다룬다.
- Facade는 사용 인터페이스를 다룬다.
- 큰 조정 객체가 모든 업무를 소유하지 않게 한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

생성 방식·타입 선택이 복잡하면 팩토리에 모아 호출자가 구체 생성 절차를 덜 알게 한다. Facade는 여러 하위 시스템을 사용하는 순서를 외부에서 간단하게 호출하도록 제공한다. Facade에서 모든 도메인 규칙까지 수행하면 서비스가 비대해질 수 있으므로 조정과 규칙의 책임을 구분한다. 단순 팩토리·Factory Method·Abstract Factory는 같은 이름으로 뭉뚱그리지 않는다.

## Java 예제

```java
interface Sender {
    void send(String text);
}

static Sender senderFactory(String channel) {
    if (!channel.equals("console")) throw new IllegalArgumentException();
    return System.out::println;
}

record RegistrationFacade(Sender sender) {
    void register(String name) {
        sender.send("등록 완료: " + name);
    }
}
```

## 주의점

이 문서는 두 역할의 비교다. GoF 생성 패턴 각각의 자세한 구조를 공부한 것으로 확장하지 않는다.

## 꼬리질문

1. 객체 선택을 담당하는 코드와 업무 호출 순서를 담당하는 코드의 변경 이유는 어떻게 다른가?
2. factory가 선택하는 객체와 facade가 제공하는 업무 호출은 어떤 변경 이유가 다를까?
3. facade에 모든 업무를 모으면 단순한 진입점이 어떤 과도한 책임으로 바뀔 수 있을까?

</details>

## 참고 자료

- [Head First · Factory examples](https://github.com/bethrobson/Head-First-Design-Patterns/tree/master/src/headfirst/designpatterns/factory) — 교재 예제에서 생성 책임을 비교한다.
- [Head First · Facade example](https://github.com/bethrobson/Head-First-Design-Patterns/tree/master/src/headfirst/designpatterns/facade) — 단순 인터페이스가 협력 객체를 조정하는 구조를 본다.
