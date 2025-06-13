---
icon: trash-xmark
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# CSS-instellingen wissen

{% hint style="warning" %}
Gebruik deze methode om CSS-instellingen te wissen wanneer u verkeerde CSS heeft ingesteld of niet meer in de instellingeninterface kunt komen na het instellen van CSS.
{% endhint %}

* Open de ontwikkelhulpprogramma's door op het Cherry Studio-venster te klikken en de sneltoets <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> in te drukken (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* Klik in het geopende ontwikkelvenster op het tabblad `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Voer handmatig `document.getElementById('user-defined-custom-css').remove()` in (kopiëren en plakken werkt meestal niet).
* Druk op Enter om de CSS-instellingen te wissen, en ga vervolgens terug naar de weergave-instellingen van Cherry Studio om de problematische CSS-code te verwijderen.