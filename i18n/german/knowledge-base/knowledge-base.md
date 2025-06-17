---
icon: book-open-cover
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Wissenbasis Tutorial

In Version 0.9.1 führt CherryStudio die lang erwartete Wissenbasis-Funktion ein.

Nachfolgend stellen wir Schritt für Schritt eine detaillierte Anleitung zur Nutzung von CherryStudio vor.

## Embedding-Modelle hinzufügen

1. Im Model-Management-Dienst nach Modellen suchen; Sie können auf "Embedding-Modelle" klicken, um schnell zu filtern;
2. Das gewünschte Modell finden und zu "Meine Modelle" hinzufügen.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Wissenbasis erstellen

1. Zugang zur Wissenbasis: Klicken Sie in der linken Symbolleiste von CherryStudio auf das Wissenbasis-Symbol, um zur Verwaltungsseite zu gelangen;
2. Wissenbasis hinzufügen: Klicken Sie auf "Hinzufügen", um mit der Erstellung zu beginnen;
3. Benennen: Geben Sie einen Namen für die Wissenbasis ein und fügen Sie ein Embedding-Modell hinzu, z.B. bge-m3, um die Erstellung abzuschließen.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Dateien hinzufügen und vektorisieren

1. Datei hinzufügen: Klicken Sie auf den "Datei hinzufügen"-Button, um die Dateiauswahl zu öffnen;
2. Datei auswählen: Wählen Sie unterstützte Dateiformate wie pdf, docx, pptx, xlsx, txt, md, mdx usw. und öffnen Sie sie;
3. Vektorisierung: Das System führt automatisch die Vektorisierung durch. Wenn ein grünes Häkchen ✓ erscheint, ist die Vektorisierung abgeschlossen.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>



## Daten aus verschiedenen Quellen hinzufügen

CherryStudio unterstützt mehrere Datenquellen:

1. Verzeichnisse: Ganze Ordner können hinzugefügt werden, Dateien unterstützter Formate im Ordner werden automatisch vektorisiert;
2. Webadressen: URLs wie [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Sitemaps: XML-formatierte Sitemaps wie [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Textnotizen: Reiner Text kann manuell eingegeben werden.

{% hint style="info" %}
Hinweise:

1. Grafiken in Dokumenten werden beim Import nicht in Vektoren umgewandelt und müssen manuell in Text konvertiert werden;
2. Die Verwendung von URLs als Quelle kann fehlschlagen: Einige Websites haben strenge Anti-Scraping-Mechanismen (oder erfordern Login/Autorisierung). Testen Sie nach dem Erstellen durch Suche;
3. Die meisten Websites bieten eine Sitemap, z.B. [CherryStudios Sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). Normalerweise unter `website-root/sitemap.xml`;
4. Falls keine Sitemap vorhanden ist: 
> a) KI zur Generierung verwenden oder ein Sitemap-Generator-Tool erstellen lassen;
> b) Öffentlich zugängliche Direct-Links (OSS/Cloud) nutzen. 
> Ein Upload-Tool für Direct-Links finden Sie bei [ocoolAI](https://one.ocoolai.com/login) nach dem Login.
{% endhint %}

## Wissenbasis durchsuchen

Nach Abschluss der Vektorisierung kann die Suche gestartet werden:

1. "Wissenbasis durchsuchen"-Button unten auf der Seite anklicken;
2. Suchbegriff eingeben;
3. Ergebnisse werden angezeigt;
4. Übereinstimmungspunktzahl wird angezeigt.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Wissenbasis in Gesprächen nutzen

1. Neues Gespräch starten: Klicken Sie im Werkzeugmenü auf "Wissenbasis" und wählen Sie eine Wissenbasis aus;
2. Frage eingeben: Das Modell generiert eine Antwort basierend auf den Suchergebnissen;
3. Quellen werden unter der Antwort angezeigt - Direktzugriff auf Originaldokumente.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>