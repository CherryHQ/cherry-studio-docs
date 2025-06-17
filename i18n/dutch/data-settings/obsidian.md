---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

---
icon: cherries
---

# Obsidian-configuratiehandleiding

Cherry Studio ondersteunt integratie met Obsidian, waardoor u volledige gesprekken of individuele berichten kunt exporteren naar een Obsidian-bibliotheek.

{% hint style="warning" %}
Voor dit proces hoeft geen extra Obsidian-plugin geïnstalleerd te worden. Omdat het importmechanisme van Cherry Studio naar Obsidian vergelijkbaar is met de Obsidian Web Clipper, wordt aanbevolen om Obsidian bij te werken naar de nieuwste versie (huidige versie moet minstens **1.7.2** zijn) om te voorkomen dat [import mislukt bij extreem lange gesprekken](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Nieuwste handleiding

{% hint style="info" %}
Vergeleken met de oude exportfunctie naar Obsidian kan de nieuwe versie automatisch het bibliotheekpad selecteren, zonder handmatige invoer van bibliotheek- of mapnamen.
{% endhint %}

### Stap 1: Cherry Studio configureren

Open in Cherry Studio _Instellingen_ → _Gegevensinstellingen_ → _Obsidian-configuratiemenu_. De dropdown toont automatisch eerder geopende Obsidian-bibliotheken op uw apparaat. Selecteer uw doelbibliotheek:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Stap 2: Gesprek exporteren

#### Volledig gesprek exporteren

Ga terug naar het gespreksscherm van Cherry Studio. Klik met de rechtermuisknop op een gesprek, selecteer _Exporteren_ en klik op _Exporteren naar Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Er verschijnt een venster om aan te passen:
1. **Properties (eigenschappen)** van de Obsidian-notitie
2. **Mapplaats** in Obsidian
3. **Verwerkingswijze** voor de export:
   - **Bibliotheek**: Selecteer een andere bibliotheek via dropdown
   - **Pad**: Kies doelmap via dropdown
   - **Notitie-eigenschappen**:
     - Labels (tags)
     - Aanmaaktijd (created)
     - Bron (source)
   - **Verwerkingsopties**:
     - **Nieuw (overschrijf indien aanwezig)**: Maakt een nieuwe notitie in de geselecteerde map, overschrijft bestaande notities met dezelfde naam.
     - **Toevoegen aan begin**: Voegt geëxporteerde inhoud toe aan het begin van een bestaande notitie.
     - **Toevoegen aan einde**: Voegt geëxporteerde inhoud toe aan het einde van een bestaande notitie.

{% hint style="info" %}
Alleen de eerste optie behoudt Properties. De laatste twee behouden geen eigenschappen.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Notitie-eigenschappen configureren</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Pad selecteren</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Verwerkingswijze selecteren</p></figcaption></figure>

Klik op _Bevestigen_ om het gesprek naar de geselecteerde map te exporteren.

#### Enkel bericht exporteren

Klik op het _drie-strepensmenu_ onder een bericht, selecteer _Exporteren_ en klik _Exporteren naar Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Enkel bericht exporteren</p></figcaption></figure>

Configureer vervolgens **eigenschappen** en **verwerkingswijze** zoals beschreven bij het [exporteren van volledige gesprekken](#dao-chu-wan-zheng-dui-hua).

### Succesvol geëxporteerd

🎉 Gefeliciteerd! U heeft de integratie voltooid en het volledige exportproces doorlopen. Veel plezier!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exporteren naar Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Exportresultaat bekijken</p></figcaption></figure>

***

## Oude handleiding (voor Cherry Studio <v1.1.13)

### Stap 1: Obsidian voorbereiden

Open uw Obsidian-bibliotheek en maak een map aan voor geëxporteerde gesprekken (bijv. "Cherry Studio"):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Noteer de naam van uw `Bibliotheek` (linksonder omcirkeld).

### Stap 2: Cherry Studio configureren

Navigeer in Cherry Studio naar _Instellingen_ → _Gegevensinstellingen_ → _Obsidian-configuratiemenu_. Voer de `Bibliotheeknaam` en `Mapnaam` in uit [Stap 1](#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

Optioneel: Voer `Globale labels` in om tags voor alle geëxporteerde gesprekken in te stellen.

### Stap 3: Gesprek exporteren

#### Volledig gesprek exporteren

Klik met rechts op een gesprek → _Exporteren_ → _Exporteren naar Obsidian_:

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Volledig gesprek exporteren</p></figcaption></figure>

Pas **notitie-eigenschappen** aan en kies een verwerkingsoptie:
- **Nieuw (overschrijf indien aanwezig)**
- **Toevoegen aan begin**
- **Toevoegen aan einde**

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Notitie-eigenschappen configureren</p></figcaption></figure>

{% hint style="info" %}
Alleen "Nieuw (overschrijf)" behoudt Properties. Overige opties behouden geen eigenschappen.
{% endhint %}

#### Enkel bericht exporteren

Klik op het _drie-strepensmenu_ onder een bericht → _Exporteren_ → _Exporteren naar Obsidian_. Volg dezelfde stappen als bij het [exporteren van volledige gesprekken](#dao-chu-wan-zheng-dui-hua).

### Succesvol geëxporteerd

🎉 Gefeliciteerd! U heeft de integratie voltooid en het volledige exportproces doorlopen. Veel plezier!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exporteren naar Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Exportresultaat bekijken</p></figcaption></figure>