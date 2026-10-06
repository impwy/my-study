# EC2·AMI·블록 스토리지

> EC2 인스턴스는 백엔드를 실행하는 가상 서버이고, AMI와 저장 볼륨은 시작 구성과 데이터 수명을 담당한다.

- **실행:** 각 인스턴스에서 백엔드를 실행하며 CPU·메모리·네트워크 요구에 맞는 유형을 고른다.
- **저장:** EBS와 instance store의 수명이 다르다.
- **접근:** VPC·보안 그룹·IAM 역할·관리 접속 방법을 함께 설정한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

EC2 인스턴스는 AWS에서 제공하는 가상 컴퓨터다. Spring Boot 백엔드를 운영한다면 Java 실행 환경을 준비하고 빌드한 실행 가능한 JAR를 전달해 실행할 수 있다. 각 인스턴스는 시작·중지·종료와 배포를 개별적으로 관리하며, 자신이 배치된 VPC의 네트워크를 사용한다. 프로그램 실행과 서버 운영은 EC2에서, 통신 경로 관리는 VPC에서 담당한다.

빌드는 소스 코드를 실행 가능한 산출물로 만드는 작업이고, 배포는 그 산출물을 실행 서버에 전달해 서비스에 반영하는 작업이다. GitHub 호스팅 러너를 사용하면 GitHub Actions에서 테스트·빌드한 JAR를 EC2로 배포할 수 있다. 빌드 성공만으로 EC2의 서비스가 업데이트되지는 않는다.

AMI에는 인스턴스를 시작하는 OS·소프트웨어 구성과 저장 매핑 정보가 있다. 인스턴스가 실행되는 동안의 컴퓨팅 수명과 EBS 볼륨의 수명은 설정에 따라 달라진다. instance store는 인스턴스와 연결된 임시 저장소다. 중단·종료·장애에서 데이터가 어떻게 남는지 따로 확인하고 필요한 백업을 만든다.

EC2에서 S3를 사용할 때는 필요한 버킷 작업을 허용하는 IAM 역할을 인스턴스에 연결할 수 있다. AWS SDK가 임시 자격 증명을 사용하도록 구성하면 애플리케이션 코드에 장기 비밀 키를 넣지 않아도 된다.

## 주의점

인스턴스 중단과 종료는 다르다. 실행 중지 후에도 남는 저장 자원의 수명과 요금 정책은 따로 확인한다. 배포할 때 서버 로컬 파일을 교체하거나 인스턴스를 새로 만드는 경우, 사용자 첨부파일이 어떻게 보존되는지도 확인한다.

## 꼬리질문

1. VPC·EC2·AMI·EBS는 각각 네트워크, 실행, 시작 구성, 저장에서 어떤 역할을 할까?
2. GitHub Actions에서 JAR 빌드가 성공했는데 서비스가 이전 버전이라면 배포·재시작·실행 버전에서 무엇을 확인할까?
3. 인스턴스를 종료한 뒤 데이터를 유지하려면 DeleteOnTermination과 백업에서 무엇을 확인해야 할까?

함께 복습: [VPC 서브넷·라우팅·보안](../vpc/subnets-routes-security.md) · [IAM 역할과 정책](../iam/roles-and-policies.md) · [배포 권한·상태 확인·롤백](../../github-actions/cd/deployment-oidc-and-rollback.md)

</details>

## 참고 자료

- [AWS · EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) — 인스턴스·AMI·스토리지·보안 그룹의 역할을 확인한다.
- [AWS · Preserve data when an instance is terminated](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preserving-volumes-on-termination.html) — instance store와 EBS의 종료 시 데이터 보존 조건을 확인한다.
- [AWS · IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) — 인스턴스에서 AWS API에 접근하는 임시 자격 증명 방식을 확인한다.
