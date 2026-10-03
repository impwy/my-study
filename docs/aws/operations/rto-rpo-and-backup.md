# RTO·RPO와 복구 검증

> 허용 중단 시간과 데이터 손실 범위를 정하고 백업에서 실제 복구되는지 확인한다.

- RTO는 목표 복구 시간이다.
- RPO는 허용하는 데이터 손실의 시간 범위다.
- 복제·백업·복구 훈련은 역할이 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

서비스가 어느 정도 오래 중단되어도 되는지와 어느 시점 이후 변경을 잃어도 되는지를 각각 정한다. 이 기준으로 백업 주기·복제·장애 전환·복구 절차를 설계한다. 백업이 존재해도 암호화 키·권한·의존 서비스·복구 순서를 갖추지 못하면 목표 시간에 복구할 수 없다. 정기적인 복원 훈련으로 목표와 실제 시간을 비교한다.

## Java 예제

시간을 비교하는 Java 예제다. RPO·RTO는 목표이며 출력은 사고 또는 복구 훈련의 실제 측정치다.

```java
import java.time.*;

static void measure(Instant lastRecoveredWrite, Instant incident, Instant restored) {
    System.out.println("실제 데이터 손실 구간=" + Duration.between(lastRecoveredWrite, incident));
    System.out.println("실제 복구 소요=" + Duration.between(incident, restored));
}
```

## 주의점

복제본은 잘못된 삭제도 따라갈 수 있다. RTO·RPO는 제품이 자동 보장하는 수치가 아니라 업무 목표와 검증 대상이다.

## 꼬리질문

1. 백업 성공 로그가 있는데도 복구 시간 목표를 못 지킬 수 있는 이유는?
2. 마지막 복구 가능 시점이 사고 30분 전이고 복구에 2시간이 걸리면 RPO·RTO 10분·1시간 목표를 만족할까?
3. 백업 다운로드 외에 검증·서비스 재연결 시간도 복구 시험에 포함해야 하는 이유는 무엇일까?

</details>

## 참고 자료

- [AWS · Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — 가용성·보안·성능·운영의 설계 기준을 확인한다.
