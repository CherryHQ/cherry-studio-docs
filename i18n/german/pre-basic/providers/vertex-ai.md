---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Vertex AI

## Tutorial-Überblick

### 1. API Key beziehen

* Vor dem Beziehen des Gemini API Keys benötigst du ein Google Cloud Projekt (falls bereits vorhanden, kann dieser Schritt übersprungen werden)
* Gehe zu [Google Cloud](https://console.cloud.google.com/projectcreate), erstelle ein Projekt, gib den Projektnamen ein und klicke auf "Projekt erstellen"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Öffne die [Vertex AI Konsole](https://console.cloud.google.com/vertex-ai)
* Aktiviere die [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) in deinem erstellten Projekt

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API-Zugriffsberechtigungen einrichten

* Öffne die [Servicekonten](https://console.cloud.google.com/iam-admin/serviceaccounts) Berechtigungsoberfläche und erstelle ein Servicekonto

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Finde das neu erstellte Servicekonto auf der Verwaltungsseite, klicke auf `Schlüssel` und erstelle einen neuen Schlüssel im JSON-Format

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Nach erfolgreicher Erstellung wird die Schlüsseldatei automatisch als JSON-Datei auf deinem Computer gespeichert. **Bewahre diese sicher auf**

## 3. Vertex AI in Cherry Studio konfigurieren

* Wähle den Anbieter Vertex AI aus
* Trage die entsprechenden Felder aus der JSON-Datei ein

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Klicke auf "Modell hinzufügen" [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) und du kannst loslegen!