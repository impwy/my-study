# React state 스냅샷과 updater

> 한 렌더의 state 값은 고정된 스냅샷이며 이전 상태 기반 변경은 updater 함수로 이어 붙인다.

- setter는 현재 지역 변수의 즉시 대입이 아니다.
- props는 부모가 전달하고 state는 소유 컴포넌트가 변경한다.
- 이전 상태가 필요하면 setState(prev => next)를 쓴다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

이벤트 핸들러는 자신이 만들어진 렌더의 count를 읽는다. count가 0인 핸들러에서 setCount(count+1)을 여러 번 호출하면 같은 1을 여러 번 요청할 수 있다. updater는 큐의 이전 결과를 받아 다음 상태를 계산하므로 세 번 증가를 순서대로 표현할 수 있다. 객체·배열 state도 직접 바꾸기보다 새 값을 만들어 다음 렌더의 입력으로 전달한다.

## React 예제

```jsx
import { useState } from 'react';
export default function Counter() {
  const [count, setCount] = useState(0);
  function addThree() {
    setCount(n => n + 1);
    setCount(n => n + 1);
    setCount(n => n + 1);
  }
  return <button onClick={addThree}>{count}</button>;
}
```

## 주의점

updater에 외부 API 호출 등 부수 효과를 넣지 않는다. 비동기 콜백은 이전 렌더의 값을 계속 참조할 수 있다.

## 꼬리질문

1. count가 0인 핸들러에서 setCount(count+1)을 세 번 하면 왜 보통 1이 될까?
2. updater 세 개는 이전 updater의 결과를 어떤 순서로 받아 3을 만들까?
3. state 객체를 직접 수정한 뒤 같은 참조를 넘기면 화면 갱신·이전 스냅샷에서 어떤 문제가 생길까?

</details>

## 참고 자료

- [React · State as a Snapshot](https://react.dev/learn/state-as-a-snapshot) — 렌더별 값과 이벤트 핸들러의 캡처를 확인한다.
- [React · Queueing State Updates](https://react.dev/learn/queueing-a-series-of-state-updates) — 배칭·updater 큐·순수 함수 조건을 확인한다.
- [React · 설치 없이 실습하기](https://react.dev/learn/installation) — 공식 샌드박스의 App.js를 예제로 바꾸어 실행한다.
