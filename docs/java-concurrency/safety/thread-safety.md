# 스레드 안전성과 불변식

> 공유 객체가 여러 스레드의 접근에도 자신의 불변식을 유지하도록 상태와 접근 경계를 설계한다.

- 공유하는 가변 상태를 먼저 찾는다.
- 상태 검사와 갱신을 같은 보호 범위에 둔다.
- 불변·격리·동기화 중 맞는 방법을 고른다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

메서드가 여러 스레드에서 호출되어도 객체의 의미가 깨지지 않는지가 기준이다. 재고를 읽어 양수인지 검사한 뒤 감소시키는 작업은 함께 보호해야 한다. 검사만 synchronized이고 감소가 밖에 있으면 여전히 경쟁이 생긴다. 가능하면 불변 값과 스레드에 한정된 상태로 공유를 줄인다. 공유가 필요하면 모든 읽기·쓰기에 같은 동기화 규칙을 적용한다.

## Java 예제

```java
static class Stock {
    private int remaining = 1;

    synchronized boolean reserve() {
        if (remaining == 0) return false;
        remaining--;
        return true;
    }
}
```

## 주의점

메서드 하나에 락을 붙였다는 사실만으로 클래스 전체가 안전한 것은 아니다. 반환한 내부 가변 컬렉션도 보호 규칙을 우회할 수 있다.

## 꼬리질문

1. 재고 조회와 감소를 각각 따로 잠그면 왜 초과 판매가 가능한가?
2. 재고 확인과 차감을 같은 synchronized 블록에 넣어야 하는 이유는 무엇일까?
3. 이 객체를 서버 두 대가 각각 가지고 있다면 JVM의 락으로 전체 재고를 보호할 수 있을까?

함께 복습: [임계 구역과 동기화](../../operating-systems/synchronization/critical-section.md) · [낙관적 락과 비관적 락](../../jpa/locks/optimistic-and-pessimistic.md)

</details>

## 참고 자료

- [JLS 17 · Threads and Locks](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) — happens-before와 모니터·volatile의 보장 범위를 확인한다.
