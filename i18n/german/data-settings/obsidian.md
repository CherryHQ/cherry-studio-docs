---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Obsidian-Konfigurationsanleitung

Cherry Studio unterstützt die Integration mit Obsidian, um vollständige Dialoge oder einzelne Nachrichten in eine Obsidian-Bibliothek zu exportieren.

{% hint style="warning" %}
Dieser Prozess erfordert keine zusätzlichen Obsidian-Plugins. Da Cherry Studio jedoch ähnlich wie der Obsidian Web Clipper funktioniert, wird empfohlen, Obsidian auf die neueste Version zu aktualisieren (mindestens **Version 1.7.2**), um [Fehler bei langen Dialogen zu vermeiden](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Aktuelle Anleitung

{% hint style="info" %}
Im Vergleich zur alten Version wählt der neue Obsidian-Export automatisch Bibliothekspfade aus, ohne manuelle Eingabe von Bibliotheksnamen oder Ordnerbezeichnungen.
{% endhint %}

### Schritt 1: Cherry Studio konfigurieren

Öffnen Sie in Cherry Studio: _Einstellungen_ → _Dateneinstellungen_ → _Obsidian-Konfiguration_. Im Dropdown-Menü werden automatisch geöffnete Obsidian-Bibliotheken angezeigt. Wählen Sie Ihre Zielbibliothek:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Schritt 2: Dialog exportieren

#### Vollständigen Dialog exportieren

Rechtsklicken Sie im Dialogbereich auf einen Dialog, wählen Sie _Exportieren_ → _Nach Obsidian exportieren_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Ein Fenster öffnet sich zur Konfiguration von:
- **Eigenschaften (Properties)** der Notiz
- **Zielordner** in Obsidian
- **Verarbeitungsmethode**:

  * **Bibliothek**: Wählen Sie andere Bibliotheken per Dropdown
  * **Pfad**: Wählen Sie den Zielordner per Dropdown
  * Obsidian-Notiz-Eigenschaften:
    - Tags
    - Erstellungsdatum
    - Quelle
  * **Verarbeitungsmethoden**:
    - **Neu (bestehende überschreiben)**: Erstellt eine neue Notiz; existierende wird überschrieben
    - **Voranstellen**: Fügt Dialog an Anfang bestehender Notiz hinzu
    - **Anfügen**: Fügt Dialog an Ende bestehender Notiz hinzu

{% hint style="info" %}
Nur die erste Methode inkludiert Eigenschaften (Properties).
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Notizeigenschaften konfigurieren</p></figcaption></figure>
<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Pfad auswählen</p></figcaption></figure>
<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Verarbeitungsmethode auswählen</p></figcaption></figure>

Nach der Konfiguration bestätigen Sie mit "OK".

#### Einzelne Nachricht exportieren

Klicken Sie bei einer Nachricht auf das _Drei-Striche-Menü_, wählen Sie _Exportieren_ → _Nach Obsidian exportieren_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Einzelne Nachricht exportieren</p></figcaption></figure>

Das Konfigurationsfenster öffnet sich erneut. Folgen Sie der obigen [Anleitung für vollständige Dialoge](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Erfolgreicher Export

🎉 Herzlichen Glückwunsch! Sie haben die Obsidian-Integration vollständig konfiguriert.

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Export nach Obsidian</p></figcaption></figure>
<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Exportierte Notiz ansehen</p></figcaption></figure>

***

## Alte Anleitung (für Cherry Studio < v1.1.13)

### Schritt 1: Obsidian vorbereiten

Erstellen Sie in Ihrer Obsidian-Bibliothek einen _Zielordner_ für exportierte Dialoge (z.B. "Cherry Studio"). Notieren Sie den **Bibliotheksnamen**:

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

### Schritt 2: Cherry Studio konfigurieren

Unter _Einstellungen_ → _Dateneinstellungen_ → _Obsidian-Konfiguration_:
- Eingabe des **Bibliotheksnamens**
- Eingabe des **Zielordners**
- Optionale **globale Tags** für alle exportierten Dialoge

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

### Schritt 3: Dialog exportieren

#### Vollständigen Dialog exportieren

Rechtsklick auf Dialog → _Exportieren_ → _Nach Obsidian exportieren_:

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Vollständigen Dialog exportieren</p></figcaption></figure>

Wählen Sie Verarbeitungsmethode und konfigurieren Sie Eigenschaften:

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Notizeigenschaften konfigurieren</p></figcaption></figure>

#### Einzelne Nachricht exportieren

Über das _Drei-Striche-Menü_ neben einer Nachricht → _Exportieren_ → _Nach Obsidian exportieren_:

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Einzelne Nachricht exportieren</p></figcaption></figure>

### Erfolgreicher Export

🎉 Integration abgeschlossen!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Export nach Obsidian</p></figcaption></figure>
<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Exportierte Notiz ansehen</p></figcaption></figure>