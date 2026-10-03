# 해시 테이블

> 키를 버킷 위치로 바꾸고 충돌을 처리해 탐색을 빠르게 한다.

- 같은 해시와 같은 키는 다르다.
- 평균 비용은 좋은 분산·부하율에 의존한다.
- equals와 hashCode 계약을 지킨다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

서로 다른 키도 같은 버킷에 갈 수 있으므로 충돌 처리가 필요하다. 체이닝은 버킷 안에 여러 항목을 두고, 개방 주소법은 다른 빈 위치를 찾는다. 항목이 늘어 부하율이 높아지면 재해시 비용을 들여 버킷을 확장할 수 있다. 이 비용 때문에 모든 연산이 언제나 O(1)인 것은 아니다.

## Java 예제

```java
import java.util.*;

record Key(int id) {
    @Override
    public int hashCode() {
        return 1;
    }
}

static void demo() {
    Map<Key, String> map = new HashMap<>();
    map.put(new Key(1), "A");
    map.put(new Key(2), "B");
    System.out.println(map.size()); // 2: 충돌해도 equals로 구별
    System.out.println(map.get(new Key(1))); // A
}
```

## 주의점

맵에 넣은 키의 equals·hashCode 결과를 바꾸면 이후 조회가 실패할 수 있다. 선형 조사 삭제에는 탐색 경로를 끊지 않는 표식·재배치 규칙이 필요하다.

## 꼬리질문

1. 해시 값이 같으면 두 객체를 같은 키로 취급해도 될까?
2. 예제의 두 키는 hashCode가 같은데도 왜 덮어쓰지 않을까?
3. 키를 넣은 뒤 equals·hashCode에 쓰이는 필드를 변경하면 조회가 왜 실패할 수 있을까?

</details>

## 참고 자료

- [Princeton · Hash Tables](https://algs4.cs.princeton.edu/34hash/) — 충돌 처리와 부하율이 탐색 비용에 미치는 영향을 확인한다.
