# 음성 모델 개선의 코드·추론 옵션·프롬프트 구분

> 음성대화 개선은 프로그램 흐름, 인식 옵션, 모델 입력 지침을 바꾸는 작업일 수 있으며 반드시 모델 가중치를 학습하는 것은 아니다.

- **코드:** 취소·버퍼·턴 접수 순서 같은 서비스 동작을 바꾼다.
- **추론 입력:** STT 탐색 옵션·인식 힌트와 LLM 지침을 바꾼다.
- **학습:** 데이터와 최적화로 모델 가중치를 조정하는 별도 과정이다.

<details>
<summary>설명과 코드 예제 펼치기</summary>

## 설명

학습 질문: “무얼 변경했는지는 알겠는데 어떻게 했나? 코드를 바꿨나, AI 모델에 무언가를 했나?”

먼저 텍스트로 같은 이름·주제를 이어 묻고, 그다음 음성 경로를 비교한다. 사용자가 ‘튜닝’이라고 말했는데 전사문이 ‘트윙’이라면 STT 단계부터 점검해야 한다. 그 입력을 모델이 존재하는 서비스처럼 설명한다면 답변 모델의 근거 없는 추측도 별도 문제다. 모든 원인을 대화 기억 누락으로 단정하지 않는다.

## 인식 호출을 바꾸는 예제

Python의 faster-whisper가 설치되고 지원하는 Whisper 모델을 준비한 환경에서 사용하는 호출 예시다. 별도 전처리로 16kHz 음성을 준비하며, 정확도 향상을 보장하는 고정 설정은 아니다.

```python
# 기존 호출의 탐색 폭이 1이었다면 비교 실험에서 3으로 조정한다.
segments, info = recognizer.transcribe(
    audio,
    language="ko",
    beam_size=3,
    initial_prompt=recent_user_text[-240:] or None,
    condition_on_previous_text=False,
)
text = "".join(segment.text for segment in segments).strip()
```

`beam_size`는 디코딩 탐색 폭이다. `initial_prompt`는 인식 때 제공하는 텍스트 힌트다. 체크포인트를 그대로 두고 이 인자만 바꿀 수 있다. 같은 방의 최근 사용자 발화로 힌트를 만들면 용어 인식에 도움을 줄 수 있지만, 잘못된 힌트와 처리 시간도 함께 평가해야 한다. 다른 방의 문맥이 섞이지 않도록 요청별로 관리한다.

## LLM 지침과 실행 설정

에이전트 코드가 반환하는 지침 문자열에 ‘그걸 같은 지시어는 앞선 대상과 연결’, ‘사용자의 정정을 이전 추측보다 우선’, ‘모르는 약어를 임의 해석하지 말고 필요하면 확인’ 같은 규칙을 넣을 수 있다. 이는 매 호출의 입력을 바꾸는 작업이며 가중치 학습은 아니다.

Ollama Modelfile의 `FROM`은 베이스 모델을, `PARAMETER num_ctx`·`num_predict`·`temperature`는 실행 조건을 지정한다. 프로필 이름을 새로 만들거나 이 값을 설정한 것을 파인튜닝으로 부르지 않는다. 학습과 추론의 기본 구분은 [기존 모델 학습 설명](ocr-model-fine-tuning.md)을 함께 본다.

## 주의점

인식 탐색을 늘리면 정확도와 지연을 함께 측정해야 한다. 힌트나 프롬프트가 약어 인식·지침 준수·환각 문제를 항상 해결하지는 않는다. 실제 전사문, 모델에 전달한 문맥, 답변 내용, 사용자가 들은 음성을 구분해 평가한다. MCP는 도구 접근을, 스킬은 반복 절차를 돕는 개발 수단이며 모델 재학습 자체를 의미하지 않는다.

## 꼬리질문

1. 프로그램 코드·추론 옵션·프롬프트·가중치 학습은 각각 무엇을 바꾸는가?
2. ‘튜닝’이 다른 단어로 전사되고 답변도 엉뚱해졌다면 어떤 순서로 원인을 분리할 것인가?
3. 인식 후보나 문맥 힌트를 늘렸을 때 정확도뿐 아니라 어떤 지연·격리·오류 조건을 확인해야 하는가?

</details>

## 참고 자료

- [faster-whisper 전사 구현](https://github.com/SYSTRAN/faster-whisper/blob/master/faster_whisper/transcribe.py) — beam size·initial prompt·언어 옵션의 의미를 확인한다.
- [Ollama Modelfile Reference](https://docs.ollama.com/modelfile) — 모델 선택·추론 설정·입력 템플릿을 구분한다.
- [Skills와 MCP의 역할](https://developers.openai.com/plugins/concepts/skills) — 도구 연결과 재사용 작업 절차의 차이를 확인한다.
