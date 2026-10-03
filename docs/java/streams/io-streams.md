# 입출력 스트림과 문자 인코딩

> 바이트 전송과 문자 변환을 구분하고 버퍼·인코딩·종료 책임을 명확히 한다.

- InputStream·OutputStream은 바이트를 다룬다.
- Reader·Writer는 문자를 다룬다.
- 읽기 크기와 데이터의 전체 길이는 다를 수 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파일·소켓에서 바이트를 읽고 필요하면 지정한 문자셋으로 문자로 변환한다. 문자와 바이트의 일대일 대응을 가정하면 다중 바이트 문자를 깨뜨릴 수 있다. 버퍼는 시스템 호출 횟수를 줄이는 데 도움을 주지만 flush와 close의 의미가 다르다. read는 요청한 길이보다 적게 읽거나 EOF를 반환할 수 있으므로 남은 범위와 종료 조건을 관리한다.

## Java 예제

```java
import java.io.*;
import java.nio.charset.StandardCharsets;

static String decode(byte[] data) throws IOException {
    try (var reader =
            new BufferedReader(
                    new InputStreamReader(
                            new ByteArrayInputStream(data), StandardCharsets.UTF_8))) {
        return reader.readLine();
    }
} // decode("안녕".getBytes(StandardCharsets.UTF_8)) → "안녕"
```

## 주의점

flush가 파일의 장애 내구성까지 보장한다고 일반화하지 않는다. 자원은 try-with-resources로 사용 범위에 맞게 닫는다.

## 꼬리질문

1. 한글 파일을 잘못된 문자셋으로 읽으면 바이트는 남아 있어도 글자가 깨지는 이유는?
2. InputStream과 Reader는 각각 어떤 단위로 입력을 해석할까?
3. 다른 문자셋으로 잘못 디코딩한 문자열을 다시 저장하면 원본 바이트를 항상 복구할 수 있을까?

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
