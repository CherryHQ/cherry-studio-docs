---
hidden: True
icon: code
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Struktura kodu

```yaml
...
├─ docs/ # Katalog dokumentacji
├─ resources/ # Katalog plików zasobów
├─ scripts/ # Katalog skryptów
└─ src/ # Główny katalog kodu źródłowego
    ├─main/ # Kod głównego procesu
    ├─preload/ # Katalog skryptów wstępnego ładowania
    └─renderer/ # Kod procesu renderowania
        ├─src/ # Kod źródłowy procesu renderowania
            ├─assets/ # Pliki zasobów
                ├─fonts/ # Pliki czcionek
                ├─images/ # Pliki grafik (np. awatary)
                └─styles/ # Pliki stylów
            ├─components/ # Komponenty
            ├─config/ # Konfiguracja
            ├─context/ # Kontekst
            ├─databases/ # Pliki związane z bazą danych
            ├─hooks/ # Niestandardowe hooki
            ├─i18n/ # Pliki internacjonalizacji
            ├─pages/ # Pliki stron
            ├─providers/ # Konfiguracja dostawców usług
            ├─services/ # Pliki usług
            ├─store/ # Pliki zarządzania stanem
            ├─types/ # Pliki definicji typów TypeScript
            ├─utils/ # Funkcje narzędziowe
            ...
        ...
    ...
...
```