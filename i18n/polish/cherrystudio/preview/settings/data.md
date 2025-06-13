---
icon: database
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Ustawienia danych

Ten interfejs umożliwia tworzenie kopii zapasowych danych klienta w chmurze i lokalnie, przeglądanie lokalnego katalogu danych oraz czyszczenie pamięci podręcznej.

### Kopia zapasowa danych

Obecnie kopia zapasowa danych obsługuje wyłącznie metodę WebDAV. Do tworzenia kopii zapasowych w chmurze możesz wybrać usługi obsługujące WebDAV.

Możesz również zsynchronizować dane między wieloma urządzeniami za pomocą schematu:  
`Komputer A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{przywracanie}}$$ `Komputer B`

#### Przykład: Jianguoyun (Nutstore)

1. Zaloguj się do Jianguoyun, kliknij nazwę użytkownika w prawym górnym rogu i wybierz "Informacje o koncie":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Wybierz "Opcje bezpieczeństwa", kliknij "Dodaj aplikację"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Wprowadź nazwę aplikacji i wygeneruj losowe hasło:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Skopiuj i zapisz hasło:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Uzyskaj adres serwera, login i hasło:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. W Cherry Studio → Ustawienia → Ustawienia danych wprowadź informacje WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Wybierz opcję tworzenia kopii zapasowej lub przywracania danych. Możesz również ustawić harmonogram automatycznych kopii zapasowych:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Usługi WebDAV z niskim progiem wejścia to zazwyczaj dyski w chmurze:
* [Jianguoyun](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (wymaga członkostwa)
* [Dysk Aliyun](https://www.alipan.com/) (wymaga zakupu)
* [Box](https://www.box.com/) (darmowa przestrzeń: 10GB, limit pliku: 250MB)
* [Dropbox](https://www.dropbox.com/) (darmowa przestrzeń: 2GB, rozszerzenie do 16GB przez zaproszenia)
* [TeraCloud](https://teracloud.jp/en/) (darmowa przestrzeń: 10GB + 5GB za zaproszenia)
* [Dysk Yandex](https://disk.yandex.com/) (darmowa przestrzeń: 10GB)

Usługi wymagające samodzielnego wdrożenia:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}