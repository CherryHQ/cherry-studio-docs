---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Online modus

{% hint style="info" %}
Voorbeelden van situaties waarbij internetverbinding nodig is:

* Tijdsgebonden informatie: bijvoorbeeld de actuele goudfuturesprijs van vandaag/deze week/zojuist.
* Real-time gegevens: zoals weer, wisselkoersen en andere dynamische waarden.
* Nieuwe kennis: bijvoorbeeld nieuwe ontwikkelingen, concepten, technologieën, enz.
{% endhint %}

### Eén: Hoe de online modus inschakelen

Klik in het vraagvenster van Cherry Studio op het pictogram 【Witte wereldbol】 om de online modus in te schakelen.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Klik op het wereldbolpictogram - online modus inschakelen</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Geeft aan dat online functie is ingeschakeld</p></figcaption></figure>

### Twee: Belangrijke opmerking - Twee modi voor online verbinding

#### Modus 1: Geïntegreerde online functie van de modelaanbieder

In dit geval kunt u na het inschakelen direct gebruikmaken van de online diensten. Heel eenvoudig.

{% hint style="warning" %}
U kunt snel controleren of een model online ondersteuning biedt door te kijken of er een klein wereldbolpictogram achter de modelnaam staat in de interface.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Ook op de modelbeheerpagina helpt deze methode u snel te identificeren welke modellen online ondersteuning bieden.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Momenteel ondersteunde modelaanbieders met online functies in Cherry Studio**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (alle modellen ondersteunen online functies)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian, etc.</mark>

{% hint style="danger" %}
Belangrijke opmerking:

Er bestaat een speciale situatie waarbij een model ondanks het ontbreken van het wereldbolpictogram toch online functionaliteit kan bieden, zoals uitgelegd in de volgende handleiding.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Modus 2: Tavily-service voor modellen zonder ingebouwde online functionaliteit

Wanneer we een groot model gebruiken zonder online functionaliteit (geen wereldbolpictogram achter de naam), maar we toch real-time informatie nodig hebben, gebruiken we de Tavily-netwerkzoekdienst.

**Bij eerste gebruik van Tavily** verschijnt er een pop-upvenster om informatie in te stellen. Volg eenvoudig de instructies!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Pop-upvenster, klik op: Instellingen</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Klik op API-sleutel verkrijgen</p></figcaption></figure>

Na het klikken wordt u automatisch doorgestuurd naar de **aanmeldpagina van Tavily**. Registreer, log in, maak een API-sleutel aan en plak deze in Cherry Studio.

{% hint style="danger" %}
Problemen met registratie? Raadpleeg de Tavily-registratiehandleiding in deze documentatiemap.
{% endhint %}

**Handleiding voor Tavily-registratie:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

De volgende interface geeft aan dat de registratie succesvol was.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Kopieer de sleutel</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Plak de sleutel - klaar!</p></figcaption></figure>

Test opnieuw om het resultaat te zien. Het toont aan dat de online zoekopdracht werkt, met standaard 5 zoekresultaten (aantal instelbaar).

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Let op: Tavily heeft maandelijkse gebruikerslimieten. Overschrijding leidt tot kosten!
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Neem bij eventuele fouten gerust contact met ons op.