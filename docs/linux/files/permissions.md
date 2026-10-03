# 파일 권한과 실행 주체

> 파일 소유자·그룹·기타 사용자 권한과 실행 프로세스의 주체를 함께 확인한다.

- r·w·x는 대상이 파일인지 디렉터리인지에 따라 의미가 다르다.
- 실행 계정에 필요한 범위만 허용한다.
- 개인 키와 공개키를 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파일의 읽기·쓰기·실행 권한과 디렉터리의 목록·항목 변경·탐색 권한을 나누어 본다. 접근하려면 중간 경로 디렉터리의 탐색 권한도 필요하다. 운영 서비스 계정과 사람의 로그인 계정은 구분하고 필요한 경로만 열어 준다. SSH 개인 키는 공유 대상이 아니며 공개키는 서버의 authorized_keys에 등록한다.

## Java 예제

POSIX 권한을 지원하는 파일 시스템에서 지정한 파일의 권한을 변경한다.

```java
import java.nio.file.*;
import java.nio.file.attribute.PosixFilePermissions;

static void ownerOnly(Path file) throws java.io.IOException {
    Files.setPosixFilePermissions(file, PosixFilePermissions.fromString("rw-------")); // 600
}
```

## 주의점

권한 오류를 해결하려고 모든 경로를 777로 바꾸지 않는다. 파일 권한 외에도 ACL·보안 정책·서비스 사용자 조건이 있을 수 있다.

## 꼬리질문

1. 파일에 읽기 권한이 있어도 중간 디렉터리 권한 때문에 접근이 막힐 수 있는 이유는?
2. 600과 700은 파일·디렉터리에서 각각 어떤 접근을 허용할까?
3. 파일에 읽기 권한이 있어도 상위 디렉터리에 실행 권한이 없으면 어떤 경로 탐색이 막힐까?

</details>

## 참고 자료

- [GNU Coreutils · File Permissions](https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html) — 파일·디렉터리 권한과 소유권의 의미를 확인한다.
- [OpenSSH · Manual Pages](https://www.openssh.com/manual.html) — 키·서버 신원·접속 설정의 의미를 확인한다.
