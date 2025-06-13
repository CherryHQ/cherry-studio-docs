
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Ollama

Ollama ist ein hervorragendes Open-Source-Tool, mit dem Sie verschiedene Large Language Models (LLMs) lokal einfach ausführen und verwalten können. Cherry Studio unterstützt jetzt die Ollama-Integration, sodass Sie in einer vertrauten Oberfläche direkt mit lokal bereitgestellten LLMs interagieren können – ohne Abhängigkeit von Cloud-Diensten!

## Was ist Ollama?

Ollama ist ein Tool, das die Bereitstellung und Nutzung von Large Language Models (LLM) vereinfacht. Es bietet folgende Vorteile:

* **Lokaler Betrieb:** Modelle laufen vollständig auf Ihrem lokalen Computer, ohne Internetverbindung, wodurch Ihre Privatsphäre und Datensicherheit geschützt werden.
* **Einfache Bedienung:** Mit einfachen Befehlszeilenanweisungen können Sie verschiedene LLMs herunterladen, ausführen und verwalten.
* **Modellvielfalt:** Unterstützt beliebte Open-Source-Modelle wie Llama 2, Deepseek, Mistral, Gemma und mehr.
* **Plattformübergreifend:** Funktioniert auf macOS, Windows und Linux.
* **Offene API:** Bietet eine mit OpenAI kompatible Schnittstelle für Integrationen mit anderen Tools.

## Warum Ollama in Cherry Studio nutzen?

* **Keine Cloud-Dienste nötig:** Keine Limitierungen durch API-Kontingente oder Kosten – nutzen Sie die volle Leistung lokaler LLMs.
* **Datenhoheit:** Alle Konversationsdaten verbleiben lokal, ohne Datenschutzbedenken.
* **Offline-Verfügbarkeit:** Interagieren Sie auch ohne Internetverbindung mit LLMs.
* **Anpassbarkeit:** Wählen und konfigurieren Sie das passende LLM für Ihre Anforderungen.

## Ollama in Cherry Studio konfigurieren

### **1. Ollama installieren und ausführen**

Installieren und starten Sie Ollama zunächst auf Ihrem Computer:

* **Ollama herunterladen:** Besuchen Sie die offizielle Website ([https://ollama.com/](https://ollama.com/)) und laden Sie das passende Installationspaket für Ihr Betriebssystem herunter.\
  Unter Linux installieren Sie Ollama direkt mit:
  
  ```sh
  curl -fsSL https://ollama.com/install.sh | sh
  ```
* **Ollama installieren:** Folgen Sie den Anweisungen des Installationsprogramms.
* **Modell herunterladen:** Öffnen Sie Terminal (oder Eingabeaufforderung) und laden Sie Ihr gewünschtes Modell mit `ollama run`. Beispiel für Llama 3.2:
  
  ```sh
  ollama run llama3.2
  ```
  Ollama lädt das Modell automatisch herunter und startet es.
* **Ollama laufend halten:** Stellen Sie sicher, dass Ollama während der Nutzung in Cherry Studio aktiv bleibt.

### **2. Ollama als KI-Anbieter hinzufügen**

Fügen Sie Ollama als benutzerdefinierten KI-Dienstleister hinzu:

* **Einstellungen öffnen:** Klicken Sie in der linken Navigationsleiste von Cherry Studio auf „Einstellungen“ (Zahnradsymbol).
* **Modellservices wählen:** Wählen Sie im Einstellungsmenü den Tab „Modellservices“.
* **Anbieter hinzufügen:** Klicken Sie in der Liste auf Ollama.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Ollama als Dienstleister konfigurieren**

Konfigurieren Sie Ollama im Dienstleisterverzeichnis:

1. **Aktivierungsstatus:**
   * Stellen Sie sicher, dass der Schalter rechts neben Ollama eingeschaltet ist.
2. **API-Schlüssel:**
   * Ollama benötigt standardmäßig **keinen** API-Schlüssel. Lassen Sie dieses Feld leer oder tragen Sie beliebigen Text ein.
3. **API-Adresse:**
   * Tragen Sie die lokale Ollama-API-Adresse ein. Normalerweise:
     ```
     http://localhost:11434/
     ```
     Passen Sie dies bei geändertem Port an.
4. **Aktivitätsdauer:** Legt die Sitzungslaufzeit in Minuten fest. Ohne neue Dialoge innerhalb dieser Zeit trennt Cherry Studio die Ollama-Verbindung automatisch.
5. **Modellverwaltung:**
   * Klicken Sie auf „+ Hinzufügen“, um manuell heruntergeladene Ollama-Modelle einzutragen.
   * Beispiel: Nach `ollama run llama3.2` tragen Sie `llama3.2` ein.
   * Klicken Sie auf „Verwalten“, um Modelle zu bearbeiten oder zu löschen.

## Nutzung starten

Nach der Konfiguration wählen Sie im Cherry Studio-Chat Ollama als Dienstleister und Ihr Modell aus, um mit lokalem LLM zu interagieren!

## Tipps & Hinweise

* **Erstmalige Modellausführung:** Beim ersten Start muss Ollama Modell-Dateien herunterladen (dauert ggf. länger).
* **Verfügbare Modelle prüfen:** Führen Sie `ollama list` im Terminal aus, um lokale Modelle anzuzeigen.
* **Hardwareanforderungen:** LLMs benötigen erhebliche Ressourcen (CPU, RAM, GPU). Stellen Sie kompatible Hardware bereit.
* **Ollama-Dokumentation:** Nutzen Sie `Ollama-Dokumentation und Modelle anzeigen` im Konfigurationsmenü für direkten Zugriff auf die offizielle Dokumentation.