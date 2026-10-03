# Pinia와 공유 상태

> 여러 컴포넌트가 필요한 상태를 store에 모으고 상태·파생 값·변경 동작의 역할을 나눈다.

- 필요한 공유 상태만 store로 올린다.
- state·getter·action을 구별한다.
- storeToRefs로 상태의 반응성 연결을 유지한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Pinia store의 state는 현재 값, getter는 파생 값, action은 변경이나 비동기 작업을 담는다. 모든 입력을 전역 store에 넣기보다 화면 밖에서도 필요한 상태인지 먼저 판단한다. store에서 상태 값을 일반 구조 분해하면 연결이 끊길 수 있어 storeToRefs로 ref를 얻고 action은 직접 사용할 수 있다. router는 URL 상태, store는 그 외 공유 상태라는 책임을 구별한다.

## Pinia 예제

앱 초기화에서 app.use(createPinia())로 등록한 뒤 사용한다.

```javascript
// stores/cart.js
import { defineStore } from 'pinia'
export const useCartStore = defineStore('cart', {
  state: () => ({ count: 0 }),
  getters: { doubled: state => state.count * 2 },
  actions: { add() { this.count++ } }
})
```

```vue
<script setup>
import { storeToRefs } from 'pinia'
import { useCartStore } from './stores/cart.js'
const cart = useCartStore()
const { count, doubled } = storeToRefs(cart)
</script>
<template><button @click="cart.add()">{{ count }} / {{ doubled }}</button></template>
```

## 주의점

인증 토큰과 민감 데이터를 무조건 브라우저 저장소에 영속화하지 않는다. SSR은 요청마다 Pinia 인스턴스·상태를 분리해야 한다.

## 꼬리질문

1. count와 doubled를 둘 다 저장하기보다 doubled를 getter로 두는 이유는 무엇일까?
2. storeToRefs 없이 count만 구조 분해하면 어떤 변경 연결을 놓칠 수 있을까?
3. 잠깐 열린 입력창의 내용을 전역 store에 두면 어떤 불필요한 수명·초기화 문제가 생길까?

</details>

## 참고 자료

- [Pinia · Defining a Store](https://pinia.vuejs.org/core-concepts/) — store 정의·사용·storeToRefs와 action을 확인한다.
- [Pinia · Getting Started](https://pinia.vuejs.org/getting-started.html) — createPinia로 앱에 등록하는 과정을 따라 한다.
