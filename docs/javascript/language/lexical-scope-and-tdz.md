# 렉시컬 스코프와 TDZ

> 이름을 찾는 범위는 코드가 선언된 위치로 결정되며 let·const는 초기화 전 접근을 허용하지 않는다.

- let·const는 블록 범위, var는 주로 함수 범위다.
- 함수는 선언 위치의 바깥 범위를 참조한다.
- TDZ에서는 undefined 대신 ReferenceError가 발생한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

중첩 함수가 변수를 읽으면 자신의 범위부터 선언 당시의 바깥 범위로 올라가 이름을 찾는다. 호출자가 같은 이름의 변수를 가지고 있어도 그것이 자동으로 선택되지는 않는다. let·const는 블록 시작부터 이름의 범위가 존재하지만 선언·초기화에 도달하기 전에는 사용할 수 없는 TDZ가 있다.

변수가 가려지는 것과 값이 복사되는 것은 다른 문제다. 콜백이 나중에 실행될 때 어떤 바인딩을 보유하는지는 클로저 문서에서 이어서 확인한다.

## JavaScript 예제

```javascript
const name = "선언 환경";
function read() { return name; }
function caller() {
  const name = "호출 환경";
  return read();
}
console.log(caller()); // 선언 환경
try {
  console.log(value);
  let value = 1;
} catch (error) {
  console.log(error.name); // ReferenceError
}
```

## 주의점

let을 단순히 “호이스팅이 안 된다”로 외우면 TDZ를 설명하기 어렵다.

## 꼬리질문

1. 선언 환경의 name과 호출 환경의 name이 다를 때 함수는 어느 값을 읽을까?
2. 블록 안에서 let 선언 전에 이름을 읽으면 바깥 값 대신 오류가 날 수 있는 이유는 무엇일까?
3. 반복문의 let과 var로 만든 콜백이 서로 다른 값을 보유할 수 있는 이유는 무엇일까?

함께 복습: [클로저의 상태 보존](../closures/captured-environment.md)

</details>

## 참고 자료

- [MDN · let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) — 블록 스코프·이름 가리기·TDZ 예제를 확인한다.
- [MDN · 클로저](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures) — 렉시컬 환경이 함수에 남는 원리를 읽는다.
