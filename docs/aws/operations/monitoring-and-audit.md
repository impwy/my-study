# CloudWatch와 CloudTrail

> 운영 지표·로그를 통한 상태 관찰과 AWS API 활동 감사를 구분한다.

- 메트릭·로그·알람을 연결한다.
- CloudTrail은 API 활동 추적에 사용한다.
- 지표와 업무 성공을 함께 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

CloudWatch의 메트릭·로그·알람은 자원 사용과 앱의 지연·오류 등 운영 상태를 관찰하게 한다. CloudTrail은 AWS 계정의 API 활동을 추적하는 데 쓰인다. CPU 급증을 찾는 질문과 누가 정책을 변경했는지 찾는 질문은 서로 다른 관측 자료를 요구한다. 로그에는 요청·이벤트 식별자를 두어 여러 서비스의 흐름을 연결하되 개인 정보와 비밀 값은 제한한다.

## 예제

오류율 상승은 앱 로그·DB 연결·배포 시점으로 좁히고, 보안 그룹 변경은 API 감사 이력에서 확인한다. 알람에는 조치 방법과 담당 범위를 연결한다.

## 주의점

메트릭 수집이 없던 과거를 항상 복원할 수는 없다. 알람 임계값·보존 기간·권한을 운영 요구에 맞춘다.

## 복습 질문

서비스가 느려진 원인과 누가 접근 정책을 바꿨는지에 같은 로그만 쓰기 어려운 이유는?

자료 구분: **기존 자료** — AWS 강의의 자원·운영 개념. **공식 자료 보완** — 현재 공식 문서의 서비스별 책임·구성 조건.

</details>

## 참고 자료

- [AWS · CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) — 메트릭·로그·알람의 목적과 수집 방식을 확인한다.
- [AWS · CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) — API 활동 감사와 기록 범위를 확인한다.
