# 바운디드 컨텍스트

> 한 모델과 용어가 일관된 의미를 갖는 경계를 정하고 경계 사이의 번역을 설계한다.

- 같은 이름도 컨텍스트에 따라 다를 수 있다.
- 경계는 업무 책임과 언어를 기준으로 정한다.
- 컨텍스트와 배포 서비스는 일대일이 아니다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

결제의 고객은 결제 수단·청구 정보가 중요하고 커뮤니티의 회원은 프로필·활동 상태가 중요하다. 두 모델을 강제로 하나로 만들면 서로 다른 변경 이유가 엮인다. 경계 사이에는 공개 계약과 변환 규칙을 두고 상대의 모델이 자신의 내부 모델로 그대로 번지는 것을 제한한다. 작은 앱에서도 모듈 경계로 먼저 구현할 수 있다.

## Java 예제

```java
record BillingCustomer(long id, String invoiceAddress) {}

record SupportCustomer(long id, String preferredChannel) {}

record CustomerRegistered(long id, String channel) {}

static SupportCustomer translate(CustomerRegistered event) {
    return new SupportCustomer(event.id(), event.channel());
}
```

## 주의점

모든 컨텍스트를 즉시 마이크로서비스로 분리하지 않는다. 업무 경계를 모르는 상태의 물리 분리는 통신 비용만 늘릴 수 있다.

## 꼬리질문

1. 같은 회원 ID를 사용하는 두 모델을 서로 다른 컨텍스트로 둘 수 있는 이유는?
2. 같은 id를 가진 두 Customer가 서로 다른 필드를 가져도 모순이 아닌 이유는 무엇일까?
3. 외부 컨텍스트의 모델을 그대로 공유하는 대신 번역 경계를 두면 어떤 변경 전파를 줄일까?

</details>

## 참고 자료

- [Eric Evans · DDD Reference](https://www.domainlanguage.com/ddd/reference/) — 엔티티·값 객체·애그리거트·컨텍스트의 원래 정의를 확인한다.
- [Alistair Cockburn · Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — 포트·어댑터로 외부 기술을 분리하는 원래 의도를 읽는다.
