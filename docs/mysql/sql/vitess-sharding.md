# MySQL과 Vitess의 역할

> MySQL이 데이터를 저장·실행하고 Vitess는 MySQL 위에서 라우팅·샤딩·운영을 지원한다.

- Vitess는 MySQL을 기반으로 수평 확장과 클러스터 운영을 지원한다.
- VTGate는 요청을 라우팅하고 VTTablet은 MySQL 인스턴스와 연결된 제어 계층이다.
- 샤딩을 도입해도 SQL·조인·트랜잭션 조건의 검토가 필요하다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

MySQL은 관계형 DBMS이고 Vitess는 MySQL 기반 데이터베이스 클러스터의 확장·운영을 위한 시스템이다. 독립적인 저장 엔진으로 MySQL을 대체하는 관계로 이해하지 않는다.

```text
애플리케이션 → VTGate → VTTablet → MySQL
                    ↘ 다른 샤드의 VTTablet → MySQL
```

샤딩은 데이터를 여러 샤드에 분산하는 방식이다. keyspace는 논리적 데이터베이스 개념이며 샤딩 키와 Vindex 등 라우팅 규칙으로 데이터 위치를 결정한다. VTGate는 질의를 적절한 대상에 보내고, VTTablet은 각 MySQL과 함께 질의 처리·운영을 지원한다.

## 주의점

하나의 샤드에서 끝나는 질의와 여러 샤드에 걸친 질의는 비용과 제약이 다르다. 분산 트랜잭션 기능도 있지만 설정·지원 범위·실패 복구·추가 비용을 확인해야 한다. 일반 MySQL과 모든 SQL 및 트랜잭션 동작이 완전히 같다고 가정하지 않는다. 먼저 실행 계획·인덱스·데이터량·자원 병목을 확인하고 수평 분산의 필요성을 판단한다. “MySQL Vitess”라는 메모만으로 실제 샤딩 적용을 확정하지 않는다.

## 꼬리질문

1. MySQL의 저장·실행과 Vitess의 라우팅·운영을 구분해야 하는 이유는?
2. 사용자별 거래 내역을 한 샤드에서 읽도록 하려면 조회 조건과 샤딩 기준이 어떻게 맞아야 할까?
3. 서로 다른 샤드의 잔액을 함께 변경하면 어떤 트랜잭션·복구·성능 조건을 추가 확인해야 할까?

</details>

## 참고 자료

- [Vitess · Overview](https://vitess.io/docs/24.0/overview/) — MySQL 위에 놓이는 Vitess의 목적과 구성 설명으로 이동한다.
- [Vitess · Tablet](https://vitess.io/docs/archive/18.0/concepts/tablet/) — VTTablet·MySQL·VTGate의 역할 관계를 확인한다.
- [Vitess · Distributed Transactions](https://vitess.io/docs/24.0/reference/features/distributed-transaction/) — 분산 트랜잭션의 범위와 운영 조건을 확인한다.
