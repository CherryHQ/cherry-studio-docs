
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# ByteDance (Doubao)

*   Accedi a [Volc Engine](https://console.volcengine.com/)
*   Fai clic diretto [qui per accedere immediatamente](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Ottenere la chiave API

*   Fai clic su [Gestione chiavi API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) nella barra laterale inferiore
*   Crea una chiave API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   Dopo la creazione riuscita, fai clic sull'icona dell'occhio accanto alla chiave API creata per visualizzarla e copiala

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Incolla la chiave API copiata in CherryStudio, quindi attiva l'interruttore del fornitore di servizi.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Attivare e aggiungere modelli

*   Attiva i modelli necessari in [Gestione attivazioni](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) nella parte inferiore della barra laterale della Console Ark. Qui puoi attivare su richiesta la serie Doubao e modelli come DeepSeek.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   Nel [documento dell'elenco dei modelli](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), trova l'ID modello corrispondente al modello desiderato.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Esempio elenco ID modello Volc Engine"><figcaption></figcaption></figure>

*   Apri le impostazioni [Servizio modelli](../../cherrystudio/preview/settings/providers.md) di Cherry Studio e trova Volc Engine
*   Fai clic su Aggiungi, quindi incolla l'ID modello ottenuto nella casella di testo ID modello

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Aggiungi i modelli uno per uno seguendo questo processo

### Indirizzo API

L'indirizzo API può essere scritto in due modi

*   Il primo è quello predefinito del client: `https://ark.cn-beijing.volces.com/api/v3/`
*   Il secondo modo è: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Non c'è differenza tra i due metodi, mantieni l'impostazione predefinita senza modifiche.

Per la differenza tra la terminazione `/` e `#`, consulta la sezione Indirizzo API nelle impostazioni del fornitore del servizio, [clicca per andare](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Esempio cURL nella documentazione ufficiale</p></figcaption></figure>