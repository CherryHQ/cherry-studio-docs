---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Tryb online

{% hint style="info" %}
Przykłady scenariuszy wymagających połączenia internetowego:

* Informacje wymagające aktualności: np. dzisiejsza/tegotygodniowa/aktualna cena złota.
* Dane w czasie rzeczywistym: np. pogoda, kursy walut i inne dynamiczne wartości.
* Nowości: np. nowe technologie, koncepcje, wydarzenia itp...
{% endhint %}

### I. Jak włączyć tryb online

W oknie rozmowy Cherry Studio kliknij ikonę 【Globus】, aby włączyć tryb online.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Kliknij ikonę globusa - włącz połączenie internetowe</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Wskaźnik włączenia trybu online</p></figcaption></figure>

### II. Uwaga: istnieją dwa tryby połączenia internetowego

#### Tryb 1: Wbudowana funkcja online w modelach dostawców usług

W tym przypadku po włączeniu funkcji można natychmiast korzystać z połączenia internetowego.

{% hint style="warning" %}
Możesz szybko sprawdzić, czy model obsługuje tryb online, patrząc na obecność ikony globusa przy nazwie modelu w górnej części interfejsu.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Ta metoda pozwala również szybko rozróżnić modele z obsługą internetu na stronie zarządzania modelami.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Obecni wspierani dostawcy modeli z trybem online:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (wszystkie modele)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian</mark>

{% hint style="danger" %}
Uwaga specjalna:
Istnieją wyjątkowe sytuacje, gdy model bez ikony globusa może korzystać z internetu, jak wyjaśniono w poniższym przewodniku.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Tryb 2: Korzystanie z usługi Tavily dla modeli bez wbudowanej obsługi internetu

Gdy używamy modelu bez wbudowanej obsługi internetu (bez ikony globusa), który wymaga dostępu do aktualnych informacji, używamy usługi wyszukiwania Tavily.

**Przy pierwszym użyciu Tavily** pojawi się okno z prośbą o konfigurację - postępuj zgodnie z instrukcjami.

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Kliknij: Przejdź do ustawień</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Kliknij "Pobierz klucz"</p></figcaption></figure>

Po kliknięciu "Pobierz klucz" nastąpi przekierowanie do **strony rejestracji Tavily**. Po zalogowaniu utwórz klucz API i skopiuj go do Cherry Studio.

{% hint style="danger" %}
Instrukcja rejestracji znajduje się w dokumentacji Tavily w tym katalogu.
{% endhint %}

**Dokumentacja rejestracji Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Poniższy interfejs oznacza pomyślną rejestrację.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Skopiuj klucz</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Wklej klucz - gotowe</p></figcaption></figure>

Testujemy działanie - wyniki pokazują pomyślne wyszukanie online z domyślną liczbą 5 wyników.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Uwaga: Tavily ma miesięczny darmowy limit, po przekroczeniu wymagana jest opłata.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: W przypadku błędów prosimy o kontakt.