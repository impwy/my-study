# 도메인 모델과 유비쿼터스 언어

> 업무의 개념·규칙을 팀이 함께 쓰는 언어와 모델로 표현한다.

- 도메인 모델은 테이블 목록 이상이다.
- 용어의 의미와 규칙을 함께 합의한다.
- 불변식은 모델의 행동으로 보호한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

업무 전문가와 개발자가 같은 단어를 다른 뜻으로 쓰면 구현의 불일치가 생긴다. 주문·발급·사용·취소의 의미와 가능한 상태 전이를 대화·테스트·코드에서 일관되게 사용한다. 모델은 실제 업무의 모든 세부를 복제하는 대신 문제 해결에 필요한 개념과 규칙을 선택한다. 단순 CRUD 영역에 모든 패턴을 적용하기보다 복잡한 핵심 규칙에 집중한다.

## Java 예제

```java
enum SubscriptionState {
    ACTIVE,
    CANCELLED
}

static class Subscription {
    SubscriptionState state = SubscriptionState.ACTIVE;

    void cancel() {
        if (state != SubscriptionState.ACTIVE) throw new IllegalStateException("이미 취소됨");
        state = SubscriptionState.CANCELLED;
    }
}
```

## 주의점

DDD는 프레임워크나 폴더 이름으로 완성되지 않는다. 모델과 용어는 새 업무 이해에 따라 계속 조정한다.

## 꼬리질문

1. 같은 “회원”이라는 단어의 의미가 팀마다 다르면 어떤 구현 문제가 생기는가?
2. cancel이라는 업무 용어를 모델 메서드로 표현하면 단순 상태 setter보다 무엇을 드러낼까?
3. 기획·운영·개발이 ACTIVE를 다르게 해석하면 상태 전이와 테스트에 어떤 문제가 생길까?

</details>

## 참고 자료

- [Eric Evans · DDD Reference](https://www.domainlanguage.com/ddd/reference/) — 엔티티·값 객체·애그리거트·컨텍스트의 원래 정의를 확인한다.
