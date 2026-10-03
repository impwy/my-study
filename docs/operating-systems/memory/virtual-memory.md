# 가상 메모리와 페이지 변환

> 프로세스의 주소를 물리 메모리의 위치로 변환해 격리와 유연한 배치를 제공한다.

- 가상 주소와 물리 주소는 다르다.
- 페이지 테이블과 TLB가 변환을 돕는다.
- 페이지 부재는 정상 처리일 수도 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

고정 크기 페이지를 서로 다른 물리 프레임에 배치하면 프로세스가 연속된 주소를 사용해도 실제 메모리는 흩어질 수 있다. TLB는 자주 쓰는 변환을 캐시한다. 접근한 페이지가 아직 적재되지 않았다면 운영체제가 가져온 뒤 명령을 다시 수행할 수 있다. 유효하지 않은 접근과 적재가 필요한 접근을 구분한다.

## Java 예제

4KiB 페이지의 주소 변환 모형이다. 실제 JVM·운영체제 페이지 테이블을 읽지 않는다.

```java
static long translate(long virtualAddress, long[] pageTable) {
    long page = virtualAddress / 4096, offset = virtualAddress % 4096;
    long frame = pageTable[Math.toIntExact(page)];
    if (frame < 0) throw new IllegalStateException("page fault");
    return frame * 4096 + offset;
} // pageTable={7,2}: 가상 주소 4099 → 물리 주소 8195
```

## 주의점

페이지 부재를 모두 프로그램 오류로 취급하지 않는다. 가상 메모리 용량과 실제 RAM 용량이 같은 것은 아니다.

## 꼬리질문

1. 연속 가상 주소가 연속 물리 메모리를 요구하지 않는 이유는?
2. 가상 페이지 0과 1이 물리 프레임 7과 2에 있어도 연속 가상 주소를 쓸 수 있는 이유는 무엇일까?
3. 페이지가 메모리에 없을 때 fault를 처리한 뒤 명령을 어떻게 재개해야 할까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
