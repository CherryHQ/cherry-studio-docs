---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Funkcje głosowe

```
Cherry Studio Instrukcja obsługi funkcji głosowych

I. Przegląd funkcji głosowych

Cherry Studio oferuje trzy główne moduły funkcji głosowych: TTS (zamiana tekstu na mowę), ASR (rozpoznawanie mowy) oraz rozmowę głosową. Te funkcje umożliwiają naturalną komunikację głosową z AI, znacznie poprawiając komfort użytkowania.

- TTS (Text-To-Speech): Konwertuje tekstową odpowiedź AI na głos
- ASR (Automatic Speech Recognition): Przekształca mowę użytkownika na tekst
- Rozmowa głosowa: Połączenie TTS i ASR zapewniające doświadczenie podobne do głosowego ChatGPT

II. Funkcja TTS (zamiana tekstu na mowę)

1. Obsługiwane typy usług

Cherry Studio obsługuje cztery typy usług TTS:

- OpenAI: Korzysta z API TTS OpenAI, wymaga klucza API
- Przeglądarkowy TTS: Wykorzystuje wbudowaną funkcję syntezy mowy w przeglądarce, darmowy bez konfiguracji
- Siliconflow: Korzysta z usługi TTS Siliconflow, wymaga klucza API
- Darmowy online TTS: Korzysta z darmowych online'owych usług TTS, bez klucza API

2. Metoda konfiguracji

1) Przejdź do strony ustawień, wybierz zakładkę "Funkcje głosowe"
2) W podzakładce "TTS":
   - Włącz funkcję TTS (przełącznik)
   - Wybierz typ usługi TTS
   - W zależności od wybranej usługi skonfiguruj parametry:
     - OpenAI: Podaj klucz API, adres API, wybierz głos i model
     - Przeglądarkowy TTS: Wybierz głos
     - Siliconflow: Podaj klucz API, adres API, wybierz głos, model, format odpowiedzi i szybkość mowy
     - Darmowy online TTS: Wybierz głos i format wyjściowy
3) Skonfiguruj filtry TTS (opcjonalnie):
   - Filtruj proces myślenia
   - Filtruj znaczniki Markdown
   - Filtruj bloki kodu
4) Ustaw, czy wyświetlać pasek postępu TTS
5) Kliknij przycisk "Testuj TTS", aby sprawdzić konfigurację

3. Metoda użycia

- Po włączeniu TTS odpowiedzi AI będą automatycznie konwertowane na głos
- W interfejsie czatu pod każdą odpowiedzią AI pojawi się przycisk odtwarzania TTS
- Kliknij przycisk odtwarzania, aby odtworzyć/wstrzymać głos
- Jeśli włączono pasek postępu TTS, pod tekstem pojawi się postęp odtwarzania
- Długie teksty są automatycznie dzielone na segmenty i odtwarzane ciągłe

III. Funkcja ASR (rozpoznawanie mowy)

1. Obsługiwane typy usług

Cherry Studio obsługuje trzy typy usług ASR:

- OpenAI: Korzysta z modelu Whisper OpenAI, wymaga klucza API
- Przeglądarka: Wykorzystuje wbudowaną funkcję rozpoznawania mowy przeglądarki, darmowe bez konfiguracji
- Serwer lokalny: Łączy się z lokalnym serwerem WebSocket do rozpoznawania mowy

2. Metoda konfiguracji

1) Przejdź do strony ustawień, wybierz zakładkę "Funkcje głosowe"
2) W podzakładce "ASR":
   - Włącz funkcję ASR (przełącznik)
   - Wybierz typ usługi ASR
   - W zależności od wybranej usługi skonfiguruj parametry:
     - OpenAI: Podaj klucz API, adres API, wybierz model
     - Przeglądarka: Brak dodatkowej konfiguracji
     - Serwer lokalny: Ustaw, czy uruchamiać serwer ASR automatycznie przy starcie aplikacji
   - Wybierz język rozpoznawania mowy (domyślnie chiński)
3) Kliknij przycisk "Testuj ASR", aby sprawdzić konfigurację

3. Metoda użycia

- Po włączeniu ASR obok pola wprowadzania pojawi się przycisk rozpoznawania mowy
- Kliknij przycisk, aby rozpocząć nagrywanie
- Po wypowiedzeniu tekstu mowa zostanie przekształcona na tekst w polu wprowadzania
- Ponowne kliknięcie przycisku kończy nagrywanie
- ASR obsługuje ciągłe rozpoznawanie wielu wypowiedzi w trybie akumulacyjnym

IV. Funkcja rozmowy głosowej

1. Cechy funkcjonalne

- Łączy TTS i ASR, oferując doświadczenie głosowej konwersacji podobne do ChatGPT
- Korzysta z pływającego okna z możliwością przeciągania
- Obsługuje tryb mówienia przy długim naciśnięciu
- Obsługuje niestandardowe skróty klawiszowe
- Obsługuje zwijanie okna
- Możliwość wyboru specjalnego modelu do rozmów głosowych
- Obsługuje niestandardowe podpowiedzi

2. Metoda konfiguracji

1) Przejdź do strony ustawień, wybierz zakładkę "Funkcje głosowe"
2) W podzakładce "Funkcje rozmowy":
   - Włącz funkcję rozmowy głosowej (przełącznik)
   - Kliknij "Wybierz model", aby wskazać model AI dla rozmów głosowych
   - Wprowadź niestandardowe podpowiedzi w polu tekstowym (opcjonalnie)
   - Kliknij "Zapisz" aby zachować podpowiedzi lub "Resetuj" aby przywrócić domyślne

3. Metoda użycia

1) W interfejsie czatu kliknij ikonę telefonu po prawej stronie pola wprowadzania
2) Otworzy się okno rozmowy głosowej z powitalnym komunikatem głosowym
3) Przytrzymaj przycisk "Przytrzymaj, aby mówić" aby rozpocząć nagrywanie (lub użyj skrótu)
4) Puść przycisk, aby zakończyć nagrywanie i przesłać do AI
5) AI generuje odpowiedź i odtwarza ją przez TTS
6) Korzystaj z przycisków sterujących:
   - Przycisk wyciszania: Kontroluje wyjście TTS
   - Przycisk pauzy: Zatrzymuje/wznawia rozmowę
   - Przycisk ustawień: Konfiguruje skróty klawiszowe
   - Przycisk zwijania: Minimalizuje okno do linii nagrywania
7) Kliknij przycisk zamknięcia, aby zakończyć rozmowę

4. Konfiguracja skrótów klawiszowych

1) W oknie rozmowy głosowej kliknij przycisk ustawień
2) W panelu ustawień kliknij przycisk skrótów
3) Naciśnij żądany klawisz (np. spacja, Shift)
4) Kliknij "Zapisz" aby zatwierdzić
5) Podczas rozmowy: przytrzymaj klawisz do nagrywania, puść do zakończenia i wysłania

V. Częste problemy i rozwiązania

1. Problemy z TTS

- Problem: Brak dźwięku TTS
  Rozwiązanie: Sprawdź czy TTS jest włączony, upewnij się o poprawnym typie usługi i konfiguracji

- Problem: Słaba jakość odtwarzania TTS
  Rozwiązanie: Spróbuj zmienić usługę TTS lub głos

- Problem: Błędy podczas odtwarzania TTS
  Rozwiązanie: Sprawdź klucz API i połączenie sieciowe

2. Problemy z ASR

- Problem: ASR nie rozpoznaje mowy
  Rozwiązanie: Sprawdź czy ASR jest włączony, upewnij się o poprawnym typie usługi i konfiguracji

- Problem: Niska dokładność rozpoznawania ASR
  Rozwiązanie: Spróbuj zmienić usługę ASR lub dostosuj położenie mikrofonu

- Problem: Błąd połączenia z serwerem ASR
  Rozwiązanie: Sprawdź działanie lokalnego serwera lub uruchom ponownie aplikację

3. Problemy z rozmową głosową

- Problem: Nie można otworzyć okna rozmowy
  Rozwiązanie: Sprawdź czy funkcja jest włączona i czy TTS/ASR są poprawnie skonfigurowane

- Problem: Brak reakcji przy długim naciśnięciu
  Rozwiązanie: Sprawdź uprawnienia mikrofonu lub uruchom ponownie rozmowę

- Problem: Brak głosowej odpowiedzi AI
  Rozwiązanie: Sprawdź czy TTS jest włączony i czy nie jest wyciszony

VI. Zaawansowane ustawienia i opcje niestandardowe

1. Zaawansowane ustawienia TTS

- Filtry: Odfiltrowywanie procesu myślenia, znaczników Markdown i bloków kodu dla płynniejszego odtwarzania
- Pasek postępu: Wyświetlanie postępu odtwarzania
- Niestandardowe głosy i modele: Dodawanie własnych opcji głosów i modeli

2. Zaawansowane ustawienia ASR

- Automatyczne uruchamianie serwera: Ustawia czy serwer ASR ma się uruchamiać przy starcie aplikacji
- Wybór języka: Wybór różnych języków rozpoznawania mowy

3. Zaawansowane ustawienia rozmowy głosowej

- Niestandardowe podpowiedzi: Dostosowywanie podpowiedzi dla AI w trybie rozmowy głosowej
- Wybór specjalnego modelu: Możliwość oddzielnego wyboru modelu AI dla rozmów głosowych
- Niestandardowe skróty klawiszowe: Ustawianie własnych skrótów kontrolujących nagrywanie

VII. Sugestie użytkowania

1. Wybór odpowiedniej usługi TTS:
   - Wysoka jakość: OpenAI lub Siliconflow
   - Bez konfiguracji: Przeglądarkowy TTS lub Darmowy online TTS

2. Wybór odpowiedniej usługi ASR:
   - Wysoka dokładność: OpenAI
   - Bez konfiguracji: Rozpoznawanie przeglądarkowe

3. Optymalizacja rozmowy głosowej:
   - Używaj słuchawek, aby uniknąć przechwycenia dźwięku TTS przez ASR
   - Stosuj w cichym otoczeniu dla lepszej rozpoznawalności
   - Niestandardowe podpowiedzi pomagają dostosować odpowiedzi AI do odtwarzania głosowego

4. Dopasowanie ustawień do potrzeb:
   - Dla komunikacji tekstowej: Włącz tylko TTS
   - Dla wprowadzania głosowego: Włącz tylko ASR
   - Dla pełnej konwersacji głosowej: Włącz funkcję rozmowy głosowej

Mamy nadzieję, że te instrukcje pomogą w pełni wykorzystać funkcje głosowe Cherry Studio i cieszyć się naturalniejszym, wygodniejszym doświadczeniem interakcji z AI!
```