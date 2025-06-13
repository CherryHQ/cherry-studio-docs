---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Samouczek konfiguracji Obsidian

Cherry Studio obsługuje integrację z Obsidian, umożliwiając eksport pełnych konwersacji lub pojedynczych wiadomości do skarbca Obsidian.

{% hint style="warning" %}
Proces ten nie wymaga instalacji dodatkowych wtyczek Obsidian. Ponieważ jednak mechanizm importowania z Cherry Studio do Obsidian działa podobnie jak Obsidian Web Clipper, zaleca się aktualizację Obsidian do najnowszej wersji (obecna wersja powinna być większa niż **1.7.2**), aby uniknąć [problemów z importowaniem zbyt długich konwersacji](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Najnowszy samouczek

{% hint style="info" %}
W porównaniu do starszej wersji eksportu do Obsidian, nowa funkcja automatycznie wybiera ścieżkę skarbca, eliminując potrzebę ręcznego wprowadzania nazw skarbców i folderów.
{% endhint %}

### Krok 1: Konfiguracja Cherry Studio

Otwórz w Cherry Studio _Ustawienia_ → _Ustawienia danych_ → menu _Konfiguracja Obsidian_. W rozwijanym polu automatycznie pojawią się nazwy skarbców Obsidian otwartych lokalnie - wybierz swój docelowy skarbiec Obsidian:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Krok 2: Eksportowanie konwersacji

#### Eksport pełnej konwersacji

Wróć do interfejsu konwersacji Cherry Studio. Kliknij prawym przyciskiem na konwersację, wybierz _Eksportuj_, następnie kliknij _Eksportuj do Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Pojawi się okno umożliwiające skonfigurowanie **właściwości (Properties)** eksportowanej notatki, **lokalizacji w Obsidian** oraz **metody przetwarzania**:

* **Skarbiec**: z menu rozwijanego możesz wybrać inny skarbiec
* **Ścieżka**: z menu rozwijanego możesz wybrać folder przeznaczony na eksportowaną konwersację
* Jako właściwości notatki (Properties):
  * Tagi (tags)
  * Data utworzenia (created)
  * Źródło (source)
* **Metody przetwarzania** w Obsidian:
  * **Utwórz nową (jeśli istnieje, nadpisz)**: tworzy nową notatkę w wybranym folderze, a w przypadku istnienia notatki o tej samej nazwie - nadpisuje ją
  * **Dołącz na początku**: dołącza wybraną konwersację na początku istniejącej notatki o tej samej nazwie
  * **Dołącz na końcu**: dołącza wybraną konwersację na końcu istniejącej notatki o tej samej nazwie

{% hint style="info" %}
Tylko pierwsza metoda dołącza właściwości (Properties) - pozostałe dwie ich nie uwzględniają.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Konfigurowanie właściwości notatki</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Wybór ścieżki</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Wybór metody przetwarzania</p></figcaption></figure>

Po wybraniu wszystkich opcji kliknij OK, aby wyeksportować pełną konwersację do odpowiedniego folderu w skarbcu Obsidian.

#### Eksport pojedynczej wiadomości

Aby wyeksportować pojedynczą wiadomość, kliknij ikonę _trzech poziomych kresek_ pod wiadomością, wybierz _Eksportuj_, następnie kliknij _Eksportuj do Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Eksport pojedynczej wiadomości</p></figcaption></figure>

Pojawi się to samo okno konfiguracyjne jak przy eksporcie pełnej konwersacji - postępuj zgodnie z instrukcją [powyższego samouczka](obsidian.md#eksport-pełnej-konwersacji).

### Eksport powiódł się

🎉 Gratulacje! Ukończyłeś konfigurację integracji Cherry Studio z Obsidian i pomyślnie przeprowadziłeś proces eksportu. Miłej pracy!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Eksport do Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Podgląd wyniku eksportu</p></figcaption></figure>



***

## Starszy samouczek (dla Cherry Studio <v1.1.13)

### Krok 1: Przygotowanie Obsidian

Otwórz skarbiec Obsidian i utwórz folder przeznaczony na eksportowane konwersacje (na ilustracji przykład folderu "Cherry Studio"):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Zanotuj nazwę wskazaną w lewym dolnym rogu - jest to nazwa twojego _skarbca_.

### Krok 2: Konfiguracja Cherry Studio

W Cherry Studio, przejdź do _Ustawienia_ → _Ustawienia danych_ → menu _Konfiguracja Obsidian_. Wprowadź nazwę _skarbca_ i nazwę _folderu_ uzyskane w [Kroku 1](obsidian.md#krok-1-przygotowanie-obsidian):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

Pole _Globalne tagi_ jest opcjonalne - możesz określić tagi, które będą dołączane do wszystkich eksportowanych konwersacji.

### Krok 3: Eksportowanie konwersacji

#### Eksport pełnej konwersacji

W interfejsie konwersacji Cherry Studio kliknij prawym przyciskiem na konwersację, wybierz _Eksportuj_, następnie kliknij _Eksportuj do Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Eksport pełnej konwersacji</p></figcaption></figure>

Pojawi się okno umożliwiające skonfigurowanie **właściwości notatki (Properties)** oraz **metody przetwarzania**:
* **Utwórz nową (jeśli istnieje, nadpisz)**: tworzy nową notatkę w folderze z [Kroku 2](obsidian.md#krok-2-konfiguracja-cherry-studio), a w przypadku istnienia notatki o tej samej nazwie - nadpisuje ją
* **Dołącz na początku**: dołącza konwersację na początku istniejącej notatki o tej samej nazwie
* **Dołącz na końcu**: dołącza konwersację na końcu istniejącej notatki o tej samej nazwie

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Konfigurowanie właściwości notatki</p></figcaption></figure>

{% hint style="info" %}
Tylko pierwsza metoda dołącza właściwości (Properties) - pozostałe dwie ich nie uwzględniają.
{% endhint %}

#### Eksport pojedynczej wiadomości

Aby wyeksportować pojedynczą wiadomość, kliknij ikonę _trzech poziomych kresek_ pod wiadomością, wybierz _Eksportuj_, następnie kliknij _Eksportuj do Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Eksport pojedynczej wiadomości</p></figcaption></figure>

Postępuj zgodnie z instrukcją jak w przypadku [eksportu pełnej konwersacji](obsidian.md#eksport-pełnej-konwersacji).

### Eksport powiódł się

🎉 Gratulacje! Ukończyłeś konfigurację integracji Cherry Studio z Obsidian i pomyślnie przeprowadziłeś proces eksportu. Miłej pracy!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Eksport do Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Podgląd wyniku eksportu</p></figcaption></figure>