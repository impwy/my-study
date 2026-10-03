# Vue의 ref와 computed

> 반응형 상태를 읽은 계산과 화면을 추적해 상태 변경 시 필요한 결과를 갱신한다.

- ref는 JavaScript에서 .value로 접근한다.
- computed는 반응형 의존성에서 파생한 값을 표현한다.
- 상태 변경과 DOM 반영 시점은 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Vue 3의 ref는 값 접근을 추적할 수 있는 객체다. computed 안에서 읽은 반응형 값이 달라지면 계산 결과가 무효화되고 필요할 때 다시 평가된다. 템플릿의 최상위 ref는 보통 자동으로 풀려 .value 없이 사용한다. 여러 상태 변경은 DOM 갱신 단계에서 묶일 수 있으므로 변경 직후 DOM을 읽어야 하면 nextTick을 기다린다.

## Java 예제

변경 통지와 파생 값을 비교하는 Java 모형이다.

```java
static class ObservableInt {
    int value;
    final java.util.List<Runnable> listeners = new java.util.ArrayList<>();

    void set(int next) {
        value = next;
        listeners.forEach(Runnable::run);
    }
}

static void demo() {
    var state = new ObservableInt();
    state.listeners.add(() -> System.out.println(state.value * 2));
    state.set(3); // 6
}
```

### Vue 3로 확인

아래 내용을 Vue Playground의 App.vue에 넣는다.

```vue
<script setup>
import { ref, computed } from 'vue'
const count = ref(0)
const doubled = computed(() => count.value * 2)
</script>

<template>
  <button @click="count++">{{ count }} / {{ doubled }}</button>
</template>
```

## 주의점

Java 코드는 변경 통지의 모형이며 Vue의 자동 의존성 추적·computed 캐시·DOM 배칭을 구현하지 않는다. reactive 객체의 원시 속성을 일반 변수로 구조 분해하면 연결을 잃을 수 있으며 defineProps의 컴파일러 처리와 구별한다.

## 꼬리질문

1. 템플릿에서는 count인데 JavaScript에서는 count.value인 이유는 무엇일까?
2. count를 두 번 바꾸어도 DOM 갱신이 묶일 수 있다면 nextTick은 무엇을 기다릴까?
3. 원시 값을 일반 변수로 복사한 뒤 원본을 바꾸면 왜 파생 계산이 자동으로 연결되지 않을 수 있을까?

</details>

## 참고 자료

- [Vue · Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals) — ref·reactive·nextTick과 구조 분해 제약을 확인한다.
- [Vue · Computed Properties](https://vuejs.org/guide/essentials/computed.html) — 파생 값의 캐시와 순수 계산 조건을 읽는다.
- [Vue Playground](https://play.vuejs.org/) — App.vue 예제를 붙여 넣고 버튼 클릭에 따른 반응성을 확인한다.
