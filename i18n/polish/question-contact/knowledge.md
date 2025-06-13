---
icon: book-bookmark
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Podstawy wiedzy

## Co to są tokens?

Toksyny to podstawowe jednostki przetwarzania tekstu w modelach AI. Można je rozumieć jako najmniejsze jednostki "myślenia" modelu. Nie są one całkowicie równoważne znakom czy słowom w naszym rozumieniu, lecz stanowią specjalny sposób segmentacji tekstu stosowany przez model.

#### 1. Segmentacja języka chińskiego
* Pojedynczy znak chiński zazwyczaj kodowany jest jako 1-2 tokens
* Przykład: `"你好"` ≈ 2-4 tokens

#### 2. Segmentacja języka angielskiego
* Typowe słowa to zwykle 1 token
* Dłuższe lub rzadkie słowa dzielone są na kilka tokenów
* Przykład:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Znaki specjalne
* Spacje, znaki interpunkcyjne również zajmują tokens
* Znak nowej linii to zazwyczaj 1 token

{% hint style="info" %}
Każdy dostawca usług ma inny Tokenizer, a nawet różne modele tego samego dostawcy mogą mieć różne Tokenizery. Ta wiedza służy wyłącznie do wyjaśnienia koncepcji tokenów.
{% endhint %}

***

## Co to jest Tokenizer?

Tokenizer to narzędzie, które konwertuje tekst na tokens dla modeli AI. Określa, jak tekst wejściowy jest dzielony na najmniejsze jednostki zrozumiałe dla modelu.

### Dlaczego modele mają różne Tokenizery?

#### 1. Różne dane treningowe
* Różne korpusy językowe prowadzą do różnych optymalizacji
* Różny poziom wsparcia wielojęzyczności
* Specjalizowane optymalizacje dla określonych dziedzin (medycyna, prawo)

#### 2. Różne algorytmy segmentacji
* BPE (Byte Pair Encoding) - stosowany w serii OpenAI GPT
* WordPiece - stosowany w Google BERT
* SentencePiece - odpowiedni dla scenariuszy wielojęzycznych

#### 3. Różne cele optymalizacji
* Skupienie na wydajności kompresji
* Koncentracja na zachowaniu znaczenia semantycznego
* Priorytetyzacja szybkości przetwarzania

### Praktyczny efekt
Ten sam tekst może mieć różną liczbę tokenów w różnych modelach:

```
Wejście: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## Co to jest model osadzania (Embedding Model)?

**Podstawowa koncepcja:** Model osadzania to technika przekształcania wysokowymiarowych danych dyskretnych (tekst, obrazy) w ciągłe wektory o niższym wymiarze, co umożliwia maszynom lepsze rozumienie i przetwarzanie złożonych danych. Wyobraź sobie to jako uproszczenie skomplikowanej układanki do prostego punktu współrzędnych, który zachowuje kluczowe cechy oryginału. W ekosystemie dużych modeli działa jako "tłumacz", przekształcając informacje zrozumiałe dla ludzi w postać numeryczną przetwarzalną przez AI.

**Zasada działania:** W przetwarzaniu języka naturalnego model osadzania może mapować słowa na określone pozycje w przestrzeni wektorowej. W tej przestrzeni słowa o podobnym znaczeniu automatycznie grupują się razem. Na przykład:
* Wektory "król" i "królowa" będą blisko siebie
* Słowa takie jak "kot" i "pies" również będą blisko
* Natomiast "samochód" i "chleb" pozostaną w znacznej odległości

**Główne zastosowania:**
* Analiza tekstu: klasyfikacja dokumentów, analiza sentymentu
* Systemy rekomendacyjne: spersonalizowane rekomendacje treści
* Przetwarzanie obrazów: wyszukiwanie podobnych obrazów
* Wyszukiwarki internetowe: optymalizacja wyszukiwania semantycznego

**Kluczowe zalety:**
1. Redukcja wymiarowości: upraszcza złożone dane do formy wektorowej
2. Zachowanie znaczenia: zachowuje kluczowe informacje semantyczne z danych źródłowych
3. Efektywność obliczeniowa: znacząco poprawia wydajność uczenia i wnioskowania modeli

**Wartość technologiczna:** Modele osadzania są podstawowym komponentem współczesnych systemów AI, zapewniając wysokiej jakości reprezentację danych dla zadań uczenia maszynowego i stanowią kluczową technologię napędzającą rozwój takich dziedzin jak NLP czy przetwarzanie obrazów.

***

## Jak działają modele Embedding w wyszukiwaniu wiedzy

**Podstawowy przepływ pracy:**

1. **Faza wstępnego przetwarzania bazy wiedzy**
* Podział dokumentów na odpowiedniej wielkości fragmenty (chunk)
* Konwersja każdego fragmentu na wektor przy użyciu modelu embedding
* Przechowywanie wektorów i oryginalnego tekstu w bazie danych wektorowej

2. **Faza przetwarzania zapytań**
* Konwersja pytania użytkownika na wektor
* Wyszukiwanie podobnych treści w bazie wektorowej
* Dostarczenie odnalezionych powiązanych treści jako kontekstu dla LLM

***

## **Co to jest MCP (Model Context Protocol)?**

MCP to otwarty protokół mający na celu standaryzację sposobu dostarczania informacji kontekstowych do dużych modeli językowych (LLM).

* **Analogia:** MCP można porównać do "pendrive'a" w dziedzinie AI. Tak jak pendrive przechowuje różne pliki i umożliwia ich natychmiastowe użycie po podłączeniu, tak serwer MCP pozwala "podłączać" różne "wtyczki" dostarczające kontekst. LLM może żądać tych wtyczek od serwera MCP, uzyskując bogatsze informacje kontekstowe i zwiększając swoje możliwości.
* **Porównanie z narzędziami funkcyjnymi (Function Tool):** Tradycyjne narzędzia funkcyjne dostarczają zewnętrzne funkcje, ale MCP stanowi wyższy poziom abstrakcji. Narzędzia funkcyjne skupiają się na konkretnych zadaniach, podczas gdy MCP zapewnia bardziej uniwersalny, modułowy mechanizm pozyskiwania kontekstu.

### **Kluczowe zalety MCP**

1. **Standaryzacja:** Udostępnia ujednolicony interfejs i format danych, umożliwiając płynną współpracę różnych LLM i dostawców kontekstu.
2. **Modularność:** Pozwala deweloperom rozbijać informacje kontekstowe na niezależne moduły (wtyczki), ułatwiając zarządzanie i ponowne wykorzystanie.
3. **Elastyczność:** LLM może dynamicznie wybierać potrzebne wtyczki kontekstowe, umożliwiając inteligentniejsze i spersonalizowane interakcje.
4. **Rozszerzalność:** Projekt MCP pozwala na dodawanie nowych typów wtyczek kontekstowych, oferując nieograniczone możliwości rozbudowy możliwości LLM.

***