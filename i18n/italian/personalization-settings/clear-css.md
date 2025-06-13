---
icon: trash-xmark
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Cancella le impostazioni CSS

{% hint style="warning" %}
Utilizzare questo metodo quando sono stati configurati CSS errati o quando non è possibile accedere all'interfaccia delle impostazioni dopo aver modificato i CSS.
{% endhint %}

* Apri la console facendo clic sulla finestra di CherryStudio e premendo <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (macOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* Nella console che appare, clicca su `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Digita manualmente `document.getElementById('user-defined-custom-css').remove()` - l'incollare il comando probabilmente non funzionerà.
* Premi Invio dopo aver inserito il comando per cancellare le impostazioni CSS, quindi torna nelle impostazioni di visualizzazione di CherryStudio per rimuovere il codice CSS problematico.