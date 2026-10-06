# 클라우드

[전체 목록](../../README.md)

## 가상화

| 문서 | 한 줄 요약 |
| --- | --- |
| [Kubernetes의 Pod·Deployment·Service](virtualization/kubernetes-building-blocks.md) | 컨테이너 실행 단위, 원하는 상태 유지, 접근 경로의 책임을 구분한다. |
| [클라우드 서비스 모델](virtualization/cloud-service-models.md) | 온디맨드 자원 사용과 IaaS·PaaS·SaaS별 관리 책임의 차이를 설명한다. |

## 컴퓨팅·스토리지

| 문서 | 한 줄 요약 |
| --- | --- |
| [OCR 모델의 학습·추론과 신분증 정보 추출](resources/ocr-model-fine-tuning.md) | OCR은 이미지의 문자를 텍스트로 변환하는 작업이며 파인튜닝은 기존 모델을 특정 데이터로 추가 학습하는 방법이다. |
| [컴퓨팅과 블록·파일·객체 스토리지](resources/compute-and-storage-boundaries.md) | 애플리케이션의 실행 자원과 데이터 보관 자원을 나누고 접근 방식에 맞는 스토리지를 선택한다. |

## 네트워크

| 문서 | 한 줄 요약 |
| --- | --- |
| [클라우드 연결 경로와 아웃바운드 통신](network/network-path-and-egress.md) | 연결 문제는 DNS·라우팅·접근 제어·서버 대기 상태를 경로 순서대로 확인한다. |

## 확장성·가용성

| 문서 | 한 줄 요약 |
| --- | --- |
| [Observability와 LGTM·Datadog](availability/observability-lgtm.md) | 메트릭·로그·트레이스를 연결해 내부 상태를 추론하고 Grafana 도구 조합과 Datadog 통합 서비스를 구분한다. |
| [백프레셔와 요청 제한](availability/backpressure-and-rate-limit.md) | 처리 가능한 속도에 맞춰 유입·대기·거절을 조정해 과부하가 시스템 전체로 번지는 것을 제한한다. |
| [지연·처리량·포화](availability/latency-throughput-saturation.md) | 부하가 늘 때 처리량·지연 분포·오류·대기열을 함께 보아 병목을 찾는다. |
| [폴백과 장애 복구의 경계](availability/fallback-and-recovery.md) | 주 경로 실패 때 대체 동작을 선택하되 부하·데이터 정확성·복구 절차를 함께 검증한다. |

