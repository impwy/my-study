# React Router와 URL 상태

> 라우터는 URL을 화면에 연결하고 파라미터·쿼리·중첩 경로를 탐색 가능한 상태로 다룬다.

- React와 React Router의 책임은 다르다.
- 동적 세그먼트와 query의 역할을 나눈다.
- 직접 URL 열기와 새로고침도 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

React 자체는 라우팅 라이브러리가 아니다. React Router의 declarative 모드에서는 BrowserRouter 안에 Routes와 Route를 구성하고 useParams로 동적 세그먼트를 읽는다. 선택된 주문 ID는 URL에 두면 링크 공유·새로고침으로 복원할 수 있다. 중첩 라우트의 자식은 부모 Outlet에 표시한다. 검색 필터·페이지 번호처럼 공유할 상태는 쿼리 문자열을 검토한다.

## Java 예제

```java
record Page(String resource, String id) {}

static Page parse(String path) {
    var match = java.util.regex.Pattern.compile("^/orders/([0-9]+)$").matcher(path);
    if (!match.matches()) throw new IllegalArgumentException("not found");
    return new Page("orders", match.group(1));
}
```

### React·React Router로 확인

react-router를 설치한 React 실습 앱에서 App을 렌더한다.

```jsx
import { BrowserRouter, Routes, Route, useParams } from 'react-router';
function OrderPage() {
  const { id } = useParams();
  return <h1>주문 {id}</h1>;
}
export default function App() {
  return <BrowserRouter><Routes>
    <Route path="/orders/:id" element={<OrderPage />} />
    <Route path="*" element={<p>찾을 수 없습니다.</p>} />
  </Routes></BrowserRouter>;
}
```

## 주의점

Java 예제는 URL 파싱 모형이다. 아래는 React Router 7 계열의 declarative API를 사용하며 다른 모드의 loader 계약과 구별한다. 클라이언트 경로·가드는 API 인가가 아니고 history 방식은 서버 fallback 설정도 필요하다.

## 꼬리질문

1. URL의 주문 ID와 메모리 state의 주문 ID를 따로 관리하면 어떤 불일치가 생길까?
2. /orders/42를 주소창에서 직접 열 때 서버는 어떤 응답을 제공해야 할까?
3. 브라우저 뒤로 가기로 필터를 복원하려면 query와 임시 UI 상태 중 어디에 두어야 할까?

</details>

## 참고 자료

- [React Router · Routing](https://reactrouter.com/start/declarative/routing) — 동적 세그먼트·중첩 경로·Outlet의 실제 구성을 확인한다.
- [React Router · Installation](https://reactrouter.com/start/declarative/installation) — declarative 모드의 설치·BrowserRouter 연결을 따라 한다.
