
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# ByteDance (Doubao)

*   Melden Sie sich bei [Volcano Engine](https://console.volcengine.com/) an
*   Direkt [hier klicken](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D), um dorthin zu gelangen

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### API-Schlüssel abrufen

*   Klicken Sie in der Seitenleiste auf [API Key Management](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey)
*   Erstellen Sie einen API-Schlüssel

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   Nach erfolgreicher Erstellung klicken Sie auf das Augensymbol neben dem erstellten API-Schlüssel, um ihn anzuzeigen und zu kopieren

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Fügen Sie den kopierten API-Schlüssel in CherryStudio ein und aktivieren Sie den Schalter des Dienstanbieters

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Modelle aktivieren und hinzufügen

*   Aktivieren Sie die benötigten Modelle unter [Activation Management](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) im Bereich der Seitenleiste der Ark-Konsole. Hier können Sie nach Bedarf die Doubao-Serie, DeepSeek und andere Modelle aktivieren

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   Finden Sie die entsprechende **Model ID** für das benötigte Modell im [Model List Documentation](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Beispiel für Modell-ID-Liste von Volcano Engine"><figcaption></figcaption></figure>

*   Öffnen Sie die [Model Service](../../cherrystudio/preview/settings/providers.md)-Einstellungen in Cherry Studio und suchen Sie nach Volcano Engine
*   Klicken Sie auf "Hinzufügen" und fügen Sie die zuvor erhaltene **Model ID** in das Textfeld "Model ID" ein

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Fügen Sie Modelle nacheinander gemäß diesem Workflow hinzu

### API-Adresse

Es gibt zwei Schreibweisen für die API-Adresse:

*   Erste Variante (Client-Standard): `https://ark.cn-beijing.volces.com/api/v3/`
*   Zweite Variante: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Beide Schreibweisen sind funktional gleichwertig. Belassen Sie die Standardeinstellung, Änderungen sind nicht erforderlich.  

Weitere Details zu den Unterschieden zwischen Endungen mit `/` und `#` finden Sie im API-Adressabschnitt der Dienstanbieterkonfiguration unter [hier](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>cURL-Beispiel aus der offiziellen Dokumentation</p></figcaption></figure>