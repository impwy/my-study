# SQL 조회·조인·집계

> 필요한 행을 고르고 관계를 연결한 뒤 집계 조건을 적용한다.

- WHERE는 행, HAVING은 그룹 조건이다.
- INNER·OUTER JOIN의 결과 행이 다르다.
- 중복·NULL·정렬을 명시적으로 고려한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

FROM과 JOIN으로 대상 관계를 만들고 WHERE로 행을 제한한 뒤 GROUP BY로 묶는다. LEFT JOIN은 오른쪽 매칭이 없어도 왼쪽 행을 남긴다. 오른쪽 조건을 WHERE에 두면 NULL 행을 제거해 외부 조인의 의도와 달라질 수 있다. ORDER BY가 없으면 반환 순서를 보장하지 않는다.

## 예제

회원과 주문을 LEFT JOIN해 주문 없는 회원을 포함한다. 주문 수를 세면 COUNT(*)와 COUNT(order_id)가 NULL 확장 행에서 다른 결과를 줄 수 있다.

## 주의점

“조회가 예전에 이 순서였다”를 정렬 계약으로 삼지 않는다. JOIN 뒤 행이 늘어난 이유를 키의 카디널리티로 점검한다.

## 복습 질문

LEFT JOIN의 오른쪽 필터를 ON과 WHERE에 둘 때 왜 결과가 달라질까?

자료 구분: **기존 자료** — DB 강의와 저장 구조 복습 메모의 개념. **공식 자료 보완** — SQL·인덱스·버전 읽기의 제품별 조건.

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
