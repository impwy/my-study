# LSM 트리와 컴팩션

> LSM은 쓰기를 메모리에 모아 정렬 파일로 내보내고 병합하면서 읽기·쓰기 비용을 조절한다.

- MemTable·정렬 파일·로그는 서로 다른 역할이다.
- 조회는 여러 계층의 최신 값을 구별해야 한다.
- 컴팩션은 파일을 병합하며 읽기·쓰기·공간 비용을 바꾼다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

대표적인 LSM 구현은 변경을 WAL에 기록하고 메모리의 MemTable에 반영한다. 메모리가 차면 정렬된 불변 파일인 SSTable로 내보낸다. 같은 키의 옛 값과 새 값이 여러 파일에 남을 수 있으므로 최신 버전을 찾는 규칙이 필요하다. 삭제도 오래된 값이 다시 보이지 않도록 tombstone 같은 표시를 사용한다.

컴팩션은 파일을 병합하고 조건이 허용하는 오래된 버전·삭제 표시를 정리한다. 이 과정은 추가 디스크 쓰기를 만들지만 파일 중첩과 조회 비용을 줄일 수 있다. 쓰기 증폭·읽기 증폭·공간 증폭과 정책을 함께 비교하며 “순차 쓰기라서 언제나 빠르다”로 단순화하지 않는다.

## Java 예제

```java
static class Store {
    final java.util.TreeMap<String, String> memory = new java.util.TreeMap<>();
    final java.util.List<java.util.NavigableMap<String, String>> runs =
            new java.util.ArrayList<>();

    void put(String key, String value) {
        memory.put(
                java.util.Objects.requireNonNull(key), java.util.Objects.requireNonNull(value));
    }

    void flush() {
        runs.add(0, new java.util.TreeMap<>(memory));
        memory.clear();
    }

    String get(String key) {
        if (memory.containsKey(key)) return memory.get(key);
        for (var run : runs) if (run.containsKey(key)) return run.get(key);
        return null;
    }
}

static void demo() {
    var store = new Store();
    store.put("a", "old");
    store.flush();
    store.put("a", "new");
    store.flush();
    System.out.println(store.get("a")); // new: 최신 run부터 조회
}
```

## 주의점

예제는 계층별 최신 값 찾기만 보이는 메모리 모델이다. WAL·디스크 저장·동시성·삭제·컴팩션은 구현하지 않았다. 실제 엔진의 파일 선택·스냅샷·Bloom filter·컴팩션 정책은 구현별로 확인한다.

## 꼬리질문

1. 같은 키가 두 SSTable에 있을 때 최신 값을 찾는 규칙이 없으면 어떤 문제가 생길까?
2. 메모리에서 키를 지우는 것만으로 삭제하면 오래된 파일의 값이 다시 보일 수 있는 이유는 무엇일까?
3. 컴팩션을 미루면 쓰기 비용 외에 읽기 비용과 디스크 공간은 어떻게 달라질까?

</details>

## 참고 자료

- [O’Neil 외 · LSM 논문](https://www.cs.umb.edu/~poneil/lsmtree.pdf) — 메모리·디스크 계층과 병합으로 쓰기 비용을 줄이는 원래 설계를 읽는다.
- [RocksDB · 구조 개요](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview) — WAL·MemTable·SST 파일·컴팩션을 실제 구현과 연결한다.
