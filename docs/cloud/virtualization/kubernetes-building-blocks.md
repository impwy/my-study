# Kubernetes의 Pod·Deployment·Service

> 컨테이너 실행 단위, 원하는 상태 유지, 접근 경로의 책임을 구분한다.

- Pod는 하나 이상의 컨테이너를 묶는다.
- Deployment는 복제·업데이트 상태를 조정한다.
- Service는 대상에 대한 네트워크 추상화다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Image는 실행 파일과 의존성의 패키지이고 Container는 그것으로 실행하는 격리 환경이다. Node 위에 Pod가 실행되며 Pod 안의 컨테이너는 네트워크 등을 공유한다. Deployment는 ReplicaSet 등을 통해 선언한 상태로 맞추고 Service는 selector·레이블 등을 통해 대상 Pod 접근을 제공한다. Pod가 교체되는 것과 안정적인 접근 경로의 유지는 서로 다른 책임이다.

## 예제

복제 수 3을 선언해도 자원 부족·이미지 오류가 있으면 세 개가 즉시 준비되지 않는다. 기본 ClusterIP Service가 생겨도 자동으로 인터넷에 공개되지는 않는다.

## 주의점

Pod 하나를 항상 컨테이너 하나로 해석하지 않는다. 이 기록은 기존 학습 글에서 확인한 기본 구성 요소에 한정한다.

## 복습 질문

Deployment가 있는데도 Service가 필요한 상황은 무엇인가?

자료 구분: **기존 자료** — 클라우드 강의·부하 실험 가이드·Kubernetes 학습 글의 개념. **공식 자료 보완** — 정의·운영 조건·측정 해석.

함께 복습: [클라우드 서비스 모델](cloud-service-models.md) · [로드밸런싱과 Auto Scaling](../../aws/operations/load-balancing-and-autoscaling.md)

</details>

## 참고 자료

- [Kubernetes · Concepts](https://kubernetes.io/docs/concepts/) — Pod·Deployment·Service의 공식 개념과 관계를 확인한다.
