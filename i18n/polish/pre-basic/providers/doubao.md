
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# ByteDance (Doubao)

*   Zaloguj się do [Volcano Engine](https://console.volcengine.com/)
*   Bezpośrednio przejdź [klikając tutaj](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Uzyskiwanie klucza API

*   Kliknij [Zarządzanie kluczami API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) w dolnym panelu bocznym
*   Utwórz klucz API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   Po utworzeniu, kliknij ikonę oka 🔍 obok klucza API, aby wyświetlić i skopiować go

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Wklej skopiowany klucz API w CherryStudio i włącz przełącznik dostawcy

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Aktywacja i dodawanie modeli

*   W dolnym panelu bocznym konsoli Ark, kliknij [Zarządzanie aktywacjami](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false), aby aktywować potrzebne modele (seria Doubao, DeepSeek itp.)

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   W [dokumentacji listy modeli](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90) znajdź ID modelu odpowiadające wybranemu modelowi

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Przykładowa lista ID modeli w Volcano Engine"><figcaption></figcaption></figure>

*   W ustawieniach Cherry Studio [Usługi modelu](../../cherrystudio/preview/settings/providers.md) znajdź Volcano Engine
*   Kliknij "Dodaj", wklej ID modelu w pole tekstowe ID modelu

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Dodaj kolejne modele, powtarzając tę procedurę

### Adres API

Dostępne są dwa formaty adresu API:
*   Domyślny w kliencie: `https://ark.cn-beijing.volces.com/api/v3/`
*   Alternatywny: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Oba formaty są funkcjonalnie równoważne - zaleca się stosowanie domyślnego bez modyfikacji.

Różnicę między końcówkami `/` i `#` wyjaśniono w dokumentacji ustawień dostawcy, [przejdź do sekcji](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Przykładowe zapytanie cURL z oficjalnej dokumentacji</p></figcaption></figure>