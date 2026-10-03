# 클라우드 연결 경로와 아웃바운드 통신

> 연결 문제는 DNS·라우팅·접근 제어·서버 대기 상태를 경로 순서대로 확인한다.

- 이름 해석 성공은 연결 성공을 보장하지 않는다.
- 라우트와 방화벽 규칙은 서로 다른 조건이다.
- NAT는 주로 내부에서 시작한 외부 연결의 응답 경로를 제공한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

서비스를 호출할 때 먼저 이름을 IP로 해석하고, 목적지로 가는 경로를 선택하며, 접근 제어를 통과한 뒤 대상 포트에 연결한다. HTTP·TLS 문제는 연결 이후에도 발생할 수 있다. 애플리케이션 로그 하나만 보고 모든 실패를 “네트워크 오류”로 묶으면 원인을 좁히기 어렵다.

인터넷으로 나가는 경로와 내부 서비스 간 경로를 따로 그린다. AWS의 프라이빗 서브넷은 퍼블릭 NAT 게이트웨이 등을 통해 외부로 요청을 시작할 수 있다. NAT가 있다고 외부에서 내부 서버로 새 연결을 직접 시작할 수 있는 것은 아니다.

## Java 예제

Java 11 이상에서 실행할 수 있다. request에는 접근 권한이 있는 실제 테스트 URL을 전달한다.

```java
static void request(java.net.URI uri) throws Exception {
    var client =
            java.net.http.HttpClient.newBuilder()
                    .connectTimeout(java.time.Duration.ofSeconds(3))
                    .build();
    var request =
            java.net.http.HttpRequest.newBuilder(uri)
                    .timeout(java.time.Duration.ofSeconds(5))
                    .GET()
                    .build();
    var response = client.send(request, java.net.http.HttpResponse.BodyHandlers.discarding());
    System.out.println(response.statusCode());
}
```

## 주의점

타임아웃만으로 차단 지점이 확정되지는 않는다. DNS 설정, 라우팅, 보안 그룹·네트워크 ACL, 리스너, TLS 로그를 함께 확인한다. 연결 타임아웃과 개별 요청 타임아웃도 구별한다.

## 꼬리질문

1. DNS가 성공하는데 TCP 연결이 타임아웃이라면 다음에 어느 구간을 확인할까?
2. 프라이빗 서버가 외부 API를 호출할 수 있는데 외부에서는 접속할 수 없는 이유는 무엇일까?
3. TCP 연결이 되는데 TLS가 실패한다면 라우트 수정 전에 무엇을 확인할까?

</details>

## 참고 자료

- [AWS · VPC 동작 원리](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) — 서브넷·라우팅·인터넷 연결을 경로 관점으로 읽는다.
- [AWS · NAT 게이트웨이](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) — 내부에서 시작한 외부 연결과 응답 경로를 확인한다.
