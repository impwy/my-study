# 분류 기준

정확한 경로는 categories.json의 slug와 sections 키를 쓴다. 문서는 `docs/category/section/topic.md`이다. 제목은 한국어, 파일명은 안정된 영문 소문자·하이픈이다.

- 원리를 다루면 CS 분류, 제품의 구체적인 구현·옵션이면 제품 분류를 선택한다. 예: 트랜잭션의 ACID → database, InnoDB gap lock → mysql.
- Java의 일반 스레드 사용·메모리 모델·동기화 → java-concurrency, 운영체제의 자원·스케줄링 → operating-systems.
- HTTP 전송·프로토콜 → network, 리소스·멱등·API 계약 → rest-api.
- Spring 컨테이너·MVC·트랜잭션 → spring, 자동 설정·프로파일·운영 엔드포인트 → spring-boot, 객체 영속화·조회 → jpa.
- 시스템의 데이터 복제·일관성·배치/스트림 처리 → ddia. 책 제목만 발견했다고 책을 읽은 내용으로 만들지 않는다.
- Linux 명령·프로세스 운영 → linux, Git 기록 관리 → git, CI/CD 워크플로 → github-actions.
- 일반 클라우드 개념 → cloud, AWS 서비스 구체 동작 → aws.
- 같은 개념이 둘 이상의 분야와 관련되면 가장 직접적인 분류에 한 파일만 두고 다른 문서에서 상대 링크를 건다.
- 현재 28개 분류 밖의 주제는 가장 적합한 분류가 없는지 먼저 확인하고 사용자에게 새 분류가 필요한 이유를 설명한다. 임의 slug를 만들어 게시하지 않는다.

자료 없음은 빈 소분류로 남긴다. 강의 수강·도서 보유·학습 계획과 실제 개념 노트를 구분한다.
