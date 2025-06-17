
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Instalacja środowiska MCP

**MCP (Model Context Protocol)** to otwarty protokół mający na celu dostarczanie informacji kontekstowych do dużych modeli językowych (LLM) w ustandaryzowany sposób. Więcej informacji o MCP znajdziesz w sekcji [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Używanie MCP w Cherry Studio

Poniżej, na przykładzie funkcji `fetch`, pokazujemy jak używać MCP w Cherry Studio. Szczegóły znajdziesz w [dokumentacji](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Przygotowanie: Instalacja uv i bun**

{% hint style="warning" %}
Cherry Studio obecnie korzysta wyłącznie z wbudowanych [uv](https://github.com/astral-sh/uv) i [bun](https://github.com/oven-sh/bun), **bez ponownego wykorzystania** wersji uv i bun zainstalowanych w systemie.
{% endhint %}

W sekcji `Ustawienia - Serwer MCP` kliknij przycisk `Instaluj`, aby automatycznie pobrać i zainstalować. Ponieważ pobieranie odbywa się bezpośrednio z GitHub, może być wolne i istnieje większe ryzyko niepowodzenia. O sukcesie instalacji decyduje obecność plików w folderze opisanym poniżej.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Katalog instalacji plików wykonywalnych:**

Windows: `C:\Users\nazwa_użytkownika\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Katalog bin</p></figcaption></figure>

**W przypadku problemów z instalacją:**

Możesz utworzyć dowiązania symboliczne do odpowiednich poleceń systemowych w tym katalogu. Jeśli folder nie istnieje, utwórz go ręcznie. Możesz też ręcznie pobrać pliki wykonywalne i umieścić je w tym katalogu:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)