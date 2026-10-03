# GitHub Actions 이벤트·잡·행렬

> 이벤트가 워크플로를 시작하고 matrix와 needs가 잡의 실행 조합과 순서를 정한다.

- 한 잡의 steps는 순서대로 실행된다.
- matrix는 여러 설정 조합으로 잡을 확장한다.
- needs는 선행 잡과의 의존 관계를 선언한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

workflow_dispatch는 수동 실행 이벤트이며 push·pull_request 등은 조건에 맞는 이벤트로 워크플로를 시작한다. 각 잡은 지정한 runner에서 실행된다. steps는 같은 잡 안에서 순서를 갖지만 별도 잡의 파일·프로세스 상태를 그대로 공유한다고 가정하지 않는다.

os 2개와 Java 버전 2개의 matrix는 제외 조건이 없다면 4개 조합을 만든다. needs: check를 둔 잡은 선행 잡의 완료를 기다리며 기본적으로 선행 잡이 성공해야 실행된다. 산출물 전달은 artifacts, 작은 결과 값 전달은 outputs 같은 명시적인 방법을 사용한다.

## Java 예제

설정 조합을 생성하는 모델이다. 워크플로는 아래 YAML로 작성한다.

```java
record Job(String os, int javaVersion) {}

static java.util.List<Job> matrix() {
    var jobs = new java.util.ArrayList<Job>();
    for (String os : java.util.List.of("ubuntu-latest", "windows-latest")) {
        for (int version : new int[] {17, 21}) jobs.add(new Job(os, version));
    }
    return java.util.List.copyOf(jobs); // 4개 조합
}
```

### 워크플로로 확인

별도 연습 저장소의 `.github/workflows/java-matrix.yml`에 저장한다.

```yaml
name: Java matrix practice
on: workflow_dispatch
jobs:
  check:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        java: [17, 21]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-java@v6
        with:
          distribution: temurin
          java-version: ${{ matrix.java }}
      - run: java -version
  report:
    needs: check
    runs-on: ubuntu-latest
    steps:
      - run: echo "All combinations succeeded"
```

## 주의점

행렬 확대는 실행 시간과 사용량을 늘린다. 선행 실패 시 report가 기본적으로 건너뛰어진다는 점을 확인한다. 아래 예제는 Java 환경만 확인하며 프로젝트 빌드·테스트를 수행하지 않는다.

## 꼬리질문

1. OS 2개·Java 버전 3개의 matrix를 만들면 잡이 몇 개 생성될까?
2. 선행 check가 실패했을 때 needs를 둔 report는 기본적으로 실행될까?
3. check에서 만든 JAR 파일을 다른 잡에서 쓰려면 어떤 전달 방법이 필요할까?

</details>

## 참고 자료

- [GitHub · 잡 사용](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs) — steps·needs·잡 간 의존 조건을 확인한다.
- [GitHub · matrix](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations) — 조합 확장과 include·exclude·동시성 제어를 읽는다.
- [actions/setup-java](https://github.com/actions/setup-java) — 지원하는 Java 배포판·버전과 사용 예제를 확인한다.
