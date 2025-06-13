---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Sprachfunktionen

```
Benutzeranleitung für die Sprachfunktionen von Cherry Studio

## I. Übersicht der Sprachfunktionen

Cherry Studio bietet drei Hauptsprachfunktionsmodule: TTS (Text-zu-Sprache), ASR (Spracherkennung) und Sprachtelefonie. Diese Funktionen ermöglichen Ihnen eine natürliche Kommunikation mit KI per Sprache und verbessern das Nutzererlebnis.

- TTS (Text-zu-Sprache): Wandelt KI-Antworten in gesprochene Sprache um
- ASR (Spracherkennung): Konvertiert Ihre Sprache in Texteingaben
- Sprachtelefonie: Kombiniert TTS und ASR für ein ChatGPT-ähnliches Spracherlebnis

## II. TTS (Text-zu-Sprache)-Funktion

### 1. Unterstützte Diensttypen

Cherry Studio unterstützt vier TTS-Diensttypen:

- OpenAI: Nutzt die TTS-API von OpenAI, erfordert API-Schlüssel
- Browser-TTS: Verwendet die integrierte Sprachsynthese des Browsers, kostenlos ohne Konfiguration
- Siliconflow: Nutzt den TTS-Dienst von Siliconflow, erfordert API-Schlüssel
- Kostenloser Online-TTS: Verwendet kostenlose Online-TTS-Dienste, kein API-Schlüssel erforderlich

### 2. Einrichtungsmethode

1) Gehen Sie zur Einstellungsseite, wählen Sie den Tab "Sprachfunktionen"
2) Im Untertab "TTS":
   - Aktivieren Sie die TTS-Funktion (Schalter umlegen)
   - Wählen Sie den TTS-Diensttyp
   - Konfigurieren Sie je nach gewähltem Dienst die Parameter:
     - OpenAI: API-Schlüssel, API-Adresse, Stimme und Modell eingeben
     - Browser-TTS: Stimme auswählen
     - Siliconflow: API-Schlüssel, API-Adresse, Stimme, Modell, Antwortformat und Sprechgeschwindigkeit konfigurieren
     - Kostenloser Online-TTS: Stimme und Ausgabeformat wählen
3) Konfigurieren Sie TTS-Filteroptionen (optional):
   - Denkprozesse filtern
   - Markdown-Markierungen filtern
   - Codeblöcke filtern
4) Legen Sie fest, ob der TTS-Fortschrittsbalken angezeigt werden soll
5) Klicken Sie auf "TTS testen", um die Konfiguration zu überprüfen

### 3. Verwendungsmethoden

- Nach Aktivierung werden KI-Antworten automatisch in Sprache umgewandelt
- Im Chat wird unter jeder KI-Antwort eine TTS-Wiedergabetaste angezeigt
- Klicken zum Abspielen/Pausieren der Sprachwiedergabe
- Bei aktiviertem Fortschrittsbalken wird der Abspielstatus unter dem Text angezeigt
- Lange Texte werden automatisch segmentiert und fortlaufend wiedergegeben

## III. ASR (Spracherkennung)-Funktion

### 1. Unterstützte Diensttypen

Cherry Studio unterstützt drei ASR-Diensttypen:

- OpenAI: Nutzt das Whisper-Modell von OpenAI, erfordert API-Schlüssel
- Browser: Verwendet die integrierte Spracherkennung des Browsers, kostenlos ohne Konfiguration
- Lokaler Server: Verbindung zu lokalem WebSocket-Server für Spracherkennung

### 2. Einrichtungsmethode

1) Gehen Sie zur Einstellungsseite, wählen Sie den Tab "Sprachfunktionen"
2) Im Untertab "ASR":
   - Aktivieren Sie die ASR-Funktion (Schalter umlegen)
   - Wählen Sie den ASR-Diensttyp
   - Konfigurieren Sie je nach Dienst die Parameter:
     - OpenAI: API-Schlüssel, API-Adresse, Modell auswählen
     - Browser: Keine zusätzliche Konfiguration
     - Lokaler Server: Festlegen, ob der ASR-Server automatisch starten soll
   - Erkennungssprache auswählen (Standard: Chinesisch)
3) Klicken Sie auf "ASR testen", um die Konfiguration zu überprüfen

### 3. Verwendungsmethoden

- Nach Aktivierung erscheint neben dem Eingabefeld eine Spracherkennungstaste
- Klicken zum Starten der Aufnahme
- Gesprochener Text wird erkannt und ins Eingabefeld übertragen
- Erneut klicken zum Beenden der Aufnahme
- Unterstützt kontinuierliche Mehrsatzerkennung im Akkumulationsmodus

## IV. Sprachtelefonie-Funktion

### 1. Funktionseigenschaften

- Kombiniert TTS und ASR für ChatGPT-ähnliche Gespräche
- Verwendet schwebende, verschiebbare Fenster
- Unterstützt "Halten zum Sprechen"-Modus
- Anpassbare Tastenkombinationen
- Fenster kann minimiert werden
- Dediziertes Sprachtelefonie-Modell wählbar
- Anpassbare Prompts

### 2. Einrichtungsmethode

1) Gehen Sie zur Einstellungsseite, wählen Sie den Tab "Sprachfunktionen"
2) Im Untertab "Telefoniefunktion":
   - Aktivieren Sie die Sprachtelefonie (Schalter umlegen)
   - Klicken Sie "Modell auswählen" für das KI-Gesprächsmodell
   - Passen Sie Prompts im Textfeld an (optional)
   - Klicken Sie "Speichern" oder "Zurücksetzen" für Standard-Prompts

### 3. Verwendungsmethoden

1) Klicken Sie im Chat auf das Sprachtelefonie-Symbol (Telefonhörer)
2) Das Fenster öffnet sich mit Willkommensansage
3) "Halten zum Sprechen"-Taste gedrückt halten (oder Tastenkombination nutzen)
4) Loslassen zum Senden der Aufnahme an die KI
5) KI generiert Antwort und gibt sie per TTS wieder
6) Steuerungsmöglichkeiten:
   - Stummschalttaste
   - Pause/Fortsetzen-Taste
   - Einstellungen-Taste für Tastenkombinationen
   - Minimierungstaste
7) Schließen-Button beendet das Gespräch

### 4. Tastenkombinationen einrichten

1) Im Sprachfenster auf "Einstellungen" klicken
2) Im Panel auf "Tastenkombination" klicken
3) Gewünschte Taste drücken (z.B. Leertaste, Umschalt)
4) "Speichern" klicken
5) Gedrückt halten zum Aufnehmen, Loslassen zum Senden

## V. Häufige Probleme und Lösungen

### 1. TTS-Probleme

- Problem: Keine Tonwiedergabe  
  Lösung: TTS-Aktivierung prüfen, Diensttyp und Parameter überprüfen

- Problem: Schlechte Tonqualität  
  Lösung: Anderen TTS-Dienst oder Stimme testen

- Problem: Fehlermeldungen bei Wiedergabe  
  Lösung: API-Schlüssel und Internetverbindung prüfen

### 2. ASR-Probleme

- Problem: Sprache wird nicht erkannt  
  Lösung: ASR-Aktivierung prüfen, Parameter und Diensttyp kontrollieren

- Problem: Geringe Erkennungsgenauigkeit  
  Lösung: Anderen ASR-Dienst testen, Mikrofonposition anpassen

- Problem: Serververbindung fehlgeschlagen  
  Lösung: Lokalen Serverstatus prüfen, Anwendung neustarten

### 3. Sprachtelefonie-Probleme

- Problem: Fenster öffnet nicht  
  Lösung: Aktivierung prüfen, TTS/ASR-Konfiguration kontrollieren

- Problem: Keine Reaktion auf "Halten zum Sprechen"  
  Lösung: Mikrofonberechtigungen prüfen, Funktion neustarten

- Problem: Keine Sprachantwort der KI  
  Lösung: TTS-Aktivierung und Stummschaltung prüfen

## VI. Erweiterte Einstellungen

### 1. TTS-Erweiterungen

- Filteroptionen: Verbessern die Sprachwiedergabe
- Fortschrittsbalken: Optionaler Wiedergabestatus
- Benutzerdefinierte Stimmen/Modelle: Eigene Optionen hinzufügen

### 2. ASR-Erweiterungen

- Autostart: Server bei App-Start automatisch laden
- Sprachenwahl: Unterschiedliche Erkennungssprachen

### 3. Sprachtelefonie-Erweiterungen

- Benutzerdefinierte Prompts: Steuern KI-Antwortstil
- Dediziertes Modell: Separat vom Haupt-Chat auswählbar
- Tastenkombinationen: Individuelle Aufnahmesteuerung

## VII. Nutzungsempfehlungen

1. TTS-Dienst wählen:
   - Für hohe Qualität: OpenAI oder Siliconflow
   - Ohne API: Browser-TTS oder kostenloser Online-TTS

2. ASR-Dienst wählen:
   - Für hohe Genauigkeit: OpenAI
   - Ohne API: Browser-Spracherkennung

3. Sprachtelefonie optimieren:
   - Kopfhörer verhindern Echo-Effekte
   - Nutzung in ruhiger Umgebung verbessert Erkennung
   - Angepasste Prompts optimieren Sprachantworten

4. Einstellungen anpassen:
   - Bei Texteingabe: Nur TTS aktivieren
   - Bei Spracheingabe: Nur ASR aktivieren
   - Für vollständige Sprachinteraktion: Sprachtelefonie nutzen

Diese Anleitung soll Ihnen helfen, die Sprachfunktionen von Cherry Studio optimal zu nutzen und ein natürliches KI-Interaktionserlebnis zu genießen!
```