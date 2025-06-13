---
icon: seal-question
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Häufig gestellte Fragen

## Häufige Fehlercodes

* **4xx (Client-Fehlerstatuscodes)**: In der Regel Anfragesyntaxfehler, Authentifizierungs- oder Autorisierungsfehler, die eine Anfrageausführung verhindern.
* **5xx (Server-Fehlerstatuscodes)**: In der Regel Server-seitige Fehler wie Serverausfälle, Anfrage-Timeouts etc.

| Fehlercode          | Mögliche Ursachen                                                   | Lösung                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4> | Ungültiges Anfrageformat etc.                                               | <p>Überprüfen Sie die Fehlermeldung im Dialog oder im <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">Konsolenfehler</a> und handeln Sie entsprechend.</p><p><mark style="color:purple;">【Häufiger Fall 1】</mark>: Bei Gemini-Modellen ggf. Kartenverifizierung erforderlich;<br><mark style="color:purple;">【Häufiger Fall 2】</mark>: Datenvolumen überschritten (häufig bei Bildmodellen);<br><mark style="color:purple;">【Häufiger Fall 3】</mark>: Nicht unterstützte oder fehlerhafte Parameter – Test mit neuem Assistant;<br><mark style="color:purple;">【Häufiger Fall 4】</mark>: Kontextlimit überschritten – Kontext löschen/neu starten/reduzieren.</p> |
| <h4>401</h4> | Authentifizierungsfehler: Modell nicht unterstützt oder Konto gesperrt                                | Anbieterkontostatus prüfen/kontaktieren                                                                                                                                                                                                                                                                                                                                                                                               |
| <h4>403</h4> | Keine Berechtigung für Anfrageoperation                                                | Gemäß Fehlermeldung oder [Konsolenfehler](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa) handeln                                                                                                                                                                                                                                                                                                                                             |
| <h4>404</h4> | Angeforderte Ressource nicht gefunden                                                | Anfragepfad prüfen etc.                                                                                                                                                                                                                                                                                                                                                                                                              |
| <h4>422</h4> | Syntax korrekt, aber semantischer Fehler                                            | JSON-Semantikfehler (z.B. Nullwert, falscher Datentyp)                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>429</h4> | Anfragerate-Limit erreicht                                                | TPM/RPM-Limit überschritten – Pause einlegen                                                                                                                                                                                                                                                                                                                                                                                          |
| <h4>500</h4> | Interner Serverfehler                                             | Bei wiederholtem Auftreten Anbieter kontaktieren                                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>501</h4> | Angeforderte Funktion nicht implementiert                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>502</h4> | Ungültige Antwort von Upstream-Server (Proxy/Gateway)                 |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>503</h4> | Server temporär überlastet/in Wartung (Retry-After Header prüfen) |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>504</h4> | Timeout bei Upstream-Anfrage (Proxy/Gateway)                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |

***

## Konsolenfehler-Anzeigemethode

* Cherry Studio Client-Fenster aktivieren und Shortcut drücken: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Cherry Studio Client-Fenster muss aktiv sein
- Konsole muss vor Anfrageausführung (z.B. Test/Dialog) geöffnet werden
{% endhint %}

* In der Konsole <mark style="color:blue;">`Network`</mark> auswählen → Letzten rot markierten <mark style="color:red;">`×`</mark> -Eintrag (<mark style="color:red;">`completions`</mark> bei Dialogen/Übersetzungen, <mark style="color:red;">`generations`</mark> bei Bildfehlern) anklicken → <mark style="color:blue;">`Response`</mark> für vollständige Antwort prüfen (Bereich ④).

> Bei unklarer Fehlerursache: Screenshot im [offiziellen Chat](https://t.me/CherryStudioAI) teilen.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Diese Methode funktioniert auch bei Modelltests, Wissensdatenbanken, Bildgenerierung etc. (Konsole immer vor Anfrage öffnen).

{% hint style="info" %}
Unterschiedliche Einträge in Spalte „Name“ (②):  
Dialog/Übersetzung/Modellcheck: <mark style="color:red;">`completions`</mark>  
Bilderstellung: <mark style="color:red;">`generations`</mark>  
Wissensdatenbank: <mark style="color:red;">`embeddings`</mark>  
{% endhint %}

***

## Formeln nicht gerendert/Fehler im Rendering

* Bei nicht gerendertem Formelcode: Trennzeichen prüfen

> **Trennzeichen-Regeln**  
> *Inline-Formeln*  
> - Einzelnes Dollarzeichen: `$formel$`  
> - Oder `\(formel\)`  
>   
> *Block-Formeln*  
> - Doppelte Dollarzeichen: `$$formel$$`  
> - Oder `\[formel\]`  
> - Beispiel: `$$\sum_{i=1}^n x_i$$`  
>   $$\sum_{i=1}^n x_i$$

* Rendering-Fehler/Zeichensalat bei chinesischem Inhalt: Engine auf KateX umstellen

***

## Wissensdatenbank-Erstellung fehlgeschlagen/Embedding-Dimension nicht abrufbar

1. Modellstatus nicht verfügbar  
> Anbieterunterstützung und Modellstatus prüfen

2. Falscher Modelltyp (kein Embedding-Modell)

***

## Modell erkennt keine Bilder/Bilderauswahl nicht möglich

1. Modellunterstützung prüfen: Visuelle Modelle haben Augensymbol neben Modellnamen  
2. Bei falscher Zuordnung: Modell im Anbietermenü finden → Einstellungen → "Bild" aktivieren  
> Hinweis: Bildoption bei nicht visuellen Modellen wirkungslos