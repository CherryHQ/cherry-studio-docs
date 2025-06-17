---
icon: book-bookmark
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Wissen

## Was sind Tokens?

Tokens sind die grundlegende Verarbeitungseinheit für Text in KI-Modellen. Man kann sie sich als kleinste "Denk"-Einheiten des Modells vorstellen. Sie entsprechen nicht genau Buchstaben oder Wörtern, sondern stellen eine spezielle, modellspezifische Textaufteilung dar.

#### 1. Chinesische Segmentierung
* Ein chinesisches Zeichen entspricht normalerweise 1-2 Tokens
* Beispiel: `"你好"` ≈ 2-4 Tokens

#### 2. Englische Segmentierung
* Häufige Wörter sind meist 1 Token
* Lange oder ungewöhnliche Wörter werden in mehrere Tokens zerlegt
* Beispiel:
  * `"hello"` = 1 Token
  * `"indescribable"` = 4 Tokens

#### 3. Sonderzeichen
* Leerzeichen und Satzzeichen verbrauchen Tokens
* Zeilenumbrüche entsprechen normalerweise 1 Token

{% hint style="info" %}
Jeder Anbieter verwendet unterschiedliche Tokenizer, selbst verschiedene Modelle desselben Anbieters können abweichen. Dieses Wissen dient nur zum Verständnis des Token-Konzepts.
{% endhint %}

***

## Was ist ein Tokenizer?

Ein Tokenizer ist das Werkzeug, mit dem KI-Modelle Text in Tokens zerlegen. Es bestimmt, wie Eingabetext in die kleinsten verständlichen Einheiten aufgeteilt wird.

### Warum verwenden verschiedene Modelle unterschiedliche Tokenizer?

#### 1. Unterschiedliche Trainingsdaten
* Unterschiedliche Korpusse führen zu abweichenden Optimierungen
* Unterschiedlicher Grad an Mehrsprachenunterstützung
* Fachspezifische Optimierungen (Medizin, Jura etc.)

#### 2. Unterschiedliche Segmentierungsalgorithmen
* BPE (Byte Pair Encoding) - OpenAI GPT-Reihe
* WordPiece - Google BERT
* SentencePiece - Ideal für multilinguale Szenarien

#### 3. Unterschiedliche Optimierungsziele
* Fokus auf Kompressionseffizienz
* Fokus auf Semantikerhalt
* Fokus auf Verarbeitungsgeschwindigkeit

### Praktische Auswirkungen
Derselbe Text kann in verschiedenen Modellen unterschiedlich viele Tokens verbrauchen:
```
Eingabe: "Hello, world!"
GPT-3: 4 Tokens
BERT: 3 Tokens
Claude: 3 Tokens
```

***

## Was sind Embedding-Modelle?

**Grundkonzept:** Embedding-Modelle transformieren hochdimensionale diskrete Daten (Text, Bilder) in niedrigdimensionale kontinuierliche Vektoren. Diese Transformation ermöglicht Maschinen ein besseres Verständnis komplexer Daten – wie die Reduktion eines Puzzles auf einen Koordinatenpunkt, der dessen Kernmerkmale bewahrt. Im KI-Ökosystem fungieren sie als "Dolmetscher", die menschenlesbare Informationen in maschinenverwertbare numerische Formen übersetzen.

**Funktionsweise:** In der Sprachverarbeitung ordnen Embedding-Modelle Wörter bestimmten Positionen im Vektorraum zu, wobei semantisch ähnliche Wörter automatisch gruppiert werden. Beispielsweise:
* "König" und "Königin" liegen nahe beieinander
* "Katze" und "Hund" als Haustierbegriffe bilden eine Cluster
* Unverbundene Begriffe wie "Auto" und "Brot" bleiben weit entfernt

**Hauptanwendungen:**
* Textanalyse: Dokumentenklassifizierung, Sentimentanalyse
* Empfehlungssysteme: Personalisierte Inhaltsvorschläge
* Bildverarbeitung: Ähnlichkeitssuche bei Bildern
* Suchmaschinen: Semantische Suchoptimierung

**Kernvorteile:**
1. Dimensionsreduktion: Komplexe Daten werden handhabbar
2. Semantischer Erhalt: Wesentliche Bedeutungsnuancen bleiben erhalten
3. Recheneffizienz: Beschleunigt Training und Inferenz von ML-Modellen

**Technischer Wert:** Embedding-Modelle sind fundamentale Bausteine moderner KI-Systeme. Sie liefern hochwertige Datendarstellungen für Machine-Learning-Aufgaben und treiben Schlüsseltechnologien in NLP und Computer Vision voran.

***

## Funktionsweise von Embedding-Modellen bei der Wissenssuche

**Arbeitsablauf:**

1. **Vorverarbeitung der Wissensbasis**
   * Dokumente werden in sinnvolle Textabschnitte (chunks) zerlegt
   * Jeder Abschnitt wird per Embedding-Modell in Vektoren transformiert
   * Vektoren und Originaltexte werden in der Vektordatenbank gespeichert

2. **Anfrageverarbeitung**
   * Nutzerfragen werden in Vektoren umgewandelt
   * Ähnliche Inhalte werden in der Vektordatenbank gesucht
   * Gefundene Inhalte dienen als Kontext für das LLM

***

## Was ist MCP (Model Context Protocol)?

MCP ist ein Open-Source-Protokoll zur standardisierten Bereitstellung von Kontextinformationen für Large Language Models (LLMs).

* **Analogie:** Man kann sich MCP als "USB-Stick" der KI-Welt vorstellen. So wie USB-Sticks beliebige Dateien speichern und an Computern nutzbar machen, können am MCP-Server "Plugins" angeschlossen werden, die Kontext bereitstellen. LLMs können bei Bedarf diese Plugins anfordern und so ihre Fähigkeiten erweitern.
* **Vergleich mit Function Tools:** Herkömmliche Function Tools stellen zwar externe Funktionen bereit, doch MCP bietet eine abstraktere Lösung. Während Function Tools aufgabenspezifisch sind, etabliert MCP einen universellen, modularen Mechanismus zur Kontextbeschaffung.

### Kernvorteile von MCP

1. **Standardisierung:** Einheitliche Schnittstellen und Datenformate ermöglichen nahtlose Zusammenarbeit verschiedener LLMs und Kontextanbieter.
2. **Modularität:** Kontextinformationen werden als unabhängige Plugins organisiert, was Verwaltung und Wiederverwendung vereinfacht.
3. **Flexibilität:** LLMs wählen dynamisch benötigte Kontext-Plugins für intelligentere, persönlichere Interaktionen.
4. **Erweiterbarkeit:** Das Design unterstützt künftige Erweiterungen mit neuen Plugintypen und schafft unbegrenzte Erweiterungsmöglichkeiten.