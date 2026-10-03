# 파일 시스템과 버퍼링

> 경로·파일 메타데이터·데이터 블록을 분리하고 메모리 버퍼와 저장 확정의 차이를 이해한다.

- 디렉터리는 이름과 파일을 연결한다.
- 파일 접근과 디스크 I/O는 일대일이 아니다.
- 캐시·버퍼·복구 정책을 함께 본다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파일 시스템은 이름 공간과 메타데이터로 파일을 찾고 데이터 블록을 관리한다. 메모리 캐시·버퍼를 사용하면 반복 접근 비용을 줄이지만 애플리케이션 쓰기 완료와 저장 장치의 내구성 확정은 같은 시점이라고 보장되지 않는다. 장애 뒤 일관성을 유지하는 저널·로그 등의 역할을 구분한다. 저장 매체가 HDD인지 SSD인지에 따라 스케줄링의 물리적 비용도 달라진다.

## Java 예제

지정한 실습 파일을 덮어쓴다. 실제 내구성은 파일 시스템·장치 조건과 메타데이터 처리까지 확인한다.

```java
import java.nio.*;
import java.nio.channels.*;
import java.nio.file.*;

static void save(Path path, byte[] data) throws java.io.IOException {
    try (FileChannel c =
            FileChannel.open(
                    path,
                    StandardOpenOption.CREATE,
                    StandardOpenOption.WRITE,
                    StandardOpenOption.TRUNCATE_EXISTING)) {
        ByteBuffer b = ByteBuffer.wrap(data);
        while (b.hasRemaining()) c.write(b);
        c.force(true);
    }
}
```

## 주의점

메모리 버퍼를 비웠다는 사실만으로 전원 장애에도 데이터가 남는다고 단정하지 않는다. 제품·파일 시스템·API의 동기화 계약을 확인한다.

## 꼬리질문

1. 파일 쓰기 함수가 반환했는데 장애 후 일부 데이터가 없을 수 있는 이유는?
2. write 반환과 force 완료는 데이터가 어느 계층까지 전달되었다는 의미가 다를까?
3. 새 파일 생성이나 rename의 장애 내구성에는 파일 내용 외에 어떤 디렉터리 메타데이터도 고려해야 할까?

</details>

## 참고 자료

- [OSTEP · 무료 교재](https://pages.cs.wisc.edu/~remzi/OSTEP/) — 해당 주제의 프로세스·가상 메모리·동시성 장을 골라 읽는다.
