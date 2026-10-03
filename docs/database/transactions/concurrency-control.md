# 락·직렬 가능성·2PL

> 동시 작업의 순서를 제한해 충돌하는 읽기·쓰기를 조정한다.

- 공유 락과 배타 락의 양립성을 본다.
- 2PL은 락 획득·해제 단계의 규약이다.
- 직렬 가능성과 회복 가능성은 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

충돌하는 연산의 순서가 어떤 직렬 실행과 같은지 분석하면 직렬 가능성을 판단할 수 있다. 2단계 락 규약은 락을 늘리는 단계가 끝난 뒤에는 새 락을 얻지 않는 규칙으로 충돌 직렬 가능성을 제공한다. 커밋까지 어떤 락을 유지하는지에 따라 연쇄 롤백과 회복 특성이 달라진다.

## SQL 예제

FOR UPDATE를 지원하는 DB의 products 테이블을 가정한다. 선택된 재고와 UPDATE의 변경 행 수를 확인하고, 판매 가능한 경우에만 커밋한다. 다른 연결에서 같은 행을 수정하며 대기를 관찰한다.

```sql
BEGIN;
SELECT stock FROM products WHERE id = 1 FOR UPDATE;
UPDATE products SET stock = stock - 1 WHERE id = 1 AND stock > 0;
-- 재고 차감 성공을 확인한 경로
COMMIT;
```

## 주의점

2PL과 두 단계 커밋(2PC)은 다른 개념이다. 락이 있어도 대기·타임아웃·교착 복구 정책이 필요하다.

## 꼬리질문

1. 직렬 가능한 실행이 항상 회복 가능한 실행인 것은 아닐 수 있는 이유는?
2. FOR UPDATE로 잠근 뒤 트랜잭션을 끝내기 전에 다른 요청이 같은 행을 수정하려 하면 어떻게 될까?
3. 여러 상품을 서로 다른 순서로 잠그면 어떤 교착과 재시도 정책이 필요할까?

</details>

## 참고 자료

- [PostgreSQL · SQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) — SQL·조인·집계·뷰·트랜잭션의 실행 예제를 확인한다.
