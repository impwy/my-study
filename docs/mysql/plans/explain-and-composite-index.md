# 실행 계획과 복합 인덱스

> 복합 인덱스는 카디널리티만으로 정렬하지 않고 필터·정렬·선두 컬럼·실제 실행 비용을 함께 검증한다.

- EXPLAIN으로 접근 방식과 추정치를 확인한다.
- 동등·범위 조건과 ORDER BY가 인덱스 순서의 효과를 바꾼다.
- 인덱스는 조회 이득과 쓰기·공간 비용을 함께 만든다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

복합 인덱스 `(user_id, created_at)`는 user_id를 먼저 비교하고 그 안에서 created_at을 비교한다. 선두 컬럼과 범위 조건이 조회 범위를 얼마나 좁히는지 확인한다. 인덱스가 있어도 선택도·함수 적용·비용 추정 때문에 다른 계획을 선택할 수 있다. “카디널리티 높은 컬럼부터”를 보편 규칙으로 사용하지 않는다.

## SQL 예제

실습 orders 테이블에 `(tenant_id, created_at, id)` 인덱스가 있다고 가정한다. 아래 EXPLAIN은 계획을 보여 주며 질의 결과를 실제로 읽는 실행 측정과 구분한다.

```sql
EXPLAIN
SELECT id FROM orders
WHERE tenant_id = 42
ORDER BY created_at, id
LIMIT 20;
```

동등 조건으로 tenant_id 범위를 좁힌 뒤 정렬과 LIMIT에 활용할 가능성을 검토한다. key·rows·Extra와 실제 데이터 분포·행 수·시간을 함께 본다. 사용자별 거래 내역에서도 `(user_id, created_at, id)`는 후보일 뿐 실제 쿼리와 계획 없이 정답으로 확정하지 않는다.

## 주의점

데이터가 특정 건수를 넘으면 단일 테이블 조회가 불가능해지는 보편 임계값은 없다. 대표 쿼리·결과량·행 폭·인덱스 크기·자원·보관 정책을 확인한다. SELECT *·대량 반환·N+1·커넥션 대기는 인덱스만으로 해결되지 않을 수 있다. [JPA 상속 전략](../../jpa/mapping/inheritance-strategies.md)의 테이블 구성과 인덱스 가능 여부도 구분한다.

## 꼬리질문

1. 복합 인덱스의 선두 컬럼을 바꾸면 사용 가능한 조회 범위가 달라지는 이유는?
2. tenant_id 동등 조건과 created_at·id 정렬에 위 인덱스가 어떤 이득을 줄 수 있을까?
3. EXPLAIN의 추정 rows가 작아도 느리다면 결과량·실측 시간·자원 대기 중 무엇을 확인할까?

</details>

## 참고 자료

- [MySQL 8.4 · Multiple-Column Indexes](https://dev.mysql.com/doc/refman/8.4/en/multiple-column-indexes.html) — 복합 인덱스와 선두 컬럼의 사용 조건을 확인한다.
- [MySQL 8.4 · Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html) — 인덱스의 효과와 비용을 함께 검토한다.
