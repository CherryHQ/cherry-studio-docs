---
icon: database
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Ustawienia danych

W tym interfejsie możesz wykonywać operacje takie jak: tworzenie kopii zapasowych danych klienta w chmurze i lokalnie, przeglądanie lokalnego katalogu danych oraz czyszczenie pamięci podręcznej.

### Kopia zapasowa danych

Obecnie kopia zapasowa danych obsługuje tylko metodę WebDAV. Do tworzenia kopii zapasowych w chmurze możesz wybrać usługę obsługującą WebDAV.

Możesz również zsynchronizować dane między wieloma urządzeniami, używając metody:  
`Komputer A` $$\xrightarrow{\text{kopia zapasowa}}$$ `WebDAV` $$\xrightarrow{\text{przywracanie}}$$ `Komputer B`.

#### Na przykładzie Jianguoyun

1.  Zaloguj się do Jianguoyun, kliknij nazwę użytkownika w prawym górnym rogu i wybierz "Informacje o koncie":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2.  Wybierz "Opcje bezpieczeństwa", a następnie kliknij "Dodaj aplikację"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3.  Wprowadź nazwę aplikacji, wygeneruj losowe hasło;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4.  Skopiuj i zapisz hasło;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5.  Uzyskaj adres serwera, konto i hasło;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6.  W ustawieniach Cherry Studio → Ustawienia danych wprowadź informacje WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7.  Wybierz tworzenie kopii zapasowej lub przywracanie danych i ustaw cykl automatycznego tworzenia kopii zapasowych.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Usługi WebDAV o niskim progu wejścia to zazwyczaj dyski w chmurze:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (wymaga członkostwa)
* [阿里云盘](https://www.alipan.com/) (wymaga zakupu)
* [Box](https://www.box.com/) (darmowa przestrzeń: 10GB, limit pliku: 250MB)
* [Dropbox](https://www.dropbox.com/) (darmowe 2GB, rozszerzenie do 16GB przez zaproszenia)
* [TeraCloud](https://teracloud.jp/en/) (darmowe 10GB, +5GB za zaproszenia)
* [Yandex Disk](https://disk.yandex.com/) (darmowy limit: 10GB)

Ponadto usługi wymagające własnej konfiguracji:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}