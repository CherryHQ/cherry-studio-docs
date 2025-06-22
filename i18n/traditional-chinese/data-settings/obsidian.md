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
該過程無需安裝額外的 Obsidian 外掛。但由於 Cherry Studio 匯入到 Obsidian 採用的原理與 Obsidian Web Clipper 類似，因此建議使用者最好將 Obsidian 升級至最新版本（當前 Obsidian 版本至少應大於 **1.7.2**），以免[如果對話過長造成匯入失敗](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0)。
{% endhint %}

## 最新教學

{% hint style="info" %}
相較舊版匯出到 Obsidian，新版匯出到 Obsidian 功能可以自動選擇庫路徑，不再需要手動輸入庫名、資料夾名。
{% endhint %}

### 第一步：配置 Cherry Studio

開啟 Cherry Studio 的_設定_ →  _資料設定_ → _Obsidian 設定_選單，下拉選單中會自動出現在本機開啟過的 Obsidian 庫名，選擇你的目標 Obsidian 庫：

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### 第二步：匯出對話

#### 匯出完整對話

回到 Cherry Studio 的對話介面，右鍵點擊對話，選擇_匯出_，點擊_匯出到 Obsidian_：

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

此時會彈出一個視窗，用於調整這條匯出到 Obsidian 中的對話筆記的 **Properties（屬性）、**所放置在Obsidian的**資料夾位置**以及匯出到 Obsidian 中的**處理方式：**

* **保管庫**：點擊下拉選單可以選擇其他 Obsidian 庫
* **路徑**：點擊下拉選單可以選擇存放匯出對話筆記的資料夾
* 作為 Obsidian 筆記屬性（Properties）：
  * 標籤（tags）
  * 建立時間（created）
  * 來源（source）
* 匯出到 Obsidian 中的**處理方式**有以下三種可選：
  * **新建（如果存在就覆蓋）**：在**路徑**處填寫的`資料夾` 裡新建一篇對話筆記，如果存在同名筆記則會覆蓋舊筆記
  * **前置**：在已存在同名筆記的情況下，將選中的對話內容匯出新增到該筆記的開頭
  * **追加**：在已存在同名筆記的情況下，將選中的對話內容匯出新增到該筆記的末尾

{% hint style="info" %}
只有第一種方式會附帶 Properties（屬性），後兩種方式不會附帶 Properties（屬性）。
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>配置筆記屬性</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>選擇路徑</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>選擇處理方式</p></figcaption></figure>

選擇完所有選項後，點選確定即可匯出完整對話到對應的 Obsidian 庫的對應資料夾。

#### 匯出單條對話

對於單條對話的匯出，則點擊對話下方的_三條槓選單_，選擇_匯出_，點擊_匯出到 Obsidian_：

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>匯出單條對話</p></figcaption></figure>

之後也會彈出與匯出完整對話時一樣的視窗，要求你配置**筆記屬性**與**筆記的處理方式**，一樣按照[上方的教學](obsidian.md#dao-chu-wan-zheng-dui-hua)完成即可。

### 匯出成功

🎉 到這裡，恭喜你完成了 Cherry Studio 聯動 Obsidian 的所有配置，並完整地將匯出流程走了一遍，enjoy yourselves!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>匯出到 Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>檢視匯出結果</p></figcaption></figure>

***

## 舊教學（適用於Cherry Studio\<v1.1.13）

### 第一步：準備 Obsidian

開啟 Obsidian 庫，建立一個用於儲存匯出對話的`資料夾`（圖中以 Cherry Studio 資料夾為例）：

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

注意記住左下角框出來的文字，這裡是你的`保管庫`名。

### 第二步：配置 Cherry Studio

在 Cherry Studio 的_設定_ →  _資料設定_ → _Obsidian 設定_選單中，輸入在[第一步](obsidian.md#di-yi-bu)中獲取到的`保管庫`名與`資料夾`名：

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

`全域標籤`處是可選的，可設定所有對話匯出後在 Obsidian 中的標籤，按需填寫。

### 第三步：匯出對話

#### 匯出完整對話

回到 Cherry Studio 的對話介面，右鍵點擊對話，選擇_匯出_，點擊_匯出到 Obsidian_。

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>匯出完整對話</p></figcaption></figure>

此時會彈出一個視窗，用於調整這條匯出到 Obsidian 中的對話筆記的 **Properties（屬性）**，以及匯出到 Obsidian 中的**處理方式**。匯出到 Obsidian 中的**處理方式**有以下三種可選：

* **新建（如果存在就覆蓋）**：在[第二步](obsidian.md#di-er-bu)中填寫的`資料夾` 裡新建一篇對話筆記，如果存在同名筆記則會覆蓋舊筆記
* **前置**：在已存在同名筆記的情況下，將選中的對話內容匯出新增到該筆記的開頭
* **追加**：在已存在同名筆記的情況下，將選中的對話內容匯出新增到該筆記的末尾

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>配置筆記屬性</p></figcaption></figure>

{% hint style="info" %}
只有第一種方式會附帶 Properties（屬性），後兩種方式不會附帶 Properties（屬性）。
{% endhint %}

#### 匯出單條對話

對於單條對話的匯出，則點擊對話下方的_三條槓選單_，選擇_匯出_，點擊_匯出到 Obsidian_。

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>匯出單條對話</p></figcaption></figure>

之後也會彈出與匯出完整對話時一樣的視窗，要求你配置**筆記屬性**與**筆記的處理方式**，一樣按照[上方的教學](obsidian.md#dao-chu-wan-zheng-dui-hua)完成即可。

### 匯出成功

🎉 到這裡，恭喜你完成了 Cherry Studio 聯動 Obsidian 的所有配置，並完整地將匯出流程走了一遍，enjoy yourselves!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>匯出到 Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>檢視匯出結果</p></figcaption></figure>