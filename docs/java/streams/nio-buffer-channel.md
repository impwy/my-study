# NIO의 Buffer와 Channel

> 채널을 통해 데이터를 옮기고 버퍼의 position·limit 상태로 읽기·쓰기를 관리한다.

- Buffer의 상태 전환이 중요하다.
- flip은 기록한 범위를 읽도록 바꾼다.
- NIO가 항상 비동기·비블로킹인 것은 아니다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

버퍼에 데이터를 채우면 position이 전진한다. flip은 limit를 현재 position으로 두고 position을 시작으로 돌려 읽을 준비를 한다. clear는 다음 쓰기를 위한 상태 재설정이며 데이터를 안전하게 지우는 연산이 아니다. Channel도 모든 타입이 같은 I/O·블로킹 모델을 갖지는 않는다. 부분 읽기·쓰기와 남은 데이터를 처리해야 한다.

## Java 예제

```java
import java.nio.ByteBuffer;

static void demo() {
    ByteBuffer buffer = ByteBuffer.allocate(8);
    buffer.putInt(42); // position=4, limit=8
    buffer.flip(); // position=0, limit=4
    System.out.println(buffer.getInt()); // 42
    buffer.clear(); // 읽을 내용 삭제가 아니라 인덱스 초기화
}
```

## 주의점

clear 전에 아직 처리할 데이터가 남았으면 덮어쓸 수 있다. Selector로 다루는 채널과 파일 채널의 조건을 구분한다.

## 꼬리질문

1. flip 없이 채운 버퍼를 읽으면 position과 limit가 어떻게 잘못 쓰일 수 있는가?
2. flip과 clear는 position·limit를 각각 어떻게 바꿀까?
3. Channel.write가 일부만 썼다면 남은 바이트를 어떻게 반복해서 보내야 할까?

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
