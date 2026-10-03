# 단위·통합·인수 테스트

> 작은 규칙의 빠른 검증과 실제 경계 연동·사용자 요구 검증을 목적별로 나눈다.

- 단위 테스트는 좁은 행동을 빠르게 확인한다.
- 통합 테스트는 실제 협력의 계약을 확인한다.
- 인수 테스트는 사용자 관점의 요구를 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

도메인 규칙은 외부 환경 없이 빠르게 반복할 수 있다. JPA 매핑·SQL·트랜잭션·이벤트 설정은 실제 프레임워크·DB와 결합한 통합 테스트가 필요하다. 전체 사용자 흐름의 인수 테스트는 요구와 실제 결과를 연결한다. 각 단계의 테스트 수를 기계적인 비율로 정하기보다 실패 위험·실행 시간·진단 비용에 맞춘다.

## Java 예제

JUnit Jupiter와 통합 테스트용 DB가 필요하다. 단위 예제는 단순 규칙이며 실제 업무 경계 테스트로 확장한다.

```java
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.sql.*;

static void verifyDatabase(Connection c) throws SQLException {
    try (Statement s = c.createStatement();
            ResultSet r = s.executeQuery("SELECT 1")) {
        assertTrue(r.next());
        assertEquals(1, r.getInt(1));
    }
} // 통합 테스트가 실습 DB 연결을 제공해 호출

static void requireQuantity(int quantity) {
    if (quantity <= 0) throw new IllegalArgumentException("quantity must be positive");
}

@Test
void rejectsZeroQuantity() {
    assertThrows(IllegalArgumentException.class, () -> requireQuantity(0));
} // 외부 자원 없이 업무 입력 경계를 검사
```

## 주의점

테스트 트랜잭션이 자동 롤백하면 실제 커밋 후 이벤트·조회 문제를 가릴 수 있다. 확인하려는 운영 경계를 테스트 환경에서도 드러낸다.

## 꼬리질문

1. JPA 엔티티의 필드 검증 테스트만으로 연관관계 저장을 검증할 수 없는 이유는?
2. SELECT 1 통과가 엔티티 매핑과 연관관계 저장 성공까지 뜻하지 않는 이유는 무엇일까?
3. 통합 테스트에서 트랜잭션 롤백만 사용하면 실제 커밋 후 동작을 어떻게 놓칠 수 있을까?

</details>

## 참고 자료

- [JUnit · User Guide](https://docs.junit.org/current/user-guide/) — 단위 테스트·픽스처·실행 구조를 확인한다.
- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
