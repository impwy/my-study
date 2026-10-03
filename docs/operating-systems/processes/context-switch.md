# 프로세스 상태와 문맥 교환

> 실행 가능한 작업을 바꿀 때 실행 위치와 상태를 저장하고 복원한다.

- 준비·실행·대기는 다르다.
- I/O 대기는 준비 큐에서 CPU만 기다리는 상태가 아니다.
- 문맥 교환에는 직접·간접 비용이 든다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

PCB 등에 현재 실행 상태를 저장하면 잠시 멈춘 작업을 이어서 실행할 수 있다. CPU를 빼앗긴 실행 작업은 준비 상태로, I/O 결과를 기다리는 작업은 대기 상태로 갈 수 있다. 교환 자체의 저장·복원 외에도 캐시·TLB 등의 효과가 실제 성능에 영향을 준다.

## Java 예제

대기 → 실행 가능 → 실행 흐름을 관찰하는 예제다. 문맥 교환 시점을 직접 제어하지 않는다.

```java
import java.util.concurrent.*;

static void demo() throws Exception {
    var signal = new CountDownLatch(1);
    Thread t =
            new Thread(
                    () -> {
                        try {
                            signal.await();
                            System.out.println("재개");
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    });
    t.start();
    signal.countDown();
    t.join();
}
```

## 주의점

커널 모드로 진입하는 모든 시스템 호출이 다른 작업으로의 문맥 교환인 것은 아니다. 모드 전환과 작업 교환을 구분한다.

## 꼬리질문

1. I/O 완료가 즉시 실행 재개를 뜻하지 않는 이유는?
2. countDown 호출 직후 대기 스레드가 반드시 CPU에서 실행 중이라고 말할 수 있을까?
3. 자바 스레드 상태 변화와 운영체제의 실제 문맥 교환 횟수는 왜 일대일 대응하지 않을까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
