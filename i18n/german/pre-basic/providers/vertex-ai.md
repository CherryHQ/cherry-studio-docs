---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Vertex AI

## Tutorial Übersicht

### 1. API-Schlüssel abrufen

*   Bevor Sie den Gemini-API-Schlüssel erhalten, benötigen Sie ein Google Cloud-Projekt (falls Sie bereits eines haben, kann dieser Schritt übersprungen werden)
*   Gehen Sie zu [Google Cloud](https://console.cloud.google.com/projectcreate) um ein Projekt zu erstellen. Füllen Sie den Projektnamen aus und klicken Sie auf "Projekt erstellen"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   Wechseln Sie zur [Vertex AI-Konsole](https://console.cloud.google.com/vertex-ai)
*   Aktivieren Sie die [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) in Ihrem erstellten Projekt

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API-Zugriffsberechtigungen einrichten

*   Öffnen Sie die [Servicekonto](https://console.cloud.google.com/iam-admin/serviceaccounts)-Berechtigungsseite und erstellen Sie ein Servicekonto

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   Suchen Sie auf der Servicekonto-Verwaltungsseite das neu erstellte Servicekonto, klicken Sie auf `Schlüssel` und erstellen Sie einen neuen JSON-formatierte Schlüssel

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   Nach erfolgreicher Erstellung wird die Schlüsseldatei automatisch als JSON-Datei auf Ihrem Computer gespeichert - **bewahren Sie diese sicher auf**

## 3. Vertex AI in Cherry Studio konfigurieren

*   Wählen Sie den Vertex AI-Anbieter
*   Füllen Sie die entsprechenden Felder der JSON-Datei ein

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Klicken Sie auf [Modell hinzufügen](https://console.cloud.google.com/vertex-ai/model-garden), und schon können Sie loslegen!\