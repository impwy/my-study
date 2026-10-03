# Composable과 생명주기 정리

> 상태와 생명주기 작업을 함수로 묶어 재사용하고 컴포넌트 종료 때 외부 자원을 정리한다.

- composable은 상태를 가진 재사용 로직을 담는다.
- 호출마다 독립 상태인지 공유 상태인지 결정한다.
- 타이머·이벤트 구독은 종료 시 해제한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Composition API는 관련 상태·계산·생명주기 처리를 같은 함수에 모을 수 있다. useTicks처럼 ref와 타이머를 묶은 함수를 setup에서 호출하면 컴포넌트의 수명과 정리가 연결된다. 함수 안에서 ref를 만들면 호출마다 별도 상태가 생기며 모듈 최상위에 만들면 공유 범위가 달라진다. 생명주기 훅 등록은 컴포넌트의 활성 setup 실행과 연결되어야 한다.

## Java 예제

자원의 시작·종료 책임을 비교하는 Java 코드다.

```java
static AutoCloseable ticker() {
    var pool = java.util.concurrent.Executors.newSingleThreadScheduledExecutor();
    var ticks = new java.util.concurrent.atomic.AtomicInteger();
    pool.scheduleAtFixedRate(
            ticks::incrementAndGet, 0, 1, java.util.concurrent.TimeUnit.SECONDS);
    return pool::shutdownNow;
} // 소유자가 close를 호출해 타이머 자원을 정리
```

### Vue 3로 확인

```javascript
// useTicks.js: 컴포넌트의 <script setup>에서 호출
import { ref, onMounted, onUnmounted } from 'vue'
export function useTicks() {
  const ticks = ref(0)
  let timer
  onMounted(() => { timer = setInterval(() => ticks.value++, 1000) })
  onUnmounted(() => clearInterval(timer))
  return { ticks }
}
```

## 주의점

composable 호출을 임의의 지연 콜백으로 옮기면 생명주기 연결이 끊길 수 있다. SSR에서는 window·타이머 같은 브라우저 작업을 서버 실행 경로와 구별하고 mounted 이후 시작하도록 설계한다.

## 꼬리질문

1. useTicks 안에서 ref를 만들면 두 컴포넌트의 카운터는 어떻게 나뉠까?
2. 컴포넌트가 사라졌는데 타이머를 해제하지 않으면 어떤 작업이 남을까?
3. 모듈 전역 상태를 SSR 요청들이 공유하면 어떤 사용자 간 상태 혼합이 가능할까?

</details>

## 참고 자료

- [Vue · Composables](https://vuejs.org/guide/reusability/composables) — 상태 재사용·훅 등록·자원 정리 조건을 확인한다.
- [Vue · Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle.html) — mounted·unmounted와 훅 등록 시점을 확인한다.
