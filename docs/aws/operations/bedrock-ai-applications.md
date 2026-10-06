# Amazon Bedrock과 교육 AI Agent

> Bedrock은 기반 모델을 활용하는 AWS 관리형 서비스이며 Agent는 모델·자료·도구를 연결해 작업을 수행하는 시스템이다.

- Bedrock은 하나의 AI 모델이 아니라 여러 기반 모델을 활용하는 서비스다.
- 자료 검색·모델 호출·도구 실행은 Agent 구성에서 별도 역할을 가진다.
- 모델·리전·기능 지원과 품질·지연·비용을 함께 확인한다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

Amazon Bedrock은 생성형 AI 애플리케이션을 만들도록 기반 모델 접근과 관련 기능을 제공하는 AWS 관리형 서비스다. Foundation Model(기반 모델)은 다양한 작업의 출발점이 되는 모델을 뜻한다. Bedrock에서 제공하는 맞춤 학습 방식과 지원 모델은 기능별로 확인해야 한다.

| 방법 | 무엇을 바꾸는가 |
| --- | --- |
| 프롬프트 개선 | 입력·지시·출력 형식 |
| RAG | 필요한 자료를 검색해 모델 입력에 제공 |
| 파인튜닝 | 학습 데이터로 모델 파라미터 조정 |
| Agent 구성 | 모델·자료·도구 호출과 작업 흐름 연결 |

교육 Agent는 학습 자료를 검색해 설명하거나 문제를 만들고, 답안을 평가해 다음 과제를 제안하는 시스템으로 구성할 수 있다. 이는 가능한 예시이며 모델 호출만으로 모든 기능이 자동 완성되는 것은 아니다. 자료의 근거, 평가 기준, 사용할 도구와 실패 처리를 정의한다.

## 주의점

AWS 문서에서 기존 Bedrock Agents Classic은 신규 고객에게 열려 있지 않다고 안내하며 관련 기능을 검토할 때 AgentCore를 안내한다. AgentCore는 Agent의 구축·실행·운영을 위한 서비스군이다. 실제 도입 전 계정·리전·모델의 지원 조건을 확인한다.

모델 학습과 Agent 개발은 다른 작업이다. 같은 평가 사례로 모델·입력 길이·재시도 정책을 비교하고 성공률·지연·사용량에 따른 비용을 함께 측정한다. 특정 호출의 비용을 모든 기능의 고정 단가로 사용하지 않는다. [OCR 모델 파인튜닝](../../cloud/resources/ocr-model-fine-tuning.md)과도 목적을 구분한다.

## 꼬리질문

1. 모델 자체와 Bedrock 서비스, Agent 작업 흐름은 각각 어떤 책임을 가지는가?
2. 교육 Agent가 자료 검색·문제 출제·답안 평가를 수행하려면 어떤 근거와 평가 기준을 연결해야 할까?
3. 더 저렴한 모델이나 짧은 입력으로 바꿀 때 비용 외에 어떤 품질·지연·지원 조건을 확인할까?

</details>

## 참고 자료

- [AWS · Amazon Bedrock FAQ](https://aws.amazon.com/bedrock/faqs/) — 기반 모델 접근과 RAG·맞춤 학습의 서비스 범위를 확인한다.
- [AWS · Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) — 기존 Agent 서비스의 동작과 신규 고객 안내를 확인한다.
- [AWS · Bedrock AgentCore Overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) — Agent 구축·실행·운영 구성 요소를 확인한다.
