---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# Vertex AI

## نظرة عامة على البرنامج التعليمي

### 1. الحصول على مفتاح API

* قبل الحصول على مفتاح Gemini API، يجب أن يكون لديك مشروع Google Cloud (يمكنك تخطي هذه الخطوة إذا كنت تملكه بالفعل)
* انتقل إلى [Google Cloud](https://console.cloud.google.com/projectcreate) لإنشاء مشروع، املأ اسم المشروع وانقر على "إنشاء مشروع"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* انتقل إلى [لوحة تحكم Vertex AI](https://console.cloud.google.com/vertex-ai)
* فعّل [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) داخل المشروع الذي أنشأته

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. تهيئة أذونات الوصول إلى API

* افتح صفحة أذونات [حسابات الخدمة](https://console.cloud.google.com/iam-admin/serviceaccounts) وقم بإنشاء حساب خدمة

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* في صفحة إدارة حسابات الخدمة، ابحث عن حساب الخدمة الذي أنشأته للتو، انقر على `المفاتيح` وقم بإنشاء مفتاح جديد بتنسيق JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* بعد الإنشاء بنجاح، سيتم حفظ ملف المفتاح تلقائيًا كملف JSON على جهازك، يُرجى **الحفاظ عليه بأمان**

## 3. تكوين Vertex AI في Cherry Studio

* اختر موفر خدمة Vertex AI
* املأ الحقول المقابلة في ملف JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

انقر لإضافة [نموذج](https://console.cloud.google.com/vertex-ai/model-garden)، ويمكنك البدء في الاستخدام بسعادة!