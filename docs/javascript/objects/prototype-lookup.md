# 프로토타입과 속성 탐색

> 객체에 없는 속성은 프로토타입 연결을 따라 찾으며 자기 속성은 상속된 속성을 가릴 수 있다.

- 자기 속성을 먼저 탐색한다.
- 프로토타입 연결은 클래스 문법과 구별한다.
- 자기 속성 삭제와 부모 속성 삭제는 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Object.create(parent)로 만든 객체의 속성 조회는 자기 객체를 확인한 뒤 parent 쪽으로 이어진다. 객체가 같은 이름의 자기 속성을 추가하면 부모 값은 남은 채 가려진다. JavaScript의 class 문법도 이 프로토타입 기반 메커니즘 위에 있다.

## JavaScript 예제

```javascript
const parent = { role: "reader" };
const child = Object.create(parent);
console.log(child.role); // reader
child.role = "writer";
console.log(Object.hasOwn(child, "role")); // true
delete child.role;
console.log(child.role, Object.hasOwn(child, "role")); // reader false
```

## 주의점

외부 입력으로 프로토타입을 임의 변경하거나 신뢰하지 않는 객체 속성을 무검증 병합하지 않는다. Object.hasOwn은 부모 속성까지 찾는 in 연산과 다르다.

## 꼬리질문

1. child에 없는 role을 읽으면 어느 객체의 값을 반환할까?
2. child.role을 추가한 뒤 삭제하면 왜 parent.role이 다시 보일까?
3. in과 Object.hasOwn으로 검사할 때 상속된 속성이 각각 어떻게 판정될까?

</details>

## 참고 자료

- [MDN · 프로토타입 체인](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain) — 속성 가리기·체인·class 문법의 관계를 확인한다.
