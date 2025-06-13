---
icon: message
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Interfaccia di Conversazione

## Assistente e Argomenti

### Assistente

`Assistente` consente di personalizzare il modello selezionato con impostazioni specifiche come prompt predefiniti e parametri preconfigurati. Queste impostazioni aiutano ad allineare il modello alle aspettative del tuo lavoro.

`Assistente di sistema predefinito` offre parametri generici (senza prompt preconfigurato). Puoi utilizzarlo direttamente o cercare altri preset nella [pagina Agenti](agents.md).

### Argomenti

`Assistente` funge da insieme padre per gli `Argomenti`. Un singolo assistente può contenere più argomenti (cioè conversazioni). Tutti gli `Argomenti` condividono le impostazioni dell'assistente come parametri e prompt predefiniti.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Pulsanti nell'Area di Conversazione

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nuovo Argomento` Crea un nuovo argomento nell'assistente corrente.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Carica Immagine/Documento` Richiede supporto del modello per le immagini. I documenti vengono analizzati come testo contestuale.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Ricerca Web` Configurabile nelle impostazioni. I risultati vengono forniti come contesto al modello. Vedi [Modalità Online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` Attiva la knowledge base. Vedi [Tutorial Knowledge Base](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Server MCP` Attiva la funzionalità MCP. Vedi [Tutorial MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Genera Immagine` Non visibile di default. Richiesta attivazione manuale per modelli compatibili (es. Gemini).

{% hint style="info" %}
Per motivi tecnici, è necessaria l'attivazione manuale del pulsante. Sarà rimosso dopo ottimizzazioni.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Seleziona Modello` Cambia modello mantenendo il contesto della conversazione.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frasi Rapide` Utilizza frasi preimpostate. Supporta variabili.

![](../../.gitbook/assets/对话界面/清空消息.png) `Svuota Messaggi` Elimina tutti i contenuti dell'argomento.

![](../../.gitbook/assets/对话界面/展开.png) `Espandi` Allarga l'area di testo per input lunghi.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Pulisci Contesto` Rimuove il contesto precedente senza cancellare i messaggi.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Token Stimati` Mostra: contesto corrente, max contesto (∞=illimitato), caratteri input, token stimati.

{% hint style="info" %}
Solo stima indicativa. I token effettivi variano per modello.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduci` Traduce in inglese il contenuto corrente.

## Impostazioni Conversazione

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Impostazioni Modello

Sincronizzate con le impostazioni dell'assistente. Vedi [Modifica Assistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Queste impostazioni influiscono solo sull'assistente corrente. Altre impostazioni sono globali.
{% endhint %}

### Impostazioni Messaggi

#### <mark style="color:blue;">**`Linea Separatrice`**</mark>:
Separa corpo messaggio e pulsanti.

{% tabs %}
{% tab title="Attivo" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Disattivo" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usa Caratteri Serif`**</mark>：
Cambia stile caratteri. Personalizzabile via [CSS personalizzato](../../personalization-settings/).

#### <mark style="color:blue;">**`Numeri di Riga per Codice`**</mark>：
Mostra numeri di riga nei blocchi di codice.

{% tabs %}
{% tab title="Disattivo" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Attivo" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocchi Codice Pieghevoli`**</mark>：
Piega automaticamente blocchi di codice lunghi.

#### <mark style="color:blue;">**`A Capo Automatico per Codice`**</mark>：
Abilita a capo automatico per righe lunghe.

#### <mark style="color:blue;">**`Processo Ragionamento Pieghevole`**</mark>：
Piega automaticamente il ragionamento del modello.

#### <mark style="color:blue;">**`Stile Messaggi`**</mark>：
Bolle o lista.

#### <mark style="color:blue;">**`Stile Codice`**</mark>：
Personalizza visualizzazione blocchi codice.

#### <mark style="color:blue;">**`Motore Formule Matematiche`**</mark>：
* KaTeX: più veloce
* MathJax: più funzionale ma lento

#### <mark style="color:blue;">**`Dimensione Caratteri Messaggi`**</mark>：
Regola dimensione testo.

### Impostazioni Input

#### <mark style="color:blue;">**`Mostra Token Stimati`**</mark>：
Visualizza token stimati per testo inserito (indicativo).

#### <mark style="color:blue;">**`Incolla Testo Lungo come File`**</mark>：
Testi lunghi incollati appaiono come file separati.

#### <mark style="color:blue;">**`Rendering Markdown per Messaggi Input`**</mark>：
Attivo solo per risposte del modello per default.

{% tabs %}
{% tab title="Disattivo" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Attivo" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduci con 3 Spazi`**</mark>：
Tre spazi consecutivi traducono input in inglese.

{% hint style="warning" %}
Sovrascrive il testo originale.
{% endhint %}

#### <mark style="color:blue;">**`Lingua Obiettivo`**</mark>：
Imposta lingua per traduzioni.

## Impostazioni Assistente

Clic destro sull'<mark style="background-color:yellow;">assistente</mark> per modificare.

### Modifica Assistente

{% hint style="info" %}
Impostazioni valide per tutti i suoi argomenti.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Impostazioni Prompt

#### <mark style="color:blue;">**`Nome`**</mark>：
Personalizzabile.

#### <mark style="color:blue;">**`Prompt`**</mark>：
Testo prompt. Consulta la pagina Agenti per esempi.

#### Impostazioni Modello

#### <mark style="color:blue;">**`Modello Predefinito`**</mark>：
Modello fisso per l'assistente. Se vuoto, usa il [modello assistente predefinito](settings/default-models.md#mo-ren-zhu-shou-mo-xing).

{% hint style="info" %}
Priorità: modello assistente > modello globale.
{% endhint %}

#### <mark style="color:blue;">**`Ripristino Automatico Modello`**</mark>：
Al nuovo argomento:  
- **Attivo**: usa modello predefinito assistente  
- **Disattivo**: usa modello argomento precedente

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark> ：
Controlla creatività (default 0.7):
* **Bassa (0-0.3)**: output coerente (es. codici)
* **Media (0.4-0.7)**: equilibrio (es. dialoghi)
* **Alta (0.8-1.0)**: creatività (es. storytelling)

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>：
Default 1. Controlla diversità lessicale:
* **Basso (0.1-0.3)**: output conservativo
* **Medio (0.4-0.6)**: equilibrio
* **Alto (0.7-1.0)**: ricchezza lessicale

{% hint style="info" %}
Ottimizza combinando temperatura e Top P per ogni scenario.
{% endhint %}

#### <mark style="color:blue;">**`Finestra Contesto (Context Window)`**</mark>
Numero messaggi conservati:
* **5-10**: conversazioni semplici
* **>10**: task complessi (maggiore consumo token)

#### <mark style="color:blue;">**`Limite Lunghezza Messaggi (MaxToken)`**</mark>
Token massimi per risposta. Limiti tipici: 32k-64k tokens.

{% hint style="success" %}
Suggerimenti:
* Chat: 500-800
* Testi brevi: 800-2000
* Codici: 2000-3600
* Testi lunghi: >4000
{% endhint %}

{% hint style="warning" %}
Impostazioni troppo basse potrebbero troncare risposte.
{% endhint %}

#### <mark style="color:blue;">**`Output in Streaming (Stream)`**</mark>
Modalità output:
* **Attivo**: output graduale (effetto macchina da scrivere)
* **Disattivo**: output completo

{% hint style="info" %}
Disattivare per modelli incompatibili.
{% endhint %}

#### <mark style="color:blue;">**`Parametri Personalizzati`**</mark>
Aggiungi parametri API custom (es. `presence_penalty`). Riferimento: [documentazione](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Priorità: parametri custom > parametri integrati.  
Usare `<nome_parametro>:undefined` per disabilitare parametri.
{% endhint %}