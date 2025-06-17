---
icon: book-open-cover
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Tutorial bazy wiedzy

W wersji 0.9.1 CherryStudio wprowadził długo oczekiwane funkcje bazy wiedzy.  

Poniżej przedstawiamy szczegółowe instrukcje korzystania z CherryStudio krok po kroku.

## Dodawanie modelu osadzania

1.  Wyszukaj model w usłudze zarządzania modelami (kliknij "Embedding Model", aby szybko filtrować);
2.  Znajdź potrzebny model i dodaj go do moich modeli.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Tworzenie bazy wiedzy

1.  Wejście do bazy wiedzy: Kliknij ikonę bazy wiedzy na lewym pasku narzędzi CherryStudio, aby przejść do strony zarządzania;
2.  Dodaj bazę wiedzy: Kliknij "Dodaj", aby rozpocząć tworzenie bazy wiedzy;
3.  Nazwij: Wprowadź nazwę bazy wiedzy i dodaj model osadzania (np. bge-m3), aby zakończyć tworzenie.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Dodawanie plików i wektoryzacja

1.  Dodaj pliki: Kliknij przycisk dodawania plików, aby otworzyć selektor plików;
2.  Wybierz pliki: Wybierz obsługiwane formaty (pdf, docx, pptx, xlsx, txt, md, mdx) i otwórz;
3.  Wektoryzacja: System automatycznie przetworzy pliki. Zielone ✓ oznacza zakończenie procesu wektoryzacji.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>



## Dodawanie danych z różnych źródeł

CherryStudio obsługuje wiele metod dodawania danych:

1.  Katalogi: Możesz dodać cały folder - obsługiwane pliki zostaną automatycznie zwektoryzowane;
2.  Linki URL: Obsługuje adresy URL, np. [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3.  Mapy witryn: Obsługuje mapy witryn w formacie XML, np. [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4.  Notatki tekstowe: Obsługuje wprowadzanie niestandardowych treści w postaci zwykłego tekstu.

{% hint style="info" %}
Wskazówki:

1.  Ilustracje w dokumentach importowanych do bazy wiedzy nie są automatycznie konwertowane na wektory - wymagają ręcznej konwersji na tekst;
2.  Użycie adresów URL jako źródła nie zawsze się powiedzie. Niektóre strony mają surowe mechanizmy anty-scrapingowe (lub wymagają logowania). Po utworzeniu zaleca się przetestowanie wyszukiwania;
3.  Większość stron udostępnia mapy witryn (np. [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml) CherryStudio). Można je często znaleźć pod adresem `domena.com/sitemap.xml`;
4.  Jeśli strona nie udostępnia mapy, można utworzyć własny plik XML. Wymagany jest publicznie dostępny link bezpośredni - linki lokalne nie są obsługiwane.

> 1)  Możesz poprosić AI o wygenerowanie mapy witryn lub stworzenie narzędzia do generowania HTML mapy;
> 2)  Linki bezpośrednie można generować przez OSS lub dyski w chmurze. Bezpłatne narzędzie do przesyłania plików dostępne jest na [ocoolAI](https://one.ocoolai.com/login) po zalogowaniu.
{% endhint %}

## Wyszukiwanie w bazie wiedzy

Po zakończeniu procesu wektoryzacji możesz przeszukiwać materiały:

1.  Kliknij przycisk wyszukiwania u dołu strony;
2.  Wprowadź zapytanie;
3.  System wyświetli wyniki wyszukiwania;
4.  Każdy wynik zawierać będzie wskazany stopień dopasowania.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Generowanie odpowiedzi z bazy wiedzy w konwersacji

1.  Utwórz nowy wątek. Kliknij "Baza wiedzy" na pasku narzędzi rozmowy i wybierz odpowiednią bazę;
2.  Wprowadź pytanie - model wygeneruje odpowiedź na podstawie wyników wyszukiwania;
3.  Źródła danych będą dołączone pod odpowiedzią dla szybkiego dostępu.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>