---
icon: message
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Interfejs konwersacji

## Asystenci i tematy

### Asystent

`Asystent` umożliwia personalizację wybranego modelu poprzez ustawienia takie jak predefiniowane podpowiedzi czy parametry, dzięki czemu model lepiej odpowiada oczekiwaniom użytkownika.

`Domyślny asystent systemowy` zawiera ogólne parametry (bez podpowiedzi), które można użyć bezpośrednio lub znaleźć odpowiednie predefinicje na [stronie agentów](agents.md).

### Temat

`Asystent` jest nadrzędny w stosunku do `Tematu`. Pojedynczy asystent może mieć wiele tematów (konwersacji), a wszystkie `Tematy` współdzielą ustawienia modelu jak parametry i predefiniowane podpowiedzi (prompt).

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Przyciski w obszarze czatu

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nowy temat` Tworzy nowy temat w bieżącym asystencie.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Prześlij obraz lub dokument` Przesyłanie obrazów wymaga wsparcia modelu. Dokumenty są automatycznie przekształcane na tekst jako kontekst dla modelu.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Wyszukiwanie internetowe` Wymaga konfiguracji w ustawieniach. Wyniki wyszukiwania są przekazywane modelowi jako kontekst. Szczegóły w [trybie online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Baza wiedzy` Aktywuje bazę wiedzy. Szczegóły w [samouczku bazy wiedzy](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Serwer MCP` Aktywuje funkcję serwera MCP. Szczegóły w [samouczku MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generuj obraz` Domyślnie ukryte. Dla modeli obsługujących generowanie obrazów (np. Gemini) wymaga ręcznej aktywacji.

{% hint style="info" %}
Z powodów technicznych musisz ręcznie aktywować przycisk, aby generować obrazy. Przycisk zostanie usunięty po optymalizacji tej funkcji.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Wybierz model` Przełącza model dla kolejnych odpowiedzi, zachowując kontekst.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Skrócone frazy` Wymaga wcześniejszego skonfigurowania w ustawieniach. Obsługuje zmienne.

![](../../.gitbook/assets/对话界面/清空消息.png) `Wyczyść wiadomości` Usuwa całą zawartość bieżącego tematu.

![](../../.gitbook/assets/对话界面/展开.png) `Rozwiń` Powiększa obszar czatu dla dłuższych tekstów.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Wyczyść kontekst` Resetuje kontekst bez usuwania treści (model "zapomina" poprzednią rozmowę).

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Szacowana liczba tokenów` Pokazuje: `bieżące tokeny kontekstu`, `maks. tokeny kontekstu` (∞ oznacza nieograniczone), `długość wiadomości`, `szacowane tokeny`.

{% hint style="info" %}
Funkcja szacuje tokeny. Rzeczywista wartość zależy od modelu. Weryfikuj u dostawcy.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Tłumacz` Tłumaczy treść z pola wprowadzania na angielski.

## Ustawienia czatu

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Ustawienia modelu

Synchronizowane z ustawieniami asystenta. Szczegóły w [edytowaniu asystenta](chat.md#edytuj-asystenta).

{% hint style="info" %}
W ustawieniach konwersacji tylko te ustawienia modelu dotyczą bieżącego asystenta. Pozostałe ustawienia mają zasięg globalny (np. zmiana stylu wiadomości na bańki).
{% endhint %}

### Ustawienia wiadomości

#### <mark style="color:blue;">**`Separator wiadomości`**</mark>:

Dodaje linię oddzielającą treść wiadomości od panelu akcji.

{% tabs %}
{% tab title="Włączony" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Wyłączony" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Użyj fontu szeryfowego`**</mark>:

Zmienia styl czcionki. Możesz też dostosować czcionkę poprzez [niestandardowy CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Pokazuj numery linii w kodzie`**</mark>:

Wyświetla numery linii w blokach kodu generowanych przez model.

{% tabs %}
{% tab title="Wyłączony" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Włączony" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Zwijalne bloki kodu`**</mark>:

Długie fragmenty kodu są automatycznie zwijane.

#### <mark style="color:blue;">**`Zawijanie wierszy kodu`**</mark>:

Długie linie kodu przekraczające szerokość okna są automatycznie zawijane.

#### <mark style="color:blue;">**`Automatyczne zwijanie procesu rozumowania`**</mark>:

Dla modeli obsługujących rozumowanie zwija etapy przetwarzania po zakończeniu.

#### <mark style="color:blue;">**`Styl wiadomości`**</mark>:

Zmienia styl interfejsu na bańki lub listę.

#### <mark style="color:blue;">**`Styl kodu`**</mark>:

Zmienia wygląd fragmentów kodu.

#### <mark style="color:blue;">**`Silnik wzorów matematycznych`**</mark>:

* KaTeX: szybszy, zoptymalizowany pod kątem wydajności;
* MathJax: wolniejszy, ale obsługuje więcej symboli i poleceń.

#### <mark style="color:blue;">**`Rozmiar czcionki wiadomości`**</mark>:

Dostosowuje wielkość czcionki w interfejsie.

### Ustawienia wprowadzania

#### <mark style="color:blue;">**`Pokaż szacowaną liczbę tokenów`**</mark>:

Wyświetla szacowane zużycie tokenów dla wprowadzanego tekstu (orientacyjne).

#### <mark style="color:blue;">**`Wklejanie długich tekstów jako pliki`**</mark>:

Wklejone długie teksty są wyświetlane jako pliki, redukując zakłócenia.

#### <mark style="color:blue;">**`Renderuj Markdown w wprowadzanych wiadomościach`**</mark>:

Wyłączone: renderuje tylko odpowiedzi modelu. Włączone: renderuje także wysłane wiadomości.

{% tabs %}
{% tab title="Wyłączone" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Włączone" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Szybkie tłumaczenie potrójnym spacją`**</mark>:

Potrójne naciśnięcie spacji w polu wprowadzania tłumaczy treść na angielski.

{% hint style="warning" %}
Uwaga: Nadpisuje oryginalny tekst.
{% endhint %}

#### <mark style="color:blue;">**`Docelowy język`**</mark>:

Ustawia język dla tłumaczenia przycisku i potrójnej spacji.

## Ustawienia asystenta

Wybierz <mark style="background-color:yellow;">nazwę asystenta</mark> → w <mark style="background-color:yellow;">menu kontekstowym</mark> wybierz odpowiednie ustawienia

### Edytuj asystenta

{% hint style="info" %}
Ustawienia asystenta dotyczą wszystkich jego tematów.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Ustawienia podpowiedzi

#### <mark style="color:blue;">**`Nazwa`**</mark>:

Dostosuj rozpoznawalną nazwę asystenta.

#### <mark style="color:blue;">**`Podpowiedź`**</mark>:

Prompt. Strukturę można wzorować na przykładach ze strony agentów.

#### Ustawienia modelu

#### <mark style="color:blue;">**`Domyślny model`**</mark>:

Można przypisać stały model dla asystenta. Bez ustawienia używany jest model globalny ([domyślny model asystenta](settings/default-models.md#default-assistant-model)).

{% hint style="info" %}
Istnieją dwa domyślne modele asystenta: globalny i przypisany do asystenta. Model przypisany ma wyższy priorytet. Brak przypisanego modelu = użycie modelu globalnego.
{% endhint %}

#### <mark style="color:blue;">**`Automatyczne resetowanie modelu`**</mark>:

Włączone: nowe tematy używają domyślnego modelu asystenta. Wyłączone: nowe tematy używają modelu ostatnio używanego w konwersacji.

> Przykład: Domyślny model to gpt-3.5-turbo. W temacie 1 zmieniono na gpt-4o. 
>
> • Włączone: Temat 2 używa gpt-3.5-turbo  
> • Wyłączone: Temat 2 używa gpt-4o

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark>:

Kontroluje losowość generowania (domyślnie 0.7):
* Niska (0-0.3): przewidywalne odpowiedzi, idealne do generowania kodu
* Średnia (0.4-0.7): balans kreatywności, polecane do konwersacji (~0.5)
* Wysoka (0.8-1.0): wysokie kreatywne możliwości, ale niższa spójność

#### <mark style="color:blue;">**`Top P (próbkowanie jądra)`**</mark>:

Domyślnie 1. Niższe wartości = bardziej konserwatywne odpowiedzi, wyższe = większa różnorodność:
* Małe (0.1-0.3): tylko najbardziej prawdopodobne słowa
* Średnie (0.4-0.6): balans różnorodności
* Duże (0.7-1.0): bogatsze i bardziej zróżnicowane treści

{% hint style="info" %}
- Parametry mogą być używane oddzielnie lub razem  
- Dostosuj wartości do typu zadania  
- Przeprowadź testy, aby znaleźć optymalne kombinacje  
- Przedziały podane orientacyjnie. Weryfikuj w dokumentacji modelu.
{% endhint %}

#### <mark style="color:blue;">**`Liczba kontekstów (Context Window)`**</mark>

Ilość wiadomości zachowywanych w kontekście:
* 5-10: do standardowych rozmów
* >10: dla skomplikowanych zadań wymagających pamięci (np. tworzenie długich tekstów)
* UWAGA: Więcej wiadomości = więcej tokenów

#### <mark style="color:blue;">**`Włącz ograniczenie długości (MaxToken)`**</mark>

Maksymalna liczba [tokenów](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) w odpowiedzi.

> Przykład: Podczas testowania modeli w CherryStudio możesz ustawić MaxToken na 1, aby sprawdzić łączność.

Większość modeli obsługuje do 32k tokenów (niektóre 64k+). 
Sugerowane wartości:
* Konwersacje: 500-800
* Krótkie teksty: 800-2000
* Generowanie kodu: 2000-3600
* Długie teksty: 4000+ (wymaga wsparcia modelu)

{% hint style="success" %}
Sugerowane:  
- Konwersacje: 500-800  
- Krótkie teksty: 800-2000  
- Generowanie kodu: 2000-3600  
- Długie teksty: 4000+ (wymaga wsparcia modelu)  
{% endhint %}

{% hint style="warning" %}
Odpowiedź może zostać przycięta (np. przy długim kodzie). Dostosuj w razie potrzeby.
{% endhint %}

#### <mark style="color:blue;">**`Strumieniowe wyjście (Stream)`**</mark>

Dane przesyłane w czasie rzeczywistym (efekt maszyny do pisania).  
Wyłączone: odpowiedź pojawia się jednorazowo (jak wiadomość w komunikatorze).  
Włączone: tekst przesyłany fragmentami.

{% hint style="info" %}
Wyłącz dla modeli nieobsługujących strumieniowania (np. o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Parametry niestandardowe`**</mark>

Dodaje dodatkowe parametry w żądaniu (np. `presence_penalty`). Dla zaawansowanych użytkowników.  
Składnia: nazwa parametru—typ—wartość. Dokumentacja: [kliknij tutaj](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Parametry niestandardowe mają wyższy priorytet niż wbudowane (nadpisują je)  
- Użyj `nazwa_parametru:undefined`, aby wykluczyć parametr  
- Sprawdź dokumentację dostawcy modelu pod kątem unikalnych parametrów
{% endhint %}