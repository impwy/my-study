# 패키지·라이브러리·모듈

> 이름 공간과 배포 묶음, 모듈의 명시적 의존·공개 범위를 구분한다.

- 패키지는 타입의 이름 공간이다.
- JAR은 클래스·자원을 묶는다.
- 모듈은 requires·exports 등 경계를 선언한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

패키지는 같은 이름의 타입 충돌과 접근 범위를 관리한다. 라이브러리는 재사용할 클래스·자원을 배포하며 JAR로 묶을 수 있다. Java 모듈 시스템에서는 module-info로 필요한 모듈과 외부에 공개하는 패키지를 선언한다. 클래스패스 사용과 모듈패스 사용은 같은 규칙으로 모두 동작하지 않으므로 실행·빌드 설정을 구분한다.

## Java 예제

```java
static void inspect(Class<?> type) {
    Module module = type.getModule();
    String pkg = type.getPackageName();
    System.out.println(module.getName());
    System.out.println(module.isExported(pkg));
    System.out.println(module.isOpen(pkg));
} // inspect(String.class): java.base의 java.lang 접근 정책 확인
```

## 주의점

코드 폴더 이름만으로 런타임 모듈 경계가 생기지 않는다. 모듈 시스템과 업무의 DDD 모듈을 구분한다.

## 꼬리질문

1. exports와 리플렉션을 위한 opens의 목적이 다른 이유는?
2. exports된 패키지에 public 클래스가 있다고 private 필드 리플렉션까지 허용될까?
3. 클래스패스의 unnamed module과 이름 있는 module의 접근 경계는 어떻게 다를까?

</details>

## 참고 자료

- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
