---
icon: database
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Dateneinstellungen

Auf dieser Oberfläche können Sie Cloud- und lokale Backups von Client-Daten durchführen, lokale Datenverzeichnisse abfragen sowie den Cache löschen.

### Datensicherung

Derzeit werden Backups nur über WebDAV unterstützt. Für Cloud-Backups können Sie einen WebDAV-fähigen Dienst nutzen.

Alternativ können Sie Daten zwischen mehreren Geräten synchronisieren über: `Computer A` $$\xrightarrow{\text{Sichern}}$$ `WebDAV` $$\xrightarrow{\text{Wiederherstellen}}$$ `Computer B`.

#### Beispiel mit Nutstore

1. Melden Sie sich bei Nutstore an, klicken Sie oben rechts auf den Benutzernamen und wählen Sie "Kontoinformationen":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Wählen Sie "Sicherheitseinstellungen" und klicken Sie auf "Anwendung hinzufügen"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Geben Sie einen Anwendungsnamen ein und generieren Sie ein zufälliges Passwort:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Notieren Sie das Passwort:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Serveradresse, Benutzername und Passwort abrufen:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Tragen Sie im Cherry Studio unter Einstellungen → Dateneinstellungen die WebDAV-Informationen ein:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Wählen Sie Backup oder Wiederherstellung aus und konfigurieren Sie bei Bedarf automatische Backups:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Niedrigschwellige WebDAV-Dienste sind typischerweise Cloud-Speicher:

* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (Premium erforderlich)
* [Alibaba Cloud Drive](https://www.alipan.com/) (Kauf erforderlich)
* [Box](https://www.box.com/) (10GB kostenlos, Dateien bis 250MB)
* [Dropbox](https://www.dropbox.com/) (2GB kostenlos, +16GB durch Empfehlungen)
* [TeraCloud](https://teracloud.jp/en/) (10GB kostenlos, +5GB durch Empfehlungen)
* [Yandex Disk](https://disk.yandex.com/) (10GB kostenlos)

Optionen für selbst gehostete Lösungen:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}