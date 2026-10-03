# JDBC 연결과 트랜잭션

> SQL 실행·값 바인딩·결과 처리·트랜잭션·연결 반환의 경계를 관리한다.

- PreparedStatement로 값을 바인딩한다.
- autoCommit과 명시적 commit·rollback을 구분한다.
- 연결 풀의 close는 보통 반환이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

JDBC Connection으로 Statement·PreparedStatement를 만들고 ResultSet을 읽는다. autoCommit이 켜져 있으면 문장별 확정 동작을 확인해야 하며 여러 변경을 묶을 때는 적절한 트랜잭션 설정과 rollback 처리가 필요하다. 연결·명령·결과 자원을 제때 닫고 예외 원인을 보존한다. Spring·JPA를 사용해도 아래의 연결 점유·트랜잭션 비용은 사라지지 않는다.

## 예제

값은 `statement.setString(1, name)`처럼 바인딩한다. 같은 업무의 여러 변경이 모두 성공해야 하면 같은 연결의 명확한 트랜잭션 경계로 묶는다.

## 주의점

값 바인딩이 임의로 만든 SQL 식별자까지 보호하지 않는다. 풀 최대 연결 수는 DB 한도·응답 시간·다른 인스턴스와 함께 계산한다.

## 복습 질문

연결을 오래 반환하지 않으면 CPU가 낮아도 요청이 왜 기다릴 수 있는가?

자료 구분: **기존 자료** — Java 강의와 자료구조 노트의 언어·API 개념. **공식 자료 보완** — Java 21 명세·자원 및 참조 계약.

</details>

## 참고 자료

- [Java · java.sql](https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/java/sql/package-summary.html) — Connection·PreparedStatement·ResultSet 계약을 확인한다.
- [Spring · @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) — 프록시 경계·롤백 조건·트랜잭션 속성을 확인한다.
