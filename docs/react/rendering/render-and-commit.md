# React의 렌더와 커밋

> 렌더는 현재 props·state로 다음 UI를 계산하고 커밋은 필요한 DOM 변경을 적용한다.

- 컴포넌트 호출과 DOM 변경은 다른 단계다.
- 렌더 계산은 같은 입력에 같은 결과를 내도록 작성한다.
- 목록의 key는 항목 정체성과 상태 보존에 영향을 준다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

React 함수 컴포넌트는 props와 state를 받아 JSX 표현을 계산한다. 렌더가 일어났다고 DOM 전체를 새로 만드는 것은 아니며 커밋에서 필요한 변경을 적용한다. 렌더 도중 외부 상태를 수정하면 다시 계산하거나 중단된 렌더에서도 효과가 남을 수 있다. 같은 데이터라도 항목 key가 달라지면 기존 컴포넌트의 상태가 유지되지 않을 수 있다.

## React 예제

React 실습 앱에서 Greeting을 렌더한다.

```jsx
export default function Greeting({ name = 'Kim' }) {
  return <h1>안녕, {name}</h1>;
}
```

## 주의점

렌더 중 API 호출·저장·타이머 등록을 하지 않는다. 개발 Strict Mode에서 추가 호출이 보이는 것은 순수성·정리 문제를 찾기 위한 검사일 수 있다.

## 꼬리질문

1. 컴포넌트가 다시 호출되었는데 DOM 내용이 같다면 무엇이 계산되고 무엇이 생략될 수 있을까?
2. 렌더 중 외부 배열에 push하면 반복 렌더에서 결과가 어떻게 달라질까?
3. 목록의 인덱스를 key로 쓰고 앞 항목을 삭제하면 입력 상태가 왜 다른 항목에 붙을 수 있을까?

</details>

## 참고 자료

- [React · Render and Commit](https://react.dev/learn/render-and-commit) — 호출·계산·DOM 반영 단계를 구별한다.
- [React · Keeping Components Pure](https://react.dev/learn/keeping-components-pure) — 렌더 중 부수 효과를 피하는 이유를 확인한다.
- [React · Rendering Lists](https://react.dev/learn/rendering-lists) — 안정적인 key와 항목 정체성을 확인한다.
