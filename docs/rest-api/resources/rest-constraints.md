# REST의 제약과 리소스

> REST는 리소스에 대한 통일된 인터페이스와 여러 제약으로 분산 시스템의 상호작용을 설계하는 스타일이다.

- 클라이언트·서버와 무상태 제약을 구분한다.
- 캐시·계층화·통일된 인터페이스가 핵심이다.
- JSON과 CRUD만으로 REST를 설명하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

리소스는 URL로 식별하고 표현을 전달해 상태와 상호작용한다. 통일된 인터페이스에는 리소스 식별, 표현을 통한 조작, 자기 서술적 메시지, 애플리케이션 상태의 엔진으로서 하이퍼미디어가 포함된다. 무상태 제약은 각 요청을 이해하는 데 필요한 문맥을 요청이 제공한다는 뜻이다. 서버가 영속 데이터를 저장하지 못한다는 의미는 아니다. 모든 API가 이 제약을 완전히 충족하는 것은 아니다.

## Java 예제

Spring MVC. 인증·인가와 실제 조회를 연결하기 전의 자원 표현 예제다.

```java
import org.springframework.web.bind.annotation.*;

record OrderView(long id, String status) {}

@RestController
static class Orders {
    @GetMapping("/orders/{id}")
    OrderView get(@PathVariable("id") long id) {
        return new OrderView(id, "CREATED");
    }
}
```

## 주의점

실용적인 HTTP JSON API를 REST라고 부르는 관행과 논문의 제약 정의를 구분한다. 이름보다 선택한 제약의 설계 효과를 설명한다.

## 꼬리질문

1. 서버가 주문 DB를 보유하는 것과 REST의 무상태 제약은 왜 모순되지 않는가?
2. GET /orders/{id}가 자원 표현을 반환하는 것과 서버가 대화별 세션 상태를 요구하는 것은 어떻게 다를까?
3. 이 URI와 JSON만으로 REST의 모든 제약을 충족했다고 말하려면 어떤 제약을 더 확인해야 할까?

</details>

## 참고 자료

- [Fielding · REST 논문 5장](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) — REST의 제약 조건과 그 설계 효과를 원문에서 확인한다.
- [RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 메서드·상태 코드·조건부 요청의 의미를 확인한다.
