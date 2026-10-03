# 공유 상태와 reducer

> 여러 화면 조각이 같은 값을 필요로 하면 공통 소유자로 상태를 올리고 변경 규칙을 reducer로 모은다.

- 공유 상태의 단일 소유자를 정한다.
- reducer는 현재 상태·action에서 다음 상태를 계산한다.
- context는 전달 경로를 줄이며 상태 저장 자체와는 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

형제 컴포넌트가 같은 선택 값을 보여야 하면 각각 복사본을 만들기보다 가장 가까운 공통 부모에 상태를 둔다. 변경이 여러 규칙으로 나뉘면 reducer가 action별 다음 상태를 계산하고 자식은 의도를 전달한다. context는 먼 자식으로 값을 전달하는 도구이며 모든 상태를 전역으로 둘 이유는 아니다. 서버에서 온 데이터의 캐시·재조회 정책은 UI 상태의 소유권과 별도로 판단한다.

## React 예제

```jsx
import { useReducer } from 'react';
function reducer(state, action) {
  if (action.type === 'increment') return { count: state.count + 1 };
  if (action.type === 'reset') return { count: 0 };
  throw new Error('unknown action');
}
export default function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return <button onClick={() => dispatch({ type: 'increment' })}>{state.count}</button>;
}
```

## 주의점

reducer 안에서 요청을 보내거나 입력 상태를 직접 변경하지 않는다. 서로 다른 위치의 state를 억지로 동기화하는 Effect를 늘리기 전에 단일 소유자를 검토한다. context 값 변경은 이를 읽는 컴포넌트 갱신에 영향을 준다.

## 꼬리질문

1. 형제 컴포넌트가 각각 count를 가지고 동기화할 때 어떤 불일치가 생길까?
2. reducer에 현재 상태와 action만 주면 변경 결과를 테스트하기 쉬운 이유는 무엇일까?
3. 모든 입력을 최상위 context에 넣으면 어떤 수명·재렌더 비용이 늘 수 있을까?

</details>

## 참고 자료

- [React · Sharing State](https://react.dev/learn/sharing-state-between-components) — 상태를 공통 부모로 올리는 기준을 확인한다.
- [React · Extracting State Logic](https://react.dev/learn/extracting-state-logic-into-a-reducer) — 순수 reducer·action·dispatch의 역할을 확인한다.
- [React · Passing Data with Context](https://react.dev/learn/passing-data-deeply-with-context) — 전달 경로와 상태 소유권을 구별한다.
