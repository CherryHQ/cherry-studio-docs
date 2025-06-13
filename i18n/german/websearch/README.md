---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Internetmodus

{% hint style="info" %}
Beispiele für Situationen, die eine Internetverbindung erfordern:

* Zeitkritische Informationen: z.B. aktuelle Goldpreise für heute/diese Woche/gerade eben.
* Echtzeitdaten: wie Wetter, Wechselkurse und andere dynamische Werte.
* Neuartiges Wissen: wie neue Phänomene, Konzepte oder Technologien...
{% endhint %}

### 1. Aktivierung der Internetverbindung

Klicken Sie im Cherry Studio-Fragefenster auf das 【Erdglobus】-Symbol, um die Internetverbindung zu aktivieren.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Erd-Symbol anklicken – Internetverbindung aktivieren</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Anzeige – Internetfunktion wurde aktiviert</p></figcaption></figure>

### 2. Wichtiger Hinweis: Zwei Internetverbindungsmodi

#### Modus 1: Integrierte Internetfunktion des Modellanbieters

In diesem Fall können Sie den Internetzugang sofort nutzen, nachdem Sie ihn aktiviert haben – äußerst einfach.

{% hint style="warning" %}
Überprüfen Sie, ob neben dem Modellnamen im Frage-Antwort-Interface ein kleines Globussymbol angezeigt wird, um schnell zu erkennen, ob das Modell Internetzugang unterstützt.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Auch in der Modellverwaltungsseite hilft diese Methode, internetfähige Modelle zu identifizieren.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Derzeit bei Cherry Studio unterstützte Anbieter mit integriertem Internetzugang:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (alle Modelle unterstützen Internet)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian u.a.</mark>

{% hint style="danger" %}
Besonderer Hinweis:

Es gibt eine Ausnahmesituation, bei der Modelle ohne Globussymbol dennoch Internetzugang ermöglichen können – siehe folgende Anleitung.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Modus 2: Tavily-Service für Modelle ohne Internetfunktion

Bei Modellen ohne integrierte Internetfunktion (ohne Globussymbol im Namen), die dennoch aktuelle Informationen benötigen, kommt der Tavily-Internetsuchdienst zum Einsatz.

**Bei erstmaliger Nutzung von Tavily** erscheint ein Popup zur Konfiguration – folgen Sie einfach der Anleitung:

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Popup – auf "Einstellungen" klicken</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Schlüssel anfordern</p></figcaption></figure>

Nach Klick auf "Schlüssel anfordern" gelangen Sie zur **Tavily-Website**. Registrieren Sie sich, erstellen Sie einen API-Schlüssel und kopieren Sie ihn in Cherry Studio.

{% hint style="danger" %}
Registrierungsanleitung siehe Tutorial "tavily.md" im gleichen Verzeichnis.
{% endhint %}

**Tavily-Registrierungsreferenz:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Diese Ansicht bestätigt eine erfolgreiche Registrierung:

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Schlüssel kopieren</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Schlüssel einfügen – fertig</p></figcaption></figure>

Erneute Anfrage mit aktiviertem Tavily-Service (Standard: 5 Suchergebnisse):

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Hinweis: Tavily hat monatliche Nutzungsgrenzen – bei Überschreitung fallen Kosten an.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Fehlermeldungen können jederzeit an uns gemeldet werden.