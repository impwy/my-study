# 이진 탐색

> 정렬된 배열에서 중간값을 비교해, 정답이 있을 수 없는 절반을 버리는 탐색 방법.

- 먼저 **정렬되어 있어야** 한다.
- 시간은 O(log n), 반복 구현의 추가 공간은 O(1)이다.
- 경계 조건과 중복 값의 반환 규칙을 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

중간값이 목표보다 작으면 왼쪽 절반에 목표가 있을 수 없다. 크면 오른쪽 절반을 버린다. 이때 **목표가 존재한다면 남은 구간 `[left, right]`에 있다**는 조건을 유지한다. 한 번 비교할 때마다 후보가 약 절반이므로 n → n/2 → n/4처럼 줄어든다.

배열 `[2, 4, 6, 8, 10, 12, 14]`에서 10을 찾는 과정:

| 남은 인덱스 | 중간 인덱스·값 | 다음 행동 |
| --- | --- | --- |
| 0–6 | 3 · 8 | 목표가 더 크므로 4–6 |
| 4–6 | 5 · 12 | 목표가 더 작으므로 4–4 |
| 4–4 | 4 · 10 | 인덱스 4 반환 |

## Java 예제

```java
static int binarySearch(int[] values, int target) {
    int left = 0;
    int right = values.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (values[mid] < target) {
            left = mid + 1;
        } else if (values[mid] > target) {
            right = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}
```

## 주의점

`left == right`에서도 후보 하나가 남으므로 `<=`를 사용한다. 검사한 mid는 `+1`·`-1`로 제외해야 같은 구간을 반복하지 않는다. 중간값 계산은 `(left + right) / 2`의 덧셈 오버플로를 피한다.

중복 값이 있으면 이 코드는 일치하는 인덱스 하나를 반환한다. 첫 위치·마지막 위치가 필요하면 [lower bound와 upper bound](lower-upper-bound.md)를 사용한다. Java `Arrays.binarySearch`는 실패 시 `-(삽입 위치) - 1`을 반환하므로 위 코드의 -1 정책과 다르다.

## 복습 질문

원소가 하나인 배열에서 `left < right`로 반복하면 왜 찾는 값을 놓칠까?

자료 구분: 기존 이진 탐색 노트의 탐색 구간 원리를 재구성했다. 안전한 mid 계산과 Java API 반환 규칙은 아래 공개 자료로 보완했다.

</details>

## 참고 자료

- [NIST · Binary search](https://xlinux.nist.gov/dads/HTML/binarySearch.html) — 정렬 전제와 탐색 정의를 확인한다.
- [Google Research · 이진 탐색의 오버플로 오류](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/) — 익숙한 mid 계산이 큰 입력에서 실패하는 이유를 읽는다.
- [Java 21 · Arrays.binarySearch](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Arrays.html#binarySearch(int%5B%5D,int)) — 정렬·중복·실패 반환값의 계약을 확인한다.
