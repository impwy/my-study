# Promise와 async·await

> Promise는 나중의 완료 결과를 표현하고 await는 해당 함수의 후속 실행을 완료 뒤로 이어 준다.

- pending에서 fulfilled 또는 rejected로 확정된다.
- async 함수는 Promise를 반환한다.
- 실패 처리와 여러 작업의 실행 순서를 명시한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

await는 모든 JavaScript 실행을 멈추는 명령이 아니다. 현재 async 함수의 후속 부분을 기다리는 결과와 연결한다. 독립 작업은 먼저 시작하고 Promise.all로 합치면 결과를 함께 기다릴 수 있다. 반면 앞 결과가 필요한 작업은 순서대로 이어야 한다. 반환값을 then 체인에서 빼먹거나 Promise를 반환하지 않으면 바깥 흐름이 실제 작업보다 먼저 완료될 수 있다.

## Java 예제

완료 결과를 이어 붙이는 Java 비교 예제다.

```java
static java.util.concurrent.CompletableFuture<Integer> result() {
    return java.util.concurrent.CompletableFuture.completedFuture(5)
            .thenApply(value -> value * 2)
            .exceptionally(error -> -1);
} // result().join() == 10
```

### JavaScript로 확인

```javascript
async function total() {
  const first = Promise.resolve(5);
  const second = Promise.resolve(7);
  const [a, b] = await Promise.all([first, second]);
  return a + b;
}
total().then(value => console.log(value)); // 12
```

## 주의점

Java CompletableFuture의 실행 스레드와 JavaScript Promise의 마이크로태스크 규칙은 다르다. Promise.all이 거절되어도 다른 작업이 자동 취소되지는 않는다. 실제 fetch는 HTTP 오류 상태도 별도로 확인한다.

## 꼬리질문

1. await를 만나면 멈추는 것은 전체 실행 환경일까, 해당 async 함수의 후속 흐름일까?
2. 독립된 두 요청을 await로 순차 호출할 때와 먼저 시작한 뒤 Promise.all로 기다릴 때 지연은 어떻게 다를까?
3. 한 요청이 실패했을 때 나머지 요청까지 멈추려면 어떤 취소 계약이 추가로 필요할까?

</details>

## 참고 자료

- [MDN · Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) — 상태·체인·Promise.all의 완료와 실패 계약을 확인한다.
- [MDN · await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) — 함수의 실행 재개와 예외 처리 규칙을 확인한다.
