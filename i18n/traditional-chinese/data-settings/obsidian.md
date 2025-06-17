---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# Obsidian 配置教學

Cherry Studio 支援與 Obsidian 聯動，將完整對話或單條對話匯出到 Obsidian 庫中。

{% hint style="warning" %}
此過程無需安裝額外的 Obsidian 外掛。但由於 Cherry Studio 導入 Obsidian 的原理與 Obsidian Web Clipper 類似，建議用戶務必將 Obsidian 升級至最新版本（當前版本至少應大於 **1.7.2**），以避免[對話過長時導入失敗](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0)。
{% endhint %}

## 最新教學

{% hint style="info" %}
相較舊版匯出功能，新版匯出至 Obsidian 功能可自動選擇庫路徑，不再需要手動輸入庫名與資料夾名稱。
{% endhint %}

### 第一步：配置 Cherry Studio

開啟 Cherry Studio 的_設置_ →  _數據設置_ → _Obsidian 配置_選單，下拉框會自動顯示本機開啟過的 Obsidian 庫名稱，選擇目標庫：

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### 第二步：匯出對話

#### 匯出完整對話

在對話介面右鍵點擊對話，選擇_匯出_ → _匯出到 Obsidian_：

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

彈出視窗可調整以下設定：
* **保管庫**：下拉選單切換其他庫
* **路徑**：下拉選單選擇存放資料夾
* **筆記屬性（Properties）**：
  * 標籤（tags）
  * 建立時間（created）
  * 來源（source）
* **處理方式**（三選一）：
  * **新建（如果存在就覆蓋）**：在目標資料夾新建筆記（覆蓋同名筆記）
  * **前置**：將內容新增至同名筆記開頭
  * **追加**：將內容新增至同名筆記末尾

{% hint style="info" %}
僅「新建」模式會附加屬性（Properties），其餘兩種模式不會附加。
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>配置筆記屬性</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>選擇路徑</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>選擇處理方式</p></figcaption></figure>

確認所有設定後點擊「確定」即可匯出。

#### 匯出單條對話

點擊單條對話下方的_三條橫槓選單_，選擇_匯出_ → _匯出到 Obsidian_：

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>匯出單條對話</p></figcaption></figure>

後續配置與[匯出完整對話流程](obsidian.md#dao-chu-wan-zheng-dui-hua)相同。

### 匯出成功

🎉 恭喜完成所有配置！您已成功整合 Cherry Studio 與 Obsidian，好好享受吧！

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>匯出到 Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>查看匯出結果</p></figcaption></figure>

***

## 舊版教學（適用 Cherry Studio < v1.1.13）

### 第一步：準備 Obsidian

建立專用資料夾（範例命名為 "Cherry Studio"），並複製左下角_保管庫名稱_：

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

### 第二步：配置 Cherry Studio

在 _設置_ → _數據設置_ → _Obsidian 配置_ 輸入保管庫名稱與資料夾名稱：

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

「全域標籤」為選填項，可設定所有匯出筆記的預設標籤。

### 第三步：匯出對話

#### 匯出完整對話

對話列表右鍵點擊，選擇_匯出_ → _匯出到 Obsidian_：

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>匯出完整對話</p></figcaption></figure>

選擇處理方式：
* **新建（覆蓋同名筆記）**
* **前置**
* **追加**

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>配置筆記屬性</p></figcaption></figure>

{% hint style="info" %}
僅「新建」模式附加 Properties 屬性。
{% endhint %}

#### 匯出單條對話

透過單條對話的_三條橫槓選單_啟動匯出：

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>匯出單條對話</p></figcaption></figure>

操作流程與[完整對話匯出](obsidian.md#dao-chu-wan-zheng-dui-hua)一致。

### 匯出成功

🎉 恭喜完成所有設定！立即體驗無縫整合的工作流吧！

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>匯出到 Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>查看匯出結果</p></figcaption></figure>