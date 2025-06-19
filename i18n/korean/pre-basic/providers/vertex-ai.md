---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# Vertex AI

## 튜토리얼 개요

### 1. API 키 가져오기

* Gemini의 API 키를 가져오기 전에 Google Cloud 프로젝트가 필요합니다(이미 있는 경우 이 과정은 건너뛸 수 있음)
* [Google Cloud](https://console.cloud.google.com/projectcreate)에 접속하여 프로젝트를 생성하고, 프로젝트 이름을 입력한 후 "프로젝트 만들기" 클릭

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI 콘솔](https://console.cloud.google.com/vertex-ai)로 이동
* 생성한 프로젝트에서 [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) 활성화

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

### 2. API 접근 권한 설정

* [서비스 계정](https://console.cloud.google.com/iam-admin/serviceaccounts) 권한 페이지에서 서비스 계정 생성

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* 서비스 계정 관리 페이지에서 새로 생성한 서비스 계정을 찾아 `키`를 클릭하고 새로운 JSON 형식 키 생성

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* 생성 성공 시 키 파일이 JSON 형식으로 자동 다운로드되며, **안전하게 보관하세요**

### 3. Cherry Studio에서 Vertex AI 설정

* Vertex AI 서비스 공급자 선택
* JSON 파일의 해당 필드 입력

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[모델](https://console.cloud.google.com/vertex-ai/model-garden) 추가 후 바로 사용을 시작할 수 있습니다!