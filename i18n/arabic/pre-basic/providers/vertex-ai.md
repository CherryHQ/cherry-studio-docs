---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# Vertex AI

## نظرة عامة على البرنامج التعليمي

### 1. الحصول على مفتاح API

*   قبل الحصول على مفتاح api الخاص بـ Gemini، يجب أن يكون لديك مشروع Google Cloud (إذا كان لديك بالفعل، يمكن تخطي هذه الخطوة)
*   انتقل إلى [Google Cloud](https://console.cloud.google.com/projectcreate) لإنشاء مشروع، املأ اسم المشروع وانقر على إنشاء مشروع

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   انتقل إلى [لوحة تحكم Vertex AI](https://console.cloud.google.com/vertex-ai)
*   قم بتمكين [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) داخل المشروع الذي تم إنشاؤه

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. إعداد أذونات الوصول إلى API

*   افتح صفحة أذونات [حسابات الخدمة](https://console.cloud.google.com/iam-admin/serviceaccounts) وقم بإنشاء حساب خدمة

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   في صفحة إدارة حسابات الخدمة، ابحث عن حساب الخدمة الذي تم إنشاؤه حديثاً، انقر على `المفاتيح` وقم بإنشاء مفتاح جديد بتنسيق JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   بعد الإنشاء بنجاح، سيتم حفظ ملف المفتاح تلقائياً على جهازك بتنسيق ملف JSON، يرجى **الحفظ بعناية**

## 3. تهيئة Vertex AI في Cherry Studio

*   اختر موفر خدمة Vertex AI
*   قم بملء الحقول المقابلة من ملف JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

انقر على إضافة [نموذج](https://console.cloud.google.com/vertex-ai/model-garden)، ويمكنك البدء في الاستخدام بسعادة!