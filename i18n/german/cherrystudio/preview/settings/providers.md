---
icon: cloud-check
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Anbietereinstellungen

Diese Seite dient nur zur Einführung der Oberflächenfunktionen. Ein Konfigurationstutorial finden Sie im Grundlagentutorial unter [Anbieterkonfiguration](../../../pre-basic/providers/).

{% hint style="info" %}
* Bei Verwendung integrierter Anbieter müssen Sie lediglich den entsprechenden Schlüssel eingeben.
* Die Bezeichnung für Schlüssel kann zwischen Anbietern variieren: Schlüssel, Key, API Key, Token usw. bezeichnen alle dasselbe Konzept.
{% endhint %}

### API-Schlüssel

In Cherry Studio unterstützt ein einzelner Anbieter mehrere Keys für Round-Robin-Verwendung. Die Abfolge erfolgt zyklisch von vorn nach hinten in der Liste.

* Fügen Sie mehrere Keys durch englische Kommas getrennt hinzu. Beispiel:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Es müssen **englische** Kommas verwendet werden.
{% endhint %}

### API-Adresse

Bei integrierten Anbietern ist normalerweise keine API-Adressangabe erforderlich. Änderungen müssen genau gemäß der offiziellen Dokumentation vorgenommen werden.

> Falls ein Anbieter eine Adresse im Format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> angibt, geben Sie nur den Basis-Teil ein (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
> 
> Cherry Studio fügt automatisch den Restpfad hinzu (<mark style="background-color:green;">/v1/chat/completions</mark>). Abweichungen können zu Funktionsstörungen führen.

{% hint style="info" %}
Hinweis: Die meisten Sprachmodell-Routen sind standardisiert. Bei abweichenden Pfaden (v2, v3/chat/completions):
* Endet die Adresse mit `/`, wird nur "<mark style="background-color:green;">chat/completions</mark>" angehängt
* Endet die Adresse mit `#`, erfolgt keine Anhängung

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Modelle hinzufügen

Klicken Sie typischerweise auf die `Verwalten`-Schaltfläche unten links, um alle unterstützten Modelle des Anbieters abzurufen. Fügen Sie gewünschte Modelle über das `+`-Symbol zur Liste hinzu.

{% hint style="info" %}
Modelle werden nicht automatisch hinzugefügt. Erst nach Klick auf `+` erscheinen sie in der Modellauswahlliste.
{% endhint %}

### Konnektivitätsprüfung

Testen Sie die Konfiguration über die Prüfschaltfläche neben dem API-Schlüsselfeld.

{% hint style="info" %}
Für Tests wird standardmäßig das letzte Dialogmodell in der Liste verwendet. Bei Fehlern prüfen Sie die Modellliste auf Fehler/inkompatible Modelle.
{% endhint %}

{% hint style="danger" %}
Nach erfolgreicher Konfiguration müssen Sie den Schalter oben rechts aktivieren. Andernfalls bleibt der Anbieter deaktiviert und Modelle sind nicht verfügbar.
{% endhint %}