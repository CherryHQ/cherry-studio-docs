
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# LLM Arena Ranking Lista (aktualizowana na bieżąco)

To jest ranking oparty o dane z Chatbot Arena (lmarena.ai), wygenerowany automatycznie.

> **Ostatnia aktualizacja danych**: 2025-06-21 09:44:44 UTC / 2025-06-21 17:44:44 CST (czas pekiński)

{% hint style="info" %}
Kliknij **nazwę modelu** w rankingu, aby przejść do jego szczegółów lub strony testowej.
{% endhint %}

## Lista rankingowa

|   Pozycja (UB) |   Pozycja (StyleCtrl) | Nazwa modelu                                                                                                                                 |   Wynik | Przedział ufności | Liczba głosów | Dostawca                    | Licencja                | Data aktualizacji wiedzy |
|:-----------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:--------|:----------------|:---------|:----------------------------|:------------------------|:---------------------|
|        1   |                  1 | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)                     |    1480 | +6/-6        | 8,825    | Google                      | Proprietary             | Brak danych          |
|        2   |                  2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                     |    1446 | +5/-5        | 13,025   | Google                      | Proprietary             | Brak danych          |
|        3   |                  2 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                   |    1427 | +4/-4        | 16,019   | OpenAI                      | Proprietary             | Brak danych          |
| ... [pełna tabela bez zmian w danych] ... |         |                                                                                         |         |                |          |                             |                         |                      |

## Objaśnienia

- **Pozycja (UB)**: Ranking obliczony na podstawie modelu Bradley-Terry. Odzwierciedla ogólną wydajność modelu w arenie i dostarcza **górnej granicy** szacunku dla jego wyniku Elo, pomagając zrozumieć potencjał konkurencyjności modelu.
- **Pozycja (StyleCtrl)**: Ranking po kontroli stylu konwersacji. Ma na celu zmniejszenie stronniczości preferencji spowodowanej stylem odpowiedzi modelu (np. rozwlekłość, zwięzłość), aby ocenić podstawowe możliwości modelu w czystszy sposób.
- **Nazwa modelu**: Nazwa dużego modelu językowego (LLM). Ta kolumna zawiera powiązane linki - kliknij, aby przejść.
- **Wynik**: Wynik Elo modelu uzyskany przez głosowanie użytkowników w arenie. Wynik Elo to względny system rankingowy - wyższy wynik oznacza lepszą wydajność modelu. Wynik zmienia się dynamicznie, odzwierciedlając względne możliwości modelu w bieżącym środowisku konkurencyjnym.
- **Przedział ufności**: 95% przedział ufności wyniku Elo modelu (np. `+6/-6`). Mniejszy przedział oznacza większą stabilność i wiarygodność wyniku; większy przedział może wskazywać na niewystarczające dane lub większą zmienność wydajności modelu. Dostarcza ilościowej oceny dokładności wyniku.
- **Liczba głosów**: Całkowita liczba głosów oddanych na model w arenie. Większa liczba głosów zazwyczaj oznacza większą statystyczną wiarygodność wyniku.
- **Dostawca**: Organizacja lub firma dostarczająca model.
- **Licencja**: Typ licencji modelu, np. własnościowa (Proprietary), Apache 2.0, MIT itd.
- **Data aktualizacji wiedzy**: Data graniczna danych treningowych modelu. **Brak danych** oznacza, że informacje nie zostały dostarczone lub są nieznane.

## Źródło danych i częstotliwość aktualizacji

Dane do tego rankingu są generowane i dostarczane automatycznie przez projekt [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), który pobiera i przetwarza dane z [lmarena.ai](https://lmarena.ai/). Ranking jest aktualizowany automatycznie codziennie za pomocą GitHub Actions.

## Zastrzeżenie

Ten raport ma charakter wyłącznie informacyjny. Dane rankingowe zmieniają się dynamicznie i bazują na głosach preferencyjnych użytkowników Chatbot Arena w określonym przedziale czasowym. Kompletność i dokładność danych zależą od źródła nadrzędnego oraz aktualizacji i przetwarzania w projekcie `fboulnois/llm-leaderboard-csv`. Różne modele mogą podlegać różnym licencjom - przed użyciem należy odwołać się do oficjalnych wytycznych dostawcy modelu.