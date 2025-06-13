
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Automatyczna Instalacja MCP

> Automatyczna instalacja MCP wymaga aktualizacji Cherry Studio do wersji v1.1.18 lub nowszej.

## Wprowadzenie do Funkcjonalności

Oprócz instalacji ręcznej, Cherry Studio posiada wbudowane narzędzie `@mcpmarket/mcp-auto-install`, które oferuje wygodniejszy sposób instalacji serwera MCP. Wystarczy, że wprowadzisz odpowiednią komendę w dialogu z dużym modelem obsługującym usługę MCP.

{% hint style="warning" %}
**Przypomnienie o fazie testowej:**

* `@mcpmarket/mcp-auto-install` jest obecnie w fazie testowej
* Efekty zależą od "inteligencji" dużego modelu — niektóre parametry są dodawane automatycznie, inne **nadal wymagają ręcznej zmiany w ustawieniach MCP**
* Obecnie źródłem wyszukiwania jest @modelcontextprotocol, można to skonfigurować samodzielnie (patrz poniżej)
{% endhint %}

## Instrukcja Użycia

Na przykład możesz wprowadzić:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Wprowadzenie polecenia w celu instalacji serwera MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfejs konfiguracji serwera MCP</p></figcaption></figure>

System automatycznie rozpozna Twoje żądanie i dokona instalacji za pomocą `@mcpmarket/mcp-auto-install`. Narzędzie obsługuje wiele typów serwerów MCP, w tym między innymi:

* filesystem (system plików)
* fetch (zapytanie sieciowe)
* sqlite (baza danych)
* itd.

> Zmienna MCP_PACKAGE_SCOPES pozwala na dostosowanie źródła wyszukiwania usług MCP. Wartość domyślna to: `@modelcontextprotocol`, a konfigurację można dostosować.

## Wprowadzenie do biblioteki `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Przykładowa konfiguracja domyślna:**

```json
// `axun-uUpaWEdMEMU8C61K` to identyfikator usługi, można go dostosować
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatyczna instalacja usług MCP (wersja beta)",
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
    "MCP_REGISTRY_PATH": "Szczegóły patrz https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` to otwartoźródłowy pakiet npm. Szczegóły i dokumentację użytkowania można znaleźć w [oficjalnym repozytorium npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` to oficjalna kolekcja usług MCP Cherry Studio.
{% endhint %}