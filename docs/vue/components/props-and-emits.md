# Vue 컴포넌트의 props와 emit

> 부모는 props로 값을 전달하고 자식은 이벤트로 변경 의도를 올려 상태의 소유자를 유지한다.

- props는 부모에서 자식으로 전달된다.
- 자식 이벤트는 부모가 처리한다.
- 객체 prop의 중첩 변경도 상태 소유권을 고려한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

자식 컴포넌트가 전달받은 count를 직접 바꾸면 부모 상태와 변경 책임이 흐려진다. 대신 increment 이벤트를 발행하고 부모가 자신의 count를 갱신한다. defineProps와 defineEmits는 script setup에서 사용하는 선언 매크로다. 이 흐름은 입력 값과 사용자 동작을 분리하며 같은 자식을 다른 부모에서도 재사용하기 쉽게 한다.

## Java 예제

```java
record Child(int count, Runnable incrementRequest) {
    void click() {
        incrementRequest.run();
    }
}

static void demo() {
    int[] parentCount = {0};
    var child = new Child(parentCount[0], () -> parentCount[0]++);
    child.click();
    System.out.println(parentCount[0]); // 1
}
```

### Vue 3로 확인

CountButton.vue와 부모 App.vue를 같은 실습 프로젝트에 둔다.

```vue
<!-- CountButton.vue -->
<script setup>
defineProps({ count: { type: Number, required: true } })
const emit = defineEmits(['increment'])
</script>
<template>
  <button @click="emit('increment')">{{ count }}</button>
</template>
```

```vue
<!-- App.vue -->
<script setup>
import { ref } from 'vue'
import CountButton from './CountButton.vue'
const count = ref(0)
</script>
<template>
  <CountButton :count="count" @increment="count++" />
</template>
```

## 주의점

Java 모형의 child.count는 자동 갱신되지 않는다. Vue의 갱신은 부모 반응형 상태와 prop 전달이 연결한다. 부모가 원시 값이 아닌 객체를 전달하면 중첩 객체를 공유하므로 단방향 데이터 흐름을 의도적으로 지켜야 한다.

## 꼬리질문

1. 자식이 count를 직접 바꾸는 것과 increment 이벤트를 보내는 것은 변경 책임이 어떻게 다를까?
2. 부모 두 곳에서 같은 자식을 쓰려면 이벤트의 의미를 얼마나 구체적으로 정해야 할까?
3. 읽기 전용 prop이어도 객체 내부를 수정할 수 있다면 어떤 숨은 결합이 생길까?

</details>

## 참고 자료

- [Vue · Props](https://vuejs.org/guide/components/props.html) — 단방향 전달과 객체 prop 변경의 제약을 확인한다.
- [Vue · Component Events](https://vuejs.org/guide/components/events.html) — 이벤트 선언·발행·부모 처리 방식을 확인한다.
- [Vue Playground](https://play.vuejs.org/) — 두 Vue 파일을 만들어 부모 상태와 자식 이벤트를 직접 확인한다.
