# 동시성 컬렉션의 연산 경계

> 동시성 컬렉션은 명시된 개별·복합 API를 안전하게 제공하지만 호출 여러 개를 자동으로 한 작업으로 묶지 않는다.

- ConcurrentHashMap은 공유 Map 접근에 맞는다.
- 검사 후 갱신에는 compute·putIfAbsent 등을 검토한다.
- 스레드 안전성과 스냅샷 일관성은 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

여러 스레드가 HashMap을 동시에 수정하는 대신 ConcurrentHashMap의 계약을 이용한다. 그러나 containsKey를 호출한 뒤 put하는 코드는 그 사이에 다른 스레드가 개입할 수 있다. 필요한 의미가 “없을 때만 넣기”라면 putIfAbsent를 선택한다. 반복자는 대체로 약한 일관성으로 변경을 허용하며, 전체 상태가 한 시점의 사진이라는 보장은 별개다.

## Java 예제

```java
import java.util.concurrent.ConcurrentHashMap;

static class Counts {
    final ConcurrentHashMap<String, Integer> values = new ConcurrentHashMap<>();

    void increment(String key) {
        values.merge(key, 1, Integer::sum);
    }

    int get(String key) {
        return values.getOrDefault(key, 0);
    }
}
```

## 주의점

Map에 저장한 값 객체가 가변이면 Map의 안전성이 값 내부 수정까지 보호하지 않는다. 여러 키에 걸친 불변식에는 별도 조정이 필요하다.

## 꼬리질문

1. ConcurrentHashMap의 get과 put을 각각 호출해 카운터를 올리면 왜 여전히 증가를 잃는가?
2. get 후 put 대신 merge를 쓰면 같은 키의 증가에서 어떤 경쟁을 막을까?
3. 두 키 사이의 잔액 이체는 각각의 merge가 원자적이어도 왜 별도 경계가 필요할까?

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
- [JLS 17 · Threads and Locks](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) — happens-before와 모니터·volatile의 보장 범위를 확인한다.
