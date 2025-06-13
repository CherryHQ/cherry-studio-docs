
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Wbudowana konfiguracja MCP

### @cherry/mcp-auto-install

Automatyczna instalacja usługi MCP (wersja beta)

### @cherry/memory

Implementacja bazująca na trwałej pamięci opartej na lokalnej mapie wiedzy. Pozwala to modelowi zapamiętać istotne informacje o użytkowniku pomiędzy różnymi rozmowami.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Implementacja serwera MCP, która dostarcza narzędzi do rozwiązywania problemów w sposób dynamiczny i refleksyjny poprzez ustrukturyzowany proces myślowy.

### @cherry/brave-search

Implementacja serwera MCP zintegrowana z interfejsem API wyszukiwania Brave, oferująca podwójną funkcjonalność wyszukiwania w sieci i lokalnie.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Serwer MCP służący do pobierania zawartości stron internetowych z podanego adresu URL.

### @cherry/filesystem

Serwer Node.js implementujący protokół kontekstu modelu (MCP) do operacji na systemie plików.