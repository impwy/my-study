# 병렬 처리와 메모리 구조

> 명령·데이터·프로세서·메모리의 조직으로 병렬성을 구분하고 통신·동기화 비용을 고려한다.

- 동시성과 병렬 실행은 다르다.
- SIMD는 같은 연산을 여러 데이터에 적용한다.
- 공유 메모리와 분산 메모리의 비용이 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파이프라인은 여러 명령 단계의 겹침으로 처리량을 높이고 SIMD는 같은 연산을 데이터 여러 개에 적용한다. 여러 코어는 다른 작업을 동시에 실행할 수 있지만 의존성이 있으면 직렬 단계가 남는다. 공유 메모리에서는 가시성·일관성과 동기화를, 분산 메모리에서는 메시지 전달·분할·통신을 고려한다. 병렬 장치 수만 늘려 전체 실행 시간이 같은 비율로 줄지 않는다.

## Java 예제

작업 크기가 고정되고 병렬화 오버헤드가 없는 Amdahl 법칙 모형이다.

```java
static double amdahl(double serialFraction, int workers) {
    return 1.0 / (serialFraction + (1.0 - serialFraction) / workers);
} // amdahl(0.25, 4) ≈ 2.29배
```

## 주의점

동시 작업 수를 병렬 CPU 수와 혼동하지 않는다. 같은 메모리의 쓰기 경합·캐시 비용을 무시하면 확장성이 떨어진다.

## 꼬리질문

1. 코어가 두 배가 되어도 프로그램 속도가 두 배가 되지 않는 이유는?
2. 직렬 비율이 25%라면 코어를 무한히 늘렸을 때 최대 가속은 얼마일까?
3. 동기화·통신 비용을 추가하면 이 계산보다 실제 가속이 작아지는 이유는 무엇일까?

</details>

## 참고 자료

- [MIT OCW · Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — 논리 회로에서 CPU·메모리까지 강의와 도식을 따라 확인한다.
- [Princeton · Analysis of Algorithms](https://algs4.cs.princeton.edu/14analysis/) — 입력 크기와 연산 횟수를 연결하고 측정과 분석을 구분한다.
