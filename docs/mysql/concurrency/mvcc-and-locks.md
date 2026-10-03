# InnoDB MVCC와 락

> 스냅샷 읽기와 잠금 읽기를 구분하고 격리 수준·인덱스 조건에 따른 동시 동작을 확인한다.

- 일관 읽기는 이전 버전을 사용할 수 있다.
- SELECT FOR UPDATE는 잠금 읽기다.
- 락 범위는 실제 접근 경로에 영향을 받는다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

MVCC는 읽는 트랜잭션에 보이는 버전을 고르는 방식으로 읽기와 쓰기의 경합을 줄인다. InnoDB의 일반 일관 읽기와 잠금 읽기·DML은 같은 방식으로 동작하지 않는다. 격리 수준과 조건에 따라 record·gap·next-key 락이 적용될 수 있다. 업무의 “없으면 생성”이나 “재고가 있으면 차감”을 사전 SELECT만으로 안전하다고 판단하지 않는다.

## 예제

재고 행을 FOR UPDATE로 읽고 검사·차감한 뒤 커밋하면 같은 변경 경쟁을 조정할 수 있다. 외부 호출 대기 중 락을 오래 보유하지 않는다.

## 주의점

MySQL REPEATABLE READ의 동작을 모든 DB의 동일 이름 격리 수준에 적용하지 않는다. 실행 계획과 인덱스가 락 범위에 영향을 준다.

## 복습 질문

일반 SELECT가 성공했다고 같은 상태로 UPDATE도 반드시 성공한다고 볼 수 없는 이유는?

자료 구분: **기존 자료** — JPA·DB·조회 최적화 자료의 원리. **공식 자료 보완** — MySQL 8.4 InnoDB 동작.

</details>

## 참고 자료

- [MySQL 8.4 · InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) — 일관 읽기·격리 수준·락의 제품별 동작을 확인한다.
