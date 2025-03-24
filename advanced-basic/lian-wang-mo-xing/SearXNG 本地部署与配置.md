CherryStudio 支持通过 SearXNG 进行网络搜索，SearXNG 是一个可本地部署的开源项目，所以与其他需要 API 提供商的配置方式略有不同。

**SearXNG项目链接**：[SearXNG](https://github.com/searxng/searxng)

## SearXNG的优势：
- 开源免费，无需API
- 隐私性相对较高
- 可高度定制化

## 本地部署 
SearXNG的部署方式既可以通过服务器部署也可以进行本地部署，为方便使用，本文档以最简单快捷的本地部署为例以满足最低使用门槛需求。

### 一、Docker 直接部署
由于SearXNG不需要复杂的环境配置，可以不用docker compose，只需要简单提供一个空闲端口即可部署，所以最快捷的方式可以使用 Docker 直接拉取镜像进行部署。
#### 1. 下载安装并配置 [docker](https://www.docker.com/) 
<figure><img src="../../.gitbook/assets/searxng_config_img_01.png"></figure>

安装后选择一个镜像存储路径：
<figure><img src="../../.gitbook/assets/searxng_config_img_02.png"></figure>
#### 2.搜索并拉取SearXNG镜像
搜索栏输入 **searxng** ：
<figure><img src="../../.gitbook/assets/searxng_config_img_03.png"></figure>

拉取镜像：
<figure><img src="../../.gitbook/assets/searxng_config_img_04.png"></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_05.png"></figure>

#### 3.运行镜像
拉取成功后来到 **images** 页面：
<figure><img src="../../.gitbook/assets/searxng_config_img_06.png"></figure>

选择拉取的镜像点击运行：
<figure><img src="../../.gitbook/assets/searxng_config_img_07.png"></figure>

打开设置项进行配置：
<figure><img src="../../.gitbook/assets/searxng_config_img_08.png"></figure>

以 8085 端口为例：
<figure><img src="../../.gitbook/assets/searxng_config_img_09.png"></figure>

运行成功后点击链接即可打开SearXNG的前端界面：
<figure><img src="../../.gitbook/assets/searxng_config_img_10.png"></figure>

出现这个页面说明部署成功：
<figure><img src="../../.gitbook/assets/searxng_config_img_11.png"></figure>


### Cherry Studio 相关配置
SearXNG本地部署成功，接下来是CherryStudio的相关配置。

来到网络搜索设置页面，选择 Searxng ：
<figure><img src="../../.gitbook/assets/searxng_config_img_12.png"></figure>

直接输入本地部署的链接发现验证失败，此时不用担心：
<figure><img src="../../.gitbook/assets/searxng_config_img_13.png"></figure>

因为直接部署后默认并没有配置json返回类型，所以无法获取数据，需要修改配置文件。

回到Docker，来到Files标签页找到镜像中找到带标签的文件夹：
<figure><img src="../../.gitbook/assets/searxng_config_img_14.png"></figure>

展开后继续往下翻，会发现另一个带标签的文件夹：
<figure><img src="../../.gitbook/assets/searxng_config_img_15.png"></figure>

继续展开，找到 **settings.yml** 配置文件：
<figure><img src="../../.gitbook/assets/searxng_config_img_16.png"></figure>

点击打开文件编辑器：
<figure><img src="../../.gitbook/assets/searxng_config_img_17.png"></figure>

找到 78 行，可以看到类型只有一个html
<figure><img src="../../.gitbook/assets/searxng_config_img_18.png"></figure>

添加 json 类型后保存，重新运行镜像
<figure><img src="../../.gitbook/assets/searxng_config_img_19.png"></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_20.png"></figure>

重新回到Cherry Studio 进行验证，验证成功：
<figure><img src="../../.gitbook/assets/searxng_config_img_21.png"></figure>

地址既可以填写本地： http://localhost : 端口号
也可以填写 docker 地址：http://host.docker.internal : 端口号

### 其他配置
此时SearXNG已具备默认联网搜索能力，如需定制搜索引擎需要自行进行配置

需要注意的是此处首选项并不能影响大模型调用时的配置
<figure><img src="../../.gitbook/assets/searxng_config_img_22.png"></figure>

如需配置需要大模型调用的搜索引擎，需在配置文件中设置：
<figure><img src="../../.gitbook/assets/searxng_config_img_23.png"></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_24.png"></figure>

配置语言参考：
<figure><img src="../../.gitbook/assets/searxng_config_img_25.png"></figure>

若内容太长直接修改不方便，可将其复制到本地IDE中，修改后粘贴到配置文件中即可。