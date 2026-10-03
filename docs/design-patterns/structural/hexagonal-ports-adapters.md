# 포트·어댑터와 의존 방향

> 핵심 업무와 외부 기술의 접점을 계약으로 나누어 실행·테스트 환경을 바꿀 수 있게 한다.

- 포트는 필요한 상호작용의 계약이다.
- 어댑터는 외부 기술과 계약을 연결한다.
- 의존 방향과 런타임 호출 방향을 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

웹 Controller는 업무를 호출하는 입력 어댑터가 될 수 있고 JPA 저장소·외부 API 클라이언트는 출력 어댑터가 될 수 있다. 핵심이 필요로 하는 저장·결제 계약을 정의하고 외부 구현을 연결한다. 런타임에서 업무가 저장소를 호출해도 코드 의존은 핵심 계약 쪽을 향하도록 설계할 수 있다. 계층 이름보다 실제 import와 생성·호출을 본다.

## Java 예제

```java
interface OrdersPort {
    String find(long id);
} // 애플리케이션이 정의한 포트

record FindOrder(OrdersPort orders) {
    String execute(long id) {
        return orders.find(id);
    }
}

record MemoryAdapter(java.util.Map<Long, String> data) implements OrdersPort {
    public String find(long id) {
        return data.get(id);
    }
}
```

## 주의점

Hexagonal Architecture는 GoF 패턴 목록의 한 항목으로 분류되는 것은 아니다. 작은 CRUD에는 분리 비용이 이익보다 클 수 있다.

## 꼬리질문

1. 런타임 호출은 바깥으로 향해도 소스 의존은 안쪽으로 향할 수 있는 이유는?
2. 어댑터가 안쪽 포트를 구현하면 소스 의존 방향은 어떤 쪽을 향할까?
3. DB 어댑터를 HTTP 어댑터로 바꿀 때 애플리케이션이 외부 예외 타입을 알고 있다면 어떤 경계가 새고 있을까?

</details>

## 참고 자료

- [Alistair Cockburn · Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — 포트·어댑터로 외부 기술을 분리하는 원래 의도를 읽는다.
