# 이벤트 루프와 마이크로태스크

> 현재 동기 실행이 끝난 뒤 Promise 등의 마이크로태스크를 처리하고 다음 태스크로 진행한다.

- 같은 실행 에이전트의 작업은 중간에 다른 작업이 끼어들지 않는다.
- 타이머의 시간은 실행 시각 보장이 아니다.
- 긴 동기 코드와 계속 추가되는 마이크로태스크는 응답을 지연시킨다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

브라우저에서는 이벤트·타이머가 태스크를 만들고 Promise의 후속 콜백은 마이크로태스크로 이어진다. 지금 실행 중인 동기 코드가 끝나야 다음 작업을 처리할 수 있다. 마이크로태스크 체크포인트에서는 새로 생긴 마이크로태스크까지 큐를 비우므로 setTimeout 0도 그보다 뒤에 실행될 수 있다. 네트워크 처리 자체는 브라우저 플랫폼에 맡길 수 있지만 콜백이 긴 CPU 작업을 대신 병렬 실행해 주지는 않는다.

## JavaScript 예제

```javascript
console.log("start");
setTimeout(() => console.log("timer"), 0);
Promise.resolve().then(() => console.log("promise"));
console.log("end");
// start → end → promise → timer
```

## 주의점

짧은 출력 순서 예제를 브라우저의 렌더링이나 Node.js의 모든 실행 단계에 그대로 일반화하지 않는다. 비동기 함수 안에서도 긴 동기 계산은 해당 실행 흐름을 막을 수 있다.

## 꼬리질문

1. setTimeout 0보다 뒤에 등록한 Promise 콜백이 먼저 실행되는 이유는 무엇일까?
2. Promise 콜백이 마이크로태스크를 계속 추가하면 다음 타이머는 어떻게 지연될까?
3. 무거운 계산을 Promise로 감싸는 것과 Worker에 맡기는 것은 어떤 실행 자원 차이가 있을까?

함께 복습: [Promise와 await](promise-and-await.md)

</details>

## 참고 자료

- [MDN · 실행 모델](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model) — 호출 스택·작업 큐·실행 완료 조건을 확인한다.
- [MDN · 마이크로태스크](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide) — 브라우저의 태스크와 마이크로태스크 순서를 더 읽는다.
