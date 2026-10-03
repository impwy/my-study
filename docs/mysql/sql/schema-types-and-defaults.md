# MySQL 스키마의 타입·제약·기본값

> 테이블은 값의 표현뿐 아니라 누락·중복·범위에 대한 계약을 함께 정의한다.

- DECIMAL의 정밀도와 소수 자릿수를 구별한다.
- NOT NULL·UNIQUE·DEFAULT는 서로 다른 제약이다.
- 입력 검증과 데이터베이스 제약을 함께 둔다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

DECIMAL(10,2)는 전체 자릿수 10개 중 소수부에 2개를 배정한다. 금액처럼 십진 값을 정확하게 다뤄야 할 때 FLOAT·DOUBLE과 구별해 선택한다. NOT NULL은 값의 부재를 제한하고 UNIQUE는 중복을 제한하며 DEFAULT는 값을 생략했을 때의 규칙이다. 기본값이 있다는 이유로 명시적인 NULL이 항상 그 값으로 대체된다고 가정하지 않는다.

예제 테이블은 payments(id BIGINT PRIMARY KEY, amount DECIMAL(10,2) NOT NULL, status VARCHAR(16) NOT NULL DEFAULT 'PENDING')을 가정한다. 상태를 생략한 INSERT와 NULL을 전달한 INSERT의 계약을 비교해 본다.

## SQL 예제

MySQL의 새 실습 테이블에서 기본값 생략과 명시적인 NULL을 비교한다. 마지막 INSERT는 strict mode에서 오류를 확인하는 입력이다.

```sql
CREATE TABLE payments (
    id BIGINT PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(16) NOT NULL DEFAULT 'PENDING'
);
INSERT INTO payments (id, amount) VALUES (1, 42.00);
SELECT id, amount, status FROM payments;
INSERT INTO payments (id, amount, status) VALUES (2, 42.00, NULL);
```

## 주의점

소수부 초과·범위 초과·명시적인 NULL의 처리 규칙을 정하고 서버 SQL mode도 확인한다. 기본값이 애플리케이션의 모든 업무 규칙을 대신하지는 않는다.

## 꼬리질문

1. DECIMAL(10,2)에 저장할 수 있는 정수부 자릿수는 몇 개일까?
2. status를 생략한 경우와 NULL을 명시한 경우는 왜 같은 요청이 아닐까?
3. 입력 검증이 있어도 UNIQUE·NOT NULL 제약을 데이터베이스에 두는 이유는 무엇일까?

</details>

## 참고 자료

- [MySQL 8.4 · DECIMAL](https://dev.mysql.com/doc/refman/8.4/en/fixed-point-types.html) — 정밀도·소수 자릿수와 값 범위를 확인한다.
- [MySQL 8.4 · INSERT](https://dev.mysql.com/doc/refman/8.4/en/insert.html) — 생략한 열과 기본값·strict mode의 관계를 읽는다.
- [MySQL 8.4 · SQL mode](https://dev.mysql.com/doc/refman/8.4/en/sql-mode.html) — 잘못된 입력이 오류·변환·경고로 처리되는 조건을 확인한다.
