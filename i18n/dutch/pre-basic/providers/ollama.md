
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Ollama

Ollama is een uitstekend open-source hulpmiddel waarmee u verschillende grote taalmodel (LLM's) gemakkelijk lokaal kunt uitvoeren en beheren. Cherry Studio ondersteunt nu Ollama-integratie, zodat u rechtstreeks met lokaal geïmplementeerde LLM kunt communiceren in een vertrouwde interface, zonder afhankelijk te zijn van clouddiensten!

## Wat is Ollama?

Ollama is een hulpmiddel dat de implementatie en het gebruik van grote taalmodel (LLM) vereenvoudigt. Het heeft de volgende kenmerken:

* **Lokaal draaien:** Modellen draaien volledig op uw lokale computer zonder internetverbinding, wat uw privacy en gegevensbeveiliging beschermt.
* **Eenvoudig te gebruiken:** Download, voer uit en beheer verschillende LLM's met eenvoudige opdrachtregelinstructies.
* **Rijk aan modellen:** Ondersteunt populaire open-source modellen zoals Llama 2, Deepseek, Mistral, Gemma en meer.
* **Cross-platform:** Werkt op macOS-, Windows- en Linux-systemen.
* **Open API:** Biedt een OpenAI-compatibele interface voor integratie met andere tools.

## Waarom Ollama gebruiken in Cherry Studio?

* **Geen cloudservice nodig:** Ontsnap aan de quota en kosten van cloud-API's en geniet van de kracht van lokale LLM's.
* **Gegevensprivacy:** Al uw gespreksgegevens blijven lokaal opgeslagen, zonder zorgen over privacylekken.
* **Offline beschikbaar:** Blijf communiceren met LLM's zelfs zonder internetverbinding.
* **Aanpassing:** Kies en configureer de LLM die het beste bij uw behoeften past.

## Ollama configureren in Cherry Studio

### **1. Ollama installeren en uitvoeren**

Installeer en draai Ollama eerst op uw computer door deze stappen te volgen:

*   **Download Ollama:** Bezoek de officiële website van Ollama ([https://ollama.com/](https://ollama.com/)) en download het juiste installatiepakket voor uw besturingssysteem.\
    Op Linux kunt u Ollama rechtstreeks installeren met dit commando:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Installeer Ollama:** Volg de instructies van het installatieprogramma om de installatie te voltooien.
*   **Download een model:** Open een terminal (of opdrachtprompt) en gebruik het `ollama run`-commando om het gewenste model te downloaden. Download bijvoorbeeld het Llama 2-model met:

    ```sh
    ollama run llama3.2
    ```

    Ollama downloadt en voert het model automatisch uit.
* **Houd Ollama actief:** Zorg dat Ollama actief blijft tijdens het gebruik van Ollama-modellen in Cherry Studio.

### **2. Voeg Ollama als provider toe in Cherry Studio**

Voeg vervolgens Ollama toe als aangepaste AI-provider in Cherry Studio:

* **Open instellingen:** Klik in de linkernavigatiebalk van Cherry Studio op "Instellingen" (tandwielpictogram).
* **Ga naar modelservices:** Selecteer in het instellingenvenster het tabblad "Modelservices".
* **Voeg een provider toe:** Klik op Ollama in de lijst.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configureer de Ollama-provider**

Configureer de Ollama-provider in de lijst met providers:

1. **Ingeschakelde status:**
   * Zorg dat de schakelaar rechts van de Ollama-provider is ingeschakeld.
2. **API-sleutel:**
   * Ollama vereist standaard **geen** API-sleutel. Laat dit veld leeg of vul willekeurige inhoud in.
3. **API-adres:**
   * Vul het lokale API-adres van Ollama in. Standaard is dit:

       ```
       http://localhost:11434/
       ```

       Wijzig dit indien u de poort heeft aangepast.
4. **Actief houden gedurende:** Stelt de sessieduur in (in minuten). Cherry Studio verbreekt automatisch de verbinding met Ollama na inactiviteit.
5. **Modelbeheer:**
   * Klik op "+ Toevoegen" om gedownloade Ollama-modelnamen handmatig toe te voegen.
   * Voer bijvoorbeeld `llama3.2` in als u dit model via `ollama run llama3.2` heeft gedownload.
   * Klik op "Beheren" om modellen te bewerken of te verwijderen.

## Aan de slag

Na deze configuratie kunt u in het chatvenster van Cherry Studio de Ollama-provider en uw gedownloade model selecteren om met lokale LLM's te chatten!

## Tips en suggesties

* **Model voor het eerst uitvoeren:** De eerste keer kan het downloaden van modellen tijd kosten - wees geduldig.
* **Beschikbare modellen bekijken:** Voer `ollama list` in de terminal uit om uw Ollama-modellen te zien.
* **Hardwarevereisten:** Grote taalmodel vereisen rekenkracht (CPU/GPU/geheugen) - controleer de systeemvereisten.
* **Ollama-documentatie:** Klik op de link `Ollama-documentatie en modellen bekijken` in de configuratiepagina om naar de officiële documentatie te gaan.