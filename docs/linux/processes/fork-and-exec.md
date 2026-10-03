# fork와 exec

> fork는 자식 프로세스를 만들고 exec는 현재 프로세스의 실행 이미지를 새 프로그램으로 바꾼다.

- 부모에는 자식 PID, 자식에는 0이 반환된다.
- 주소 공간은 독립적으로 이어진다.
- wait로 자식 종료 상태를 회수한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

fork 이후 부모와 자식은 각자의 실행 흐름으로 돌아간다. 실제 메모리 복사는 copy-on-write 등의 구현으로 최적화될 수 있지만 변수 변경이 보통 서로의 주소 공간을 직접 수정하는 것은 아니다. 열린 파일 기술자는 복사되어 같은 열린 파일 설명을 참조할 수 있다. exec가 성공하면 새 프로그램으로 교체되므로 기존 호출 다음으로 정상 반환하지 않는다.

## 예제

셸은 자식에서 exec로 명령을 실행하고 부모는 적절히 wait한다. 원래 일지의 “부모에서 PID 0” 메모는 반대로 수정했다.

## 주의점

fork 실패는 -1이다. 다중 스레드 프로세스에서 fork 이후 exec 전 실행 가능한 동작에는 제약이 있으므로 별도로 확인한다.

## 복습 질문

fork의 반환값으로 부모와 자식의 실행 분기를 어떻게 나누는가?

자료 구분: **기존 자료** — 운영체제 강의와 SSH·셸·tmux 메모의 원리. **공식 자료 보완** — 매뉴얼의 실행 모드·반환값·권한 규칙.

함께 복습: [프로세스와 스레드](../../operating-systems/processes/process-thread.md) · [프로세스 상태와 문맥 교환](../../operating-systems/processes/context-switch.md)

</details>

## 참고 자료

- [Linux man-pages · fork](https://man7.org/linux/man-pages/man2/fork.2.html) — 반환값·상속 자원·다중 스레드 제약을 확인한다.
- [Linux man-pages · execve](https://man7.org/linux/man-pages/man2/execve.2.html) — 프로그램 교체와 반환·유지되는 상태를 확인한다.
