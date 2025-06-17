
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Konfiguracja i używanie MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Otwórz ustawienia Cherry Studio.
2. Znajdź opcję `Serwery MCP`.
3. Kliknij `Dodaj serwer`.
4. Wprowadź parametry serwera MCP ([link referencyjny](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Możliwe pola do wypełnienia:
   * Nazwa: dowolna nazwa, np. `fetch-server`
   * Typ: wybierz `STDIO`
   * Polecenie: wpisz `uvx`
   * Parametry: wpisz `mcp-server-fetch`
   * (mogą występować dodatkowe parametry w zależności od serwera)
5. Kliknij `Zapisz`.

{% hint style="success" %}
Po skonfigurowaniu Cherry Studio automatycznie pobierze wymagany serwer MCP - `fetch server`. Po zakończeniu pobierania możemy rozpocząć korzystanie! Uwaga: jeśli konfiguracja mcp-server-fetch się nie powiedzie, spróbuj zrestartować komputer.
{% endhint %}

### Włączanie usługi MCP w oknie czatu

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* W konfiguracji `Serwery MCP` pomyślnie dodano serwer MCP

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Przykład działania**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Jak widać na powyższym obrazku, po integracji z funkcją `fetch` MCP, Cherry Studio może lepiej zrozumieć intencje zapytań użytkownika, uzyskać istotne informacje z sieci i dostarczyć bardziej precyzyjne, kompleksowe odpowiedzi.