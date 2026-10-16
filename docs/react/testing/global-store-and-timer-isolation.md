# 전역 스토어·타이머의 테스트 격리

> 컴포넌트를 제거해도 모듈 전역 스토어와 타이머는 남을 수 있으므로 각 자원의 초기 상태와 종료 방법을 함께 관리한다.

- **수명:** React 트리와 모듈 전역 상태의 수명은 다르다.
- **정리:** 상태만 비우면 예약된 콜백이 다음 테스트를 다시 바꿀 수 있다.
- **원칙:** 의도된 앱 동작을 바꾸기보다 테스트 경계에서 격리한다.

<details>
<summary>설명과 TypeScript 예제·꼬리질문 펼치기</summary>

## 설명

앱 전체가 공유하는 Zustand 스토어는 화면을 언마운트해도 유지될 수 있다. 화면 이동 뒤에도 토스트를 보여 주려는 설계라면 이 수명은 정상이다. 테스트는 별개이므로 토스트의 메시지·식별자와 자동 숨김 타이머를 함께 초기화한다.

이전 성공 메시지가 남아 있으면 다음 테스트의 `findByText`가 **새 작업의 성공 전에** 이전 메시지를 찾을 수 있다. 이후 토스트의 `key`가 바뀌어 새 DOM으로 교체되면 잡아 둔 요소가 떨어져 나간다. 이때 문제는 단언의 대기 시간이 아니라 잘못 공유된 초기 상태다. [DOM 요소를 다시 조회해야 하는 이유](async-ui-completion.md)도 함께 본다.

## TypeScript 예제

Zustand 5의 vanilla 스토어 예시다. 스토어를 사용하는 UI의 변경은 테스트에서 `act`로 감싼다.

```ts
// toast-store.ts
import { createStore } from 'zustand/vanilla';

export const toastStore = createStore<{
  id: number;
  message: string | null;
}>(() => ({ id: 0, message: null }));

let hideTimer: ReturnType<typeof setTimeout> | undefined;

export function showToast(message: string) {
  clearTimeout(hideTimer);
  toastStore.setState((state) => ({ id: state.id + 1, message }));
  hideTimer = setTimeout(() => {
    toastStore.setState({ message: null });
    hideTimer = undefined;
  }, 2600);
}

export function resetToast() {
  clearTimeout(hideTimer);
  hideTimer = undefined;
  toastStore.setState(toastStore.getInitialState(), true);
}
```

```ts
// test/setup.ts
import { act, cleanup } from '@testing-library/react';
import { afterEach } from 'vitest';
import { resetToast } from '../toast-store';

afterEach(() => {
  cleanup();
  act(() => resetToast());
});
```

## 주의점

`cleanup()`은 렌더한 React 트리를 정리한다. 모듈 변수·타이머·스토어·`localStorage`까지 일괄 복원하지 않는다. 스토어가 액션도 담는다면 일부 필드로 전체 상태를 대체하지 말고 `getInitialState()` 등으로 원래 상태와 액션을 보존한다. 중첩 객체를 직접 변이하면 초기 상태 참조까지 오염될 수 있다.

가짜 타이머를 쓰는 테스트는 예약 작업과 실제 타이머 복귀도 관리한다. 모든 타이머를 무조건 실행하면 폴링처럼 새 작업을 만드는 콜백이 이어질 수 있으므로 자원을 소유한 모듈의 취소 함수를 우선한다. 공유 스토어를 쓰는 테스트의 동시 실행은 `afterEach`만으로 안전해지지 않는다.

## 꼬리질문

1. `cleanup()` 뒤에도 이전 토스트가 다음 렌더에서 보인다면 어떤 객체가 화면보다 오래 살아 있는가?
2. 메시지만 `null`로 바꾸고 타이머를 남기면 다음 테스트의 새 토스트는 어떻게 영향을 받을까?
3. 화면 이동 시 토스트 유지가 요구사항이라면 앱의 수명을 바꾸지 않고 테스트 독립성을 어떻게 확보할까?

</details>

## 참고 자료

- [Zustand · How to reset state](https://zustand.docs.pmnd.rs/learn/guides/how-to-reset-state) — `getInitialState()`를 사용하는 초기화 패턴을 확인한다.
- [Zustand · Testing](https://zustand.docs.pmnd.rs/learn/guides/testing) — 테스트 경계에서 스토어를 복원하고 `act`로 반영하는 방법을 읽는다.
- [Testing Library · cleanup](https://testing-library.com/docs/react-testing-library/api/#cleanup) — React 트리 정리의 책임과 자동 실행 조건을 확인한다.
