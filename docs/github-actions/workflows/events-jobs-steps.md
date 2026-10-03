# 워크플로·이벤트·잡·스텝

> 이벤트가 워크플로를 시작하고 잡이 실행 환경을 가지며 스텝이 순서대로 작업한다.

- 워크플로는 YAML로 정의한다.
- 잡 사이에는 needs로 의존성을 둔다.
- 스텝의 실패와 실행 조건을 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

push·pull_request·수동 실행 등 이벤트와 필터로 실행 조건을 정한다. 각 잡은 지정한 runner에서 실행되고 잡 안의 스텝은 순차 실행된다. 잡들은 needs 등 의존이 없으면 병렬 실행될 수 있으며 파일 시스템을 당연히 공유하지 않는다. 코드 checkout·런타임 준비·테스트·산출물 전달을 필요한 범위로 구성한다.

## Java 예제

Actions의 Java 스텝에서 실행하는 코드다. 이벤트·잡 선언 자체는 워크플로 YAML에서 설정한다.

```java
static void context() {
    for (String key :
            new String[] {"GITHUB_EVENT_NAME", "GITHUB_JOB", "GITHUB_SHA", "GITHUB_WORKSPACE"})
        System.out.println(key + "=" + System.getenv(key));
}
```

## 주의점

학습용 예제의 권한·이벤트 조건을 운영에 그대로 복사하지 않는다. action의 신뢰성과 버전 고정·토큰 권한도 확인한다.

## 꼬리질문

1. 같은 워크플로의 두 잡이 서로의 파일을 자동으로 볼 수 없는 이유는?
2. GITHUB_SHA를 기록하면 빌드 산출물이 어느 코드에서 만들어졌는지 어떻게 연결할 수 있을까?
3. needs로 잡 순서를 연결해도 파일은 자동 공유되지 않는데 어떤 전달 방식이 필요할까?

</details>

## 참고 자료

- [GitHub · Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — 이벤트·잡·스텝·권한·의존 관계의 정확한 문법을 확인한다.
