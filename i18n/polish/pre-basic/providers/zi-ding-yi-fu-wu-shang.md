
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Niestandardowi Dostawcy Usług

Cherry Studio nie tylko integruje główne usługi modeli AI, ale także daje Ci potężne możliwości dostosowywania. Dzięki funkcji **Niestandardowi Dostawcy AI**, możesz łatwo podłączyć dowolny potrzebny Ci model AI.

## Dlaczego warto używać niestandardowych dostawców AI?

* **Elastyczność:** Nie jesteś ograniczony wstępną listą dostawców - możesz swobodnie wybierać modele AI najlepiej dopasowane do Twoich potrzeb.
* **Różnorodność:** Testuj modele AI z różnych platform, odkrywając ich unikalne zalety.
* **Kontrola:** Bezpośrednio zarządzaj kluczami API i adresami dostępu, zapewniając bezpieczeństwo i prywatność.
* **Personalizacja:** Podłączaj modele wdrożone prywatnie, spełniając specyficzne wymagania biznesowe.

## Jak dodać niestandardowego dostawcę AI?

W zaledwie kilku krokach możesz dodać własnego niestandardowego dostawcę AI w Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Otwórz ustawienia:** W lewym pasku nawigacyjnym Cherry Studio kliknij „Ustawienia” (ikona koła zębatego).
2. **Przejdź do usług modelowych:** Na stronie ustawień wybierz zakładkę „Usługi Modelowe”.
3. **Dodaj dostawcę:** Na stronie „Usługi Modelowe” zobaczysz listę istniejących dostawców. Kliknij przycisk „+ Dodaj” pod listą, aby otworzyć okno „Dodaj Dostawcę”.
4. **Wprowadź informacje:** W oknie musisz podać następujące dane:
   * **Nazwa dostawcy:** Nadaj swojemu niestandardowemu dostawcy rozpoznawalną nazwę (np.: MyCustomOpenAI).
   * **Typ dostawcy:** Wybierz typ dostawcy z listy rozwijanej. Obecnie obsługiwane:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Zapisz konfigurację:** Po wypełnieniu kliknij „Dodaj”, aby zapisać konfigurację.

## Konfiguracja niestandardowego dostawcy AI

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Po dodaniu znajdź nowego dostawcę na liście i wykonaj szczegółową konfigurację:

1. **Status aktywności:** Po prawej stronie listy niestandardowych dostawców znajduje się przełącznik - włącz go, aby aktywować usługę.
2. **Klucz API:**
   * Wpisz klucz API (API Key) dostarczony przez Twojego dostawcę AI.
   * Kliknij przycisk „Sprawdź” po prawej stronie, aby zweryfikować poprawność klucza.
3. **Adres API:**
   * Podaj podstawowy adres URL API (Base URL).
   * Koniecznie sprawdź oficjalną dokumentację Twojego dostawcy AI, aby uzyskać prawidłowy adres API.
4. **Zarządzanie modelami:**
   * Kliknij „+ Dodaj”, aby ręcznie dodać ID modelu, który chcesz używać u tego dostawcy (np. `gpt-3.5-turbo`, `gemini-pro`).

   <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

   * Jeśli nie znasz dokładnej nazwy modelu, sprawdź oficjalną dokumentację dostawcy AI.
   * Klikając „Zarządzaj”, możesz edytować lub usunąć istniejące modele.

## Rozpoczęcie pracy

Po wykonaniu powyższej konfiguracji możesz w interfejsie czatu Cherry Studio wybrać swojego niestandardowego dostawcę AI i model, aby rozpocząć rozmowę z AI!

## Użycie vLLM jako niestandardowego dostawcy AI

vLLM to szybka i łatwa w użyciu biblioteka wnioskowania LLM, podobna do Ollama. Oto jak zintegrować vLLM z Cherry Studio:

1. **Zainstaluj vLLM:** Postępuj zgodnie z oficjalną dokumentacją vLLM ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # jeśli używasz pip
    uv pip install vllm # jeśli używasz uv
    ```
2. **Uruchom usługę vLLM:** Uruchom serwis korzystając z interfejsu kompatybilnego z OpenAI. Dwie główne metody:

    * Uruchomienie poprzez `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Uruchomienie poprzez `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Upewnij się, że usługa uruchomiła się poprawnie i nasłuchuje na domyślnym porcie `8000`. Możesz także określić port za pomocą parametru `--port`.

3. **Dodaj dostawcę vLLM w Cherry Studio:**
   * Postępuj zgodnie z wcześniejszymi krokami, aby dodać nowego dostawcę.
   * **Nazwa dostawcy:** `vLLM`
   * **Typ dostawcy:** Wybierz `OpenAI`.
4. **Skonfiguruj dostawcę vLLM:**
   * **Klucz API:** Ponieważ vLLM nie wymaga klucza API, możesz zostawić to pole puste lub wpisać dowolną wartość.
   * **Adres API:** Podaj adres API vLLM (domyślnie: `http://localhost:8000/`; zmień port w razie potrzeby).
   * **Zarządzanie modelami:** Dodaj nazwę modelu załadowanego w vLLM. Dla przykładu `python -m vllm.entrypoints.openai.api_server --model gpt2` wpisz `gpt2`.
5. **Rozpocznij rozmowę:** Teraz możesz wybrać dostawcę vLLM i model (np. `gpt2`) w Cherry Studio, aby rozpocząć konwersację z LLM napędzanym przez vLLM!

## Wskazówki i techniki

* **Dokładnie czytaj dokumentację:** Przed dodaniem niestandardowego dostawcy sprawdź jego dokumentację dotyczącą kluczy API, adresów dostępu i nazw modeli.
* **Weryfikuj klucze API:** Korzystaj z przycisku „Sprawdź”, aby szybko zweryfikować klucze API.
* **Zwracaj uwagę na adresy API:** Adresy API różnią się w zależności od dostawcy i modelu - upewnij się, że podajesz prawidłowy adres.
* **Dodawaj tylko potrzebne modele:** Dodawaj wyłącznie modele, których faktycznie używasz, unikając nadmiarowych wpisów.