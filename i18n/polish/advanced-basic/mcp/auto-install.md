
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Automatyczna instalacja MCP

> Automatyczna instalacja MCP wymaga uaktualnienia Cherry Studio do wersji v1.1.18 lub nowszej.

## Funkcje

Oprócz ręcznej instalacji, Cherry Studio posiada wbudowane narzędzie `@mcpmarket/mcp-auto-install`, które zapewnia wygodniejszy sposób instalacji serwera MCP. Wystarczy wprowadzić odpowiednią komendę podczas rozmowy z dużym modelem językowym wspierającym usługi MCP.

{% hint style="warning" %}
**Przypomnienie o fazie testów:**

* Narzędzie `@mcpmarket/mcp-auto-install` jest obecnie w fazie testów
* Efektywność zależy od "inteligencji" dużego modelu — czasami parametry dodawane są automatycznie, czasami **należy ręcznie zmienić niektóre ustawienia w konfiguracji MCP**
* Obecnie źródła wyszukiwania pochodzą z @modelcontextprotocol, ale można to skonfigurować (wyjaśniono poniżej)
{% endhint %}

## Instrukcje użytkowania

Na przykład możesz wprowadzić:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Wprowadzanie polecenia instalacji serwera MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfejs konfiguracji serwera MCP</p></figcaption></figure>

System automatycznie rozpozna twoje potrzeby i zakończy instalację za pomocą `@mcpmarket/mcp-auto-install`. Narzędzie obsługuje różne typy serwerów MCP, w tym między innymi:

* filesystem (system plików)
* fetch (żądania sieciowe)
* sqlite (baza danych)
* i inne...

> Zmienna MCP\_PACKAGE\_SCOPES pozwala dostosować źródło wyszukiwania usług MCP. Domyślna wartość to: `@modelcontextprotocol`.

## Opis biblioteki `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Przykładowa konfiguracja domyślna:**

```json
// `axun-uUpaWEdMEMU8C61K` to identyfikator usługi — można go dostosować
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Szczegóły na https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` to otwartoźródłowy pakiet npm. Szczegółowe informacje i dokumentację można znaleźć w [oficjalnym repozytorium npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` reprezentuje oficjalną kolekcję usług MCP Cherry Studio.
{% endhint %}