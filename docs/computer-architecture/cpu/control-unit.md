# 데이터 경로와 제어 장치

> 제어 신호가 레지스터·ALU·버스의 데이터 흐름을 선택한다.

- 데이터 경로는 값이 이동·계산되는 부분이다.
- 제어 장치는 어떤 작업을 언제 할지 정한다.
- 하드와이어와 마이크로프로그램 방식이 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

한 명령어도 레지스터 전송과 ALU 연산 같은 작은 작업으로 나눠 볼 수 있다. 제어 장치는 명령어와 현재 상태를 받아 필요한 선택·쓰기 신호를 만든다. 마이크로프로그램은 제어 기억장치의 작은 명령을 순서대로 실행해 이 흐름을 표현한다.

## Java 예제

주요 제어 신호를 단순화한 모형이다. 실제 신호 조합은 명령어 집합과 설계에 따라 다르다.

```java
enum Op {
    LOAD,
    ADD,
    STORE
}

record Signals(boolean memoryRead, boolean aluAdd, boolean memoryWrite) {}

static Signals decode(Op op) {
    return switch (op) {
        case LOAD -> new Signals(true, false, false);
        case ADD -> new Signals(false, true, false);
        case STORE -> new Signals(false, false, true);
    };
}
```

## 주의점

버스에 여러 장치가 동시에 값을 내보내지 않게 선택 규칙이 필요하다. ISA 명령어와 제어용 마이크로명령을 같은 층위로 읽지 않는다.

## 꼬리질문

1. ALU가 있어도 제어 신호 없이는 올바른 명령을 수행하지 못하는 이유는?
2. STORE에서 메모리 쓰기 신호 대신 읽기 신호를 켜면 의도한 동작이 왜 되지 않을까?
3. 여러 사이클로 나뉘는 명령에서는 opcode 외에 어떤 상태가 제어 신호 결정에 필요할까?

</details>

## 참고 자료

- [MIT OCW · Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — 논리 회로에서 CPU·메모리까지 강의와 도식을 따라 확인한다.
