
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# GitHub Copilot

Aby używać GitHub Copilot, musisz najpierw posiadać konto GitHub i subskrybować usługę GitHub Copilot. Bezpłatna wersja również działa, ale nie obsługuje najnowszego modelu Claude 3.7. Więcej informacji znajdziesz na [oficjalnej stronie GitHub Copilot](https://github.com/features/copilot).

## Uzyskiwanie kodu urządzenia

Kliknij "Zaloguj się przez GitHub", aby uzyskać Device Code i skopiować go.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Przykładowy obraz uzyskiwania Device Code"><figcaption><p>Uzyskiwanie Device Code</p></figcaption></figure>

## Wprowadź kod urządzenia w przeglądarce i udziel autoryzacji

Po uzyskaniu Device Code, kliknij link aby otworzyć przeglądarkę. Zaloguj się na swoje konto GitHub, wprowadź Device Code i udziel autoryzacji.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Przykładowy obraz autoryzacji GitHub"><figcaption><p>Autoryzacja GitHub</p></figcaption></figure>

Po udzieleniu autoryzacji, wróć do Cherry Studio i kliknij "Połącz z GitHub". Po udanym połączeniu zostaną wyświetlone nazwa użytkownika GitHub i awatar.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Przykładowy obraz udanego połączenia z GitHub"><figcaption><p>Udane połączenie z GitHub</p></figcaption></figure>

## Kliknij "Zarządzaj", aby uzyskać listę modeli

Kliknij przycisk "Zarządzaj" u dołu strony, aby automatycznie pobrać aktualnie obsługiwane modele.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Przykładowy obraz uzyskiwania listy modeli"><figcaption><p>Uzyskiwanie listy modeli</p></figcaption></figure>

## Częste problemy

### Uzyskanie Device Code nie powiodło się, spróbuj ponownie

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Przykładowy obraz błędu uzyskiwania Device Code"><figcaption><p>Błąd uzyskiwania Device Code</p></figcaption></figure>

Obecne żądania są budowane przy użyciu Axios, który nie obsługuje proxy SOCKS. Użyj proxy systemowego lub HTTP, lub zamiast ustawiać proxy w CherryStudio, użyj globalnego proxy. Najpierw upewnij się, że masz aktywne połączenie internetowe, aby uniknąć problemów z uzyskiwaniem Device Code.