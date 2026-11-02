# Kubernetes 롤링 업데이트와 무중단 배포의 조건

> 새 Pod를 교체하는 순서, 신·구 버전의 호환성, 실제 업무 복구를 함께 설계해야 배포 중 서비스 연속성을 유지할 수 있다.

- **전제:** 추가 Pod를 띄울 자원과 신·구 버전이 함께 사용할 데이터·API 계약이 필요하다.
- **원리:** 호환성 준비 → 소비자 → 생산자 → 프론트엔드 순으로 전환하고 단계마다 성공을 확인한다.
- **한계:** 애플리케이션 롤링 배포와 단일 호스트·데이터 저장소의 고가용성은 별개의 문제다.

<details>
<summary>운영 사례·배포 순서·성공 판정 펼치기</summary>

## 사례의 출발점

아래는 **사용자가 제공한 2026-11-02 운영 점검 기록**을 정리한 것이다. 이 문서를 작성하면서 운영 서버와 설정 파일을 재점검한 것은 아니다.

| 항목 | 제공된 운영 기록 |
| --- | --- |
| 애플리케이션 | API 2개·Web 2개·Worker 1개 모두 Ready |
| API/Web 배포 전략 | `maxUnavailable: 0`, `maxSurge: 1` |
| 상태·종료 처리 | readiness·liveness·startup probe, 종료 유예 330초 |
| Migration | 배포 전 단일 Job 실행 |
| 프론트엔드 | 버전별 정적 파일 유지, `index.html` 원자적 전환 |
| 실시간 복구 | WebSocket 재접속 후 애플리케이션 `sync` 사용 가능 |
| 데이터 계층 | PostgreSQL·MongoDB·Kafka·Redis 각각 1개, 단일 호스트 |

이 조건에서는 **Rolling Update + [Expand–Migrate–Contract](../../ddia/models/expand-migrate-contract.md)**가 일상 패치의 합리적인 기본안이다. 제공된 기록상 현재 스크립트는 API·Worker·Web 변경을 함께 적용하므로, 아래 단계별 전환은 **아직 적용하지 않은 개선 설계**다.

## 배포 방식 선택

| 방식 | 전환 방법 | 이 사례에서의 판단 |
| --- | --- | --- |
| Rolling Update | 새 Pod를 추가하고 이전 Pod를 점진적으로 제거 | 기존 설정 활용, 일상 패치의 기본안 |
| Blue-Green | 두 환경을 준비한 뒤 트래픽 전환 | 빠른 환경 전환이 필요한 변경에 검토. 병행하는 애플리케이션 자원은 대략 2배가 될 수 있지만 전체 비용이 항상 2배인 것은 아님 |
| Canary | 일부 트래픽으로 검증한 뒤 확대 | 라우팅과 버전별 지표 비교를 갖추었을 때 검토. 작은 트래픽에서는 판정에 시간이 더 필요 |

Blue-Green도 DB 호환성 문제를 없애지는 않는다. 방식별 자원과 전환 조건은 [AWS의 Blue-Green 설명](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/introduction.html)과 함께 판단한다.

## 배포 순서와 각 단계의 완료 조건

```text
CI 검증 · 이미지 digest 고정
  → 클러스터 용량 · 저장소 상태 · 최근 복구 검증 확인
  → 호환 가능한 확장 migration 완료 대기
  → Worker: 구·신 이벤트를 읽는 소비자 준비 완료
  → API: 롤링 완료 확인 후 새 형식 쓰기 활성화
  → Web: 정적 파일 게시 후 index.html 전환
  → HTTP·인증된 WebSocket 업무 시나리오 검사
  → 오류율·지연·큐 적체 관찰
```

**Worker → API → Web은 이 사례의 이벤트 의존관계에 따른 순서**다. 모든 시스템의 고정 규칙은 아니다. 새 생산자를 켜기 전에 소비자가 이전·새 형식을 모두 처리하도록 준비하는 [Prepare → Activate 원칙](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)을 적용한 설계다. Worker가 1개이면 교체·리밸런스 중 처리 지연도 관찰한다.

## 성공 판정과 롤백

readiness와 `/api/v1/config` 응답만으로 배포 성공을 판정하지 않는다. 다음 수치는 **이 사례의 시작 기준안**이며 서비스 SLO·기존 기준선·표본 수에 맞춰 조정한다.

| 게이트 | 기준안 |
| --- | --- |
| HTTP | 5xx 비율 1% 미만, p95 지연은 기준선의 1.5배 이내 |
| Pod | 새 CrashLoop·OOM·예상 밖 재시작 없음 |
| 비동기 처리 | consumer lag와 Outbox oldest age가 지속 증가하지 않음 |
| 업무 흐름 | 로그인 → 대화 조회 → WebSocket 인증 → 전송 → 재접속·sync 성공 |
| 관찰 | 최소 30분 soak를 시작점으로 삼되 트래픽·업무 주기에 따라 연장 |

30분 자체가 안전을 증명하지 않는다. [단계적 공개와 관찰 지침](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)은 충분한 업무 표본과 단계별 상태 확인을 강조한다.

실패하면 **새 기능 비활성화·이전 Web 진입점 복구 → 호환성 확인 후 API 이전 digest → Worker 이전 digest** 순으로 복구한다. DB 확장 구조는 남기고 필요한 수정은 forward migration으로 처리한다. 이미 열린 브라우저와 남아 있는 새 이벤트 때문에, 순서만 지킨다고 롤백이 안전해지는 것은 아니다. [API·WebSocket 호환성](../../rest-api/contracts/rolling-deployment-compatibility.md)에서 복구 조건을 확인한다.

## 주의점

- `maxUnavailable: 0`은 rollout의 가용 Pod 수 제약이다. 잘못된 readiness, 자원 부족, 종료 중 요청 실패까지 막지는 않는다. 종료 중인 Pod도 자원을 사용하므로 surge 여유를 확보한다.
- readiness는 요청 처리 준비, startup은 초기 기동 보호, liveness는 재시작 판단이다. Ready를 실제 업무 처리 가능성과 맞춘다.
- 330초 종료 유예에는 `preStop` 시간도 포함된다. SIGTERM 처리·진행 중 요청 종료·연결 drain을 구현해야 하며, 유예시간만 길게 설정해서는 부족하다.
- API/Web에 `PDB(minAvailable: 1)`을 검토하되, PDB는 주로 eviction 기반 자발적 중단을 제한하며 **Deployment 자체의 롤링 업데이트를 제어하지 않는다**.
- `minReadySeconds`를 5초에서 30초로 늘리는 것은 검토안이다. Available 판정의 안정화 대기이며 Service의 트래픽 유입을 30초 보류하는 기능은 아니다. 릴리스 SHA annotation도 장애 추적에 활용한다.
- 단일 호스트·단일 저장소 장애, 저장소 엔진 자체 패치는 별도 HA·복구 설계가 필요하다. 이번 기록은 설계 정리이며 운영 코드를 변경하거나 배포하지 않았다.

## 꼬리질문

1. `maxUnavailable: 0`이어도 사용자 요청이 실패할 수 있는 이유는 무엇인가?
2. 새 이벤트 형식을 도입할 때 Worker 준비와 API 활성화 사이에 어떤 검증을 넣어야 할까?
3. Pod를 여러 개 유지하는 것만으로 단일 호스트·단일 DB 장애까지 해결할 수 없는 이유는 무엇인가?

함께 복습: [Pod·Deployment·Service](../virtualization/kubernetes-building-blocks.md) · [배포 권한·상태 확인·롤백](../../github-actions/cd/deployment-oidc-and-rollback.md)

</details>

## 참고 자료

- [Kubernetes · Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — surge·unavailable·minReadySeconds와 rollout 상태의 의미를 확인한다.
- [Kubernetes · Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) — Pod 종료 유예·훅·엔드포인트 처리와 정상 종료의 관계를 확인한다.
- [Kubernetes · Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) — PDB의 보호 범위와 롤링 업데이트·비자발적 장애와의 차이를 확인한다.
