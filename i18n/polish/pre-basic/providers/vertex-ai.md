---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Vertex AI

## Przegląd samouczka

### 1. Uzyskanie klucza API

* Przed uzyskaniem klucza API Gemini potrzebujesz projektu Google Cloud (jeśli już go masz, pomiń ten krok)
* Przejdź do [Google Cloud](https://console.cloud.google.com/projectcreate), utwórz projekt, wpisz nazwę projektu i kliknij "Utwórz projekt"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Przejdź do [konsoli Vertex AI](https://console.cloud.google.com/vertex-ai)
* W utworzonym projekcie aktywuj [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Konfiguracja uprawnień dostępu API

* Otwórz panel [konta usług](https://console.cloud.google.com/iam-admin/serviceaccounts) i utwórz konto usługi

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Na stronie zarządzania kontami usług znajdź utworzone konto, kliknij `Klucze` i utwórz nowy klucz w formacie JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Po utworzeniu plik klucza zostanie automatycznie zapisany na komputerze w formacie JSON - **zachowaj go bezpiecznie**

## 3. Konfiguracja Vertex AI w Cherry Studio

* Wybierz dostawcę usług Vertex AI
* Wypełnij odpowiednie pola danymi z pliku JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Kliknij "Dodaj [model](https://console.cloud.google.com/vertex-ai/model-garden)" i można rozpocząć korzystanie!\