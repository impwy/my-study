# 주소 지정 방식

> 명령어가 실제 피연산자의 값이나 위치를 찾는 규칙이다.

- 즉시 값과 주소를 구분한다.
- 직접·간접·레지스터·상대 주소가 있다.
- 유효 주소는 계산 결과다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

즉시 방식은 명령어에 값이 있고 직접 방식은 저장 위치가 있다. 간접 방식은 먼저 읽은 내용이 실제 주소다. 베이스·인덱스·변위 등을 더해 배열이나 상대 위치를 접근할 수도 있다. 명령어 형식의 비트 수와 메모리 접근 횟수 사이에 선택 비용이 생긴다.

## Java 예제

주소 지정 방식을 배열 접근으로 비교한 모형이며 실제 CPU 명령어 코드는 아니다.

```java
static void demo() {
    int[] memory = new int[16];
    memory[3] = 8;
    memory[8] = 42;
    int immediate = 3;
    int direct = memory[3];
    int indirect = memory[memory[3]];
    System.out.println(immediate + "," + direct + "," + indirect); // 3,8,42
}
```

## 주의점

레지스터 번호와 메모리 주소를 혼동하지 않는다. 같은 표기라도 ISA마다 인코딩·연산 의미가 다를 수 있다.

## 꼬리질문

1. 간접 주소 지정은 직접 방식보다 어떤 추가 접근이 필요할까?
2. 직접 방식과 간접 방식에서 주소 3을 해석하는 단계는 어떻게 다를까?
3. 배열 원소 접근을 기반 주소+인덱스 방식으로 표현하면 어떤 계산이 필요할까?

</details>

## 참고 자료

- [MIT OCW · Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — 논리 회로에서 CPU·메모리까지 강의와 도식을 따라 확인한다.
