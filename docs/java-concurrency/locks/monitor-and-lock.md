# 모니터와 명시적 락

> 락은 같은 상태를 다루는 스레드들의 임계 영역 진입을 조정하고 메모리 가시성을 연결한다.

- synchronized는 객체 모니터를 사용한다.
- 명시적 락은 finally에서 해제한다.
- 대기 조건은 반복해서 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

synchronized 블록은 선택한 모니터를 획득한 스레드만 진입하게 한다. 같은 모니터의 해제와 이후 획득 사이에는 happens-before 관계가 있다. ReentrantLock은 시도·시간 제한·Condition 같은 제어를 제공한다. wait나 await 이후에는 신호를 받았더라도 조건이 이미 달라졌거나 허위 깨움이 있을 수 있으므로 while로 조건을 다시 검사한다.

## 예제

`lock.lock(); try { /* 상태 검사와 갱신 */ } finally { lock.unlock(); }`가 기본 구조다. 여러 락이 필요하면 전체 코드에서 획득 순서를 통일한다.

## 주의점

서로 다른 객체를 잠그면 같은 필드를 보호하지 못한다. 외부 호출 중 락을 오래 보유하면 지연과 교착 위험이 커진다.

## 복습 질문

조건 대기를 if로 한 번만 검사하면 어떤 경쟁 상황을 놓치는가?

자료 구분: **기존 자료** — 스레드·동기화 강의와 동시성 노트의 원리. **공식 자료 보완** — JMM·표준 동시성 API의 보장 범위.

</details>

## 참고 자료

- [JLS 17 · Threads and Locks](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) — happens-before와 모니터·volatile의 보장 범위를 확인한다.
- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
