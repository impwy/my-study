# JVM 메모리와 GC

> GC는 도달할 수 없는 객체의 메모리를 회수하며 애플리케이션 자원 전체를 관리하지 않는다.

- 객체는 대체로 힙, 메서드 호출은 스레드별 스택을 사용한다.
- 도달 가능성은 사용 의도와 다르다.
- GC 정책과 성능은 로그·측정으로 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

실행 중 메서드의 지역 변수·호출 정보는 스택 프레임과 연결된다. 객체는 다른 객체나 실행 중 참조를 통해 도달 가능한 동안 살아 있을 수 있다. 사용하지 않더라도 장기 캐시나 static 컬렉션이 붙잡으면 회수되지 않는 메모리 누수가 생긴다. GC는 객체 수명과 메모리 회수를 다루지만 파일 핸들·DB 연결·스레드 종료까지 대신하지 않는다.

## Java 예제

```java
import java.lang.ref.WeakReference;
import java.util.*;

static void demo() {
    List<byte[]> retained = new ArrayList<>();
    byte[] data = new byte[1024];
    var weak = new WeakReference<>(data);
    retained.add(data);
    data = null;
    System.out.println(weak.get() != null); // 리스트의 강한 참조가 남음
    retained.clear(); // 이제 회수 가능; 즉시 회수된다는 뜻은 아님
}
```

## 주의점

GC가 모든 객체를 매번 즉시 회수하거나 한 가지 알고리즘으로 동작한다고 가정하지 않는다. collector별 정지 시간과 처리량의 교환 관계를 본다.

## 꼬리질문

1. 더 쓰지 않는 객체가 살아 있는 참조에 연결되어 있으면 GC가 회수할 수 있는가?
2. 지역 변수 data를 null로 바꾸어도 객체가 살아 있는 참조 경로는 무엇일까?
3. 회수 가능 상태와 실제 GC 실행 시점을 구분하면 메모리 관측을 어떻게 해석해야 할까?

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
