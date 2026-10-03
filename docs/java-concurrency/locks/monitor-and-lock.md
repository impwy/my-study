# 모니터와 명시적 락

> 락은 같은 상태를 다루는 스레드들의 임계 영역 진입을 조정하고 메모리 가시성을 연결한다.

- synchronized는 객체 모니터를 사용한다.
- 명시적 락은 finally에서 해제한다.
- 대기 조건은 반복해서 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

synchronized 블록은 선택한 모니터를 획득한 스레드만 진입하게 한다. 같은 모니터의 해제와 이후 획득 사이에는 happens-before 관계가 있다. ReentrantLock은 시도·시간 제한·Condition 같은 제어를 제공한다. wait나 await 이후에는 신호를 받았더라도 조건이 이미 달라졌거나 허위 깨움이 있을 수 있으므로 while로 조건을 다시 검사한다.

## Java 예제

```java
static class Slot {
    private String value;

    synchronized void put(String next) throws InterruptedException {
        while (value != null) wait();
        value = java.util.Objects.requireNonNull(next);
        notifyAll();
    }

    synchronized String take() throws InterruptedException {
        while (value == null) wait();
        String result = value;
        value = null;
        notifyAll();
        return result;
    }
}
```

## 주의점

서로 다른 객체를 잠그면 같은 필드를 보호하지 못한다. 외부 호출 중 락을 오래 보유하면 지연과 교착 위험이 커진다.

## 꼬리질문

1. 조건 대기를 if로 한 번만 검사하면 어떤 경쟁 상황을 놓치는가?
2. wait가 락을 놓고 다시 잡는 사이 다른 스레드가 조건을 바꾸면 while이 무엇을 막을까?
3. 서로 다른 조건을 기다리는 스레드가 있을 때 notify 하나만 쓰면 어떤 진행 문제가 생길까?

</details>

## 참고 자료

- [JLS 17 · Threads and Locks](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) — happens-before와 모니터·volatile의 보장 범위를 확인한다.
- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
