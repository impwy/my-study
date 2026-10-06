# AWS

[전체 목록](../../README.md)

## IAM

| 문서 | 한 줄 요약 |
| --- | --- |
| [IAM 역할과 정책](iam/roles-and-policies.md) | AWS 자원 접근은 주체·정책·조건으로 판단하고 장기 키 대신 적절한 임시 자격 증명을 사용한다. |

## VPC

| 문서 | 한 줄 요약 |
| --- | --- |
| [VPC 서브넷·라우팅·보안](vpc/subnets-routes-security.md) | VPC는 서버를 배치하는 가상 네트워크이며, 서브넷·경로·보안 규칙으로 통신 가능 범위를 정한다. |

## EC2

| 문서 | 한 줄 요약 |
| --- | --- |
| [EC2·AMI·블록 스토리지](ec2/instance-ami-storage.md) | EC2 인스턴스는 백엔드를 실행하는 가상 서버이고, AMI와 저장 볼륨은 시작 구성과 데이터 수명을 담당한다. |

## S3

| 문서 | 한 줄 요약 |
| --- | --- |
| [S3 객체와 저장소 선택](s3/object-storage.md) | S3는 파일을 객체 키로 저장하는 서비스이며, 백엔드는 DB에 파일 식별자를 기록하고 권한에 따라 파일 접근을 제공할 수 있다. |

## RDS

| 문서 | 한 줄 요약 |
| --- | --- |
| [RDS Multi-AZ와 읽기 복제본](rds/multi-az-and-read-replica.md) | 관리형 DB의 장애 대비와 읽기 확장을 구분하고 실제 배포 방식의 동작을 확인한다. |

## 로드밸런싱·모니터링

| 문서 | 한 줄 요약 |
| --- | --- |
| [CloudWatch와 CloudTrail](operations/monitoring-and-audit.md) | 운영 지표·로그를 통한 상태 관찰과 AWS API 활동 감사를 구분한다. |
| [RTO·RPO와 복구 검증](operations/rto-rpo-and-backup.md) | 허용 중단 시간과 데이터 손실 범위를 정하고 백업에서 실제 복구되는지 확인한다. |
| [로드밸런싱과 Auto Scaling](operations/load-balancing-and-autoscaling.md) | 트래픽 분산과 인스턴스 수 조정을 결합하되 상태·용량·준비 시간을 함께 설계한다. |

