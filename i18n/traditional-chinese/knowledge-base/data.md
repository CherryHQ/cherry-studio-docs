---
icon: database
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 資料儲存說明

在 Cherry Studio 知識庫中添加的數據全部儲存在本機，在添加過程中會複製一份文件放在 Cherry Studio 資料儲存目錄。

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>知識庫處理流程圖</p></figcaption></figure>

向量資料庫：[https://turso.tech/libsql](https://turso.tech/libsql)

當文件被添加到 Cherry Studio 知識庫之後，文件會被切分為若干個片段，然後這些片段會交給嵌入模型進行處理。

當使用大模型進行問答的時候，會查詢和問題相關的文字片段一併交給大語言模型處理。

如果對資料隱私有要求，建議使用本機嵌入資料庫和本機大語言模型。