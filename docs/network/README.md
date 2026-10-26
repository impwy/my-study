# 네트워크

[전체 목록](../../README.md)

## TCP/IP

| 문서 | 한 줄 요약 |
| --- | --- |
| [CIDR와 경로 선택](tcp-ip/cidr-and-forwarding.md) | 주소의 네트워크 접두어와 라우팅 테이블의 가장 긴 일치로 다음 홉을 결정한다. |
| [TCP/IP 계층과 라우팅](tcp-ip/layers-and-routing.md) | 주소·경로·전송·응용 규약의 책임을 나누어 데이터가 상대 애플리케이션까지 가는 흐름을 설명한다. |
| [링크 계층과 오류 검출](tcp-ip/ethernet-and-error-control.md) | 같은 링크의 프레임 전달·매체 접근·오류 검출을 종단 간 전송 보장과 구분한다. |

## TCP·UDP

| 문서 | 한 줄 요약 |
| --- | --- |
| [AI 전화 상담의 음성 파이프라인: STT·TTS와 speech-to-speech](transport/ai-call-voice-pipeline.md) | 전화 상담은 통화 음성을 서버로 연결한 뒤 STT → LLM → TTS로 처리하거나, 음성을 직접 이해하고 응답하는 speech-to-speech 방식으로 구성한다. |
| [RTP: 실시간 음성의 순서와 재생 시점을 전달하기](transport/rtp.md) | RTP는 음성·영상 패킷에 순서 번호와 타임스탬프 등을 붙여 수신 측의 실시간 재생을 돕지만, 전달 성공이나 지연을 보장하지 않는다. |
| [SIP: 통화의 시작·변경·종료를 제어하는 신호](transport/sip.md) | SIP는 누구와 어떤 조건으로 통화할지 제어하는 시그널링 프로토콜이며, 실제 음성은 별도의 미디어 경로로 흐른다. |
| [SRTP: 실시간 통화 미디어 보호하기](transport/srtp.md) | SRTP는 RTP 미디어에 기밀성·메시지 인증·재전송 공격 방지 기능을 제공하며, 통화 제어 신호의 TLS 보호와는 적용 구간이 다르다. |
| [TCP 바이트 스트림과 메시지 경계](transport/tcp-byte-stream.md) | TCP는 순서 있는 바이트 스트림을 제공하므로 응용 메시지의 경계는 애플리케이션이 정해야 한다. |
| [TCP와 UDP 선택](transport/tcp-and-udp.md) | TCP의 연결·바이트 스트림과 UDP의 데이터그램을 요구하는 지연·신뢰성·경계 조건으로 비교한다. |
| [흐름 제어와 혼잡 제어](transport/flow-and-congestion-control.md) | 수신자가 받을 수 있는 양과 네트워크가 감당할 수 있는 양을 각각 고려해 전송을 조절한다. |

## DNS

| 문서 | 한 줄 요약 |
| --- | --- |
| [DNS 이름 해석](dns/name-resolution.md) | 리졸버는 캐시와 계층적 권한 서버를 이용해 이름에 해당하는 레코드를 찾는다. |

## HTTP·TLS

| 문서 | 한 줄 요약 |
| --- | --- |
| [CORS와 브라우저 출처](http-tls/cors.md) | CORS는 다른 출처의 응답을 웹 페이지에 공유할 수 있는지 정하며 서버 인증·인가와 별개다. |
| [HTTP 메서드와 상태 코드](http-tls/http-semantics.md) | HTTP의 메서드·상태 코드는 요청 의도와 결과를 전달하는 공통 계약이다. |
| [SSE와 WebSocket 및 STOMP의 역할](http-tls/websocket-and-stomp.md) | SSE는 HTTP 응답으로 서버 이벤트를 전달하고, WebSocket은 양방향 메시지를 교환하며, STOMP는 메시지의 명령·구독·목적지를 정의한다. |
| [TLS와 HTTPS](http-tls/tls-handshake.md) | TLS는 상대 인증·키 합의로 만든 보안 채널에 HTTP를 실어 전송 중 데이터를 보호한다. |

