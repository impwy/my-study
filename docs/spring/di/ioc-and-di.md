# IoC와 의존성 주입

> 객체의 생성·연결을 컨테이너에 맡기고 필요한 협력 객체를 외부에서 받는다.

- IoC는 제어 주체의 이동이다.
- DI는 의존 객체를 공급하는 방법이다.
- 생성자 주입은 필수 의존성을 드러낸다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

서비스가 자신의 저장소 구현을 직접 만들면 생성과 사용 책임이 섞인다. 생성자에서 저장소 인터페이스를 받으면 실제 구현의 선택을 조립 단계로 옮길 수 있다. Spring 컨테이너는 빈 정의와 설정에 따라 객체를 만들고 의존성을 연결한다. 이 구조는 기술 구현의 교체와 테스트 대역 사용을 쉽게 하지만 인터페이스를 모든 클래스에 기계적으로 붙이라는 뜻은 아니다.

## 예제

OrderService가 OrderRepository를 생성자로 받으면 테스트는 메모리 저장소를, 실행 설정은 JPA 저장소를 연결할 수 있다.

## 주의점

new로 직접 만든 객체에는 Spring 빈의 프록시·후처리가 자동 적용되지 않는다. 순환 의존성은 책임 분리가 필요한 신호일 수 있다.

## 복습 질문

의존 객체를 직접 생성하는 코드가 사라지면 어떤 결정이 조립 단계로 이동하는가?

자료 구분: **기존 자료** — Spring 강의·이벤트·트랜잭션 노트의 개념. **공식 자료 보완** — 공식 문서의 프록시·실행 시점·롤백 조건.

</details>

## 참고 자료

- [Spring · IoC Container](https://docs.spring.io/spring-framework/reference/core/beans/introduction.html) — 빈·컨테이너·의존성 주입의 기본 역할을 확인한다.
- [Alistair Cockburn · Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — 포트·어댑터로 외부 기술을 분리하는 원래 의도를 읽는다.
