# JavaScript

[전체 목록](../../README.md)

## 타입·스코프

| 문서 | 한 줄 요약 |
| --- | --- |
| [JavaScript 타입과 형 변환](language/types-and-coercion.md) | 변수의 값 타입은 실행 중 달라질 수 있으며 자동 형 변환과 명시적 변환을 구별해야 한다. |
| [렉시컬 스코프와 TDZ](language/lexical-scope-and-tdz.md) | 이름을 찾는 범위는 코드가 선언된 위치로 결정되며 let·const는 초기화 전 접근을 허용하지 않는다. |

## 클로저

| 문서 | 한 줄 요약 |
| --- | --- |
| [클로저와 상태 보존](closures/captured-environment.md) | 함수는 자신이 만들어진 렉시컬 환경을 참조해 바깥 함수가 종료된 뒤에도 상태를 사용할 수 있다. |

## 프로토타입

| 문서 | 한 줄 요약 |
| --- | --- |
| [프로토타입과 속성 탐색](objects/prototype-lookup.md) | 객체에 없는 속성은 프로토타입 연결을 따라 찾으며 자기 속성은 상속된 속성을 가릴 수 있다. |

## 비동기·이벤트 루프

| 문서 | 한 줄 요약 |
| --- | --- |
| [Promise와 async·await](async/promise-and-await.md) | Promise는 나중의 완료 결과를 표현하고 await는 해당 함수의 후속 실행을 완료 뒤로 이어 준다. |
| [이벤트 루프와 마이크로태스크](async/event-loop-and-microtasks.md) | 현재 동기 실행이 끝난 뒤 Promise 등의 마이크로태스크를 처리하고 다음 태스크로 진행한다. |

