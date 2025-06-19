---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Vertex AI

## Tutorial-Übersicht

### 1. API-Schlüssel abrufen

* Bevor Sie den Gemini-API-Schlüssel erhalten, benötigen Sie ein Google Cloud-Projekt (falls bereits vorhanden, kann dieser Schritt übersprungen werden)
* Gehen Sie zu [Google Cloud](https://console.cloud.google.com/projectcreate) und erstellen Sie ein Projekt, indem Sie den Projektnamen eingeben und auf "Projekt erstellen" klicken

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Rufen Sie die [Vertex AI-Konsole](https://console.cloud.google.com/vertex-ai) auf
* Aktivieren Sie die [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) im erstellten Projekt

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API-Zugriffsberechtigungen einrichten

* Öffnen Sie die [Servicekonto-Berechtigungsseite](https://console.cloud.google.com/iam-admin/serviceaccounts) und erstellen Sie ein Servicekonto

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Finden Sie auf der Servicekonto-Verwaltungsseite das soeben erstellte Servicekonto, klicken Sie auf `Schlüssel` und erstellen Sie einen neuen Schlüssel im JSON-Format

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Nach erfolgreicher Erstellung wird die Schlüsseldatei automatisch im JSON-Format auf Ihrem Computer gespeichert. Bitte **bewahren Sie diese sicher auf**

## 3. Vertex AI in Cherry Studio konfigurieren

* Wählen Sie den Vertex AI-Anbieter
* Tragen Sie die entsprechenden Felder der JSON-Datei ein

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Klicken Sie auf "Modell hinzufügen" ([Modelle](https://console.cloud.google.com/vertex-ai/model-garden)), um mit der Nutzung zu beginnen!