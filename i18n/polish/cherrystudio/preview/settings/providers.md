---
icon: cloud-check
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Ustawienia dostawców

Ta strona zawiera jedynie opis funkcji interfejsu. Instrukcje konfiguracyjne znajdziesz w samouczku [Konfiguracja dostawców](../../../pre-basic/providers/) w podstawowych samouczkach.

{% hint style="info" %}
* Przy korzystaniu z wbudowanych dostawców wystarczy podać odpowiedni klucz.
* Różni dostawcy mogą używać różnych nazw dla klucza: klucz, Key, API Key, token – wszystkie odnoszą się do tego samego elementu.
{% endhint %}

### Klucz API

W Cherry Studio pojedynczy dostawca obsługuje rotację wielu kluczy w kolejności sekwencyjnej od pierwszego do ostatniego.

* Wiele kluczy dodaje się, rozdzielając je angielskim przecinkiem, jak w poniższym przykładzie:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Należy używać **wyłącznie** angielskiego przecinka.
{% endhint %}

### Adres API

Przy korzystaniu z wbudowanych dostawców zwykle nie trzeba podawać adresu API. Jeśli konieczna jest zmiana, należy ściśle stosować się do adresów podanych w oficjalnej dokumentacji.

> Jeśli dostawca podaje adres w formacie <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, wystarczy wpisać część podstawową adresu (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio automatycznie dołączy pozostałą część ścieżki (<mark style="background-color:green;">/v1/chat/completions</mark>). Niewłaściwe wypełnienie może uniemożliwić działanie.

{% hint style="info" %}
Uwaga: Większość dostawców używa ujednoliconej ścieżki dla modeli językowych. Jeśli ścieżka API dostawcy to np. v2 lub v3/chat/completions, można ręcznie wpisać odpowiednią wersję zakończoną `/`. Gdy ścieżka jest niestandardowa, podaj pełny adres zakończony `#`.

Podsumowanie:
* Adres zakończony `/` powoduje automatyczne dołączenie "<mark style="background-color:green;">chat/completions</mark>"
* Adres zakończony `#` używa wyłącznie podanego adresu bez modyfikacji.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Dodawanie modeli

Standardowo kliknięcie przycisku `Zarządzaj` w lewym dolnym rogu strony konfiguracji automatycznie pobiera wszystkie obsługiwane modele. Z listy kliknij `+` przy wybranym modelu, aby dodać go do listy.

{% hint style="info" %}
Modele z okna podręcznego NIE są dodawane automatycznie. Aby pojawiły się w głównej liście modeli, należy kliknąć `+` przy każdym wybranym modelu.
{% endhint %}

### Test połączenia

Kliknij przycisk testu obok pola klucza API, aby sprawdzić poprawność konfiguracji.

{% hint style="info" %}
Test domyślnie używa ostatniego modelu konwersacyjnego z listy. W przypadku błędu sprawdź, czy lista nie zawiera nieobsługiwanych modeli.
{% endhint %}

{% hint style="danger" %}
Po pomyślnej konfiguracji **koniecznie włącz przełącznik w prawym górnym rogu**. W przeciwnym razie dostawca pozostanie nieaktywny, a jego modele nie pojawią się w liście.
{% endhint %}