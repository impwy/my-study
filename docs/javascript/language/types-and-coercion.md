# JavaScript 타입과 형 변환

> 변수의 값 타입은 실행 중 달라질 수 있으며 자동 형 변환과 명시적 변환을 구별해야 한다.

- 타입은 변수 선언보다 현재 값에 붙는다.
- ===는 타입 강제 변환 없이 비교한다.
- const는 재대입을 막으며 객체 전체를 불변으로 만들지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

JavaScript의 기본 값은 string·number·boolean·bigint·symbol·undefined·null로 나뉜다. 객체는 속성을 가진 참조 값이다. let 변수에는 다른 타입의 값을 다시 넣을 수 있다. +는 문자열 연결로 바뀔 수 있고 ==는 비교 전 변환을 수행할 수 있으므로 API 입력은 기대 타입을 명시적으로 검사한다.

Java의 Object 변수에 여러 객체를 넣는 예제와 비교하되, Java 변수의 정적 타입은 Object로 유지된다는 차이를 기억한다.

## Java 예제

값 표현을 비교하는 Java 코드다. JavaScript의 자동 형 변환을 구현하지 않는다.

```java
static void demo() {
    Object value = 3;
    System.out.println(value.getClass().getSimpleName()); // Integer
    value = "3";
    System.out.println(value.getClass().getSimpleName()); // String
    System.out.println(Integer.parseInt((String) value) + 2); // 명시적 변환: 5
}
```

### JavaScript로 확인

브라우저 콘솔 또는 Node.js에서 실행한다.

```javascript
console.log("3" + 2);         // "32"
console.log(Number("3") + 2); // 5
console.log(3 == "3");       // true
console.log(3 === "3");      // false
const state = { count: 0 };
state.count++;
console.log(state.count);     // 1
```

## 주의점

typeof null은 "object"이며 NaN은 number 타입이다. JSON의 큰 정수 ID가 안전한 number 범위를 넘으면 문자열 등의 계약이 필요하다. Java의 ==와 JavaScript의 ==를 같은 계약으로 읽지 않는다.

## 꼬리질문

1. "3" + 2와 Number("3") + 2의 결과가 다른 이유는 무엇일까?
2. 3 == "3"과 3 === "3"은 각각 어떤 비교를 수행할까?
3. const 객체의 속성을 변경할 수 있다면 API 상태를 불변으로 다루려면 무엇이 더 필요할까?

</details>

## 참고 자료

- [MDN · 타입과 자료구조](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures) — 기본 타입·자동 변환·안전한 정수 범위를 확인한다.
- [MDN · const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) — 바인딩 고정과 객체 가변성의 차이를 확인한다.
