---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Vertex AI

## Przegląd samouczka

### 1. Uzyskiwanie klucza API

* Przed uzyskaniem klucza API Gemini musisz mieć projekt Google Cloud (jeśli już go posiadasz, ten krok możesz pominąć)
* Przejdź do [Google Cloud](https://console.cloud.google.com/projectcreate) aby utworzyć projekt, wpisz nazwę projektu i kliknij "Utwórz projekt"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Przejdź do [Konsoli Vertex AI](https://console.cloud.google.com/vertex-ai)
* W utworzonym projekcie aktywuj [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Konfiguracja uprawnień dostępu do API

* Otwórz panel [konta usługowego](https://console.cloud.google.com/iam-admin/serviceaccounts) i utwórz nowe konto usługowe

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Na stronie zarządzania kontami usługowymi znajdź utworzone konto, kliknij `Klucze` i utwórz nowy klucz w formacie JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Po pomyślnym utworzeniu, plik klucza zostanie automatycznie zapisany na twoim komputerze w formacie JSON - **zachowaj go bezpiecznie**

## 3. Konfiguracja Vertex AI w Cherry Studio

* Wybierz dostawcę Vertex AI
* Wypełnij odpowiednie pola danymi z pliku JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Kliknij "Dodaj [model](https://console.cloud.google.com/vertex-ai/model-garden)" i możesz zacząć korzystać!