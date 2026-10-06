# Java

[전체 목록](../../README.md)

## 언어·타입

| 문서 | 한 줄 요약 |
| --- | --- |
| [JDBC 연결과 트랜잭션](language/jdbc-boundary.md) | SQL 실행·값 바인딩·결과 처리·트랜잭션·연결 반환의 경계를 관리한다. |
| [기본형·참조형과 값 전달](language/value-and-reference.md) | Java는 기본형 값과 객체 참조 값을 모두 복사해서 메서드에 전달한다. |
| [제어 흐름과 배열](language/control-flow-and-arrays.md) | 조건·반복으로 실행 경로를 정하고 배열의 길이와 인덱스 경계를 지킨다. |
| [패키지·라이브러리·모듈](language/packages-and-modules.md) | 이름 공간과 배포 묶음, 모듈의 명시적 의존·공개 범위를 구분한다. |
| [포매터·린터·정적 분석의 역할](language/formatting-and-static-analysis.md) | 코드 형식 통일과 잠재 문제 탐지는 서로 다른 역할이며 자동 도구를 요구사항 검증과 함께 사용한다. |

## 객체지향

| 문서 | 한 줄 요약 |
| --- | --- |
| [상속과 다형성](oop/inheritance-and-polymorphism.md) | 상위 타입으로 사용하는 객체의 재정의된 인스턴스 메서드는 실제 객체 타입에 따라 실행된다. |

## 컬렉션·제네릭

| 문서 | 한 줄 요약 |
| --- | --- |
| [컬렉션과 제네릭](collections/collections-and-generics.md) | 컬렉션은 저장·탐색 방식으로 고르고, 제네릭으로 원소 타입의 계약을 표현한다. |

## 예외

| 문서 | 한 줄 요약 |
| --- | --- |
| [예외와 자원 정리](exceptions/exception-and-resources.md) | 실패를 호출자에게 전달하는 경로와 파일·연결을 닫는 경로를 함께 설계한다. |

## 스트림

| 문서 | 한 줄 요약 |
| --- | --- |
| [NIO의 Buffer와 Channel](streams/nio-buffer-channel.md) | 채널을 통해 데이터를 옮기고 버퍼의 position·limit 상태로 읽기·쓰기를 관리한다. |
| [스트림 파이프라인](streams/stream-pipeline.md) | 스트림은 데이터 저장소가 아니라 원소를 필터링·변환·집계하는 계산 흐름이다. |
| [입출력 스트림과 문자 인코딩](streams/io-streams.md) | 바이트 전송과 문자 변환을 구분하고 버퍼·인코딩·종료 책임을 명확히 한다. |

## JVM·GC

| 문서 | 한 줄 요약 |
| --- | --- |
| [JVM 메모리와 GC](jvm/jvm-memory-and-gc.md) | GC는 도달할 수 없는 객체의 메모리를 회수하며 애플리케이션 자원 전체를 관리하지 않는다. |

