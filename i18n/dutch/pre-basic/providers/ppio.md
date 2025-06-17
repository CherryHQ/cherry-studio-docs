
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# PPIO Paiou Cloud

## Cherry Studio integratie met PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#handleiding-overzicht)Overzicht van de handleiding <a href="#handleiding-overzicht" id="handleiding-overzicht"></a>

Cherry Studio is een multi-model desktopclient die momenteel ondersteuning biedt voor: Windows, Linux en MacOS installatiepakketten. Het combineert mainstream LLM-modellen en biedt ondersteuning voor meerdere scenario's. Gebruikers kunnen hun werk efficiëntie verbeteren via intelligent gespreksbeheer, open-source aanpassingen en multi-thema-interfaces.

Cherry Studio is nu volledig geïntegreerd met het **PPIO high-performance API-kanaal** – met bedrijfsniveau rekencapaciteit garandeert het **DeepSeek-R1/V3 snelle responstijden** en **99,9% servicebeschikbaarheid**, wat zorgt voor een vlotte ervaring.

De onderstaande handleiding bevat een complete integratieoplossing (inclusief API-sleutelconfiguratie), waarmee u binnen 3 minuten de geavanceerde modus van "Cherry Studio intelligente planning + PPIO high-performance API" activeert.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-ga-naar-cherrystudio-voeg-ppio-toe-als-modelprovider)1. Ga naar CherryStudio en voeg "PPIO" toe als modelprovider <a href="#1-ga-naar-cherrystudio-voeg-ppio-toe-als-modelprovider" id="1-ga-naar-cherrystudio-voeg-ppio-toe-als-modelprovider"></a>

Download eerst Cherry Studio via de officiële website: [https://cherry-ai.com/download](https://cherry-ai.com/download) (indien niet bereikbaar, gebruik de Quark Cloud-schakel: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Klik op Instellingen linksonder, geef een aangepaste providernaam op: `PPIO`, klik op "Bevestigen"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Ga naar [Paiou Computing Cloud API-sleutelbeheer](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), klik op 【Gebruikersavatar】-【API-sleutelbeheer】om naar het dashboard te gaan

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Klik op 【+ Creëren】 om een nieuwe API-sleutel aan te maken. Geef een aangepaste sleutelnaam op. **De gegenereerde sleutel wordt alleen bij aanmaak getoond – kopieer en bewaar deze in een document om latere problemen te voorkomen**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Vul in CherryStudio de API-sleutel in: ga naar Instellingen, selecteer 【PPIO Paiou Cloud】, voer de op de website gegenereerde API-sleutel in en klik op 【Controleren】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Selecteer model: bijv. deepseek/deepseek-r1/community. Gebruik andere modellen door deze simpelweg te vervangen.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 en V3 community-versies zijn voor testdoeleinden (volledige parameteruitvoering). Voor productiegebruik moet u **rechargen en overschakelen naar de non-community versie**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-modelconfiguratie)2. Configuratie voor modelgebruik <a href="#2-modelconfiguratie" id="2-modelconfiguratie"></a>

(1) Klik op 【Controleren】 - bij succesvolle verbinding is het model direct bruikbaar

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Klik tenslotte op 【@】, selecteer het DeepSeek R1-model onder PPIO-provider en start uw gesprek~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Bronmateriaal: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-video-handleiding)3. Video-handleiding voor PPIO×Cherry Studio <a href="#3-video-handleiding" id="3-video-handleiding"></a>

Voor visueel leren vindt u op Bilibili een video-tutorial met stap-voor-stap uitleg over PPIO API+Cherry Studio configuratie. Klik op de link voor directe toegang → [《【Frustrated by DeepSeek buffering?】PPIO Cloud + DeepSeek full version = zero congestion》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Video-materiaal: sola】