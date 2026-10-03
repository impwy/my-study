# Spring

[전체 목록](../../README.md)

## IoC·DI

| 문서 | 한 줄 요약 |
| --- | --- |
| [IoC와 의존성 주입](di/ioc-and-di.md) | 객체의 생성·연결을 컨테이너에 맡기고 필요한 협력 객체를 외부에서 받는다. |

## 빈 생명주기

| 문서 | 한 줄 요약 |
| --- | --- |
| [빈 생명주기와 싱글턴](lifecycle/bean-lifecycle.md) | 컨테이너는 빈의 생성·주입·초기화·종료를 관리하며 기본 싱글턴은 컨테이너 안에서 공유된다. |

## AOP

| 문서 | 한 줄 요약 |
| --- | --- |
| [AOP 프록시와 자기 호출](aop/proxy-boundary.md) | Spring의 기본 프록시 방식에서는 프록시를 통과하는 호출에 부가 기능이 적용된다. |

## MVC

| 문서 | 한 줄 요약 |
| --- | --- |
| [Spring MVC 요청 처리](mvc/request-flow.md) | DispatcherServlet은 요청을 적절한 핸들러에 연결하고 입력·결과 변환과 오류 처리를 조정한다. |

## 트랜잭션

| 문서 | 한 줄 요약 |
| --- | --- |
| [Spring 트랜잭션 경계](transactions/transaction-boundary.md) | 하나의 업무에서 함께 성공해야 하는 DB 변경을 명확한 트랜잭션 경계로 묶는다. |
| [트랜잭션 이벤트와 전달 실패](transactions/transaction-events.md) | 이벤트 리스너의 실행 시점과 실행 스레드, 이벤트의 내구성을 각각 설계한다. |

