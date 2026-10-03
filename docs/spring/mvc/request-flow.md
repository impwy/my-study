# Spring MVC 요청 처리

> DispatcherServlet은 요청을 적절한 핸들러에 연결하고 입력·결과 변환과 오류 처리를 조정한다.

- Controller는 HTTP 경계를 담당한다.
- 검증·메시지 변환과 도메인 규칙을 구분한다.
- 업무 처리는 애플리케이션·도메인으로 옮긴다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

요청이 들어오면 매핑 정보로 핸들러를 찾고 인자 해석·검증을 거쳐 실행한다. 응답은 반환 형태에 따라 뷰 처리 또는 HttpMessageConverter를 통한 본문 변환으로 이어진다. 예외 처리기는 오류를 HTTP 계약으로 바꿀 수 있다. 입력 DTO의 형식 검증과 “이미 사용한 쿠폰은 다시 쓸 수 없다” 같은 도메인 불변식은 서로 다른 책임이다.

## Java 예제

Spring MVC와 Jakarta Validation 구현체가 필요하다. 실제 주문 저장은 예제에서 생략한다.

```java
import jakarta.validation.Valid;
import jakarta.validation.constraints.Positive;

import org.springframework.web.bind.annotation.*;

record OrderRequest(@Positive int quantity) {}

@RestController
static class Orders {
    @PostMapping("/orders")
    String create(@Valid @RequestBody OrderRequest request) {
        return "quantity=" + request.quantity();
    }
}
```

## 주의점

JSON 요청의 @RequestBody와 폼·쿼리 인자 바인딩을 혼동하지 않는다. 클라이언트 검증만으로 서버 검증을 대체하지 않는다.

## 꼬리질문

1. 필수 필드 검증과 재고 소진 검사를 서로 다른 곳에 두는 이유는?
2. JSON 파싱과 @Valid 검증 중 어느 단계가 먼저이며 각각 실패하면 무엇을 확인할까?
3. 양수 검증을 통과한 주문도 재고가 부족할 수 있는데 이 검사는 어느 계층에 둘까?

</details>

## 참고 자료

- [Spring · Web MVC](https://docs.spring.io/spring-framework/reference/web/webmvc.html) — 요청 매핑·검증·예외 처리가 실행되는 흐름을 확인한다.
- [RFC 9110 · HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 메서드·상태 코드·조건부 요청의 의미를 확인한다.
