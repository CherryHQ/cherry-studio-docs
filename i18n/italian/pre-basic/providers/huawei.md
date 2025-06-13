
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Huawei Cloud

1. Vai su [Huawei Cloud](https://auth.huaweicloud.com/authui/login) per creare un account e accedere

2. Fai clic su [questo link](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) per accedere alla console ModelArts

3. Autorizzazione

<details>

<summary>Passaggi di autorizzazione (salta se già autorizzato)</summary>

1. Dopo essere entrato nella pagina del link in (2), segui le indicazioni per accedere alla pagina di autorizzazione (fai clic su IAM sub-utente → Nuova delega → Utente normale)

![](<../../.gitbook/assets/image (49).png>)

2. Dopo aver fatto clic su Crea, torna alla pagina del link in (2)
3. Verrà visualizzato un messaggio di permessi insufficienti, fai clic su "Clicca qui" nel messaggio
4. Aggiungi l'autorizzazione esistente e conferma

![](<../../.gitbook/assets/image (50).png>)

Nota: Questo metodo è adatto per principianti, non c'è bisogno di leggere troppo, basta seguire le indicazioni e cliccare. Se riesci ad autorizzare con successo in una volta, puoi procedere a modo tuo.

</details>

4. Fai clic su Gestione autenticazione nella barra laterale, crea una chiave API (segreto) e copiala

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Quindi in CherryStudio crea un nuovo provider di servizi

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Dopo averlo creato, inserisci la chiave segreta

5. Fai clic su Distribuzione modelli nella barra laterale e reclama tutti

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. Fai clic su Chiamata

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Copia l'indirizzo al punto ①, incollalo nell'indirizzo del provider di servizi di CherryStudio e aggiungi un "#" alla fine

e aggiungi un "#" alla fine

e aggiungi un "#" alla fine

e aggiungi un "#" alla fine

e aggiungi un "#" alla fine

Perché aggiungere "#"? [Vedi qui](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Ovviamente, puoi anche non guardare lì e procedere seguendo il tutorial;
>
> Puoi anche utilizzare il metodo di eliminare v1/chat/completions per compilare, purché tu sappia come farlo, puoi procedere a modo tuo; se non sai come fare, assicurati di seguire il tutorial.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Quindi copia il nome del modello al punto ②, in CherryStudio fai clic sul pulsante "+ Aggiungi" per creare un nuovo modello

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Inserisci il nome del modello, non aggiungere nulla di superfluo, non includere virgolette, copia esattamente come nell'esempio.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Fai clic sul pulsante Aggiungi modello per completare l'aggiunta.

{% hint style="info" %}
Poiché su Huawei Cloud ogni modello ha un indirizzo diverso, è necessario creare un nuovo provider di servizi per ogni modello, ripetendo i passaggi precedenti.
{% endhint %}