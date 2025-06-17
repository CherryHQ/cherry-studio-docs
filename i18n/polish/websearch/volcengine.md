---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Integracja Volcano Engine z dostępem do internetu

### 1. Logowanie/rejestracja konta Volcano Engine <a href="#rclz7" id="rclz7"></a>

Odwiedź oficjalną stronę: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Oficjalna strona Volcano Engine</p></figcaption></figure>

### 2. Tworzenie „Mojej aplikacji” z dostępem do internetu <a href="#gvzaa" id="gvzaa"></a>

**2.1** Zaloguj się do Volcano Engine i przejdź do strony **Volcano Ark**: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

**2.2** **Kliknij kolejno:**<mark style="color:red;">**„Moje aplikacje” → „Utwórz aplikację” → „Zero kodu” → „Czat jeden na jednego”**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Wypełnianie informacji i publikacja aplikacji <a href="#zzdfe" id="zzdfe"></a>

**Nazwa aplikacji**: Wpisz dowolną nazwę (pola z<mark style="color:red;">**\* są wymagane**</mark>, pozostałe można pominąć)

<mark style="color:red;">**Kluczowe: włącz wtyczkę internetową (wymagana wcześniejsza aktywacja)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1 Aktywacja funkcji wtyczki internetowej (zwróć uwagę na koszty i darmowe limity) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Kliknij „Kup teraz” i wykonaj kroki aż pojawi się poniższy ekran, co oznacza pomyślną aktywację</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Status aktywacji – gotowe</p></figcaption></figure>

Wróć do ekranu „Wypełnianie informacji o aplikacji”.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2 Konfiguracja zaawansowana wyszukiwania w Internecie <a href="#sp6uz" id="sp6uz"></a>

Dostosuj do swoich potrzeb:

* Dla precyzyjnej kontroli: użyj opcji<mark style="color:purple;">**„Wywołanie niestandardowe”**</mark>
* Domyślnie:<mark style="color:purple;">**„Wywołanie automatyczne”**</mark>
* Dla maksymalnej aktualności:<mark style="color:purple;">**„Wymuś włączenie”**</mark>

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3 Publikacja aplikacji <a href="#fe1gf" id="fe1gf"></a>

Kliknij **„Opublikuj”** w prawym górnym rogu.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Uzyskiwanie klucza API <a href="#jtqlu" id="jtqlu"></a>

Kliknij kolejno: **„Przewodnik po API” → „Wybierz i skopiuj klucz API” → „Wyświetl i wybierz”**

Skopiuj klucz API i przejdź do Cherry Studio, aby go wkleić.

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

**Uwaga**: Jeśli brak klucza, kliknij **„Utwórz klucz API”** w prawym górnym rogu okna.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Używanie klucza API w Cherry Studio dla deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1 Otwórz Cherry Studio → „Ustawienia” → „Wpisz nazwę” → „Typ: openAI” <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2 Konfiguracja URL i klucza <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Szukasz adresu? Znajdź go tutaj (pamiętaj o „/”):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3 Dodawanie nazwy modelu <a href="#qmh3i" id="qmh3i"></a>

**Uwaga**: Skopiuj nazwę modelu z mniejszego tekstu poniżej.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Podgląd efektów <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>