---
icon: database
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Gegevensinstellingen

Via dit scherm kunt u back-ups van clientgegevens in de cloud en lokaal maken, lokale gegevensmappen raadplegen en de cache wissen.

### Gegevensback-up

Momenteel ondersteunt gegevensback-up alleen de WebDAV-methode. U kunt een WebDAV-ondersteunende service kiezen voor cloudback-ups.

U kunt gegevens synchroniseren via: `A电脑` $$\xrightarrow{\text{back-up}}$$ `WebDAV` $$\xrightarrow{\text{herstel}}$$ `B电脑`

#### Voorbeeld met Jianguoyun

1. Log in op Jianguoyun, klik op de gebruikersnaam in de rechterbovenhoek en selecteer "Accountgegevens":
   
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecteer "Beveiligingsopties" en klik op "App toevoegen"
   
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Voer de app-naam in en genereer een wachtwoord:
   
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Kopieer en bewaar het wachtwoord:
   
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Verkrijg het serveradres, account en wachtwoord:
   
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Ga in Cherry Studio-instellingen → Gegevensinstellingen en vul de WebDAV-gegevens in:
   
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Kies voor back-up of gegevensherstel en stel desgewenst een automatisch back-upschema in:
   
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Lichtgewicht WebDAV-services zijn vaak cloudopslagdiensten:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (abonnement vereist)
* [阿里云盘](https://www.alipan.com/) (aankoop vereist)
* [Box](https://www.box.com/) (gratis opslagruimte: 10GB, bestandsgrootte beperkt tot 250MB)
* [Dropbox](https://www.dropbox.com/) (gratis opslag: 2GB, uitbreidbaar tot 16GB via uitnodigingen)
* [TeraCloud](https://teracloud.jp/en/) (gratis opslag: 10GB, +5GB via uitnodigingen)
* [Yandex Disk](https://disk.yandex.com/) (gratis gebruikers: 10GB)

Zelfgehoste oplossingen:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}