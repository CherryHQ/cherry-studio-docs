---
icon: database
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 資料儲存說明

在 Cherry Studio 知識庫中新增的資料全部儲存在本地端，新增過程中會複製一份文件存放在 Cherry Studio 資料儲存目錄

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>知識庫處理流程圖</p></figcaption></figure>

向量資料庫：[https://turso.tech/libsql](https://turso.tech/libsql)

當文件被新增至 Cherry Studio 知識庫後，文件會被切分為多個片段，這些片段將交由嵌入模型進行處理

使用大型模型問答時，系統會檢索與問題相關的文字片段，一併交由大型語言模型處理

若對資料隱私有特殊要求，建議採用本地端嵌入資料庫與本地端大型語言模型