# InnoDB MVCC와 락

> 스냅샷 읽기와 잠금 읽기를 구분하고 격리 수준·인덱스 조건에 따른 동시 동작을 확인한다.

- 일관 읽기는 이전 버전을 사용할 수 있다.
- SELECT FOR UPDATE는 잠금 읽기다.
- 락 범위는 실제 접근 경로에 영향을 받는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

MVCC는 읽는 트랜잭션에 보이는 버전을 고르는 방식으로 읽기와 쓰기의 경합을 줄인다. InnoDB의 일반 일관 읽기와 잠금 읽기·DML은 같은 방식으로 동작하지 않는다. 격리 수준과 조건에 따라 record·gap·next-key 락이 적용될 수 있다. 업무의 “없으면 생성”이나 “재고가 있으면 차감”을 사전 SELECT만으로 안전하다고 판단하지 않는다.

## SQL 예제

InnoDB의 inventory 실습 테이블에서 실행한다. 변경 행 수 1은 차감 성공, 0은 대상이 없거나 현재 재고가 조건을 만족하지 않음을 뜻한다.

```sql
UPDATE inventory
SET stock = stock - 1
WHERE id = 1 AND stock > 0;
```

## 주의점

MySQL REPEATABLE READ의 동작을 모든 DB의 동일 이름 격리 수준에 적용하지 않는다. 실행 계획과 인덱스가 락 범위에 영향을 준다.

## 꼬리질문

1. 일반 SELECT가 성공했다고 같은 상태로 UPDATE도 반드시 성공한다고 볼 수 없는 이유는?
2. 이전 일반 SELECT에서 stock=1을 보았어도 UPDATE 결과가 0이 될 수 있는 이유는 무엇일까?
3. 조건부 UPDATE도 락 대기나 교착에 실패할 수 있다면 어떤 트랜잭션 재시도가 필요할까?

</details>

## 참고 자료

- [MySQL 8.4 · InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) — 일관 읽기·격리 수준·락의 제품별 동작을 확인한다.
