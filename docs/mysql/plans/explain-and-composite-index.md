# 실행 계획과 복합 인덱스

> 실제 필터·정렬·조인 조건과 데이터 분포를 기준으로 인덱스의 효과를 검증한다.

- EXPLAIN으로 접근 방식과 추정치를 확인한다.
- 복합 키의 순서가 사용 가능한 범위를 바꾼다.
- 인덱스는 쓰기·공간 비용도 만든다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

복합 인덱스 `(user_id, created_at)`는 먼저 user_id로 묶고 그 안에서 created_at 순서를 갖는다. 선두 조건과 범위 조건이 어떤 부분을 좁히는지 생각한다. 조건에 인덱스가 있어도 선택도가 낮거나 함수를 적용하거나 비용이 더 크면 계획은 달라질 수 있다. 실행 계획의 추정과 실제 소요 시간·행 수를 함께 관찰한다.

## Java 예제

MySQL JDBC 연결과 orders 스키마가 필요하다. key·rows는 계획의 추정 정보다.

```java
import java.sql.*;

static void explain(Connection c, long tenant) throws SQLException {
    try (PreparedStatement p =
            c.prepareStatement(
                    "EXPLAIN SELECT id FROM orders WHERE tenant_id=? ORDER BY created_at,id"
                        + " LIMIT 20")) {
        p.setLong(1, tenant);
        try (ResultSet r = p.executeQuery()) {
            while (r.next())
                System.out.println(
                        r.getString("key")
                                + ":"
                                + r.getLong("rows")
                                + ":"
                                + r.getString("Extra"));
        }
    }
}
```

## 주의점

인덱스만 추가해 모든 느린 쿼리를 해결하지 않는다. SELECT *·대량 결과·N+1·커넥션 대기도 별도 원인이 될 수 있다.

## 꼬리질문

1. 두 컬럼 순서를 바꾸면 어떤 질의의 사용 가능 범위가 달라지는가?
2. 인덱스가 (tenant_id, created_at, id)이면 조건과 정렬을 어떤 순서로 활용할 수 있을까?
3. EXPLAIN의 추정 rows가 작아도 실제로 느리다면 어떤 실행 측정과 데이터 분포를 확인할까?

</details>

## 참고 자료

- [MySQL 8.4 · Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html) — 인덱스 선택·복합 키·쓰기 비용의 관계를 확인한다.
