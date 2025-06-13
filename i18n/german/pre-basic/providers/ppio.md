
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# PPIO Cloud

## Cherry Studio Integration mit PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Tutorial Übersicht <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio ist ein Multi-Model-Desktop-Client, der derzeit Unterstützung für Windows-, Linux- und macOS-Installationspakete bietet. Er vereint führende LLM-Modelle und bietet vielseitige KI-Assistenz. Mit intelligentem Gesprächsmanagement, Open-Source-Anpassung und Multi-Thema-Interface verbessern Nutzer ihre Arbeitseffizienz.

Cherry Studio ist nun tiefgreifend mit **PPIOs Hochleistungs-API** integriert – durch unternehmenssichere Rechenleistung für **DeepSeek-R1/V3 Blitzantworten** und **99,9 % Serviceverfügbarkeit**, für ein reibungsloses Erlebnis.

Nachfolgend die vollständige Anleitung (mit API-Schlüssel-Konfiguration), um den „Cherry Studio Smart Mode + PPIO Hochleistungs-API“ in nur 3 Minuten zu aktivieren.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. In Cherry Studio „PPIO“ als Modellanbieter hinzufügen <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Laden Sie Cherry Studio von der offiziellen Website herunter: [https://cherry-ai.com/download](https://cherry-ai.com/download) (Alternativ über Quark Cloud: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Klicken Sie unten links auf „Einstellungen“, wählen Sie als Anbieternamen: `PPIO` und bestätigen Sie mit „OK“.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Navigieren Sie zu [PPIO API-Schlüsselverwaltung](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), klicken Sie auf [Benutzeravatar] → [API-Schlüsselverwaltung].

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Klicken Sie auf [+ Erstellen], vergeben Sie einen Namen. **Der generierte Schlüssel wird nur einmalig angezeigt – speichern Sie ihn unbedingt!**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Fügen Sie in Cherry Studio den Schlüssel ein: Einstellungen → [PPIO Cloud] → API-Schlüssel einfügen → [Prüfen].

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Modellauswahl: z.B. deepseek/deepseek-r1/community. Andere Modelle können jederzeit gewechselt werden.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 und V3 community sind Vollversionen zum Testen. Für regelmäßige Nutzung **bitte auf Nicht-Community-Version wechseln** (Kontoaufladung erforderlich).

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Modellkonfiguration <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Nach erfolgreicher Verbindung ([Prüfen]-Bestätigung) ist das Modell einsatzbereit.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Klicken Sie auf [@], wählen Sie das DeepSeek R1-Modell unter PPIO – los geht‘s!

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

[Quellenhinweis: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)]

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Video-Tutorial: PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Für visuelle Lernende: Unser [Bilibili-Video](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2) zeigt Schritt-für-Schritt, wie Sie „PPIO API + Cherry Studio“ konfigurieren. Titel: **【Noch wütend über DeepSeek-Ladekreise?】PPIO Cloud + DeepSeek Vollversion = Kein Lag, sofortiger Start**.

[Videoquelle: sola]