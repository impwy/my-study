# 배포 권한·상태 확인·롤백

> 검증한 산출물을 제한된 권한으로 배포하고 실제 상태 확인 뒤 실패를 복구한다.

- CI 성공과 배포 성공을 구분한다.
- OIDC는 신뢰 조건에 따른 임시 자격 증명을 사용한다.
- 동시 배포와 롤백 기준을 정한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

테스트·빌드 뒤 어느 커밋의 산출물을 배포하는지 고정한다. 클라우드 인증은 저장한 장기 키 대신 OIDC 기반 역할을 검토하며 저장소·브랜치·환경 등 신뢰 조건을 제한한다. 배포 명령 성공 뒤 readiness·대표 요청·오류 지표를 확인한다. 실패 시 어떤 이전 버전으로 돌아가며 DB 변경이 호환되는지까지 계획한다.

## 예제

main의 보호된 환경에만 배포 역할을 허용한다. 배포 concurrency로 이전·현재 배포가 동시에 운영을 바꾸지 않게 조정한다.

## 주의점

컨테이너 이미지만 되돌려도 호환되지 않는 DB 마이그레이션은 되돌아가지 않는다. OIDC를 쓴다고 모든 브랜치를 신뢰해도 되는 것은 아니다.

## 복습 질문

애플리케이션 롤백 전에 DB 스키마 호환성을 확인해야 하는 이유는?

자료 구분: **기존 자료** — CI/CD 가이드와 배포 기록의 흐름. **공식 자료 보완** — 공식 워크플로·인증·권한 조건.

함께 복습: [워크플로·이벤트·잡·스텝](../workflows/events-jobs-steps.md) · [Actuator 상태와 메트릭](../../spring-boot/actuator/health-and-metrics.md)

</details>

## 참고 자료

- [GitHub · Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — 이벤트·잡·스텝·권한·의존 관계의 정확한 문법을 확인한다.
- [GitHub · OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect) — OIDC 토큰과 클라우드 신뢰 조건을 확인한다.
