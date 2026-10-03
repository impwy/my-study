# 생산자–소비자

> 한정된 버퍼에서 비어 있는 칸과 준비된 항목을 조정한다.

- 생산자는 공간, 소비자는 항목을 기다린다.
- 버퍼 변경에는 상호 배제가 필요하다.
- 조건은 깨어난 뒤 다시 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

빈 칸·채워진 칸을 나타내는 세마포어와 버퍼 구조를 보호하는 mutex를 조합할 수 있다. 생산자는 빈 칸을 확보하고 넣은 뒤 항목 수를 알린다. 소비자는 반대로 처리한다. 대기 중 다른 실행이 상태를 바꿀 수 있으므로 조건 대기는 보통 while 검사로 감싼다.

## Java 예제

```java
import java.util.concurrent.*;

static void demo() throws InterruptedException {
    BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(1);
    Thread producer =
            new Thread(
                    () -> {
                        try {
                            queue.put(42);
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    });
    producer.start();
    System.out.println(queue.take());
    producer.join();
}
```

## 주의점

버퍼 락을 잡은 채 공간 확보를 기다리면 다른 작업도 못 움직일 수 있다. 대기와 락 획득 순서를 검토한다.

## 꼬리질문

1. notify를 받았다는 사실만으로 항목이 남아 있다고 믿으면 왜 위험할까?
2. 용량이 1인 큐에 생산자가 두 번째 항목을 넣으려 하면 언제 진행할 수 있을까?
3. 소비자를 종료할 때 단순히 큐를 비우는 것 외에 어떤 종료 신호가 필요할까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
