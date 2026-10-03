# 프로세스와 스레드

> 프로세스는 실행 자원의 경계를, 스레드는 그 안의 실행 흐름을 제공한다.

- 프로세스별 주소 공간이 기본 격리 경계다.
- 스레드는 힙 등을 공유하고 실행 스택은 각자 갖는다.
- 공유에는 동기화 책임이 따른다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

프로그램 파일은 정적인 명령·데이터이고 프로세스는 실행 중인 인스턴스다. 운영체제는 실행 위치·레지스터·자원 정보를 관리한다. 여러 스레드는 같은 프로세스의 데이터를 쉽게 공유할 수 있지만 경합과 한 스레드의 오류가 영향을 줄 수 있다. 프로세스 사이에서는 IPC 같은 명시적 통신을 사용한다.

## Java 예제

```java
static void demo() throws InterruptedException {
    int[] shared = {0};
    Thread worker = new Thread(() -> shared[0] = 42);
    worker.start();
    worker.join();
    System.out.println(shared[0]); // 42: join으로 완료·가시성을 확인
    System.out.println(ProcessHandle.current().pid());
}
```

## 주의점

프로세스의 가상 주소 분리가 모든 자원 비공유를 뜻하지 않는다. 파일·공유 메모리 등은 별도 정책으로 공유할 수 있다.

## 꼬리질문

1. 스레드마다 스택이 있어도 힙 객체를 함께 수정하면 왜 문제가 생길까?
2. worker의 지역 변수와 shared 배열의 저장 공간은 어떻게 다를까?
3. join 없이 다른 스레드가 shared[0]을 읽으면 완료 시점과 가시성을 어떻게 보장해야 할까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
