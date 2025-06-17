---
icon: database
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 데이터 저장 설명

Cherry Studio 지식 베이스에 추가되는 데이터는 모두 로컬에 저장됩니다. 추가 과정에서 문서의 사본이 Cherry Studio 데이터 저장 디렉토리에 복사됩니다.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>지식 베이스 처리 흐름도</p></figcaption></figure>

벡터 데이터베이스: [https://turso.tech/libsql](https://turso.tech/libsql)

문서가 Cherry Studio 지식 베이스에 추가된 후, 파일은 여러 조각으로 분할되며, 이러한 조각들은 임베딩 모델에서 처리됩니다.

대규모 언어 모델을 사용해 질문에 답변할 때는 관련 텍스트 조각을 검색하여 대규모 언어 모델에 함께 전달합니다.

데이터 프라이버시 요구사항이 있는 경우, 로컬 임베딩 데이터베이스와 로컬 대규모 언어 모델 사용을 권장합니다.