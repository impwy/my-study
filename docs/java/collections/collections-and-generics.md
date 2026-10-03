# 컬렉션과 제네릭

> 컬렉션은 저장·탐색 방식으로 고르고, 제네릭으로 원소 타입의 계약을 표현한다.

- List는 순서, Set은 중복 제거, Map은 키 매핑에 맞는다.
- 임의 접근과 중간 삽입 비용을 구분한다.
- 제네릭 타입은 기본적으로 불공변이다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

ArrayList는 배열 기반이라 인덱스 접근이 빠르고 중간 삭제에는 이동이 필요하다. HashMap은 해시와 동등성으로 키를 찾으며 정렬 순서를 보장하지 않는다. TreeMap은 키 순서를 유지한다. `List<Dog>`는 `List<Animal>`의 하위 타입이 아니다. 그렇다면 다른 Animal을 넣어 Dog 목록의 계약을 깨뜨릴 수 있기 때문이다. 읽기나 쓰기 목적에 따라 와일드카드의 범위를 정한다.

## 예제

순서 있는 결과는 `List<String>`, 방문 여부는 `Set<Integer>`, 단어 빈도는 `Map<String,Integer>`로 표현한다. 중복을 제거하면서 정렬 순서도 필요하면 TreeSet을 검토한다.

## 주의점

equals가 같다고 판단한 두 객체는 같은 hashCode를 가져야 한다. 키의 동등성 관련 필드를 저장 후 바꾸면 해시 탐색이 깨질 수 있다.

## 복습 질문

HashMap과 TreeMap 중 어떤 요구사항이 선택을 가르는가?

자료 구분: **기존 자료** — Java 강의와 자료구조 노트의 언어·API 개념. **공식 자료 보완** — Java 21 명세·자원 및 참조 계약.

</details>

## 참고 자료

- [Java SE 21 · API 문서](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html) — 사용한 타입의 계약·예외·시간 비용 설명을 확인한다.
- [Java Language Specification 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) — 타입·호출·예외·언어 규칙을 정확한 명세로 확인한다.
