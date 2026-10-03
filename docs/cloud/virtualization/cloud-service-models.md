# 클라우드 서비스 모델

> 온디맨드 자원 사용과 IaaS·PaaS·SaaS별 관리 책임의 차이를 설명한다.

- 클라우드는 단순한 원격 서버 이상의 특성을 가진다.
- 모델마다 사용자가 운영하는 범위가 다르다.
- 관리형 서비스도 사용자 책임을 없애지 않는다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

클라우드의 특성에는 필요 시 셀프 서비스, 넓은 네트워크 접근, 자원 풀링, 빠른 탄력성, 사용량 측정이 있다. IaaS는 인프라 자원을 제공하며 사용자가 OS·응용 운영을 맡는 범위가 크다. PaaS는 응용 실행 환경을, SaaS는 완성된 응용 사용을 제공한다. 같은 제공자 안에서도 서비스에 따라 보안·설정·데이터 책임이 달라진다.

## 주의점

관리형이라고 백업·복구·접근 권한을 확인하지 않아도 되는 것은 아니다. 비용과 용량·서비스 제한도 관리 대상이다.

## 꼬리질문

1. IaaS에서 관리형 DB로 옮기면 어떤 운영 책임이 줄고 어떤 책임이 남는가?
2. 운영체제 패치 책임이 공급자로 이동해도 데이터·권한 설정 책임은 누구에게 남을까?
3. 서비스별 책임 경계가 일반적인 IaaS·PaaS 표와 다를 수 있다면 무엇을 확인해야 할까?

</details>

## 참고 자료

- [NIST SP 800-145 · Cloud Definition](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 클라우드의 특성과 서비스·배포 모델 정의를 확인한다.
- [AWS · Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — 가용성·보안·성능·운영의 설계 기준을 확인한다.
