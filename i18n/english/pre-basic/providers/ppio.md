
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# PPIO Paiou Cloud

## Cherry Studio Integration with PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#tutorial-overview) Tutorial Overview <a href="#tutorial-overview" id="tutorial-overview"></a>

Cherry Studio is a multi-model desktop client currently supporting installation packages for Windows, Linux, and macOS systems. It integrates mainstream LLM models to provide multi-scenario assistance. Users can enhance work efficiency through smart conversation management, open-source customization, and multi-theme interfaces.

Cherry Studio is now deeply integrated with **PPIO's High-Performance API Channel** – leveraging enterprise-grade computing power to ensure **high-speed response for DeepSeek-R1/V3** and **99.9% service availability**, delivering a fast and smooth experience.

The tutorial below provides a complete integration solution (including API key configuration), enabling the advanced mode of **Cherry Studio Intelligent Scheduling + PPIO High-Performance API** within 3 minutes.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-enter-cherrystudio-add-ppio-as-model-provider)1. Enter Cherry Studio and Add "PPIO" as Model Provider <a href="#id-1-enter-cherrystudio-add-ppio-as-model-provider" id="id-1-enter-cherrystudio-add-ppio-as-model-provider"></a>

First download Cherry Studio from the official website: [https://cherry-ai.com/download](https://cherry-ai.com/download) (If inaccessible, download your required version from Quark Netdisk: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Click the settings icon in the bottom left corner, set the provider name to `PPIO`, and click "OK"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Visit [PPIO Computing Cloud API Key Management ](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), click 【User Avatar】→【API Key Management】 to enter console

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Click 【+ Create】 to generate a new API key. Customize a key name. **Generated keys are visible only at creation – immediately copy and save them to avoid affecting future usage**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) In Cherry Studio settings, select 【PPIO Paiou Cloud】, enter the API key generated on the official website, then click 【Verify】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Select model: using deepseek/deepseek-r1/community as example. Switch directly if needing other models.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 and V3 community versions are for trial use only. They are full-parameter models with identical stability and performance. For high-volume usage, **top up and switch to non-community versions**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-model-usage-configuration)2. Model Usage Configuration <a href="#id-2-model-usage-configuration" id="id-2-model-usage-configuration"></a>

(1) After clicking 【Verify】 and seeing successful connection, it's ready for use

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Finally, click 【@】 and select the newly added DeepSeek R1 model under PPIO provider to start chatting~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Partial material source: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-video-tutorial)3. PPIO×Cherry Studio Video Tutorial <a href="#id-3-ppio%C3%97cherry-studio-video-tutorial" id="id-3-ppio%C3%97cherry-studio-video-tutorial"></a>

For visual learners, we've prepared a Bilibili video tutorial. Follow step-by-step instructions to quickly master **PPIO API + Cherry Studio** configuration. Click the link to jump directly:  
→ [《Still going crazy over DeepSeek's endless spinning? PPIO Cloud + DeepSeek Full-Power Edition =? No more congestion, take off immediately》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Video material source: sola】