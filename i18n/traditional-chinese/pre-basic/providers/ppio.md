
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# PPIO 派歐雲

## Cherry Studio 接入 PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)教程概述 <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio 是一款多模型桌面客戶端，目前支援：Windows 、Linux 、MacOS 系電腦安裝包。它聚合主流 LLM 模型，提供多場景輔助。用戶可透過智能會話管理、開源客製化、多主題介面來提升工作效率。

Cherry Studio 現已與 **PPIO 高效能 API 通道** 深度適配——透過企業級算力保障，實現 **DeepSeek-R1/V3 高速響應** 與 **99.9% 服務可用性**，帶給您快速流暢的體驗。

下方教程包含完整接入方案（含金鑰配置），3 分鐘開啟「Cherry Studio 智能調度 + PPIO 高效能 API」的進階模式。

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. 進入 CherryStudio，添加 "PPIO" 作為模型提供商 <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

首先前往官網下載 Cherry Studio：[ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) （如果進不去可以打開下面的夸克網盤連結下載自己需要的版本：[https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

（1）先點擊左下角設定，自訂提供商名稱為：`PPIO`，點擊"確定"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

（2）前往 [派歐算力雲 API 金鑰管理](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio)，點擊【用戶頭像】—【API 金鑰管理】進入控制台

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

點擊 【+ 創建】按鈕來創建新的 API 金鑰。自訂一個金鑰名稱，**生成的金鑰僅在生成時顯示，務必複製並保存到文件中，以免影響後續使用**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

（3）在 CherryStudio 填入金鑰 點擊設定，選擇【PPIO 派歐雲】，輸入官網生成的 API 金鑰，最後點擊【檢查】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

（4）選擇模型：以 deepseek/deepseek-r1/community 為例，如需更換其他模型，可直接更換。

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 和 V3 community 版本僅供大家嚐鮮，也是全參數滿血版模型，穩定性和效果無差異，如需大量調用則須 **充值並切換到非 community 版本**。

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. 模型使用配置 <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

（1）點擊【檢查】顯示連接成功後即可正常使用

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

（2）最後點擊【@】選擇 PPIO 供應商下剛剛添加的 DeepSeek R1 模型，即可成功開始聊天～

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【部分素材來源：[ 陳恩 ](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. PPIO×Cherry Studio 影片使用教程 <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

若您更傾向直觀學習，我們在 B 站準備了影片教學。透過手把手教學，助您快速掌握「PPIO API+Cherry Studio」的配置方法，點擊下方連結直達影片，開啟流暢開發體驗 → [《 【還在為 DeepSeek 瘋狂轉圈抓狂？】派歐雲+DeepSeek 滿血版 =？不再擁堵，即刻起飛》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【影片素材來源：sola】