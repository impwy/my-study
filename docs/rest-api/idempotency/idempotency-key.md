# 멱등 키와 요청 재시도

> 응답이 유실되어 같은 업무 요청을 재시도해도 결과가 중복 생성되지 않도록 요청의 정체성을 저장한다.

- 타임아웃은 실패 확정이 아니다.
- 업무 효과와 결과 기록을 함께 보호한다.
- 같은 키에 다른 내용이 오면 정책이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

클라이언트가 결제 요청을 보냈지만 응답을 못 받았을 때 서버는 이미 처리했을 수 있다. 재시도마다 새 결제를 생성하면 중복 효과가 생긴다. 업무 범위 안에서 멱등 키를 식별하고 처리 중·완료 상태와 결과를 저장해 동일 요청에 일관된 결과를 돌려준다. 중복 방지 기록과 실제 DB 변경은 가능한 한 같은 트랜잭션으로 묶는다. 외부 결제에는 외부 시스템의 멱등성·상태 확인도 필요하다.

## Java 예제

Java HTTP 요청 구성이다. Idempotency-Key는 서버와 합의한 API 계약이며 서버의 원자적 상태 저장을 대신하지 않는다.

```java
import java.net.URI;
import java.net.http.*;

static HttpRequest payment(URI endpoint, String key, String sameBody) {
    return HttpRequest.newBuilder(endpoint)
            .header("Idempotency-Key", key)
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(sameBody))
            .build();
} // 같은 논리 요청의 재시도에는 동일 key와 동일 본문 사용
```

## 주의점

멱등 키 저장소의 만료·충돌·동시 처리와 외부 호출 후 장애를 따로 설계한다. Kafka 프로듀서 멱등성은 업무 결제 중복 방지와 범위가 다르다.

## 꼬리질문

1. 서버가 요청을 처리한 직후 응답 연결이 끊기면 클라이언트는 무엇을 확인해야 하는가?
2. 헤더를 추가하는 것만으로 서버의 중복 업무 효과가 막히지 않는 이유는 무엇일까?
3. 같은 키에 다른 본문을 보내면 서버는 어떤 검증·충돌 응답·보존 기간 정책이 필요할까?

</details>

## 참고 자료

- [RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 메서드·상태 코드·조건부 요청의 의미를 확인한다.
- [Apache Kafka 4.1 · Design](https://kafka.apache.org/41/design/design/) — 로그·복제·전달 보장의 적용 범위를 확인한다.
