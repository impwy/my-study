# 패키지·라이브러리·모듈

> 이름 공간과 배포 묶음, 모듈의 명시적 의존·공개 범위를 구분한다.

- 패키지는 타입의 이름 공간이다.
- JAR은 클래스·자원을 묶는다.
- 모듈은 requires·exports 등 경계를 선언한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

패키지는 같은 이름의 타입 충돌과 접근 범위를 관리한다. 라이브러리는 재사용할 클래스·자원을 배포하며 JAR로 묶을 수 있다. Java 모듈 시스템에서는 module-info로 필요한 모듈과 외부에 공개하는 패키지를 선언한다. 클래스패스 사용과 모듈패스 사용은 같은 규칙으로 모두 동작하지 않으므로 실행·빌드 설정을 구분한다.

## 예제

모듈 A가 B의 공개 패키지 타입을 사용하려면 필요한 읽기 관계와 B의 exports를 확인한다. 리플렉션은 opens 등 별도의 접근 조건이 관련될 수 있다.

## 주의점

코드 폴더 이름만으로 런타임 모듈 경계가 생기지 않는다. 모듈 시스템과 업무의 DDD 모듈을 구분한다.

## 복습 질문

exports와 리플렉션을 위한 opens의 목적이 다른 이유는?

자료 구분: **기존 자료** — Java 강의와 자료구조 노트의 언어·API 개념. **공식 자료 보완** — Java 21 명세·자원 및 참조 계약.

</details>

## 참고 자료

- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
