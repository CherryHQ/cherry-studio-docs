---
icon: database
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Datenspeicherungsinformationen

Alle in die Cherry Studio-Wissensdatenbank hinzugefügten Daten werden lokal gespeichert. Während des Hinzufügevorgangs wird eine Kopie des Dokuments im Cherry Studio-Datenspeicherverzeichnis angelegt.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Wissensdatenbank-Verarbeitungsdiagramm</p></figcaption></figure>

Vektor-Datenbank: [https://turso.tech/libsql](https://turso.tech/libsql)

Nachdem ein Dokument der Cherry Studio-Wissensdatenbank hinzugefügt wurde, wird die Datei in mehrere Segmente aufgeteilt, die dann dem Einbettungsmodell zur Verarbeitung übergeben werden.

Bei der Verwendung großer Modelle für Frage-Antwort-Systeme werden die zur Frage relevanten Textsegmente identifiziert und gemeinsam mit der Anfrage an das Large Language Model übermittelt.

Bei Anforderungen an die Datenprivatssphäre wird die Verwendung einer lokalen Einbettungsdatenbank und eines lokalen Large Language Models empfohlen.