---
icon: message
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Chat-Oberfläche

## Assistenten und Themen

### Assistent

Ein `Assistent` ermöglicht die Personalisierung des gewählten Modells durch Einstellungen wie Prompt-Vorlagen und Parameter-Presets. Diese Anpassungen helfen dem Modell, besser auf Ihre Arbeitsanforderungen einzugehen.

Der `Systemstandard-Assistent` bietet allgemeine Parameter (ohne vordefinierten Prompt). Sie können ihn direkt nutzen oder auf der [Agentenseite](agents.md) nach passenden Vorlagen suchen.

### Themen

`Assistenten` sind übergeordnete Container für `Themen` (Conversations). Ein Assistent kann mehrere Themen enthalten. Alle `Themen` nutzen dieselben Parametereinstellungen und Prompt-Vorlagen des übergeordneten Assistenten.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Tasten im Chat-Bereich

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Neues Thema` Erstellt ein neues Thema im aktuellen Assistenten.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Bilder/Dokumente hochladen` Bilder erfordern Modellunterstützung. Dokumente werden automatisch in Text konvertiert und als Kontext bereitgestellt.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Websuche` Benötigt konfigurierte Sucheinstellungen. Suchergebnisse werden als Kontext an das Modell übergeben. Details: [Internetmodus](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Wissensdatenbank aktivieren` Details: [Wissensdatenbank-Anleitung](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP-Server` Aktiviert die MCP-Serverfunktion. Details: [MCP-Anleitung](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Bilder generieren` Standardmäßig ausgeblendet. Für bildfähige Modelle (z.B. Gemini) muss die Taste manuell aktiviert werden.

{% hint style="info" %}
Aus technischen Gründen muss die Taste manuell aktiviert werden. Sie wird nach Funktionsoptimierung entfernt.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Modell auswählen` Wechselt für zukünftige Interaktionen zum angegebenen Modell (Kontext bleibt erhalten).

![](../../.gitbook/assets/对话界面/快捷短语.png) `Schnellphrasen` Nutzt vordefinierte Phrasen aus den Einstellungen (Variablen unterstützt).

![](../../.gitbook/assets/对话界面/清空消息.png) `Alle Nachrichten löschen` Löscht alle Inhalte im aktuellen Thema.

![](../../.gitbook/assets/对话界面/展开.png) `Erweitern` Vergrößert den Chat-Bereich für lange Texteingaben.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Kontext löschen` Kürzt den für das Modell verfügbaren Kontext (vorherige Dialoge werden "vergessen").

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Geschätzte Token-Anzahl` Anzeige: `Aktueller Kontext`, `Maximaler Kontext` (∞ = unbegrenzt), `Zeichen in Eingabe`, `Geschätzte Token`.

{% hint style="info" %}
Nur zur Orientierung. Die tatsächliche Token-Anzahl variiert je Modell. Bitte Modellanbieter konsultieren.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Übersetzen` Übersetzt den aktuellen Eingabetext ins Englische.

## Chat-Einstellungen

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Modelleinstellungen

Synchron mit den `Modelleinstellungen` im Assistenten-Menü. Details: [Assistent bearbeiten](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Änderungen wirken sich nur auf den aktuellen Assistenten aus. Andere Einstellungen gelten global (z.B. werden Änderungen der Nachrichtenanzeige auf alle Assistenten angewendet).
{% endhint %}

### Nachrichteneinstellungen

#### <mark style="color:blue;">**`Nachrichtentrenner`**</mark>:

Fügt eine Trennlinie zwischen Nachrichtentext und Aktionsbereich hinzu.

{% tabs %}
{% tab title="Ein" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Aus" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Serifenschrift verwenden`**</mark>：

Schaltet zwischen Schriftarten um. Schriftarten lassen sich auch per [CSS anpassen](../../personalization-settings/).

#### <mark style="color:blue;">**`Zeilenumbrüche in Codeblöcken anzeigen`**</mark>：

Zeigt Zeilennummern in Codeausgaben an.

{% tabs %}
{% tab title="Aus" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ein" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Codeblöcke zusammenklappbar`**</mark>：

Klappt lange Codeblöcke automatisch ein.

#### <mark style="color:blue;">**`Zeilenumbrüche in Codeblöcken`**</mark>：

Ermöglicht automatische Zeilenumbrüche bei breiten Codezeilen.

#### <mark style="color:blue;">**`Denkvorgänge automatisch einklappen`**</mark>：

Klappt Denkprozesse bei kompatiblen Modellen nach Abschluss automatisch ein.

#### <mark style="color:blue;">**`Nachrichtenformat`**</mark>：

Umschaltung zwischen Blasenansicht und Listenansicht.

#### <mark style="color:blue;">**`Code-Stil`**</mark>：

Ändert die Darstellung von Codeblöcken.

#### <mark style="color:blue;">**`Mathematik-Engine`**</mark>：

* KaTeX: Schnellere Renderinggeschwindigkeit
* MathJax: Langsamer, aber umfassendere Symbol- und Befehlsunterstützung

#### <mark style="color:blue;">**`Schriftgröße`**</mark>：

Passt die Schriftgröße im Chatbereich an.

### Eingabeeinstellungen

#### <mark style="color:blue;">**`Geschätzte Token anzeigen`**</mark>：

Zeigt geschätzte Token-Verbrauchszahl für Eingaben an (nicht für Kontexttoken, nur zur Orientierung).

#### <mark style="color:blue;">**`Lange Texte als Dateien einfügen`**</mark>：

Konvertiert lange eingefügte Texte automatisch in Datei-Icons (reduziert Eingabestörungen).

#### <mark style="color:blue;">**`Markdown in Nachrichten rendern`**</mark>：

Schaltet Markdown-Rendering nur für empfangene Nachrichten oder auch für gesendete Nachrichten ein.

{% tabs %}
{% tab title="Aus" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ein" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Dreimal Leertaste zum Übersetzen`**</mark>：

Übersetzt nach dreimaligem Drücken der Leertaste den Eingabetext ins Englische.

{% hint style="warning" %}
Achtung: Überschreibt den Originaltext.
{% endhint %}

#### <mark style="color:blue;">**`Zielsprache`**</mark>：

Legt die Zielsprache für die Übersetzungsfunktionen fest.

## Assistenteneinstellungen

Rechtsklick auf den <mark style="background-color:yellow;">Assistentennamen</mark> → Auswahl im Kontextmenü

### Assistent bearbeiten

{% hint style="info" %}
Einstellungen gelten für alle Themen im Assistenten.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Prompteinstellungen

#### <mark style="color:blue;">**`Name`**</mark>：

Benutzerdefinierter Anzeigename.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Anleitungstext zur Modellsteuerung. Siehe Agentenseite für Beispiele.

#### Modelleinstellungen

#### <mark style="color:blue;">**`Standardmodell`**</mark>：

Fixiert ein Standardmodell für diesen Assistenten. Ohne Einstellung greift das [globale Standardmodell](settings/default-models.md#mo-ren-zhu-shou-mo-xing).

{% hint style="info" %}
Assistentenmodell hat Priorität vor dem globalen Standardmodell. Bei nicht gesetztem Assistentenmodell: Assistentenmodell = globales Modell.
{% endhint %}

#### <mark style="color:blue;">**`Modell automatisch zurücksetzen`**</mark>：

Wenn aktiviert, werden neue Themen mit dem Assistenten-Standardmodell gestartet. Andernfalls wird das letzte genutzte Modell beibehalten.

> Beispiel: Assistentenmodell ist gpt-3.5-turbo. In Thema1 wird zu gpt-4o gewechselt.
>
> Aktiviert: Thema2 startet mit gpt-3.5-turbo
>
> Deaktiviert: Thema2 startet mit gpt-4o

#### <mark style="color:blue;">**`Temperature`**</mark>：

Steuert Zufälligkeit der Ausgaben (Standard: 0.7):

* Niedrig (0-0.3): Vorhersehbare Ergebnisse → ideal für Code/Statistik
* Mittel (0.4-0.7): Ausgewogen → ideal für Dialoge
* Hoch (0.8-1.0): Kreativ → ideal für Brainstorming

#### <mark style="color:blue;">**`Top P`**</mark>：

Standardwert 1. Niedrigere Werte → fokussiertere Wortauswahl.

* Klein (0.1-0.3): Konservativ → für technische Texte
* Mittel (0.4-0.6): Ausgewogen → für Dialoge
* Groß (0.7-1.0): Vielfältig → für kreative Aufgaben

{% hint style="info" %}
- Kombination von Temperature und Top P möglich
- Optimale Werte durch Experimente finden
- Parameterbereiche dienen nur der Orientierung
{% endhint %}

#### <mark style="color:blue;">**`Kontextfenster`**</mark>

Maximale Anzahl gespeicherter Nachrichten (höhere Werte erhöhen Token-Verbrauch):

* 5-10: Normale Dialoge
* \>10: Komplexe Aufgaben mit Langzeitkontext
* ! Token-Verbrauch steigt mit Nachrichtenanzahl

#### <mark style="color:blue;">**`MaxToken aktivieren`**</mark>

Maximale Token-Zahl pro Antwort. Beeinflusst Antwortqualität und Länge.

> Beispiel: Bei Konnektivitätstests reicht MaxToken=1.

MaxToken-Obergrenzen variieren je Modell (32k/64k/mehr). Empfehlungen:

{% hint style="success" %}
Empfohlene Werte:
* Dialoge: 500-800
* Kurztexte: 800-2000
* Code: 2000-3600
* Langtexte: ≥4000 (nur bei Modellunterstützung)
{% endhint %}

{% hint style="warning" %}
Bei zu niedrigen Werten: Abbruch, unvollständige Antworten.
{% endhint %}

#### <mark style="color:blue;">**`Streamingausgabe`**</mark>

Daten werden kontinuierlich übertragen (Schreibmaschinen-Effekt). Bei Deaktivierung: Antworten werden vollständig übermittelt.

{% hint style="info" %}
Falls Modell kein Streaming unterstützt: Deaktivieren (z.B. o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Benutzerdefinierte Parameter`**</mark>

Zusätzliche Parameter (z.B. `presence_penalty`) im Request-Body. Dokumentation: [Anleitung](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Benutzerparameter haben Vorrang vor Standardparametern
- Parameter ausschließen mit <kbd>Parametername:undefined</kbd>
- Modellspezifische Parameter in Anbieterdokumentation prüfen
{% endhint %}