# 입출력 스트림과 문자 인코딩

> 바이트 전송과 문자 변환을 구분하고 버퍼·인코딩·종료 책임을 명확히 한다.

- InputStream·OutputStream은 바이트를 다룬다.
- Reader·Writer는 문자를 다룬다.
- 읽기 크기와 데이터의 전체 길이는 다를 수 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파일·소켓에서 바이트를 읽고 필요하면 지정한 문자셋으로 문자로 변환한다. 문자와 바이트의 일대일 대응을 가정하면 다중 바이트 문자를 깨뜨릴 수 있다. 버퍼는 시스템 호출 횟수를 줄이는 데 도움을 주지만 flush와 close의 의미가 다르다. read는 요청한 길이보다 적게 읽거나 EOF를 반환할 수 있으므로 남은 범위와 종료 조건을 관리한다.

## 예제

텍스트 파일은 `Files.newBufferedReader(path, StandardCharsets.UTF_8)`처럼 인코딩을 명시한다. 바이너리 이미지에는 문자 Reader를 사용하지 않는다.

## 주의점

flush가 파일의 장애 내구성까지 보장한다고 일반화하지 않는다. 자원은 try-with-resources로 사용 범위에 맞게 닫는다.

## 복습 질문

한글 파일을 잘못된 문자셋으로 읽으면 바이트는 남아 있어도 글자가 깨지는 이유는?

자료 구분: **기존 자료** — Java 강의와 자료구조 노트의 언어·API 개념. **공식 자료 보완** — Java 21 명세·자원 및 참조 계약.

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
