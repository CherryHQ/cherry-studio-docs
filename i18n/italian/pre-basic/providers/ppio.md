
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# PPIO Paiou Cloud

## Cherry Studio Integration with PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Panoramica del Tutorial <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio è un client desktop multimodello che attualmente supporta: pacchetti di installazione per computer Windows, Linux e MacOS. Aggrega modelli LLM mainstream, offrendo assistenza in scenari multiuso. Gli utenti possono migliorare l'efficienza lavorativa grazie a: gestione intelligente delle conversazioni, personalizzazione open-source e interfacce a più temi.

Cherry Studio è ora pienamente compatibile con i **canali API ad alte prestazioni di PPIO**—garantendo potenza di calcolo enterprise per **DeepSeek-R1/V3 a risposta ultraveloce** e **99.9% di disponibilità del servizio**, offrendoti un'esperienza fluida.

Il tutorial qui sotto contiene la soluzione di integrazione completa (inclusa configurazione API key). In 3 minuti attiverai la modalità avanzata di "Cherry Studio + API ad alte prestazioni PPIO".

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Entra in CherryStudio e aggiungi "PPIO" come fornitore di modelli <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Scarica Cherry Studio dal sito ufficiale: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (se non accessibile, usa il link Quark: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Clicca l'icona impostazioni in basso a sinistra. Imposta un nome personalizzato per il provider: `PPIO`, poi clicca "Conferma"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Vai alla [gestione API key di PPIO](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio). Clicca [Avatar utente] → [Gestione API Key] per accedere al pannello di controllo

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Clicca [+ Crea] per generare una nuova API key. Assegna un nome e **copia immediatamente la chiave (visibile solo alla creazione)**. Conservala per uso futuro.

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) In CherryStudio: Seleziona provider [PPIO], inserisci l'API key generata e clicca [Verifica]

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Seleziona un modello, ad esempio: deepseek/deepseek-r1/community. Per cambiare modello, modifica direttamente l'impostazione.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

> Le versioni community di DeepSeek R1/V3 sono gratuite per test, ma **per uso intensivo è necessaria ricarica per le versioni non community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Configurazione modello <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Dopo verifica connessione riuscita, il modello è pronto all'uso

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Clicca [@], seleziona il modello DeepSeek R1 sotto il provider PPIO, e inizia a chattare!

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

> [Fonte parziale: Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Tutorial video PPIO×Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Per apprendimento visivo, abbiamo preparato un video su Bilibili. Impara rapidamente a configurare "PPIO API+Cherry Studio": [《 DeepSeek lento? PPIO + DeepSeek full-speed = niente attese! 》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

> [Fonte video: sola]