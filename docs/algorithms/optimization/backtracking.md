# 백트래킹

> 가능한 선택을 시도하고 돌아와 상태를 복원하며 해를 탐색한다.

- 선택 → 재귀 → 복원 순서.
- 불가능한 가지를 일찍 자른다.
- 전체 해를 찾는 비용은 결과 수보다 작을 수 없다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

순열 생성은 현재 자리에 넣을 원소를 선택한 뒤 남은 자리를 같은 방식으로 채우는 과정이다. 복원은 다음 후보가 이전 후보의 영향을 받지 않게 하는 작업이다. 제약을 어긴 부분 해는 완성해도 유효하지 않으므로 더 내려가지 않는다. 가지치기의 정당성은 문제 조건으로 설명해야 한다.

## Java 예제

```java
import java.util.*;

static void subsets(int[] a, int i, List<Integer> chosen, List<List<Integer>> out) {
    if (i == a.length) {
        out.add(List.copyOf(chosen));
        return;
    }
    subsets(a, i + 1, chosen, out);
    chosen.add(a[i]);
    subsets(a, i + 1, chosen, out);
    chosen.remove(chosen.size() - 1);
}
```

## 주의점

visited나 배열 변경을 복원하지 않으면 다른 가지가 누락된다. 중복 값이 있는 순열은 같은 결과를 반복 생성하지 않는 규칙이 필요하다.

## 꼬리질문

1. 상태 복원을 빼면 두 번째 탐색 가지가 어떤 영향을 받을까?
2. 결과에 chosen 자체를 넣으면 이미 저장한 부분집합이 왜 바뀔까?
3. 양수만 있는 합 목표 문제에서 목표를 넘은 가지를 자르는 규칙은 음수에서도 안전할까?

</details>

## 참고 자료

- [MIT OCW · Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 동적 계획법 강의에서 상태·점화식·부분 문제 순서를 복습한다.
