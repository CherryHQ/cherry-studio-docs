---
icon: database
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Dateneinstellungen

Diese Oberfläche ermöglicht Cloud- und lokale Datensicherungen, Abfrage des lokalen Datenverzeichnisses sowie Cache-Bereinigung für Client-Daten.

### Datensicherung

Derzeit werden Datensicherungen nur über WebDAV unterstützt. Sie können WebDAV-fähige Dienste für Cloud-Sicherungen nutzen.

Daten können auch über das Schema `Computer A` $$\xrightarrow{\text{Sicherung}}$$ `WebDAV` $$\xrightarrow{\text{Wiederherstellung}}$$ `Computer B` zwischen verschiedenen Geräten synchronisiert werden.

#### Beispiel mit Nutzeria Cloud

1. Melden Sie sich bei Nutzeria Cloud an, klicken Sie auf den Benutzernamen oben rechts und wählen Sie „Kontoinformationen“:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Wählen Sie „Sicherheitsoptionen“ und klicken Sie auf „Anwendung hinzufügen“:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Geben Sie einen Anwendungsnamen ein und generieren Sie ein zufälliges Passwort:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Notieren Sie das generierte Passwort:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Rufen Sie Serveradresse, Benutzernamen und Passwort ab:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Tragen Sie die WebDAV-Informationen in Cherry Studio unter Einstellungen → Dateneinstellungen ein:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Wählen Sie Daten-Sicherung oder Wiederherstellung und konfigurieren Sie ggf. automatische Sicherungsintervalle:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Niederschwellige WebDAV-Dienste bieten typischerweise Cloud-Speicher:

* [Nutzeria Cloud](https://www.jianguoyun.com/)
* [123Speicher](https://www.123pan.com/) (Premium erforderlich)
* [Alibaba Cloud Disk](https://www.alipan.com/) (Kauf erforderlich)
* [Box](https://www.box.com/) (10 GB kostenlos, 250 MB Dateigrößenlimit)
* [Dropbox](https://www.dropbox.com/) (2 GB kostenlos, 16 GB durch Empfehlungen)
* [TeraCloud](https://teracloud.jp/en/) (10 GB kostenlos + 5 GB durch Empfehlungen)
* [Yandex Disk](https://disk.yandex.com/) (10 GB kostenlos)

Selbstgehostete Alternativen:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}