# PostgreSQL 페이지·튜플과 MVCC

> 행 버전을 페이지에 저장하고 트랜잭션 가시성으로 읽을 버전을 고르며 불필요해진 버전을 정리한다.

- ctid는 물리 위치이며 영속 업무 식별자가 아니다.
- UPDATE는 새 행 버전을 만들 수 있다.
- VACUUM은 불필요해진 버전 정리에 관여한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

테이블의 heap에는 페이지와 튜플 형태로 행 버전이 저장된다. ctid는 블록 번호와 튜플 위치를 나타내지만 업데이트·이동으로 바뀔 수 있다. MVCC는 각 트랜잭션에서 보이는 버전을 판단한다. 갱신이 항상 같은 페이지 안에서 이루어지거나 commit 직후 이전 버전이 즉시 지워지는 것은 아니다. 아직 다른 트랜잭션이 필요로 하는 버전은 유지해야 한다.

## Java 예제

PostgreSQL과 users 테이블의 JDBC 연결이 필요하다.

```java
import java.sql.*;

static void inspect(Connection c, long id) throws SQLException {
    try (PreparedStatement p =
            c.prepareStatement("SELECT id, ctid::text, xmin::text FROM users WHERE id=?")) {
        p.setLong(1, id);
        try (ResultSet r = p.executeQuery()) {
            while (r.next())
                System.out.println(r.getLong(1) + ":" + r.getString(2) + ":" + r.getString(3));
        }
    }
}
```

## 주의점

기존 일지의 “항상 같은 페이지 갱신”과 “트랜잭션 후 바로 정리” 설명을 조건부 동작으로 수정했다. 기본 페이지 크기와 인덱스 구현은 구성·제품 문서로 확인한다.

## 꼬리질문

1. 같은 논리 행의 ctid가 바뀌어도 업무 식별자가 유지되어야 하는 이유는?
2. 같은 id 행을 UPDATE한 뒤 다시 조회하면 ctid가 바뀔 수 있는 이유는 무엇일까?
3. xmin이나 ctid를 영구 업무 식별자로 저장하면 VACUUM·갱신에서 어떤 문제가 생길까?

</details>

## 참고 자료

- [PostgreSQL · Database Physical Storage](https://www.postgresql.org/docs/current/storage.html) — 페이지·튜플·물리 위치와 HOT·정리를 확인한다.
