# 예외와 자원 정리

> 실패를 호출자에게 전달하는 경로와 파일·연결을 닫는 경로를 함께 설계한다.

- checked 예외는 처리 또는 선언이 필요하다.
- try-with-resources는 AutoCloseable을 정리한다.
- 예외를 삼키면 실패가 성공처럼 보인다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

예외가 발생하면 정상 흐름을 중단하고 맞는 catch를 찾으며 호출 스택을 거슬러 올라간다. RuntimeException과 Error 계열은 checked 예외 처리 의무의 대상이 아니다. try-with-resources는 생성에 성공한 자원을 역순으로 닫는다. 본문 실패와 close 실패가 함께 일어나면 닫기 실패가 suppressed 예외로 남을 수 있다. 복구할 수 없다면 문맥을 추가하고 원인을 보존해 전달한다.

## 예제

파일 처리에는 `try (var reader = Files.newBufferedReader(path)) { /* 읽기 */ }`처럼 사용 범위를 묶는다. 실패 로그를 남겼다는 이유로 빈 결과를 반환하지 않는다.

## 주의점

finally에서 return하거나 새 예외를 던지면 원래 결과·예외를 가릴 수 있다. DB 연결은 풀에 반환되는 close의 의미도 확인한다.

## 복습 질문

파일 읽기와 close가 동시에 실패하면 어떤 예외가 우선 남는가?

자료 구분: **기존 자료** — Java 강의와 자료구조 노트의 언어·API 개념. **공식 자료 보완** — Java 21 명세·자원 및 참조 계약.

</details>

## 참고 자료

- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
