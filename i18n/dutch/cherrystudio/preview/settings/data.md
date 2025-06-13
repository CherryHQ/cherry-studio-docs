---
icon: database
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Gegevensinstellingen

In deze interface kunt u cloud- en lokale back-ups van clientgegevens maken, lokale gegevensmappen opvragen en de cache leegmaken.

### Gegevensback-up

Momenteel ondersteunt gegevensback-up alleen de WebDAV-methode. U kunt een service kiezen die WebDAV ondersteunt voor cloudback-ups.

U kunt ook gegevenssynchronisatie over meerdere apparaten bereiken via:  
`Computer A` $$\xrightarrow{\text{back-up}}$$ `WebDAV` $$\xrightarrow{\text{herstel}}$$ `Computer B`.

#### Voorbeeld met NutzCloud

1. Log in op NutzCloud, klik op de gebruikersnaam in de rechterbovenhoek en selecteer "Accountgegevens":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecteer "Beveiligingsopties" en klik op "App toevoegen"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Voer de applicatienaam in en genereer een wachtwoord:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Kopieer en noteer het wachtwoord:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Verkrijg serveradres, account en wachtwoord:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Vul in Cherry Studio-instellingen → Gegevensinstellingen de WebDAV-informatie in:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Kies back-up of herstel van gegevens en stel het interval voor automatische back-ups in:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV-diensten met lage instapdrempel zijn meestal cloudopslag:

* [NutzCloud](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (vereist lidmaatschap)
* [Aliyun Drive](https://www.alipan.com/) (vereist aankoop)
* [Box](https://www.box.com/) (gratis ruimte 10GB, bestandslimiet 250MB)
* [Dropbox](https://www.dropbox.com/) (gratis 2GB, uitbreidbaar tot 16GB via uitnodigingen)
* [TeraCloud](https://teracloud.jp/en/) (gratis 10GB + 5GB via uitnodigingen)
* [Yandex Disk](https://disk.yandex.com/) (10GB gratis ruimte)

Zelf te implementeren diensten:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}