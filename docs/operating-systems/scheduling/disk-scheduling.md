# 디스크 스케줄링

> 저장장치의 접근 요청 순서를 조정해 이동 비용과 공정성을 관리한다.

- HDD는 탐색·회전 지연이 있다.
- SSTF·SCAN은 이동 순서를 최적화한다.
- 정책의 기아·응답 편차를 본다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

FCFS는 요청 순서를 지키지만 헤드 이동이 길어질 수 있다. SSTF는 현재 가까운 요청부터 처리해 먼 요청이 기다릴 수 있다. SCAN은 한 방향으로 이동하며 처리하고 되돌아온다. SSD는 기계적 헤드 이동이 없으므로 같은 물리 비용 모델을 그대로 적용하지 않는다.

## Java 예제

기계식 디스크의 트랙 이동 비용 모형이며 실제 장치 큐를 제어하지 않는다.

```java
import java.util.*;

static long sstf(int head, List<Integer> requests) {
    var pending = new ArrayList<>(requests);
    long movement = 0;
    while (!pending.isEmpty()) {
        final int current = head;
        int next =
                pending.stream()
                        .min(Comparator.comparingLong(x -> Math.abs((long) x - current)))
                        .orElseThrow();
        movement += Math.abs((long) next - head);
        head = next;
        pending.remove(Integer.valueOf(next));
    }
    return movement;
}
```

## 주의점

과거 HDD용 정책의 설명을 모든 저장장치의 현재 최적 설정으로 제시하지 않는다.

## 꼬리질문

1. SCAN이 SSTF보다 응답 편차를 줄일 수 있는 이유는?
2. 현재 헤드가 50이고 요청이 10·48·90이면 SSTF는 어떤 순서로 처리할까?
3. 헤드 탐색이 없는 SSD에서도 같은 이동 거리 최적화가 핵심일까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
