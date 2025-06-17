---
icon: database
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Impostazioni Dati

Questa interfaccia consente operazioni quali backup locale e nel cloud dei dati del client, consultazione della directory dati locale e cancellazione della cache.

### Backup Dati

Attualmente, il backup dei dati è supportato solo tramite WebDAV. Puoi scegliere servizi compatibili con WebDAV per effettuare backup nel cloud.

Puoi anche sincronizzare i dati su più dispositivi tramite:  
`Computer A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{ripristino}}$$ `Computer B`

#### Esempio con Nutstore

1. Accedi a Nutstore, clicca sul nome utente in alto a destra e seleziona "Informazioni account":
   <figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Seleziona "Opzioni di sicurezza" e clicca "Aggiungi applicazione"
   <figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Inserisci il nome dell'applicazione e genera una password casuale;
   <figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copia e registra la password;
   <figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Ottieni indirizzo server, account e password;
   <figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. In Cherry Studio > Impostazioni > Impostazioni dati, inserisci le informazioni WebDAV;
   <figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Scegli di eseguire il backup o il ripristino dei dati, e imposta l'intervallo temporale per il backup automatico.
   <figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
I servizi WebDAV con minori barriere all'accesso sono generalmente fornitori di cloud storage:

* [Nutstore](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (richiede abbonamento)
* [Alibaba Cloud Drive](https://www.alipan.com/) (richiede acquisto)
* [Box](https://www.box.com/) (spazio gratuito: 10GB, limite per singolo file: 250MB)
* [Dropbox](https://www.dropbox.com/) (2GB gratuiti, fino a 16GB con inviti)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuiti + 5GB con inviti)
* [Yandex Disk](https://disk.yandex.com/) (10GB gratuiti)

Alternative che richiedono installazione autonoma:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}