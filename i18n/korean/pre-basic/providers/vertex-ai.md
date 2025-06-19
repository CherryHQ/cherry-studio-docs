---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# Vertex AI

## 튜토리얼 개요

### 1. APIKey 획득 방법

* Gemini API 키를 획득하려면 먼저 Google Cloud 프로젝트가 필요합니다(이미 보유한 경우 이 단계 건너뛰기).
* [Google Cloud](https://console.cloud.google.com/projectcreate)에서 프로젝트를 생성하고, 프로젝트명을 입력한 후 "프로젝트 만들기" 버튼을 클릭하세요.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI 콘솔](https://console.cloud.google.com/vertex-ai)로 이동합니다.
* 생성한 프로젝트 내에서 [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)를 활성화하세요.

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API 접근 권한 설정

* [서비스 계정](https://console.cloud.google.com/iam-admin/serviceaccounts) 권한 페이지에서 새 서비스 계정을 생성하세요.

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* 서비스 계정 관리 페이지에서 방금 생성한 계정을 찾아 `키`를 클릭한 후 새로운 JSON 형식 키를 생성하세요.

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* 생성 완료 시 키 파일이 JSON 형식으로 자동 다운로드됩니다. **이 파일을 안전하게 보관해 주세요.**

## 3. Cherry Studio에서 Vertex AI 설정

1. Vertex AI 서비스 제공업체를 선택하세요.
2. JSON 파일의 해당 필드 값을 입력하세요.

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[모델 추가](https://console.cloud.google.com/vertex-ai/model-garden)를 클릭하면 바로 사용하실 수 있습니다!\\