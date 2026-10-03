# S3 객체와 저장소 선택

> S3는 객체를 키로 저장하며 블록·공유 파일 저장소와 접근 모델이 다르다.

- 버킷·객체 키·메타데이터를 구분한다.
- 버전 관리·수명 주기·접근 정책을 설계한다.
- 폴더 모양의 접두어는 파일 시스템 디렉터리와 다르다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

S3 객체는 키와 데이터·메타데이터로 관리하며 API로 접근한다. EBS는 서버의 블록 장치, EFS는 공유 파일 접근을 제공하는 다른 모델이다. 필요한 업데이트·공유·용량·접근 방식에 따라 고른다. S3의 버전 관리와 수명 주기로 변경 복구·보존·저장 클래스를 관리할 수 있다. 공개 접근은 버킷 정책과 차단 설정을 명확히 확인한다.

## Java 예제

AWS SDK for Java 2.x s3 모듈과 구성된 클라이언트·권한이 필요하다.

```java
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.HeadObjectRequest;

static long size(S3Client s3, String bucket, String key) {
    return s3.headObject(HeadObjectRequest.builder().bucket(bucket).key(key).build())
            .contentLength();
} // 객체는 bucket+key로 식별; 디렉터리 파일 핸들이 아니다.
```

## 주의점

백업을 업로드했다는 사실과 복구가 가능한지는 다르다. 권한·버전·암호화 키·보존 정책을 함께 확인한다.

## 꼬리질문

1. S3와 EBS를 “그냥 저장 공간”으로만 비교하면 어떤 접근 방식의 차이를 놓치는가?
2. key에 /가 포함되어도 일반 파일 시스템의 디렉터리와 같지 않은 이유는 무엇일까?
3. 객체 목록을 한 번만 조회하면 1000개가 넘는 결과를 어떻게 놓칠 수 있을까?

</details>

## 참고 자료

- [AWS · S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) — 객체·버킷·버전·수명 주기와 접근 제어를 확인한다.
- [AWS · EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) — AMI·인스턴스·스토리지·네트워크 수명을 확인한다.
- [Java API 사용 안내](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html) — S3 객체 조회와 Java 클라이언트 사용 예제를 확인한다.
