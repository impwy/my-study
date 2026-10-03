# SQL 조회·조인·집계

> 필요한 행을 고르고 관계를 연결한 뒤 집계 조건을 적용한다.

- WHERE는 행, HAVING은 그룹 조건이다.
- INNER·OUTER JOIN의 결과 행이 다르다.
- 중복·NULL·정렬을 명시적으로 고려한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

FROM과 JOIN으로 대상 관계를 만들고 WHERE로 행을 제한한 뒤 GROUP BY로 묶는다. LEFT JOIN은 오른쪽 매칭이 없어도 왼쪽 행을 남긴다. 오른쪽 조건을 WHERE에 두면 NULL 행을 제거해 외부 조인의 의도와 달라질 수 있다. ORDER BY가 없으면 반환 순서를 보장하지 않는다.

## Java 예제

users·orders 스키마가 있는 JDBC 연결을 받는다.

```java
import java.sql.*;

static void totals(Connection c, String status) throws SQLException {
    String sql =
            "SELECT u.id, COUNT(o.id) FROM users u LEFT JOIN orders o "
                    + "ON o.user_id=u.id AND o.status=? GROUP BY u.id";
    try (PreparedStatement p = c.prepareStatement(sql)) {
        p.setString(1, status);
        try (ResultSet r = p.executeQuery()) {
            while (r.next()) System.out.println(r.getLong(1) + ":" + r.getLong(2));
        }
    }
}
```

## 주의점

“조회가 예전에 이 순서였다”를 정렬 계약으로 삼지 않는다. JOIN 뒤 행이 늘어난 이유를 키의 카디널리티로 점검한다.

## 꼬리질문

1. LEFT JOIN의 오른쪽 필터를 ON과 WHERE에 둘 때 왜 결과가 달라질까?
2. 주문 없는 사용자의 COUNT(o.id)와 COUNT(*)는 각각 얼마일까?
3. status 조건을 WHERE로 옮기면 LEFT JOIN의 어떤 행이 제거될까?

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
