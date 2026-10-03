# 클로저와 상태 보존

> 함수는 자신이 만들어진 렉시컬 환경을 참조해 바깥 함수가 종료된 뒤에도 상태를 사용할 수 있다.

- 클로저는 함수와 선언 환경의 결합이다.
- 팩토리 호출마다 독립된 환경을 만들 수 있다.
- 상태를 값 복사로만 이해하면 나중의 변경을 놓친다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

카운터 팩토리가 함수를 반환하면 반환된 함수는 count 바인딩에 계속 접근한다. 팩토리를 두 번 호출하면 count가 둘 생기지만 한 번의 호출에서 반환한 여러 함수는 같은 환경을 공유할 수 있다. 이벤트 핸들러와 비동기 콜백에서 이 참조가 유지되므로 불필요한 큰 객체를 오래 붙잡는 경우도 살핀다.

## Java 예제

```java
static java.util.function.IntSupplier counter() {
    int[] count = {0}; // 람다는 effectively final인 참조를 캡처
    return () -> ++count[0];
}

static void demo() {
    var a = counter();
    var b = counter();
    System.out.println(a.getAsInt()); // 1
    System.out.println(a.getAsInt()); // 2
    System.out.println(b.getAsInt()); // 1
}
```

### JavaScript로 확인

```javascript
function counter() {
  let count = 0;
  return () => ++count;
}
const a = counter();
const b = counter();
console.log(a(), a(), b()); // 1 2 1
```

## 주의점

Java 람다의 지역 변수 캡처 제약은 JavaScript와 다르다. 배열로 상태를 담은 Java 예제는 단일 스레드 비교용이며 스레드 안전성을 보장하지 않는다.

## 꼬리질문

1. counter를 두 번 호출했을 때 count가 독립적인 이유는 무엇일까?
2. 같은 count를 읽고 쓰는 두 함수를 한 번에 반환하면 상태는 어떻게 공유될까?
3. 이벤트 핸들러를 해제하지 않고 큰 객체를 캡처하면 어떤 메모리 보유가 생길까?

</details>

## 참고 자료

- [MDN · 클로저](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures) — 함수 팩토리·렉시컬 환경·반복문 캡처 문제를 확인한다.
