# Vue Router의 경로와 파라미터

> URL을 화면 상태와 연결하고 같은 화면의 파라미터 변경도 새로운 탐색으로 처리한다.

- 동적 세그먼트는 route.params에 들어간다.
- RouterLink·RouterView가 탐색과 화면 표시를 나눈다.
- 같은 컴포넌트를 재사용하면 mounted만으로 변경을 잡지 못한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

orders/:id는 여러 주문 URL을 하나의 화면 정의로 연결한다. RouterLink는 탐색 링크, RouterView는 일치한 컴포넌트 표시를 맡는다. 같은 경로 패턴에서 id만 바뀌면 컴포넌트가 재사용될 수 있으므로 파라미터 변화에 따라 조회를 다시 수행한다. URL에는 공유·새로고침에 필요한 화면 식별 상태를 두고 임시 입력·모달 상태와 구별한다.

## Java 예제

경로에서 파라미터를 추출하는 비교 예제다. Vue Router의 탐색·히스토리를 구현하지 않는다.

```java
static String orderId(String path) {
    var match = java.util.regex.Pattern.compile("^/orders/([0-9]+)$").matcher(path);
    if (!match.matches()) throw new IllegalArgumentException("not found");
    return match.group(1);
} // /orders/42 → 42
```

### Vue 3로 확인

```javascript
// router.js: 앱 초기화에서 app.use(router), 루트에 <RouterView /> 필요
import { createRouter, createWebHistory } from 'vue-router'
import OrderPage from './OrderPage.vue'
export const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/orders/:id', component: OrderPage }]
})
```

```vue
<!-- OrderPage.vue -->
<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>
<template>주문 {{ route.params.id }}</template>
```

## 주의점

라우트 가드는 화면 탐색 제어이며 서버의 API 인가를 대체하지 않는다. HTML history 모드에서 URL을 직접 열려면 서버의 SPA fallback도 필요하다. 빠른 ID 변경 시 이전 요청의 늦은 결과를 덮어쓰지 않게 처리한다.

## 꼬리질문

1. /orders/1에서 /orders/2로 이동해 컴포넌트를 재사용하면 어떤 생명주기 훅을 기대할 수 없을까?
2. route.params.id를 감시해야 하는 데이터 요청은 어떤 상태를 초기화해야 할까?
3. 클라이언트 가드가 있어도 서버가 주문 소유자를 따로 검증해야 하는 이유는 무엇일까?

</details>

## 참고 자료

- [Vue Router · Getting Started](https://router.vuejs.org/guide/) — 라우터 등록과 RouterLink·RouterView 연결을 따라 해 본다.
- [Vue Router · Dynamic Matching](https://router.vuejs.org/guide/essentials/dynamic-matching.html) — 파라미터 변경과 컴포넌트 재사용을 확인한다.
