# 스키마·제약 조건·뷰

> 테이블의 구조와 데이터 규칙을 DB에 선언하고 조회 표현을 뷰로 제공한다.

- DDL과 DML의 목적을 구분한다.
- PK·FK·UNIQUE·NOT NULL은 서로 다른 규칙이다.
- 뷰와 실제 저장 테이블은 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

스키마는 테이블·컬럼·타입·제약 등을 정의한다. 기본 키는 행 식별, 외래 키는 참조 관계, UNIQUE는 중복 제한, NOT NULL은 값 존재 조건을 표현한다. 애플리케이션 검증만으로 동시 요청의 중복을 막기 어려우므로 DB 제약을 최종 방어로 사용한다. 일반 뷰는 질의 표현이며 제품별 materialized view와 같은 물리 저장을 가정하지 않는다.

## 예제

발급 테이블에 `(user_id,coupon_id)` UNIQUE를 선언하면 동시 중복 INSERT 중 하나가 실패할 수 있다. 오류를 업무 결과로 변환한다.

## 주의점

FK·NULL·트랜잭션 DDL 동작은 제품별로 다를 수 있다. 운영 마이그레이션에는 기존 데이터와 락·호환성도 고려한다.

## 복습 질문

사전 중복 조회를 했는데도 UNIQUE 제약이 필요한 이유는?

자료 구분: **기존 자료** — DB 강의와 저장 구조 복습 메모의 개념. **공식 자료 보완** — SQL·인덱스·버전 읽기의 제품별 조건.

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
- [MySQL 8.4 · InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) — 일관 읽기·격리 수준·락의 제품별 동작을 확인한다.
