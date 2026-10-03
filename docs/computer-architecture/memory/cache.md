# 메모리 계층과 캐시

> 자주 쓰는 데이터를 가까이 두어 느린 메모리 접근을 줄인다.

- 시간·공간 지역성을 활용한다.
- hit·miss와 교체·쓰기 정책을 구분한다.
- 주소 매핑에 따라 충돌이 생긴다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

레지스터·캐시·주기억장치·보조기억장치는 속도·용량·가격이 다르다. 캐시는 보통 개별 바이트 대신 블록을 가져와 가까운 데이터의 재사용을 노린다. 직접 사상은 특정 위치에만 넣고 연관 사상은 후보 위치를 넓힌다. 캐시 미스가 잦으면 계산보다 기다리는 시간이 커질 수 있다.

## Java 예제

주소 분해 모형이다. Java 객체의 실제 물리 주소나 하드웨어 캐시 적중을 측정하는 코드는 아니다.

```java
static void addressParts(long address) {
    long block = address / 64; // 64바이트 캐시 라인
    long set = block % 128; // 128개 세트
    long tag = block / 128;
    long offset = address % 64;
    System.out.println("set=" + set + ", tag=" + tag + ", offset=" + offset);
}
```

## 주의점

적중률만 높다고 전체 성능이 좋다고 결론 내리지 않는다. miss penalty·쓰기 비용·접근 패턴도 본다.

## 꼬리질문

1. 지역성이 없는 접근에서 캐시 용량만 늘리면 항상 효과가 있을까?
2. 같은 세트로 매핑되는 두 주소의 간격은 이 모형에서 몇 바이트일까?
3. 충돌 미스와 용량 미스를 구별하면 캐시 용량·연관도 중 어떤 변경을 검토할 수 있을까?

</details>

## 참고 자료

- [MIT OCW · Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — 논리 회로에서 CPU·메모리까지 강의와 도식을 따라 확인한다.
