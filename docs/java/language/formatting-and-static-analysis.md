# 포매터·린터·정적 분석의 역할

> 코드 형식 통일과 잠재 문제 탐지는 서로 다른 역할이며 자동 도구를 요구사항 검증과 함께 사용한다.

- 포매터는 공백·줄바꿈 등 코드 형식을 맞춘다.
- 린터·정적 분석은 정해진 규칙에 따른 스타일·복잡성·잠재 문제를 찾는다.
- 도구 통과만으로 업무 정합성이나 설계 타당성이 증명되지 않는다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

| 도구 | 주요 역할 |
| --- | --- |
| google-java-format | Java 소스 형식 통일 |
| ktlint | Kotlin 스타일 검사와 지원 규칙의 포맷 수정 |
| detekt | Kotlin 코드 복잡성·잠재 문제 등 정적 분석 |
| [SonarQube](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview) | 코드 품질·보안 관련 정적 분석 |

Java 포매터는 존재하며 IDE 포매터나 google-java-format을 사용할 수 있다. 정적 분석 도구는 코드를 실행하지 않고 규칙에 따라 문제 후보를 찾는다. 같은 “코드 검사”라고 해도 형식 수정과 잠재 결함 탐지는 다르다.

## 주의점

포맷 변경과 동작 변경을 구분하면 리뷰에서 중요한 로직을 찾기 쉽다. 규칙·도구 버전·예외 기준을 팀에서 합의한다. 정적 분석이 통과해도 결제 중복·잘못된 정책·트랜잭션 경계는 별도 테스트와 리뷰가 필요하다. 무료 플랜의 코드량·프로젝트 범위는 바뀔 수 있으므로 특정 무료 한도를 고정된 학습 사실로 외우지 않는다.

## 꼬리질문

1. 포맷 수정과 정적 분석이 서로 다른 검증 목적을 가지는 이유는?
2. AI가 결제 로직과 포맷을 함께 바꿨다면 리뷰에서 중요한 변경을 어떻게 드러낼까?
3. 린터와 정적 분석을 모두 통과해도 요구사항 오류가 남을 수 있는 이유는?

</details>

## 참고 자료

- [google · google-java-format](https://github.com/google/google-java-format) — Java 포매터의 역할과 사용 조건을 확인한다.
- [ktlint](https://github.com/ktlint/ktlint) — Kotlin 린터와 포매터의 기능을 확인한다.
- [detekt](https://detekt.dev/) — Kotlin 정적 분석의 목적과 규칙을 확인한다.
