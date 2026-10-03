# 격리 수준과 동시성 이상

> 동시에 실행된 트랜잭션에서 어떤 값을 관찰하고 충돌을 어떻게 처리할지 정한다.

- dirty·non-repeatable·phantom read를 구분한다.
- 제품마다 같은 수준 이름의 구현이 다를 수 있다.
- 갱신 유실·write skew도 별도로 검토한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

격리 수준은 읽기 현상과 직렬 실행에 가까운 정도를 조절한다. 낮은 수준은 더 많은 중간·최신 변경을 볼 수 있고 높은 수준은 락·검증·중단 비용이 생길 수 있다. 같은 데이터를 읽은 뒤 각자 판단하는 업무는 읽기 일관성만으로 충분하지 않을 수 있다. 엔진의 스냅샷·락 규칙을 확인한다.

## SQL 예제

MySQL InnoDB의 accounts 실습 테이블에서 실행한다. 두 SELECT 사이에 별도 연결의 UPDATE·COMMIT을 실행해 관찰 값을 비교한다.

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
SELECT balance FROM accounts WHERE id = 1;
-- 이 사이에 다른 연결이 해당 행을 변경하고 COMMIT
SELECT balance FROM accounts WHERE id = 1;
COMMIT;
```

## 주의점

격리 수준만 높이면 모든 동시성 문제가 자동 해결된다고 주장하지 않는다. 실패 시 전체 트랜잭션 재시도가 필요한 경우도 있다.

## 꼬리질문

1. 반복 읽기가 같다는 사실만으로 서로 다른 행의 업무 불변식이 지켜질까?
2. 두 SELECT 사이 다른 연결이 같은 행을 갱신하면 선택한 DB의 격리 수준에서는 무엇을 보게 될까?
3. 각각 다른 행을 수정하는 두 트랜잭션이 공통 업무 규칙을 깨는 write skew는 어떻게 막을까?

</details>

## 참고 자료

- [MySQL 8.4 · InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) — 일관 읽기·격리 수준·락의 제품별 동작을 확인한다.
