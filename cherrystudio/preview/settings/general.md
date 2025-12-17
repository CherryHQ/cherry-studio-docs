---
icon: sliders
---

# 常规设置

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

#### 第一部分：基础环境配置 <a href="#headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-yi-bu-fen-ji-chu-huan-jing-pei-zhi-chang-gui-she-zhi-0" id="headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-yi-bu-fen-ji-chu-huan-jing-pei-zhi-chang-gui-she-zhi-0"></a>

这部分决定了软件的显示语言、网络连接方式及渲染性能。

**1. 语言 (Language)**

* **功能详解：** 切换软件界面的显示语言。

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

* **支持列表：** 点击右侧下拉菜单可见，支持 **简体中文、繁体中文、英语、德语、日语、俄语、希腊语、西班牙语、法语、葡萄牙语**。
* **💡 使用场景：** 如果您习惯阅读英文技术文档或为了截图给国外开发者反馈问题，可在此切换。

**2. 代理模式 (Proxy Mode)**

* **功能详解：**
  * **系统代理 (System Proxy):** 软件会自动跟随您的 Windows/macOS 系统的网络设置。如果您在电脑上开启了全局加速器，软件会自动使用该网络。
* **💡 关键提示：** Cherry Studio 主要是调用 OpenAI、Claude 等海外模型 API。**如果您遇到“连接超时”、“API 请求失败”等红色报错**，请首先检查您的电脑软件是否开启，并确认此处是否为“系统代理”。

**3. 拼写检查 (Spell Check)**

* **功能详解：** 开启后，在对话框输入文本时，系统会自动检测拼写错误（主要针对英文单词），并在错误单词下显示红色波浪线。
* **💡 建议：**
  * 如果您经常用**英文**与 AI 对话，建议**开启**。
  * 如果您主要使用**中文**，建议**关闭**，以免出现误报干扰视觉。

**4. 禁用硬件加速 (Disable Hardware Acceleration)**

* **功能详解：** Cherry Studio 基于 Electron 框架开发，默认利用显卡（GPU）来渲染界面以获得更流畅的体验。开启此开关意味着**强制使用 CPU 渲染**。
* **⚠️ 故障排查专用：** 正常情况下请**保持关闭**（即滑块为灰色）。
* **何时需要开启？** 如果您的软件出现以下画面问题，请开启此选项并重启软件：
  * 软件界面黑屏、白屏或闪烁。
  * 界面字体模糊或撕裂。
  * 在配置较低的电脑上操作明显卡顿。

***

#### 第二部分：消息与提醒 (通知设置) <a href="#headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-er-bu-fen-xiao-xi-yu-ti-xing-tong-zhi-she-zhi-0" id="headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-er-bu-fen-xiao-xi-yu-ti-xing-tong-zhi-she-zhi-0"></a>

控制软件在后台运行时如何打扰您。

**1. 助手消息 (Assistant Message)**

* **功能详解：** 当您切换到其他软件工作，而 AI 终于生成完长篇回复时，系统会弹出通知提醒您。
* **💡 建议：** **开启**。特别是使用推理模型（如 o1）或生成长文时，避免枯燥等待。

**2. 备份 (Backup)**

* **功能详解：** 当软件进行数据自动备份或手动备份完成时发送通知。
* **💡 建议：** **开启**。确保您知道数据是否安全存档。

**3. 知识库 (Knowledge Base)**

* **功能详解：** 知识库构建索引通常比较耗时，开启后，索引构建完成会通知您。
* **💡 建议：** **开启**。

***

#### 第三部分：软件行为习惯 (启动与托盘) <a href="#headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-san-bu-fen-ruan-jian-xing-wei-xi-guan-qi-dong-yu-tuo-pan" id="headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-san-bu-fen-ruan-jian-xing-wei-xi-guan-qi-dong-yu-tuo-pan"></a>

这部分设置决定了 Cherry Studio 是像“微信”一样常驻后台，还是像普通软件一样用完即走。

**1. 启动 (Startup)**

* **开机自动启动：**
  * **开启场景：** 如果 Cherry Studio 是您的主力生产力工具，建议开启，开机即用。
* **启动时最小化到托盘：**
  * **配合使用：** 通常配合“开机自启”使用。开启后，开机时软件会在后台静默启动，不会直接弹出主窗口挡住桌面，保持桌面整洁。

**2. 托盘 (System Tray)**

* **显示托盘图标：**
  * 建议始终**开启**。方便在右下角快速唤出软件或查看状态。
* **关闭时最小化到托盘 (关键设置)：**
  * **开启 (🟢)：** 点击窗口右上/左上的 `X` 关闭按钮时，软件**不会退出**，而是缩到右下角托盘。这样下次打开也是“秒开”，且正在进行的对话不会中断。
  * **关闭 (⚪)：** 点击 `X` 就是彻底杀掉进程退出软件。
  * **💡 强烈建议：** **开启**。保持软件常驻后台体验最佳。

***

#### 第四部分：高级选项 <a href="#headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-si-bu-fen-gao-ji-xuan-xiang-0" id="headingc1f7c3c4e1e6438d82ae1f2c59b65b95-di-si-bu-fen-gao-ji-xuan-xiang-0"></a>

**1. 隐私设置**

* **匿名发送错误报告和数据统计：**
  * 开启此项有助于开发者修复 Bug。数据是完全匿名的（不包含您的聊天记录和 API Key），建议开启以支持开源项目发展。

**2. 开发者模式**

* **启用开发者模式：**
  * **功能：** 开启后，可能会在界面上显示更多的调试信息（例如原始的 Prompt 数据包、Token 计算细节等），或者允许访问尚未完全发布的测试功能。
  * **💡 建议：** 普通用户建议**关闭**，以免界面出现过多看不懂的技术参数，影响沉浸式体验。

***

#### 📝 总结：推荐设置方案 <a href="#headingc1f7c3c4e1e6438d82ae1f2c59b65b95-zong-jie-tui-jian-she-zhi-fang-an-0" id="headingc1f7c3c4e1e6438d82ae1f2c59b65b95-zong-jie-tui-jian-she-zhi-fang-an-0"></a>

* **极客/重度用户：**
  * [x] &#x20;开机自动启动
  * [x] &#x20;关闭时最小化到托盘
  * [x] &#x20;禁用硬件加速（仅在画面异常时）
  * [x] &#x20;启用开发者模式
* **普通/办公用户：**
  * [ ] &#x20;开机自动启动 (按需)
  * [x] &#x20;关闭时最小化到托盘 (强烈推荐)
  * [x] &#x20;助手消息通知
  * [ ] &#x20;拼写检查 (主要用中文则关闭)
