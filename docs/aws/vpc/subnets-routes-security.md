# VPC 서브넷·라우팅·보안

> 서브넷의 위치와 경로, 보안 그룹·네트워크 ACL을 구분해 연결 가능성을 판단한다.

- 서브넷은 가용 영역에 속한다.
- public·private은 경로와 연결 조건으로 판단한다.
- 보안 그룹과 NACL의 상태 처리 방식이 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

VPC는 논리적으로 분리한 네트워크이고 서브넷의 라우팅 테이블은 목적지에 따른 다음 경로를 정한다. 인터넷 게이트웨이 경로가 있는 서브넷에서도 인스턴스의 주소·보안·OS 방화벽 조건이 갖춰져야 인터넷 접근이 된다. 보안 그룹은 상태 기반 허용 규칙을, NACL은 서브넷 경계의 별도 규칙을 사용한다. NAT는 private 자원의 외부 시작 연결을 지원하는 선택지다.

## Java 예제

AWS SDK for Java 2.x ec2 모듈. 라우트 조회만으로 접근 가능 여부 전체가 판정되지는 않는다.

```java
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeRouteTablesRequest;

static void routes(Ec2Client ec2, String routeTableId) {
    var response =
            ec2.describeRouteTables(
                    DescribeRouteTablesRequest.builder().routeTableIds(routeTableId).build());
    response.routeTables()
            .forEach(
                    t ->
                            t.routes()
                                    .forEach(
                                            r ->
                                                    System.out.println(
                                                            r.destinationCidrBlock()
                                                                    + ":"
                                                                    + r.gatewayId()
                                                                    + ":"
                                                                    + r.natGatewayId())));
}
```

## 주의점

NAT 게이트웨이는 외부에서 임의로 내부 앱에 들어오는 공개 진입점이 아니다. 0.0.0.0/0 경로가 있다고 모든 포트가 자동 허용되는 것은 아니다.

## 꼬리질문

1. 인터넷 게이트웨이 경로가 있어도 접속이 안 되면 어떤 조건을 더 확인할까?
2. 0.0.0.0/0이 인터넷 게이트웨이를 가리켜도 인스턴스에 공인 IP가 없으면 무엇이 달라질까?
3. 라우팅이 정상인데 연결이 실패하면 보안 그룹·NACL·서버 리스닝 중 무엇을 순서대로 확인할까?

</details>

## 참고 자료

- [AWS · VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) — 서브넷·라우팅·보안 그룹·연결의 역할을 확인한다.
- [Java API 사용 안내](https://docs.aws.amazon.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html) — Java에서 라우팅 테이블을 조회하는 요청·응답 API를 확인한다.
