# TCP와 UDP 선택

> TCP의 연결·바이트 스트림과 UDP의 데이터그램을 요구하는 지연·신뢰성·경계 조건으로 비교한다.

- UDP는 데이터그램 경계를 유지한다.
- UDP 자체는 전달·순서를 보장하지 않는다.
- 응용 계층에서 신뢰성을 추가할 수도 있다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

TCP는 연결 상태를 유지하며 바이트 순서와 손실 복구를 처리한다. UDP는 독립된 데이터그램을 보내고 누락·중복·순서 변경이 가능하다. 손실이 있어도 최신 정보가 중요하거나 별도 전송 제어를 구현하려는 응용에서는 UDP를 선택할 수 있다. QUIC처럼 UDP 위에서 신뢰성 있는 연결을 구현한 프로토콜도 있다. 따라서 UDP를 썼다는 사실만으로 시스템 전체가 신뢰성 없다고 판단하지 않는다.

## Java 예제

```java
import java.net.*;
import java.nio.charset.StandardCharsets;

static void send(InetAddress host, int port) throws java.io.IOException {
    byte[] data = "hello".getBytes(StandardCharsets.UTF_8);
    try (DatagramSocket socket = new DatagramSocket()) {
        socket.send(new DatagramPacket(data, data.length, host, port));
    }
} // send 성공은 수신·처리 확인이 아니다.
```

## 주의점

UDP가 항상 빠르거나 TCP가 실시간 서비스에 불가능하다는 식으로 단정하지 않는다. 혼잡 제어·패킷 크기·응용 설계도 결과를 좌우한다.

## 꼬리질문

1. UDP 위에서 순서와 재전송을 구현하면 어떤 책임이 애플리케이션으로 이동하는가?
2. UDP send가 예외 없이 반환해도 상대가 메시지를 받았다고 확정할 수 있을까?
3. 중복·순서·재전송을 추가하려면 패킷에 어떤 식별 정보와 응답 규칙을 넣어야 할까?

</details>

## 참고 자료

- [RFC 9293 · TCP](https://www.rfc-editor.org/rfc/rfc9293.html) — 바이트 스트림·연결 상태·재전송·윈도 의미를 확인한다.
- [RFC 1122 · Internet Host Requirements](https://www.rfc-editor.org/rfc/rfc1122.html) — 링크·인터넷·전송 계층의 책임을 확인한다.
