# 클라우드 서비스 모델

> 온디맨드 자원 사용과 IaaS·PaaS·SaaS별 관리 책임의 차이를 설명한다.

- 클라우드는 단순한 원격 서버 이상의 특성을 가진다.
- 모델마다 사용자가 운영하는 범위가 다르다.
- 관리형 서비스도 사용자 책임을 없애지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

클라우드의 특성에는 필요 시 셀프 서비스, 넓은 네트워크 접근, 자원 풀링, 빠른 탄력성, 사용량 측정이 있다. IaaS는 인프라 자원을 제공하며 사용자가 OS·응용 운영을 맡는 범위가 크다. PaaS는 응용 실행 환경을, SaaS는 완성된 응용 사용을 제공한다. 같은 제공자 안에서도 서비스에 따라 보안·설정·데이터 책임이 달라진다.

## 예제

VM에 DB를 직접 설치하는 경우와 관리형 DB를 쓰는 경우는 패치·백업의 책임이 다르다. 업무 계정 권한과 데이터 보호는 둘 다 설계해야 한다.

## 주의점

관리형이라고 백업·복구·접근 권한을 확인하지 않아도 되는 것은 아니다. 비용과 용량·서비스 제한도 관리 대상이다.

## 복습 질문

IaaS에서 관리형 DB로 옮기면 어떤 운영 책임이 줄고 어떤 책임이 남는가?

자료 구분: **기존 자료** — 클라우드 강의·부하 실험 가이드·Kubernetes 학습 글의 개념. **공식 자료 보완** — 정의·운영 조건·측정 해석.

</details>

## 참고 자료

- [NIST SP 800-145 · Cloud Definition](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 클라우드의 특성과 서비스·배포 모델 정의를 확인한다.
- [AWS · Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — 가용성·보안·성능·운영의 설계 기준을 확인한다.
