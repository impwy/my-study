# SSE 응답의 UTF-8 인코딩과 브라우저 표시

> 개발자도구에서는 한글이 정상인데 직접 연 화면에서 깨진다면 실제 응답 헤더와 문서 디코딩을 함께 확인한다.

- **전제:** SSE의 이벤트 스트림은 UTF-8이며 `EventSource`는 UTF-8로 디코딩한다.
- **원리:** 같은 바이트도 다른 문자 인코딩으로 읽으면 다른 문자가 되므로 전송 바이트와 표시 과정의 해석을 구분한다.
- **주의:** SSE의 `charset`은 선택 사항이다. 생략됐다는 사실만으로 서버가 잘못된 SSE를 보냈다고 단정하지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

Chrome 개발자도구에서는 `{"content":"앞"}`이 보이는데, SSE URL을 주소창에서 직접 열면 `{"content":"ì•ž"}`로 보이는 증상을 관찰했다. 실제 응답 헤더는 `Content-Type: text/event-stream`이었고 `charset`이 없었다.

`앞`의 UTF-8 바이트는 `EC 95 9E`다. 이 바이트를 Windows-1252로 읽으면 `ì•ž`가 된다. 따라서 관찰된 증상은 문서 표시 과정에서 인코딩을 다르게 해석한 패턴과 일치한다. 당시 Chrome의 `document.characterSet` 값은 확인되지 않았으므로 브라우저가 선택한 인코딩 자체를 측정한 것으로 기록하지 않는다.

주소창에서 응답을 문서로 보는 경로와 `EventSource`로 SSE를 수신하는 경로는 구분한다. 후자는 표준에 따라 UTF-8을 사용한다. 일반 문서 표시에서는 명시적인 인코딩 정보가 없을 때 추정이 개입할 수 있다.

## 예제

Spring MVC의 기존 메서드에서 `ResponseEntity<SseEmitter>`를 반환하는 예다. 첫 본문이 전송되기 전에 다음 응답 헤더를 정한다.

```java
return ResponseEntity.ok()
        .contentType(MediaType.parseMediaType(
                "text/event-stream;charset=UTF-8"))
        .body(emitter);
```

원래 `SseEmitter` 반환 타입을 사용할 경우에는 메서드 인자로 받은 `HttpServletResponse`에 먼저 설정할 수도 있다. 두 방법 중 하나를 사용한다.

```java
response.setContentType("text/event-stream;charset=UTF-8");
```

서버를 다시 실행한 뒤 새 요청의 Response Headers에 `charset=UTF-8`이 있는지 확인하고 화면의 한글과 비교한다. Console의 `document.characterSet`도 표시 인코딩을 확인하는 단서다. 실제 전송 바이트도 UTF-8이어야 하며, 헤더만으로 이미 깨진 문자열이 복구되지는 않는다.

## 주의점

위 설정은 원인 분석에 맞춘 수정안이다. 당시 수정 후 화면이 정상화됐다는 확인 결과는 확보하지 않았으므로 해결 완료로 기록하지 않는다. `Transfer-Encoding: chunked`는 HTTP/1.1 본문 전송 방식이며 문자 인코딩 지정과 역할이 다르다. `data:{}`는 [직렬화 대상과 오버로드](sse-emitter-media-type.md)를 별도로 조사한다.

## 꼬리질문

1. 같은 `EC 95 9E` 바이트가 `앞`과 `ì•ž`로 보일 수 있는 이유는 무엇인가?
2. 개발자도구만 정상인 SSE 응답을 조사할 때 Response Headers와 `document.characterSet`을 어떤 순서로 비교할 것인가?
3. 서버에서 이미 잘못 만들어진 문자열을 UTF-8로 전송했다면 `charset=UTF-8`을 추가하는 것만으로 복구할 수 있는가?

</details>

## 참고 자료

- [WHATWG SSE 표준](https://html.spec.whatwg.org/multipage/server-sent-events.html) — EventSource의 UTF-8 디코딩과 이벤트 파싱 규칙을 확인한다.
- [W3C HTTP charset 설명](https://www.w3.org/International/articles/http-charset/index.en) — 문서 응답의 문자 인코딩 표시와 브라우저의 해석을 이해한다.
- [text/event-stream 미디어 타입 정의](https://html.spec.whatwg.org/multipage/iana.html#text/event-stream) — charset이 선택 사항이며 지정한다면 UTF-8이어야 한다는 조건을 확인한다.
