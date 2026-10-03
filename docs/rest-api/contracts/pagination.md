# 페이지네이션과 안정적인 정렬

> 목록을 나눠 읽을 때 정렬·경계·변경 중 데이터의 일관성을 명확히 한다.

- 페이지 크기·최대값을 제한한다.
- 같은 정렬 값의 순서를 식별자로 보완한다.
- offset과 cursor의 장단점이 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

offset 방식은 몇 행을 건너뛰고 읽는지 나타내며 임의 페이지 접근에 편하다. 깊은 페이지와 동시 삽입·삭제에서는 비용·중복·누락을 고려한다. cursor 방식은 마지막 정렬 키 이후를 읽고 안정적인 순서와 복합 키가 필요하다. 사용자가 다음 페이지를 받는 동안 데이터가 바뀌었을 때 허용할 의미를 API 계약으로 정한다.

## 예제

created_at DESC, id DESC로 정렬하고 마지막 두 값을 cursor 조건에 사용하면 같은 시각의 행을 명확히 구분할 수 있다. 실제 조회 조건과 인덱스도 맞춘다.

## 주의점

페이지네이션에 컬렉션 fetch join을 무심코 결합하지 않는다. cursor가 있다고 동일 시점의 완전한 스냅샷이 자동 보장되지는 않는다.

## 복습 질문

created_at만 정렬할 때 같은 시각의 여러 행이 페이지 경계에서 문제가 되는 이유는?

자료 구분: **기존 자료** — 네트워크 워크북과 API 학습 자료의 설계 원리. **공식 자료 보완** — 논문·RFC·조회 계약.

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
- [Hibernate ORM 6.6 · User Guide](https://docs.hibernate.org/orm/6.6/userguide/html_single/) — 매핑·엔티티 상태·조회·락과 실제 SQL의 관계를 확인한다.
