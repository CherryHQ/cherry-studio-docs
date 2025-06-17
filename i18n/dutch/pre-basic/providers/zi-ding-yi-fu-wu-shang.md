
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Aangepaste Providers

Cherry Studio biedt niet alleen geïntegreerde AI-modeldiensten, maar geeft je ook krachtige aanpassingsmogelijkheden. Met de functie **Aangepaste AI-Provider** kun je eenvoudig elke gewenste AI-model integreren.

## Waarom een aangepaste AI-provider nodig?

* **Flexibiliteit:** Niet beperkt door vooraf ingestelde providerslijsten; kies vrij het AI-model dat het beste bij je behoeften past.
* **Diversiteit:** Experimenteer met AI-modellen van verschillende platforms om hun unieke voordelen te ontdekken.
* **Controle:** Beheer je API-sleutels en toegangsadressen direct voor maximale veiligheid en privacy.
* **Maatwerk:** Sluit privé geïmplementeerde modellen aan voor specifieke bedrijfsbehoeften.

## Een aangepaste AI-provider toevoegen

Voeg in enkele stappen je aangepaste AI-provider toe aan Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Instellingen openen:** Klik in de linkernavigatiebalk van Cherry Studio op het tandwielpictogram ("Instellingen").
2. **Naar modeldiensten gaan:** Selecteer het tabblad "Modeldiensten" in instellingen.
3. **Provider toevoegen:** Klik op de "+ Toevoegen"-knop onder de bestaande providerslijst om het pop-upvenster te openen.
4. **Gegevens invullen:**
   * **Providernaam:** Geef een herkenbare naam (bijv. MyCustomOpenAI)
   * **Providertype:** Selecteer uit de lijst:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Configuratie opslaan:** Klik op "Toevoegen" na het invullen.

## Aangepaste AI-provider configureren

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Na toevoeging moet je de provider in de lijst vinden en configureren:

1. **Inschakelstatus:** Schakel de aan/uit-schakelaar rechts in om de service te activeren.
2. **API-sleutel:**
   * Voer je API Key in
   * Klik op "Controleren" om de sleutel te valideren
3. **API-adres:**
   * Voer het basis-URL in voor API-toegang
   * Raadpleeg officiële documentatie voor correcte URL
4. **Modelbeheer:**
   * Klik op "+ Toevoegen" om model-ID's (zoals `gpt-3.5-turbo`) handmatig toe te voegen
   
    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>
    
   * Raadpleeg officiële documentatie voor modelnamen
   * Gebruik "Beheren" om toegevoegde modellen te bewerken/verwijderen

## Aan de slag

Na configuratie kun je in het chatscherm je aangepaste provider en model selecteren om met AI te praten!

## vLLM als aangepaste AI-provider gebruiken

vLLM is een snelle, gebruiksvriendelijke LLM-inferentiebibliotheek vergelijkbaar met Ollama. Zo integreer je het:

1. **vLLM installeren:** Volg de officiële handleiding:
    ```sh
    pip install vllm # voor pip
    uv pip install vllm # voor uv
    ```
2. **vLLM-service starten:** Start met OpenAI-compatibele interface:
    * Gebruik `vllm.entrypoints.openai.api_server`:
    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```
    * Of gebruik `uvicorn`:
    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```
   > De service luistert standaard op poort `8000`. Gebruik `--port` voor aangepaste poorten.
3. **vLLM-provider toevoegen:**
   * Volg de eerdere stappen om een provider toe te voegen
   * **Providernaam:** `vLLM`
   * **Providertype:** Selecteer `OpenAI`
4. **vLLM-provider configureren:**
   * **API-sleutel:** Leeg laten of willekeurige waarde (niet vereist)
   * **API-adres:** `http://localhost:8000/` (pas poort aan indien nodig)
   * **Modelbeheer:** Voeg modelnaam toe (bijv. `gpt2` als in voorbeeld)
5. **Gesprek starten:** Selecteer vLLM-provider en model om te beginnen!

## Tips

* **Documentatie lezen:** Controleer altijd officiële documentatie voor API-sleutels, adressen en modelnamen
* **API-sleutel controleren:** Gebruik de "Controleren"-knop om sleutelgeldigheid te verifiëren
* **API-adres verifiëren:** Verschillende providers/modellen hebben mogelijk unieke adressen
* **Modellen selectief toevoegen:** Voeg alleen echt benodigde modellen toe voor optimale prestaties