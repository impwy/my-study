# SSE의 조각 묶기와 전체 답변 전송

> Flux에서 언제 값을 내보내고 send를 호출하는지에 따라 조각별 전송과 전체 답변 전송이 결정된다.

- **전제:** AI 서비스가 `Flux<String>`으로 응답 조각을 내보낸다. 한 조각이 반드시 한 글자나 한 문장은 아니다.
- **원리:** `bufferUntil()`은 조건이 맞는 조각까지 묶고, `collectList()`는 원본 스트림이 정상 종료될 때 전체 목록을 내보낸다.
- **주의:** 버퍼링하면 첫 표시가 늦어진다. 전송 단위와 화면에서 문자열을 누적하는 방식은 각각 정한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

각 조각을 받을 때마다 `emitter.send()`를 호출하면 작은 SSE 이벤트가 연속으로 전송된다. `bufferUntil()`로 문자열 조각을 모은 뒤 합치면 전송 횟수가 줄어든다. `collectList()`는 원본의 완료 신호가 올 때까지 값을 보관하므로 완성된 답변 하나를 만들 수 있다.

처리 흐름은 `Flux<String>` → `Mono<List<String>>` → `Mono<String>`이다. 이 `Mono<String>`의 값을 받아 `send()`를 한 번 호출하면 전체 답변을 담은 이벤트 하나를 전송한다. 실제 send 호출의 올바른 형태는 [SseEmitter 미디어 타입](sse-emitter-media-type.md)을 참고한다.

## 예제

Reactor Core가 필요하다. 다음 코드는 연산자 동작을 설명하는 작은 입력 예다.

```java
Flux<String> grouped = Flux.just("안", "녕", "하세요", ".", " 반갑습니다", ".")
        .bufferUntil(chunk ->
                chunk.contains(".") || chunk.contains("?")
                        || chunk.contains("!") || chunk.contains("\n"))
        .map(chunks -> String.join("", chunks));
```

첫 결과는 `안녕하세요.`, 다음 결과는 ` 반갑습니다.`다. 조건을 충족한 조각도 현재 버퍼에 포함된다. 정상 종료 시 남은 버퍼도 내보내지만 오류 종료 시 미완성 버퍼를 내보내지는 않는다.

```java
Mono<String> fullAnswer = productChatService.chatStream(message, userId)
        .collectList()
        .map(chunks -> String.join("", chunks));
```

원본 서비스가 정상 종료돼야 전체 답변이 전달된다. 원본이 끝나지 않으면 계속 기다리고, 오류나 취소가 발생하면 부분 답변 목록은 전달되지 않는다.

## 주의점

마침표·물음표·느낌표·줄바꿈을 찾는 코드는 문법적인 문장 분석기가 아니다. 소수점이나 URL에도 반응하고, 한 조각에 여러 문장이 있어도 그 조각을 내부에서 나누지는 않는다. 정확한 문장 경계가 필요하면 누적 문자열에서 경계를 찾고 남은 꼬리를 관리하는 처리가 필요하다.

화면에서 이어진 답변으로 보이기만 하면 되는 경우에는 작은 이벤트를 유지한 채 클라이언트가 `content`를 누적해 표시할 수 있다. 전체 답변을 한 번만 반환한다면 일반 HTTP JSON 응답도 선택할 수 있다. SSE와 WebSocket 어느 쪽도 자동으로 문장을 묶어 주지는 않는다.

## 꼬리질문

1. `collectList()` 뒤의 구독 콜백은 마지막 조각이 도착했을 때와 원본이 정상 종료됐을 때 중 언제 실행되는가?
2. 한 조각이 `첫 문장. 둘째 문장.`이면 `bufferUntil()`은 왜 이벤트 두 개를 만들지 않는가?
3. 생성 중 오류가 날 때까지의 답변을 보여 줘야 한다면 전체를 모으는 설계와 조각별 전송 중 무엇을 선택할 것인가?

</details>

## 참고 자료

- [Reactor Flux API](https://projectreactor.io/docs/core/3.7.17/api/reactor/core/publisher/Flux.html) — bufferUntil과 collectList의 완료·오류·취소 동작을 확인한다.
- [Reactor의 배치 처리 연산자](https://projectreactor.io/docs/core/release/reference/advancedFeatures/advanced-three-sorts-batching.html) — 버퍼를 생성하고 닫는 기준을 비교한다.
