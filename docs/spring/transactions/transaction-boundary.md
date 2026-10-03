# Spring 트랜잭션 경계

> 하나의 업무에서 함께 성공해야 하는 DB 변경을 명확한 트랜잭션 경계로 묶는다.

- 기본 프록시 호출 경계를 확인한다.
- 기본 롤백 규칙과 전파 속성을 구분한다.
- 외부 시스템은 같은 DB 롤백 범위에 들지 않는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

@Transactional은 지정한 트랜잭션 관리자와 전파 규칙으로 실행 경계를 만든다. 기본 설정에서는 RuntimeException·Error가 롤백 대상이고 checked 예외에는 별도 규칙이 필요할 수 있다. REQUIRED는 기존 트랜잭션에 참여하고 REQUIRES_NEW는 별도의 트랜잭션을 시작한다. 내부 메서드 호출·예외를 잡아 정상 반환하는 흐름까지 함께 보아야 실제 결과를 이해할 수 있다.

## 예제

주문 생성과 재고 변경은 같은 DB 트랜잭션으로 묶을 수 있다. 이미 성공한 외부 결제는 DB rollback만으로 취소되지 않으므로 취소 API·상태 확인·보상 절차가 필요하다.

## 주의점

readOnly는 최적화 힌트와 제품별 동작이 있으며 일반적인 쓰기 금지 장치로 믿지 않는다. 외부 호출을 긴 DB 트랜잭션 안에 두면 연결·락 점유가 길어진다.

## 복습 질문

결제 성공 뒤 DB 저장이 실패하면 DB 트랜잭션만으로 해결되지 않는 부분은?

자료 구분: **기존 자료** — Spring 강의·이벤트·트랜잭션 노트의 개념. **공식 자료 보완** — 공식 문서의 프록시·실행 시점·롤백 조건.

함께 복습: [AOP 프록시와 자기 호출](../aop/proxy-boundary.md) · [트랜잭션 이벤트와 전달 실패](transaction-events.md)

</details>

## 참고 자료

- [Spring · @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) — 프록시 경계·롤백 조건·트랜잭션 속성을 확인한다.
- [Spring · Transaction-bound Events](https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html) — 커밋 전·후 리스너의 동작 범위를 확인한다.
