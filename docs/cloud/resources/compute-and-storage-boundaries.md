# 컴퓨팅과 블록·파일·객체 스토리지

> 애플리케이션의 실행 자원과 데이터 보관 자원을 나누고 접근 방식에 맞는 스토리지를 선택한다.

- CPU·메모리 용량과 저장 용량·IOPS는 다른 자원이다.
- 블록·파일·객체는 데이터에 접근하는 인터페이스가 다르다.
- 인스턴스 종료와 데이터 삭제의 관계는 서비스 설정으로 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

컴퓨팅은 코드를 실행하는 CPU·메모리 자원이고 스토리지는 데이터를 보관하는 자원이다. 블록 스토리지는 디스크처럼 제공되어 보통 파일시스템을 얹는다. 파일 스토리지는 경로·디렉터리로 접근하며 여러 클라이언트가 공유하는 용도로 쓰인다. 객체 스토리지는 버킷과 키로 객체를 읽고 쓰며 일반적인 디스크의 임의 위치 갱신과 계약이 다르다.

데이터베이스 디스크, 공유 파일, 이미지 업로드를 같은 저장 방식으로 취급하지 않는다. AWS에서는 EBS·EFS·S3가 각각의 대표 예다. 계산 자원을 늘려도 느린 디스크나 잘못된 접근 패턴이 자동으로 해결되지는 않는다.

## Java 예제

버킷·키로 객체를 찾는 메모리 모델이다. 실제 클라우드 저장이나 내구성을 구현하지 않는다.

```java
record ObjectKey(String bucket, String key) {}

static void demo() {
    var objects = new java.util.HashMap<ObjectKey, byte[]>();
    var key = new ObjectKey("images", "users/42/profile.png");
    objects.put(key, new byte[] {1, 2, 3});
    System.out.println(objects.get(key).length); // 3
    System.out.println(objects.containsKey(new ObjectKey("images", "users/42"))); // false
}
```

## 주의점

객체 키의 /는 일반적으로 디렉터리 경로가 아니라 키의 일부다. 복제·내구성·백업·인스턴스 종료 시 볼륨 삭제 정책은 별개로 확인한다. 단순 저장 용량 외에 처리량·지연 시간·요청 비용도 비교한다.

## 꼬리질문

1. 객체 키가 users/42/profile.png라면 users/42라는 디렉터리 객체도 자동으로 생길까?
2. 데이터베이스 파일과 사용자 업로드 사진에 같은 저장소를 쓰기 전에 무엇을 확인할까?
3. 컴퓨팅 인스턴스를 삭제해도 데이터를 보존하려면 어떤 수명 주기 설정을 확인해야 할까?

</details>

## 참고 자료

- [AWS · 스토리지 개요](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html) — EBS·EFS·S3의 접근 방식과 사용 목적을 비교한다.
