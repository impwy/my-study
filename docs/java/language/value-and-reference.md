# 기본형·참조형과 값 전달

> Java는 기본형 값과 객체 참조 값을 모두 복사해서 메서드에 전달한다.

- 참조 값의 복사와 객체 복사는 다르다.
- 매개변수 재대입은 호출자 변수를 바꾸지 않는다.
- 같은 객체의 내부 변경은 호출자에게 보인다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

변수에는 기본형 값 또는 객체를 가리키는 참조 값이 들어 있다. 메서드 호출은 그 값을 새 매개변수에 복사한다. 객체를 넘겼을 때 두 변수가 같은 객체를 가리키므로 필드 변경은 공유되지만, 매개변수에 새 객체를 대입해도 원래 변수의 참조는 그대로다. 두 int 매개변수만 바꾸는 swap이 호출자 배열을 바꾸지 못하는 이유도 값 전달이다.

## Java 예제

```java
static class Box {
    int value = 1;
}

static void change(Box box) {
    box.value = 2;
    box = new Box();
    box.value = 3;
}

static void demo() {
    Box original = new Box();
    change(original);
    System.out.println(original.value);
} // 2
```

## 주의점

참조형을 “참조에 의한 전달”이라고 부르면 변수 자체가 공유된다고 오해하기 쉽다. null 참조는 객체를 가리키지 않는다.

## 꼬리질문

1. 객체의 필드 수정과 매개변수 재대입의 결과가 다른 이유는?
2. box 매개변수에 새 객체를 대입해도 original 참조가 바뀌지 않는 이유는 무엇일까?
3. 같은 객체의 필드 수정이 호출자에게 보이는 것과 참조 자체를 전달하는 것은 어떻게 구분할까?

</details>

## 참고 자료

- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
