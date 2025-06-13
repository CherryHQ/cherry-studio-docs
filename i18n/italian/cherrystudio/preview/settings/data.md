---
icon: database
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Configurazione dei Dati

Questa interfaccia consente operazioni quali backup cloud e locali dei dati del client, query della directory dati locale e cancellazione della cache.

### Backup dei Dati

Attualmente, il backup dei dati supporta solo il metodo WebDAV. Puoi scegliere un servizio compatibile con WebDAV per eseguire backup cloud.

Puoi anche sincronizzare i dati su più dispositivi attraverso il flusso: `Computer A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{ripristino}}$$ `Computer B`.

#### Esempio con Nutstore

1. Accedi a Nutstore, clicca sul nome utente in alto a destra e seleziona "Informazioni account":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Seleziona "Opzioni di sicurezza", clicca "Aggiungi applicazione":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Inserisci il nome dell'applicazione e genera una password casuale:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copia e salva la password:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Ottieni indirizzo server, account e password:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Nelle impostazioni di Cherry Studio → Configurazione dati, inserisci le informazioni WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Seleziona backup o ripristino dati e imposta l'intervallo di backup automatico:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Servizi WebDAV con soglia d'accesso bassa sono generalmente piattaforme cloud:

* [Nutstore](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (richiede abbonamento)
* [Aliyun Disk](https://www.alipan.com/) (a pagamento)
* [Box](https://www.box.com/) (spazio gratuito: 10GB, limite file singolo: 250MB)
* [Dropbox](https://www.dropbox.com/) (2GB gratuiti, espandibili fino a 16GB con inviti)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuiti + 5GB aggiuntivi tramite inviti)
* [Yandex Disk](https://disk.yandex.com/) (10GB per utenti gratuiti)

Alternativamente, servizi che richiedono installazione autonoma:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}