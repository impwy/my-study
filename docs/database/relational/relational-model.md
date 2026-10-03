# 관계형 모델과 키

> 테이블의 행을 구별하고 관계·제약으로 데이터의 의미를 지킨다.

- 후보키는 유일성과 최소성을 갖는다.
- 기본키·외래키의 역할은 다르다.
- 제약은 코드 검증과 함께 DB에서도 지킨다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

개념 모델의 개체·관계를 DB의 테이블·키로 옮긴다. 기본키는 후보키 중 선택한 식별자이고 외래키는 다른 행의 키를 참조한다. 릴레이션 이론의 집합과 SQL의 중복 행·NULL 규칙을 구분한다. 업무상 유일한 값은 별도 UNIQUE 제약으로 표현할 수 있다.

## Java 예제

키의 유일성과 업무 속성의 유일성을 비교하는 메모리 모형이다.

```java
import java.util.*;

record User(long id, String email) {}

static void demo() {
    List<User> users = List.of(new User(1, "a@example.org"), new User(2, "a@example.org"));
    long distinctIds = users.stream().map(User::id).distinct().count();
    long distinctEmails = users.stream().map(User::email).distinct().count();
    System.out.println(distinctIds + "," + distinctEmails); // 2,1
}
```

## 주의점

외래키가 있다고 조회가 항상 빠른 것은 아니다. 제약·참조 방향·인덱스의 역할을 따로 본다.

## 꼬리질문

1. 기본키만 있으면 업무상 중복 가입을 막을 수 있을까?
2. 서로 다른 기본키를 가진 두 행이 같은 이메일을 가질 때 어떤 제약이 추가로 필요할까?
3. 외래키가 존재하는 것과 업무상 유효한 상태 전이가 보장되는 것은 어떻게 다를까?

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
