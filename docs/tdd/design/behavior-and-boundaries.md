# 행동과 경계값 테스트

> 요구한 결과와 불변식을 검증하고 입력·상태·실패 경계를 대표하는 사례를 선택한다.

- 메서드 호출보다 관찰 가능한 행동을 우선한다.
- 빈 값·경계·중복·실패를 고려한다.
- 테스트는 결정적이고 독립적이어야 한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

테스트가 어떤 요구를 지키는지 먼저 한 문장으로 적는다. 정상 예제 하나만으로 빈 입력·최소·최대·동시 중복·만료 시점을 설명할 수 없다. 같은 결과 집합을 만드는 대표 동치 클래스와 경계 사례를 선택한다. 시간·난수·외부 서비스는 통제할 수 있는 협력자로 분리하고 테스트 간 실행 순서 의존을 없앤다.

## Java 예제

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

static int first(int[] a, int target) {
    for (int i = 0; i < a.length; i++) if (a[i] == target) return i;
    return -1;
}

@Test
void boundaries() {
    assertEquals(-1, first(new int[] {}, 7));
    assertEquals(0, first(new int[] {7}, 7));
    assertEquals(0, first(new int[] {7, 7}, 7));
}
```

## 주의점

private 메서드의 모양을 과도하게 고정하면 리팩터링을 막는다. 많은 테스트 수와 높은 커버리지가 좋은 요구 검증과 같은 뜻은 아니다.

## 꼬리질문

1. 빈 배열과 한 원소 테스트가 각각 어떤 경계 오류를 찾는가?
2. 중복 원소 테스트는 단순히 찾기 성공 외에 어떤 반환 계약을 고정할까?
3. 정렬 방식이나 내부 반복문을 바꿔도 유지되어야 하는 테스트는 무엇을 관찰해야 할까?

</details>

## 참고 자료

- [Martin Fowler · Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) — 테스트·구현·리팩터링을 짧은 반복으로 연결하는 이유를 읽는다.
- [JUnit · User Guide](https://docs.junit.org/current/user-guide/) — 단위 테스트·픽스처·실행 구조를 확인한다.
