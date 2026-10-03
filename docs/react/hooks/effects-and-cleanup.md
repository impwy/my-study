# useEffect와 cleanup

> Effect는 커밋된 화면을 외부 시스템과 동기화하고 의존성 변경·종료 때 이전 작업을 정리한다.

- Effect는 렌더 계산 밖의 동기화를 다룬다.
- 사용한 반응형 값은 의존성에 반영한다.
- 타이머·구독·요청은 재실행과 종료를 고려한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

props의 delay로 동작하는 타이머는 delay가 달라지면 이전 타이머를 지우고 새 타이머를 시작해야 한다. useEffect의 cleanup은 다음 setup 전에, 그리고 컴포넌트 제거 때 실행된다. 화면 값을 다른 화면 값에서 계산할 수 있다면 우선 렌더 안의 파생 계산을 검토하며 불필요한 Effect state를 늘리지 않는다. useState·useEffect 같은 훅은 함수 컴포넌트나 custom hook의 최상위에서 일정한 호출 순서를 유지한다.

## React 예제

```jsx
import { useEffect, useState } from 'react';
export default function Ticks({ delay = 1000 }) {
  const [ticks, setTicks] = useState(0);
  useEffect(() => {
    const timer = setInterval(() => setTicks(n => n + 1), delay);
    return () => clearInterval(timer);
  }, [delay]);
  return <p>{ticks}</p>;
}
```

## 주의점

delay는 양수여야 한다. []로 의존성을 숨기면 값 변경에 맞는 재동기화가 누락될 수 있다. 개발 Strict Mode의 추가 setup→cleanup→setup은 정리 구현을 점검하는 흐름이며 ref로 한 번만 실행하게 막는 것을 해결책으로 삼지 않는다.

## 꼬리질문

1. delay가 바뀌었는데 이전 interval을 지우지 않으면 몇 개의 타이머가 남을 수 있을까?
2. cleanup에서 같은 timer 식별자를 사용해야 하는 이유는 무엇일까?
3. 처음 마운트 때만 실행하려고 의존성을 빼면 어떤 props·state 값이 오래된 채 남을까?

</details>

## 참고 자료

- [React · Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) — 외부 동기화·cleanup·개발 검사 흐름을 확인한다.
- [React · Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks) — useState·useEffect 등의 호출 위치 제약을 확인한다.
- [React · 설치 없이 실습하기](https://react.dev/learn/installation) — 공식 샌드박스에서 타이머 예제를 실행하고 제거 시 정리를 확인한다.
