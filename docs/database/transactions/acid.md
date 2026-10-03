# 트랜잭션과 ACID

> 여러 데이터 변경을 하나의 논리적 작업으로 관리한다.

- 원자성·일관성·격리성·지속성.
- commit과 rollback의 경계를 정한다.
- 업무 불변식은 올바른 코드·제약도 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

원자성은 작업 전체가 반영되거나 되돌아가는 범위를 제공한다. 지속성은 완료한 결과를 장애 뒤에도 유지하는 성질이다. 격리성은 동시 실행의 관찰 규칙을 정한다. 일관성은 DB가 모든 업무 규칙을 자동 이해한다는 뜻이 아니라 올바른 변경과 제약으로 유효한 상태를 유지한다는 관점이다.

## SQL 예제

accounts의 두 기존 계좌에서 100을 이체하는 실습이다. 두 UPDATE가 각각 한 행을 변경했는지 확인한 뒤 모두 성공한 경우에만 COMMIT한다. 실패하거나 대상이 없으면 ROLLBACK한다.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- 변경 행 수와 업무 조건을 확인한 성공 경로
COMMIT;
```

## 주의점

하나의 로컬 DB 트랜잭션이 외부 HTTP 결제까지 자동 롤백하지 않는다. 프로세스 메모리 변경도 별도 수명과 복구 정책을 갖는다.

## 꼬리질문

1. 외부 결제 성공 뒤 DB 롤백이 발생하면 어떤 별도 처리가 필요할까?
2. 두 번째 UPDATE가 실패하면 첫 번째 변경도 롤백해야 하는 이유는 무엇일까?
3. 외부 결제 호출을 이 블록 안에 넣어도 DB rollback이 외부 결제를 취소할 수 있을까?

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
