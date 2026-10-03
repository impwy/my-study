# RDS Multi-AZ와 읽기 복제본

> 관리형 DB의 장애 대비와 읽기 확장을 구분하고 실제 배포 방식의 동작을 확인한다.

- Multi-AZ는 가용성 목적의 구성이다.
- 읽기 복제본은 읽기 분산에 사용할 수 있다.
- 복제 지연과 복구 시간을 고려한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

RDS는 엔진 운영 일부를 관리하지만 스키마·쿼리·접근·복구 설계는 사용자 책임으로 남는다. Multi-AZ와 읽기 복제본은 목적이 다르며, 전통적인 Multi-AZ DB 인스턴스의 standby를 일반 읽기 확장 서버로 가정하면 안 된다. 다른 Multi-AZ 클러스터·Aurora 배포는 구성과 읽기 방식이 다르므로 제품별로 확인한다.

## 주의점

복제는 실수로 삭제한 데이터도 전달할 수 있으므로 백업과 다르다. 장애 전환 시간 동안의 재연결·재시도도 검토한다.

## 꼬리질문

1. 가용성을 위한 standby와 읽기 확장을 위한 replica를 구분해야 하는 이유는?
2. DB 인스턴스 장애 전환이 끝나도 애플리케이션의 기존 연결을 다시 확인해야 하는 이유는 무엇일까?
3. 쓰기 직후 replica에서 조회한 결과가 오래된 상태라면 어떤 일관성 정책이 필요할까?

</details>

## 참고 자료

- [AWS · RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) — 관리형 DB·Multi-AZ·읽기 복제본의 목적을 확인한다.
