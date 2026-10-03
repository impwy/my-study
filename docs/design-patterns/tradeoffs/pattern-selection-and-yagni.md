# 디자인 패턴의 적용 조건과 YAGNI

> 패턴은 실제로 바뀌는 지점을 분리할 때 쓰고 예상만 있는 확장성의 비용을 함께 계산한다.

- 먼저 현재 요구와 반복되는 변경 지점을 적는다.
- 추상화의 이점과 클래스·탐색·디버깅 비용을 비교한다.
- YAGNI는 현재 필요한 단순성과 유지보수성을 포기하라는 말이 아니다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

패턴 이름을 먼저 고르면 문제보다 많은 객체·인터페이스가 생길 수 있다. 배송 방법 두 개의 고정된 요금을 고르는 요구라면 enum과 switch만으로 충분할 수 있다. 배송사마다 외부 API·계산 규칙·테스트 대역이 달라지고 독립적으로 교체해야 한다면 Strategy 같은 분리가 이익을 줄 수 있다.

적용 이유를 “확장성” 한 단어로 끝내지 않고 어떤 변경이 어디에 국한되는지 적는다. 반대로 아직 쓰지 않는 확장 지점은 구현 시간뿐 아니라 읽기·수정·디버깅 비용을 만든다. 현재 코드의 이름·작은 함수·검증 가능한 경계를 정리하는 리팩터링은 미래 기능을 미리 만드는 일과 구별한다.

## Java 예제

```java
enum Shipping {
    STANDARD,
    EXPRESS
}

static int fee(Shipping shipping) {
    return switch (shipping) {
        case STANDARD -> 3000;
        case EXPRESS -> 5000;
    };
}

static void demo() {
    System.out.println(fee(Shipping.STANDARD)); // 현재의 작은 요구
}
```

## 주의점

예제 요금은 임의의 값이다. 작은 switch가 항상 옳거나 Strategy가 항상 과하다는 결론은 아니다. 실제 변경 빈도·외부 의존·테스트 난이도가 달라지면 선택을 다시 평가한다.

## 꼬리질문

1. 배송 방법이 두 개라는 이유만으로 Strategy가 필요한지 판단하려면 어떤 추가 정보가 필요할까?
2. 각 배송사마다 다른 API와 실패 정책이 생기면 기존 switch의 책임은 어떻게 커질까?
3. 아직 없는 기능을 위한 추상화와 현재 코드의 유지보수 리팩터링은 어떻게 구별할까?

</details>

## 참고 자료

- [Martin Fowler · YAGNI](https://martinfowler.com/bliki/Yagni.html) — 예상 기능의 구현·지연·유지 비용과 리팩터링의 차이를 읽는다.
