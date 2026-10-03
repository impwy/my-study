# TCP 바이트 스트림과 메시지 경계

> TCP는 순서 있는 바이트 스트림을 제공하므로 응용 메시지의 경계는 애플리케이션이 정해야 한다.

- 한 번의 write와 한 번의 read는 대응하지 않는다.
- 순서 번호·확인 응답·재전송이 신뢰성을 지원한다.
- 길이·구분자·고정 크기 등으로 프레이밍한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

애플리케이션이 100바이트를 두 번 보내도 수신자는 200바이트를 한 번에 읽거나 더 작은 조각으로 읽을 수 있다. TCP 세그먼트 경계는 응용 메시지 경계가 아니다. 수신 코드는 아직 부족한 바이트를 기다리고, 이미 받은 버퍼에서 여러 메시지를 꺼낼 수 있어야 한다. 길이 기반 프레이밍은 헤더를 먼저 읽고 허용한 범위 안의 본문 길이를 확인하는 방식이다.

## Java 예제

```java
import java.io.*;

static byte[] readFrame(DataInputStream in) throws IOException {
    int length = in.readInt(); // 송신 측도 4바이트 길이 접두어 사용
    if (length < 0 || length > 1024 * 1024) throw new IOException("invalid length");
    byte[] message = new byte[length];
    in.readFully(message);
    return message;
}

static void writeFrame(DataOutputStream out, byte[] message) throws IOException {
    out.writeInt(message.length);
    out.write(message);
    out.flush();
}
```

## 주의점

연결 성공은 상대의 업무 처리 성공을 뜻하지 않는다. 타임아웃·정상 종료·재시도 시 중복 업무 효과는 응용 프로토콜에서 다룬다.

## 꼬리질문

1. 두 번 보낸 메시지가 한 번의 read로 들어와도 왜 TCP 오류가 아닌가?
2. readFully를 한 번의 read로 바꾸면 일부만 도착한 메시지를 어떻게 잘못 처리할까?
3. 길이 제한 없이 원격 입력대로 배열을 할당하면 어떤 자원 고갈이 가능할까?

함께 복습: [TCP와 UDP 선택](tcp-and-udp.md) · [HTTP 메서드와 상태 코드](../http-tls/http-semantics.md)

</details>

## 참고 자료

- [RFC 9293 · TCP](https://www.rfc-editor.org/rfc/rfc9293.html) — 바이트 스트림·연결 상태·재전송·윈도 의미를 확인한다.
