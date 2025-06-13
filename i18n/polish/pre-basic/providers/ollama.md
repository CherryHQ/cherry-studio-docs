
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Ollama

Ollama to doskonałe narzędzie open source, które umożliwia łatwe uruchamianie i zarządzanie różnymi dużymi modelami językowymi (LLM) lokalnie. Cherry Studio obsługuje teraz integrację z Ollama, pozwalając na bezpośrednią interakcję z lokalnie wdrożonym LLM w znanym interfejsie, bez konieczności polegania na usługach w chmurze!

## Co to jest Ollama?

Ollama to narzędzie upraszczające wdrażanie i używanie dużych modeli językowych (LLM). Oto jego kluczowe cechy:

* **Lokalne działanie:** Modele działają całkowicie na Twoim komputerze, bez potrzeby połączenia internetowego, chroniąc Twoją prywatność i bezpieczeństwo danych.
* **Łatwość użycia:** Za pomocą prostych poleceń wiersza poleceń możesz pobierać, uruchamiać i zarządzać różnymi LLM.
* **Bogactwo modeli:** Obsługuje różne popularne modele open source jak Llama 2, Deepseek, Mistral, Gemma i inne.
* **Wieloplatformowość:** Działa na systemach macOS, Windows i Linux.
* **Otwarte API:** Posiada interfejs kompatybilny z OpenAI, co umożliwia integrację z innymi narzędziami.

## Dlaczego warto używać Ollama w Cherry Studio?

* **Bez konieczności korzystania z usług w chmurze:** Żadnych limitów ani opłat za API - w pełni wykorzystaj możliwości lokalnego LLM.
* **Prywatność danych:** Wszystkie dane konwersacji pozostają lokalnie, bez ryzyka naruszenia prywatności.
* **Dostępność offline:** Korzystaj z LLM nawet bez połączenia internetowego.
* **Modyfikowalność:** Wybieraj i konfiguruj LLM dokładnie pod swoje potrzeby.

## Konfiguracja Ollama w Cherry Studio

### **1. Instalacja i uruchomienie Ollama**

Najpierw zainstaluj i uruchom Ollama na swoim komputerze:

*   **Pobierz Ollama:** Odwiedź oficjalną stronę Ollama ([https://ollama.com/](https://ollama.com/)) i pobierz instalator odpowiedni dla Twojego systemu.\
    W systemie Linux możesz zainstalować za pomocą polecenia:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Zainstaluj Ollama:** Postępuj zgodnie z instrukcjami instalatora.
*   **Pobierz model:** W terminalu (lub wierszu poleceń) użyj `ollama run`, aby pobrać wybrany model. Przykład dla modelu Llama 2:

    ```sh
    ollama run llama3.2
    ```
* **Utrzymuj Ollama w stanie uruchomienia:** Pozostaw Ollama aktywną podczas pracy z modelami w Cherry Studio.

### **2. Dodawanie dostawcy Ollama w Cherry Studio**

Dodaj Ollama jako niestandardowego dostawcę AI w Cherry Studio:

* **Otwórz ustawienia:** Kliknij ikonę ⚙️ w lewym panelu nawigacyjnym.
* **Przejdź do usług modeli:** Wybierz zakładkę "Model Services".
* **Dodaj dostawcę:** Kliknij pozycję Ollama na liście.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Konfiguracja dostawcy Ollama**

Skonfiguruj szczegóły dostawcy Ollama:

1. **Stan włączenia:**
   * Włącz suwak po prawej stronie, aby aktywować dostawcę.
2. **Klucz API:**
   * Ollama nie wymaga klucza API - pozostaw pole puste lub wpisz dowolną wartość.
3. **Adres API:**
   * Wpisz lokalny adres API Ollama (domyślnie):
       ```
       http://localhost:11434/
       ```
4. **Czas utrzymania aktywności:** Określ czas (w minutach) przed automatycznym rozłączeniem nieaktywnej sesji.
5. **Zarządzanie modelami:**
   * Kliknij "+ Dodaj", aby ręcznie wprowadzić nazwę pobranego modelu (np. `llama3.2`)
   * Użyj przycisku "Zarządzaj" do edycji lub usuwania modeli.

## Rozpoczęcie korzystania

Po konfiguracji wybierz Ollama i pobrany model w interfejsie czatu Cherry Studio, aby rozpocząć lokalną konwersację!

## Wskazówki i porady

* **Pierwsze uruchomienie modelu:** Pobieranie modelu może trwać dłużej - uzbrój się w cierpliwość.
* **Przegląd modeli:** Uruchom `ollama list` w terminalu, aby zobaczyć pobrane modele.
* **Wymagania sprzętowe:** Upewnij się, że Twój komputer spełnia wymagania sprzętowe modelu (CPU, RAM, GPU).
* **Dokumentacja Ollama:** Skorzystaj z linku `查看Ollama文档和模型` w konfiguracji, aby przejść do oficjalnej dokumentacji.