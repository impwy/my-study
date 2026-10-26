# SseEmitter 미디어 타입 인자와 빈 JSON

> 미디어 타입을 전달한 메서드에 따라 이벤트 빌더를 데이터로 직렬화할 수도, 빌더 안의 ChatChunk를 직렬화할 수도 있다.

- **전제:** Spring MVC의 `SseEmitter`와 JSON 메시지 변환기를 사용한다.
- **원리:** `send(builder, JSON)`은 빌더를 데이터로 감싸고, `send(builder)`는 빌더를 풀어서 등록된 데이터를 전송한다.
- **주의:** `data:{}`를 관찰하면 실제 직렬화 대상부터 확인하며, DTO에 getter가 없다고 먼저 단정하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

다음 코드의 두 번째 인자는 `data()`가 아닌 `send()`에 전달된다.

```java
emitter.send(
        SseEmitter.event().name("message").data(new ChatChunk(token)),
        MediaType.APPLICATION_JSON
);
```

인자가 두 개이므로 `send(Object, MediaType)`가 선택된다. 이 메서드는 첫 번째 인자를 새 이벤트의 데이터로 감싼다. 첫 번째 인자는 `ChatChunk`를 보관한 이벤트 빌더다. 따라서 바깥 이벤트의 데이터는 빌더 객체가 되고, JSON 변환기는 빌더를 직렬화한다. 빌더 안의 데이터를 꺼내 이벤트를 만드는 처리를 거치지 않는다.

관찰된 응답은 `data:{}`였다. 출력할 JSON 속성이 없는 객체의 처리 결과는 변환기 설정에 따라 빈 객체 또는 직렬화 예외가 될 수 있다. 핵심은 `ChatChunk` 대신 빌더를 직렬화했다는 점이다.

## 예제

Java 17 이상, Spring MVC와 JSON 메시지 변환기가 필요하다. `emitter`와 `token`은 기존 컨트롤러의 변수다.

```java
public record ChatChunk(String content) {}

emitter.send(
        SseEmitter.event()
                .name("message")
                .data(new ChatChunk(token), MediaType.APPLICATION_JSON)
);
```

이번에는 `data()`가 `ChatChunk`와 JSON 힌트를 함께 보관한다. 인자 하나인 `send(SseEventBuilder)`는 빌더를 풀어서 이벤트 필드와 실제 데이터를 얻는다. 변환기는 `ChatChunk.content`를 읽으므로 `token`이 `"안녕하세요"`일 때 다음을 전송한다.

```text
event:message
data:{"content":"안녕하세요"}

```

전체 응답의 `Content-Type: text/event-stream`과 데이터 직렬화 힌트인 `APPLICATION_JSON`은 역할이 다르다. 응답 문자 인코딩은 [SSE 응답 인코딩](sse-response-encoding.md), 조각을 묶는 기준은 [SSE 전송 단위](sse-stream-buffering.md)를 참고한다.

## 주의점

`APPLICATION_JSON` 자체가 빈 값을 만드는 옵션은 아니다. 미디어 타입을 생략해서 동작했다면, 인자를 추가하면서 호출한 오버로드와 괄호 위치가 바뀌었는지 먼저 확인한다. record 선언을 임의로 수정하기 전에 전송한 객체의 실제 타입을 추적한다.

## 꼬리질문

1. `send(builder, APPLICATION_JSON)`을 호출하면 실제 JSON 변환 대상은 무엇이며, 그 객체는 어떻게 이벤트 데이터가 되는가?
2. `public record ChatChunk(String content) {}`가 있는데도 `data:{}`가 나오면 호출 코드의 어느 괄호를 먼저 확인할 것인가?
3. 빌더의 JSON 직렬화 결과가 `{}` 대신 예외가 되더라도 메서드 선택에 관한 원인 설명은 왜 유지되는가?

</details>

## 참고 자료

- [Spring SseEmitter 구현](https://github.com/spring-projects/spring-framework/blob/v7.0.0/spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/SseEmitter.java) — 두 send 오버로드와 빌더의 데이터 보관 과정을 추적한다.
- [Spring ResponseBodyEmitterReturnValueHandler 구현](https://github.com/spring-projects/spring-framework/blob/v7.0.0/spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/ResponseBodyEmitterReturnValueHandler.java) — 실제 데이터 타입과 미디어 타입으로 변환기를 고르는 과정을 확인한다.
