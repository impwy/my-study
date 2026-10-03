# 폴링·인터럽트·DMA

> CPU와 입출력 장치가 상태를 확인하고 데이터를 옮기는 책임을 나눈다.

- 폴링은 CPU가 상태를 반복 확인한다.
- 인터럽트는 사건이 생겼음을 알린다.
- DMA는 데이터 이동의 CPU 관여를 줄인다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

프로그램 입출력은 CPU가 장치와 직접 상호작용한다. 인터럽트 방식은 완료·요청을 신호로 알려 CPU가 다른 일을 할 수 있게 한다. DMA는 제어기가 메모리와 장치 사이의 블록 이동을 맡는다. CPU는 초기 설정과 완료 처리에 참여하며 버스·메모리 대역폭은 여전히 공유된다.

## Java 예제

설정 → 다른 작업 → 완료 통지 순서의 모형이다. CompletableFuture가 DMA나 하드웨어 인터럽트를 구현한다는 뜻은 아니다.

```java
import java.util.concurrent.CompletableFuture;

static void model() {
    var transfer = CompletableFuture.supplyAsync(() -> new byte[] {1, 2, 3});
    System.out.println("CPU: 다른 작업");
    transfer.thenAccept(data -> System.out.println("완료 통지: " + data.length)).join();
}
```

## 주의점

인터럽트는 데이터 전체를 전달하는 방식과 동일하지 않다. DMA라고 CPU 비용·메모리 경합이 모두 0이 되는 것은 아니다.

## 꼬리질문

1. DMA가 있어도 CPU가 설정과 완료 처리를 맡는 이유는?
2. 전송을 맡긴 뒤 CPU가 다른 일을 할 수 있다는 것과 전송 비용이 0이라는 것은 왜 다를까?
3. 완료 통지 전에 버퍼를 재사용하면 어떤 소유권 문제가 생길까?

</details>

## 참고 자료

- [MIT OCW · Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — 논리 회로에서 CPU·메모리까지 강의와 도식을 따라 확인한다.
