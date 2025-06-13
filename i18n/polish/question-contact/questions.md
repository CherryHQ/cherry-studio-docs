---
icon: seal-question
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Często zadawane pytania

## Typowe kody błędów

* **4xx (Kody stanu błędu klienta)**: Zwykle oznaczają błędy składni żądania, niepowodzenie autoryzacji lub uwierzytelnienia, uniemożliwiające wykonanie żądania.
* **5xx (Kody stanu błędu serwera)**: Zwykle wskazują błędy po stronie serwera, takie jak awaria serwera, przekroczenie czasu przetwarzania żądania itp.

| Kod błędu         | Możliwe przyczyny                                                   | Rozwiązanie                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4>     | Nieprawidłowy format treści żądania itp.                            | <p>Sprawdź zwróconą treść błędu lub zobacz <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">konsolę</a> w poszukiwaniu błędów i postępuj zgodnie z instrukcjami.</p><p><mark style="color:purple;">[Typowy przypadek 1]</mark>: Dla modeli Gemini może być wymagana weryfikacja karty;<br><mark style="color:purple;">[Typowy przypadek 2]</mark>: Przekroczenie limitu danych (częste w modelach wizyjnych) - rozmiar obrazu przekracza limit pojedynczego żądania;<br><mark style="color:purple;">[Typowy przypadek 3]</mark>: Użyto nieobsługiwanych parametrów lub błędne parametry. Prztestuj pomocnika w czystym środowisku;<br><mark style="color:purple;">[Typowy przypadek 4]:</mark> Kontekst przekroczył limit. Wyczyść kontekst, rozpocznij nową rozmowę lub zmniejsz liczbę kontekstów.</p> |
| <h4>401</h4>     | Niepowodzenie uwierzytelnienia: model nieobsługiwany lub konto serwera zablokowane | Skontaktuj się z dostawcą usługi w celu weryfikacji stanu konta                                                                                                                                                                                                                                                                                                                                                                          |
| <h4>403</h4>     | Brak uprawnień do wykonania operacji                                | Działaj zgodnie z komunikatami o błędach zwróconymi w rozmowie lub w [konsoli](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                       |
| <h4>404</h4>     | Nie można odnaleźć żądanego zasobu                                 | Sprawdź ścieżkę żądania itp.                                                                                                                                                                                                                                                                                                                                                                                                             |
| <h4>422</h4>     | Prawidłowy format żądania, ale błąd semantyczny                     | Serwer może przetworzyć żądanie, ale nie może go wykonać. Typowe dla błędów semantycznych JSON (np. wartości null; wymagany ciąg znaków, podano liczbę lub wartość logiczną itp.).                                                                                                                                                                                                                                                           |
| <h4>429</h4>     | Osiągnięto limit liczby żądań                                      | Przekroczono limit liczby żądań (TPM lub RPM), poczekaj chwilę przed ponowieniem                                                                                                                                                                                                                                                                                                                                                         |
| <h4>500</h4>     | Wewnętrzny błąd serwera, nie można zrealizować żądania              | W przypadku ciągłego występowania skontaktuj się z dostawcą usługi                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>501</h4>     | Serwer nie obsługuje żądanej funkcji                                |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <h4>502</h4>     | Serwer bramy lub proxy otrzymał nieprawidłową odpowiedź ze zdalnego serwera |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <h4>503</h4>     | Serwer tymczasowo nie może przetworzyć żądania z powodu przeciążenia lub konserwacji |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <h4>504</h4>     | Serwer bramy lub proxy nie odebrał żądania ze zdalnego serwera w czasie |                                                                                                                                                                                                                                                                                                                                                                                                                                       |



***



## Metoda sprawdzania błędów w konsoli

* Kliknij w okno klienta Cherry Studio i użyj skrótu <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Aktywne okno musi być oknem klienta Cherry Studio, aby wywołać konsolę;
- Najpierw otwórz konsolę, zanim wykonasz żądanie (test, rozmowa itp.), aby zebrać informacje.
{% endhint %}

* W otwartym oknie konsoli kliknij <mark style="color:blue;">`Network`</mark> → Znajdź ostatni element w sekcji ② z czerwoną ikoną <mark style="color:red;">`×`</mark> (dla błędów rozmów, tłumaczeń: <mark style="color:red;">`completions`</mark>; dla błędów malowania: <mark style="color:red;">`generations`</mark>) → Kliknij <mark style="color:blue;">`Response`</mark> aby zobaczyć pełną odpowiedź (obszar ④ na ilustracji).

> Jeśli nie możesz ustalić przyczyny błędu, prześlij zrzut ekranu do [oficjalnej grupy dyskusyjnej](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Metoda działa nie tylko w rozmowach, ale także przy testowaniu modeli, dodawaniu bazy wiedzy, malowaniu itp. W każdym przypadku najpierw otwórz konsolę, a następnie wykonaj żądanie.·

{% hint style="info" %}
Nazwa w sekcji Name (na ilustracji ②) różni się w zależności od scenariusza:<br>
Rozmowa, tłumaczenie, test modelu: <mark style="color:red;">`completions`</mark>&#x20;<br>
Malowanie: <mark style="color:red;">`generations`</mark><br>
Tworzenie bazy wiedzy: <mark style="color:red;">`embeddings`</mark>&#x20;
{% endhint %}

***



## Nierenderowane formuły/błędy renderowania formuł

* Gdy formuła nie jest renderowana, lecz wyświetlany jest jej kod, sprawdź obecność ograniczników:

> **Sposób użycia ograniczników**<br>
> _Formuły w tekście_<br>
> - Pojedynczy znak dolara: `$formula$`<br>
> - Lub `\(` i `\)`: `\(formula\)`<br><br>
> _Bloki formuł_<br>
> - Podwójny znak dolara: `$$formula$$`<br>
> - Lub `\[formula\]`<br>
> - Przykład: `$$\sum_{i=1}^n x_i$$`<br>
>   $$\sum_{i=1}^n x_i$$

* Błędy renderowania formuł/często przy zawartości chińskiej – spróbuj przełączyć silnik formuł na KateX.



***



## Nie można utworzyć bazy wiedzy/niepowodzenie pobrania wymiarów osadzania

1. Model niedostępny

> Sprawdź, czy model jest obsługiwany przez dostawcę oraz czy działa poprawnie.

2. Użyto modelu bez funkcji osadzania

***

## Model nie rozpoznaje obrazów/nie można przesłać lub wybrać obrazu

Najpierw upewnij się, czy model obsługuje rozpoznawanie obrazów. Popularne modele w Cherry Studio są odpowiednio kategoryzowane – ikona oka przy nazwie modelu oznacza tę funkcję.

Modele z obsługą obrazów umożliwiają przesyłanie plików graficznych. Jeśli funkcje nie są prawidłowo przypisane, przejdź do listy modeli u dostawcy, kliknij przycisk ustawień przy nazwie modelu i zaznacz opcję obrazów.

Szczegółowe informacje można znaleźć u dostawcy usługi. Podobnie jak modele osadzania, modele bez obsługi wzroku nie wymagają włączania tej funkcji – jej zaznaczenie nie zmieni zachowania modelu.