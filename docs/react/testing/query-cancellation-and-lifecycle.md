# Query 취소와 네트워크 요청의 수명

> TanStack Query의 취소 신호를 실제 요청까지 전달해야 쿼리 취소와 네트워크 중단을 연결할 수 있다.

- **연결:** `queryFn`의 `signal`을 API 래퍼와 `fetch`까지 전달한다.
- **구분:** Query 상태의 취소·캐시 제거·실제 요청 중단은 같은 보장이 아니다.
- **한계:** 클라이언트 취소는 서버가 이미 실행한 변경을 되돌리지 않는다.

<details>
<summary>설명과 TypeScript 예제·꼬리질문 펼치기</summary>

## 설명

화면이 사라져도 응답을 캐시에 남기려는 동작이 유용할 수 있다. TanStack Query v5에서 마지막 구독자가 제거됐다고 모든 요청이 무조건 중단되는 것은 아니다. `AbortSignal`을 소비하는지와 사용하는 API가 취소에 대응하는지가 중요하다.

취소 신호는 연결된 요청에만 작용한다. `queryFn`이 `signal`을 받아도 API 래퍼가 버리면 실제 `fetch`는 계속될 수 있다. 이 요청이나 후속 작업이 테스트 경계를 넘으면 다른 테스트의 MSW 핸들러·기록과 섞일 수 있다.

## TypeScript 예제

TanStack Query v5와 `fetch`를 사용하는 클라이언트 코드다. API 래퍼가 신호를 전달하고 HTTP 오류를 별도로 처리한다.

```ts
import { queryOptions } from '@tanstack/react-query';

type PurchasedItem = { id: number; title: string };

async function getJson<T>(path: string, signal: AbortSignal): Promise<T> {
  const response = await fetch(path, { signal });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json() as Promise<T>;
}

export const purchasedQuery = queryOptions({
  queryKey: ['purchased'],
  queryFn: ({ signal }) =>
    getJson<PurchasedItem[]>('/api/purchased', signal),
});
```

테스트가 소유한 QueryClient를 종료하는 단계에서는 먼저 React 트리를 언마운트해 재요청을 만드는 구독을 제거하고, 추적 중인 조회를 취소한 뒤 캐시를 비울 수 있다.

```ts
cleanup();
await queryClient.cancelQueries();
queryClient.clear();
```

## 주의점

**`clear()`는 캐시만 지우고 취소를 전혀 하지 않는다고 단정하면 부정확하다.** v5 구현에서 쿼리를 제거하는 과정은 Query의 취소도 호출한다. 그러나 신호를 전달하지 않은 HTTP 요청이나 Query 밖의 타이머·콜백까지 종료하는 보장은 아니다. 명시적 `cancelQueries()`도 신호 전달이 빠진 네트워크 요청을 마법처럼 멈추지 못한다.

이미 MSW나 실제 서버가 받은 요청은 취소 뒤에도 처리 효과를 남길 수 있다. mutation의 서버 변경, 앱이 따로 만든 요청, 폴링·소켓은 각각 수명과 정리 방법을 설계한다. 취소를 넣는 것과 [사용자 흐름의 완료를 기다리는 것](async-ui-completion.md)은 서로 보완한다.

## 꼬리질문

1. `queryFn`에서 받은 `signal`이 API 래퍼에서 사라지면 화면 종료 시 실제 요청에는 어떤 차이가 생기는가?
2. `cancelQueries()` 뒤에도 서버 요청 기록이 늘었다면 요청의 어느 시점과 어떤 후속 작업을 확인해야 할까?
3. 이미 결제가 처리된 뒤 클라이언트가 요청을 취소했다면 중복 결제를 막기 위해 어떤 별도 계약이 필요한가?

</details>

## 참고 자료

- [TanStack Query · Query Cancellation](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation) — 기본 언마운트 동작과 `AbortSignal` 연결 방법을 확인한다.
- [TanStack Query · QueryClient](https://tanstack.com/query/latest/docs/reference/QueryClient) — `cancelQueries`와 `clear`의 API 계약을 비교한다.
- [TanStack Query · Query 구현](https://github.com/TanStack/query/blob/main/packages/query-core/src/query.ts) — 쿼리 제거 시 `destroy()`가 내부 취소를 호출하는 경로를 확인한다.
