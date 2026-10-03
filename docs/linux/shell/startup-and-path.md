# 셸 초기화와 PATH

> 셸 종류·실행 모드에 맞는 설정 파일과 PATH 검색 순서를 확인한다.

- zshrc는 대화형 zsh의 설정이다.
- PATH는 명령 검색 경로의 순서다.
- Bash와 zsh의 초기화 규칙을 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

대화형 셸·로그인 셸·스크립트 실행은 서로 다른 초기화 경로를 사용할 수 있다. macOS에서 zshrc에 둔 설정이 비대화형 배포 스크립트에 그대로 적용된다고 가정하지 않는다. PATH는 명령 이름을 찾는 순서를 정하므로 앞에 다른 실행 파일이 있으면 같은 명령도 다른 버전이 실행된다. 기존 PATH를 보존하고 추가 경로를 신뢰할 수 있는 위치로 제한한다.

## 예제

`command -v java`로 어떤 실행 파일을 고르는지 확인하고 `java -version`으로 실제 버전을 확인한다. 설정 변경 뒤 적절한 새 셸에서 다시 검사한다.

## 주의점

zsh 전용 설정을 Bash 스크립트에 복사하지 않는다. 공개 기록에는 개인 환경 파일의 키·접속 정보를 복사하지 않는다.

## 복습 질문

터미널에서는 실행되는 명령이 CI에서 안 보이면 어떤 초기화 차이를 확인할까?

자료 구분: **기존 자료** — 운영체제 강의와 SSH·셸·tmux 메모의 원리. **공식 자료 보완** — 매뉴얼의 실행 모드·반환값·권한 규칙.

</details>

## 참고 자료

- [Zsh · Startup Files](https://zsh.sourceforge.io/Doc/Release/Files.html) — 대화형·로그인 셸의 설정 파일 순서를 확인한다.
- [GNU Bash · Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) — 셸 확장·환경 변수·리다이렉션·초기화 규칙을 확인한다.
