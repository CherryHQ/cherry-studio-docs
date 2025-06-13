
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Benutzerdefinierte Anbieter

Cherry Studio integriert nicht nur führende KI-Modelldienste, sondern bietet Ihnen auch leistungsstarke Anpassungsmöglichkeiten. Mit der Funktion **Benutzerdefinierte KI-Anbieter** können Sie problemlos jedes gewünschte KI-Modell einbinden.

## Warum benutzerdefinierte KI-Anbieter?

* **Flexibilität:** Nicht eingeschränkt durch vordefinierte Anbieterlisten, frei wählbare KI-Modelle für Ihre Anforderungen.
* **Vielfalt:** Experimentieren Sie mit KI-Modellen verschiedener Plattformen und entdecken Sie deren einzigartige Stärken.
* **Kontrolle:** Direkte Verwaltung Ihrer API-Schlüssel und Zugriffsadressen für Sicherheit und Privatsphäre.
* **Anpassung:** Integration privat bereitgestellter Modelle für spezifische Geschäftsanforderungen.

## Hinzufügen benutzerdefinierter KI-Anbieter

Fügen Sie in nur wenigen Schritten Ihren benutzerdefinierten KI-Anbieter zu Cherry Studio hinzu:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Einstellungen öffnen:** Klicken Sie im linken Navigationsbereich von Cherry Studio auf "Einstellungen" (Zahnradsymbol).
2. **Modellservices aufrufen:** Wählen Sie im Einstellungsbereich den Tab "Modellservices".
3. **Anbieter hinzufügen:** Unter "Modellservices" finden Sie die bestehende Anbieterliste. Klicken Sie auf "+ Hinzufügen", um das Popup zu öffnen.
4. **Informationen eingeben:** Füllen Sie im Popup folgende Felder aus:
   * **Anbietername:** Vergeben Sie einen erkennbaren Namen (z.B.: MyCustomOpenAI).
   * **Anbietertyp:** Wählen Sie den Typ aus der Dropdown-Liste. Aktuell unterstützt:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Konfiguration speichern:** Klicken Sie auf "Hinzufügen", um die Konfiguration zu speichern.

## Konfiguration benutzerdefinierter KI-Anbieter

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Nach dem Hinzufügen konfigurieren Sie den Anbieter in der Liste:

1. **Aktivierungsstatus:** Der Schalter rechts aktiviert den jeweiligen Dienst.
2. **API-Schlüssel:**
   * Tragen Sie den API-Schlüssel Ihres KI-Anbieters ein.
   * Überprüfen Sie die Gültigkeit mit der "Prüfen"-Schaltfläche.
3. **API-Adresse:**
   * Geben Sie die Basis-URL des KI-Dienstes ein.
   * Konsultieren Sie die offizielle Dokumentation für die korrekte Adresse.
4.  **Modellverwaltung:**
    * Fügen Sie manuell Modell-IDs hinzu (z.B. `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>
    * Bei Unsicherheit zur Modellbezeichnung: Offizielle Anbieterdokumentation beachten.
    * Verwenden Sie "Verwalten" zum Bearbeiten oder Löschen vorhandener Modelle.

## Nutzung starten

Nach abgeschlossener Konfiguration wählen Sie im Chat-Interface von Cherry Studio Ihren benutzerdefinierten KI-Anbieter und starten die Konversation!

## vLLM als benutzerdefinierten KI-Anbieter nutzen

vLLM ist eine schnelle LLM-Inferenzbibliothek ähnlich wie Ollama. So binden Sie vLLM in Cherry Studio ein:

1.  **vLLM installieren:** Folgen Sie der offiziellen Anleitung: [https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)

    ```sh
    pip install vllm # bei pip-Nutzung
    uv pip install vllm # bei uv-Nutzung
    ```
2.  **vLLM-Dienst starten:** Nutzen Sie die OpenAI-kompatible Schnittstelle:
    * Variante 1:

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Variante 2:

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

    Der Dienst läuft standardmäßig auf Port `8000`. Mit `--port` können Sie einen anderen Port festlegen.

3. **vLLM-Anbieter in Cherry Studio hinzufügen:**
   * Anbieter hinzufügen wie oben beschrieben.
   * **Anbietername:** `vLLM`
   * **Anbietertyp:** `OpenAI` auswählen.
4. **vLLM konfigurieren:**
   * **API-Schlüssel:** Leerlassen oder beliebigen Wert eintragen (vLLM benötigt keinen Schlüssel).
   * **API-Adresse:** vLLM-API-Adresse eintragen (Standard: `http://localhost:8000/`, bei Portänderung anpassen).
   * **Modellverwaltung:** Namen des in vLLM geladenen Modells eintragen (z.B. `gpt2` bei Beispielbefehl).
5. **Konversation starten:** Wählen Sie in Cherry Studio den vLLM-Anbieter und das Modell (z.B. `gpt2`) aus.

## Tipps & Hinweise

* **Dokumentation lesen:** Konsultieren Sie vor dem Hinzufügen immer die offizielle Dokumentation Ihres KI-Anbieters für API-Schlüssel, Adressen und Modellnamen.
* **API-Schlüssel prüfen:** Nutzen Sie die "Prüfen"-Funktion, um Fehler zu vermeiden.
* **API-Adresse beachten:** Unterschiedliche Anbieter und Modelle haben spezifische Adressen.
* **Modelle gezielt hinzufügen:** Fügen Sie nur benötigte Modelle ein, um Überladung zu vermeiden.