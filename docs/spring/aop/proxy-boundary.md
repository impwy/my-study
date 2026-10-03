# AOP 프록시와 자기 호출

> Spring의 기본 프록시 방식에서는 프록시를 통과하는 호출에 부가 기능이 적용된다.

- 대상 객체와 프록시를 구분한다.
- 같은 객체 내부 호출은 프록시를 우회한다.
- 트랜잭션·비동기 경계를 실제 호출로 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

호출자가 컨테이너에서 받은 프록시를 호출하면 프록시는 대상 실행 앞뒤로 트랜잭션 등 부가 기능을 적용한다. 대상 메서드에서 `this.other()`를 호출하는 경로는 그 프록시를 다시 통과하지 않는다. 그래서 내부 메서드의 @Transactional에 기대한 새 경계가 생기지 않을 수 있다. 역할을 다른 빈으로 분리하거나 경계 위치를 바꾸어 외부 호출 경로를 분명히 한다.

## Java 예제

Spring의 기본 프록시 기반 AOP와 트랜잭션 관리 활성화를 가정한다.

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
static class OrderService {
    public void outer() {
        inner();
    } // this.inner(): 프록시를 지나지 않음

    @Transactional
    public void inner() {
        System.out.println("저장 작업");
    }
} // 프록시 방식에서 외부 빈이 주입받은 OrderService.inner()를 호출해야 advice 적용
```

## 주의점

메서드 접근 제어와 final 등 프록시 제약은 프록시 방식·버전에 따라 확인한다. AspectJ 방식과 기본 프록시 모드를 혼동하지 않는다.

## 꼬리질문

1. 어노테이션이 붙었는데 트랜잭션이 시작되지 않을 때 호출 경로에서 무엇을 확인할까?
2. outer에 트랜잭션이 없다면 inner의 어노테이션이 내부 호출에서 새 트랜잭션을 시작할까?
3. inner를 다른 서비스 빈으로 분리하면 호출 경로의 어느 지점에 프록시가 생길까?

</details>

## 참고 자료

- [Spring · @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) — 프록시 경계·롤백 조건·트랜잭션 속성을 확인한다.
