# 학습 기록 방법

질문·복습 답변은 로컬 초안으로 저장한다. **“이번 내용 정리해줘” / “아카이빙해줘”**를 요청하면 현재 대화의 초안을 검증해 게시한다.

| 요청 | 동작 |
| --- | --- |
| “volatile이 원자성을 보장해?” | 설명 후 초안 저장 |
| “이번 내용 정리해줘” | 현재 대화 초안 검증·게시 |
| “쌓인 내용 전체를 정리해줘” | 모든 대기 초안 검증·통합·게시 |
| “이번에는 기록하지 마” | 해당 답변 기록 제외 |
| 계획 모드 | 내용 검토만 수행 |

한 개념은 `docs/category/section/topic.md` 한 파일에 둔다. 동일 주제는 기존 내용을 보완하고 관련 개념은 링크한다. 제목·한 문장 요약·핵심 3개 이하·접힌 설명/예제/주의점/복습 질문·참고 링크와 읽을 이유를 사용한다.

기존 자료에서 확인한 내용과 공식 자료로 보완한 내용을 구분한다. 빈 노트·책 제목·향후 계획을 학습 내용으로 만들지 않는다. 실제 개념 본문이 없는 분류는 빈 목록을 유지한다. 프로젝트 링크는 자동으로 추가하지 않는다.

원본 파일·개인 경로·처리 목록·대화 초안은 로컬에 보관한다. 공개 저장소에는 재구성한 학습 내용과 공개 링크만 넣는다. 원본 책·강의 전문과 실습 정답을 전재하지 않는다.

게시 직전 최신 `main`을 읽고 문서·목록을 한 커밋으로 반영한다. 원격 문서가 바뀌었으면 내용을 다시 읽어 통합하고 한 번 재시도한다. 강제 푸시하지 않는다. 변경이 없으면 커밋하지 않고 실패 시 초안을 보존한다.

## 스킬

[스킬 원본](tools/my-study-archive/SKILL.md) · [분류 기준](tools/my-study-archive/references/categories.md) · [문서 템플릿](tools/my-study-archive/references/template.md)

개인 설치 원본은 `~/.codex/skills/my-study-archive`, 현재 탐색 경로는 `~/.agents/skills/my-study-archive`의 연결로 구성한다. 전역 `~/.codex/AGENTS.md`는 기술 학습에 이 스킬을 적용하도록 한다. 새 채팅에서 적용하며, 스킬이 보이지 않으면 Codex를 다시 시작한다.

스킬은 Codex가 선택·실행하는 작업 지침이다. 다른 앱의 대화까지 상시 수집하는 백그라운드 프로그램은 아니다. 스킬·전역 지침을 지원하는 이 컴퓨터의 Codex 대화에 적용된다.

Python 3·기존 `gh` 인증이 필요하다. `scripts/archive.py`는 초안 저장·목록 생성·게시·게시 없는 미리보기를 제공한다. 상태 경로는 `$CODEX_HOME/archives/my-study`이며 미설정 시 `~/.codex/archives/my-study`를 사용한다.

[공식 스킬 안내](https://learn.chatgpt.com/docs/build-skills) · [전역 지침 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
