---
icon: cloud-check
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Impostazioni del provider

Questa pagina descrive solo le funzionalità dell'interfaccia. Per le istruzioni di configurazione, consulta il tutorial [Configurazione dei provider](../../../pre-basic/providers/) nella sezione delle nozioni di base.

{% hint style="info" %}
* Quando si utilizzano provider integrati, è sufficiente inserire la chiave corrispondente.
* Denominazioni diverse tra provider per chiavi (秘钥, Key, API Key, 令牌) fanno tutte riferimento allo stesso elemento.
{% endhint %}



### Chiave API

In Cherry Studio, un singolo provider supporta il polling multiplo di chiavi con un ciclo sequenziale dall'inizio alla fine della lista.

* Inserire più chiavi separandole con virgole inglesi, come nell'esempio:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Utilizzare **esclusivamente** virgole inglesi.
{% endhint %}

### Indirizzo API

Generalmente non è necessario inserire l'indirizzo API quando si utilizzano provider integrati. Se necessario modificarlo, seguire rigorosamente l'indirizzo fornito nella documentazione ufficiale corrispondente.

> Se il provider fornisce un indirizzo nel formato <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, inserire solo la parte root (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio concatenerà automaticamente il percorso rimanente (<mark style="background-color:green;">/v1/chat/completions</mark>). Un inserimento non conforme potrebbe causare malfunzionamenti.

{% hint style="info" %}
Nota: La maggior parte dei provider ha percorsi API standardizzati per modelli linguistici. Se il percorso API del provider utilizza versioni come v2 o v3/chat/completions:
* Terminare l'indirizzo con `/` per concatenare automaticamente "chat/completions"
* Terminare con `#` per disabilitare la concatenazione e utilizzare esattamente l'indirizzo inserito

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}



### Aggiunta modelli

Normalmente, cliccando il pulsante `Gestisci` nell'angolo inferiore sinistro della pagina di configurazione, vengono recuperati automaticamente tutti i modelli supportati dal provider. Aggiungere i modelli desiderati alla lista cliccando `+`.

{% hint style="info" %}
I modelli nella finestra popup non vengono aggiunti automaticamente. È necessario cliccare `+` accanto a ciascun modello per renderli disponibili nella selezione.
{% endhint %}


### Verifica connettività

Cliccare il pulsante di verifica accanto al campo della chiave API per testare la configurazione.

{% hint style="info" %}
Il test utilizza l'ultimo modello conversazionale nella lista. In caso di errore, verificare che tutti i modelli aggiunti siano validi e supportati.
{% endhint %}

{% hint style="danger" %}
Dopo una configurazione corretta, attivare l'interruttore in alto a destra, altrimenti i modelli del provider rimarranno indisponibili.
{% endhint %}