# React

[전체 목록](../../README.md)

## 렌더링

| 문서 | 한 줄 요약 |
| --- | --- |
| [React의 렌더와 커밋](rendering/render-and-commit.md) | 렌더는 현재 props·state로 다음 UI를 계산하고 커밋은 필요한 DOM 변경을 적용한다. |

## props·state

| 문서 | 한 줄 요약 |
| --- | --- |
| [React state 스냅샷과 updater](state/snapshot-and-updaters.md) | 한 렌더의 state 값은 고정된 스냅샷이며 이전 상태 기반 변경은 updater 함수로 이어 붙인다. |

## Hooks

| 문서 | 한 줄 요약 |
| --- | --- |
| [useEffect와 cleanup](hooks/effects-and-cleanup.md) | Effect는 커밋된 화면을 외부 시스템과 동기화하고 의존성 변경·종료 때 이전 작업을 정리한다. |

## 상태 관리·라우팅

| 문서 | 한 줄 요약 |
| --- | --- |
| [React Router와 URL 상태](routing/routes-and-url-state.md) | 라우터는 URL을 화면에 연결하고 파라미터·쿼리·중첩 경로를 탐색 가능한 상태로 다룬다. |
| [공유 상태와 reducer](routing/shared-state-and-reducer.md) | 여러 화면 조각이 같은 값을 필요로 하면 공통 소유자로 상태를 올리고 변경 규칙을 reducer로 모은다. |

## 테스트

| 문서 | 한 줄 요약 |
| --- | --- |
| [MSW 핸들러와 테스트 자원의 격리](testing/msw-handler-and-fixture-isolation.md) | MSW 핸들러 초기화와 앱 자원 정리를 구분하고 테스트가 만든 DOM·쿼리·스토어·모킹 데이터를 각 수명에 맞게 종료한다. |
| [Query 취소와 네트워크 요청의 수명](testing/query-cancellation-and-lifecycle.md) | TanStack Query의 취소 신호를 실제 요청까지 전달해야 쿼리 취소와 네트워크 중단을 연결할 수 있다. |
| [비동기 UI 테스트의 완료 조건](testing/async-ui-completion.md) | 요청이 핸들러에 도착한 시점과 사용자 흐름의 완료를 구분하고, 이번 동작으로 바뀐 화면을 확인한 뒤 테스트를 끝낸다. |
| [전역 스토어·타이머의 테스트 격리](testing/global-store-and-timer-isolation.md) | 컴포넌트를 제거해도 모듈 전역 스토어와 타이머는 남을 수 있으므로 각 자원의 초기 상태와 종료 방법을 함께 관리한다. |
| [테스트 순서 의존과 seed 재현](testing/test-order-and-reproducibility.md) | 순서를 바꿀 때 깨지는 테스트는 seed로 재현을 고정하고 선행 테스트와 공유 상태를 좁혀 원인을 찾는다. |

