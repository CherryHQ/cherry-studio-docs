---
icon: database
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Instrukcje przechowywania danych

Wszystkie dane dodane do bazy wiedzy Cherry Studio są przechowywane lokalnie. Podczas dodawania dokument jest kopiowany do katalogu przechowywania danych Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Schemat procesu bazy wiedzy</p></figcaption></figure>

Baza danych wektorowa: [https://turso.tech/libsql](https://turso.tech/libsql)

Po dodaniu dokumentu do bazy wiedzy Cherry Studio, plik jest dzielony na kilka fragmentów, które następnie przetwarza model osadzania.

Podczas korzystania z dużego modelu do pytań i odpowiedzi, wyszukiwane są fragmenty tekstu powiązane z pytaniem i przekazywane do przetwarzania przez duży model językowy.

Jeśli wymagana jest prywatność danych, zaleca się korzystanie z lokalnej osadzonej bazy danych i lokalnego dużego modelu językowego.