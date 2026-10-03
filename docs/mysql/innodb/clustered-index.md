# InnoDB 클러스터드 인덱스

> InnoDB는 클러스터드 인덱스 리프에 행을 저장하고 보조 인덱스에서 행 식별 키를 이용한다.

- 일반적으로 기본 키가 클러스터드 키다.
- 보조 인덱스 조회는 행 조회를 더 요구할 수 있다.
- 키 크기는 보조 인덱스 공간에도 영향을 준다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

행을 저장하는 클러스터드 인덱스와 별도로 보조 인덱스를 둔다. 보조 인덱스의 레코드는 클러스터드 키를 포함하므로 필요한 컬럼이 보조 인덱스에 없으면 클러스터드 인덱스로 추가 접근할 수 있다. 커버링 인덱스는 해당 조회에 필요한 값을 인덱스에서 얻는 경우다. 기본 키가 없을 때의 키 선택은 InnoDB 규칙에 따른다.

## SQL 예제

users에 PK(id)와 보조 인덱스(email)가 있고 name은 해당 인덱스에 포함되지 않는다고 가정한다. 두 조회의 계획과 Extra를 비교한다.

```sql
EXPLAIN SELECT id FROM users WHERE email = 'learner@example.org';
EXPLAIN SELECT id, name FROM users WHERE email = 'learner@example.org';
```

## 주의점

클러스터드 인덱스를 “물리 디스크에 항상 완벽히 연속 저장”이라고 해석하지 않는다. 넓은 기본 키는 여러 보조 인덱스 크기에 영향을 준다.

## 꼬리질문

1. 보조 인덱스에서 큰 기본 키를 포함하면 공간 비용이 왜 반복되는가?
2. email 인덱스에서 id만 반환하는 조회와 name까지 반환하는 조회의 추가 접근은 어떻게 다를까?
3. 기본키를 긴 문자열로 바꾸면 각 보조 인덱스의 공간 비용에 어떤 영향이 있을까?

</details>

## 참고 자료

- [MySQL · Clustered and Secondary Indexes](https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html) — 행 저장과 보조 인덱스의 기본 키 포함 방식을 확인한다.
