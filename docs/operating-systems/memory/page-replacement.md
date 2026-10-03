# 페이지 교체와 스래싱

> 빈 프레임이 없을 때 내보낼 페이지를 고르고 메모리 부족의 반복 비용을 관리한다.

- FIFO·LRU·최적 알고리즘의 정보가 다르다.
- 지역성에 맞는 작업 집합이 중요하다.
- FIFO에는 Belady의 이상 현상이 가능하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

최적 교체는 미래에 가장 늦게 쓰일 페이지를 내보내지만 실제 미래를 알 수 없으므로 비교 기준이다. LRU는 최근 사용이 가까운 미래의 단서라는 가정으로 오래 안 쓴 페이지를 고른다. 필요한 작업 집합보다 프레임이 적으면 계속 내보내고 가져오며 실제 작업보다 I/O에 시간을 쓰는 스래싱이 생길 수 있다.

## Java 예제

페이지 참조열의 LRU 모형이며 OS가 정확한 LRU를 구현한다고 가정하지 않는다.

```java
import java.util.*;

static int lruMisses(int[] pages, int capacity) {
    if (capacity < 1) throw new IllegalArgumentException();
    var resident = new LinkedHashMap<Integer, Boolean>(16, 0.75f, true);
    int misses = 0;
    for (int page : pages) {
        if (resident.get(page) == null) {
            misses++;
            if (resident.size() == capacity)
                resident.remove(resident.keySet().iterator().next());
            resident.put(page, true);
        }
    }
    return misses;
}
```

## 주의점

FIFO의 프레임 수 증가가 항상 부재 감소를 보장하지 않는다. 정확한 LRU의 추적 비용도 평가한다.

## 꼬리질문

1. CPU 사용률이 낮은데 디스크 I/O만 높다면 스래싱을 어떻게 의심할까?
2. 용량 2에서 참조 1·2·1·3을 처리하면 마지막에 어떤 페이지가 교체될까?
3. LRU가 작업 집합 전체를 담지 못할 때 반복 참조 패턴에서 어떤 미스가 계속 생길까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
