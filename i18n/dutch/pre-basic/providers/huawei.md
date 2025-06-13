
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Huawei Cloud

1.  Ga naar [Huawei Cloud](https://auth.huaweicloud.com/authui/login) om een account aan te maken en in te loggen
2.  Klik op [deze link](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) om naar het ModelArts-dashboard te gaan
3.  Autorisatie

<details>

<summary>Autorisatiestappen (overslaan indien reeds geautoriseerd)</summary>

1.  Na het openen van de link in stap 2, ga naar de autorisatiepagina volgens de aanwijzingen (klik op IAM-subgebruiker → Nieuwe delegatie → Standaardgebruiker)

![](<../../.gitbook/assets/image (49).png>)

2.  Na het aanmaken, keer terug naar de pagina van stap 2
3.  Er verschijnt een melding over onvoldoende toegangsrechten, klik op "Klik hier" in de melding
4.  Voeg bestaande autorisatie toe en bevestig

![](<../../.gitbook/assets/image (50).png>)

&#x20;Opmerking: Deze methode is geschikt voor beginners, zonder veel inhoud te bekijken. Volg gewoon de aanwijzingen. Als je in één keer kunt autoriseren, gebruik dan je eigen methode.

</details>

4.  Klik op de zijbalk "Autorisatiebeheer", maak een API Key (geheime sleutel) aan en kopieer deze

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Maak vervolgens een nieuwe serviceprovider aan in CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Voer de geheime sleutel in na het aanmaken



5.  Klik op de zijbalk "Modelimplementatie", claim alles

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6.  Klik op "Aanroepen"

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Kopieer het adres bij ①, plak het in het serviceprovideradres in CherryStudio en voeg "#" toe aan het einde

en voeg "#" toe aan het einde

en voeg "#" toe aan het einde

en voeg "#" toe aan het einde

en voeg "#" toe aan het einde

Waarom "#" toevoegen? [Zie hier](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Je kunt dit ook negeren en gewoon de tutorial volgen;  
> je kunt ook de methode gebruiken waarbij je v1/chat/completions verwijdert. Gebruik je eigen methode als je weet hoe, maar volg de tutorial als je niet zeker bent.



<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Kopieer vervolgens de modelnaam bij ②, ga naar CherryStudio en klik op de knop "+Toevoegen" om een nieuw model aan te maken

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Voer de modelnaam in, voeg niets extra's toe, gebruik geen aanhalingstekens en kopieer precies zoals in het voorbeeld.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Klik op de knop "Model toevoegen" om het proces te voltooien.

{% hint style="info" %}
Omdat elk model in Huawei Cloud een ander adres heeft, moet je voor elk model een nieuwe serviceprovider aanmaken door bovenstaande stappen te herhalen.
{% endhint %}