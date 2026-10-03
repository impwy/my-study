# tmux와 원격 작업 관찰

> 원격 접속과 작업 세션을 분리하고 로그·프로세스 상태로 실제 실행을 확인한다.

- session·window·pane을 구분한다.
- detach와 프로세스 종료는 다르다.
- 서비스 수명은 별도 관리 정책이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

tmux는 서버 프로세스가 유지되는 동안 터미널 세션을 보존하며 분리했다가 다시 붙을 수 있게 한다. session 안에 window와 pane을 나누어 작업·로그를 볼 수 있다. SSH 연결이 끊겨도 tmux 안의 작업을 계속 둘 수 있지만 서버 재부팅·프로세스 종료에 대한 영속 실행 관리를 대신하지 않는다. 운영 서비스는 서비스 관리자와 재시작·로그 정책을 검토한다.

## 예제

`tmux new -s study`로 시작하고 detach한 뒤 `tmux attach -t study`로 돌아온다. 작업 완료 여부는 창 존재가 아니라 로그와 종료 상태로 확인한다.

## 주의점

운영 작업을 남겨 둔 tmux에 중요한 비밀이 보이지 않게 한다. kill-session은 작업을 종료할 수 있으므로 detach와 구분한다.

## 복습 질문

SSH 재접속이 가능한 것과 서버 재부팅 후 작업 복원이 가능한 것은 왜 다른가?

자료 구분: **기존 자료** — 운영체제 강의와 SSH·셸·tmux 메모의 원리. **공식 자료 보완** — 매뉴얼의 실행 모드·반환값·권한 규칙.

</details>

## 참고 자료

- [tmux · Getting Started](https://github.com/tmux/tmux/wiki/Getting-Started) — 세션·창·패널과 attach·detach 사용법을 확인한다.
