---
icon: book-bookmark
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Kennisoverzicht

## Wat zijn tokens?

Tokens zijn de basiseenheden waarmee AI-modellen tekst verwerken, te beschouwen als de kleinste "denk"-eenheden van het model. Ze komen niet exact overeen met karakters of woorden zoals wij die begrijpen, maar vertegenwoordigen een speciale tekstsegmentatiemethode van het model zelf.

#### 1. Chinese woordscheiding
* Een Chinees karakter wordt gewoonlijk gecodeerd als 1-2 tokens
* Bijvoorbeeld: `"你好"` ≈ 2-4 tokens

#### 2. Engelse woordscheiding
* Veelvoorkomende woorden zijn gewoonlijk 1 token
* Langere of ongebruikelijke woorden worden opgesplitst in meerdere tokens
* Bijvoorbeeld:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Speciale tekens
* Spaties, leestekens en dergelijke gebruiken ook tokens
* Een regeleinde is gewoonlijk 1 token

{% hint style="info" %}
Elke aanbieder heeft een andere Tokenizer, en zelfs verschillende modellen van dezelfde aanbieder kunnen verschillende Tokenizers hebben. Deze kennis dient enkel om het concept van tokens te verduidelijken.
{% endhint %}

***

## Wat is een Tokenizer?

Een Tokenizer (woordscheidingsprogramma) is het hulpmiddel waarmee een AI-model tekst in tokens omzet. Het bepaalt hoe invoertekst wordt opgesplitst in de kleinste eenheden die het model kan begrijpen.

### Waarom hebben verschillende modellen verschillende Tokenizers?

#### 1. Verschillende trainingsgegevens
* Verschillende corpus leiden tot verschillende optimalisatierichtingen
* Variërende niveaus van meertalige ondersteuning
* Gespecialiseerde optimalisatie voor specifieke domeinen (zoals gezondheidszorg, recht)

#### 2. Verschillende woordscheidingsalgoritmen
* BPE (Byte Pair Encoding) - gebruikt door OpenAI GPT-reeks
* WordPiece - gebruikt door Google BERT
* SentencePiece - geschikt voor meertalige scenario's

#### 3. Verschillende optimalisatiedoelen
* Sommige richten zich op compressie-efficiëntie
* Andere op semantisch behoud
* Weer anderen op verwerkingssnelheid

### Praktische impact
Dezelfde tekst kan verschillende aantallen tokens genereren in verschillende modellen:

```
Invoer: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## Wat is een Embedding Model?

**Basisconcept:** Een embedding-model is een techniek die hoog-dimensionale discrete gegevens (tekst, afbeeldingen etc.) omzet in laag-dimensionale continue vectoren. Deze transformatie stelt machines in staat complexe gegevens beter te begrijpen en verwerken. Vergelijk het met het vereenvoudigen van een complexe puzzel tot een eenvoudig coördinaatpunt dat toch de sleutelkenmerken behoudt. In grote model-ecosystemen fungeert het als "tolk" die menselijke informatie vertaalt naar berekenbare numerieke vormen voor AI.

**Werking:** In natuurlijke taalverwerking positioneert een embedding-model woorden als specifieke punten in een vectorruimte. In deze ruimte groeperen semantisch verwante woorden automatisch bij elkaar. Bijvoorbeeld:
* De vectoren van "koning" en "koningin" liggen dichtbij elkaar
* Huisdierwoorden als "kat" en "hond" zijn ook dichtbij
* Onverwante woorden als "auto" en "brood" liggen ver uit elkaar

**Belangrijkste toepassingsgebieden:**
* Tekstanalyse: documentclassificatie, sentimentanalyse
* Aanbevelingssystemen: gepersonaliseerde contentaanbevelingen
* Afbeeldingsverwerking: vergelijkbare afbeeldingen vinden
* Zoekmachines: semantische zoekoptimalisatie

**Kernvoordelen:**
1. Dimensionaliteitsreductie: vereenvoudigt complexe gegevens
2. Semantisch behoud: behoudt sleutelbetekenissen uit originele gegevens
3. Rekenrendement: verbetert modeltrainings- en deductiesnelheid aanzienlijk

**Technische waarde:** Embedding-modellen vormen fundamentele componenten in moderne AI-systemen, bieden hoogwaardige datarepresentaties voor machine learning-taken en zijn cruciale technologieën voor ontwikkelingen in natuurlijke taalverwerking en computervisie.

***

## Hoe Embedding-modellen werken in kennisondersteuning

**Basiswerkstroom:**

1. **Voorbewerkingsfase voor kennisbank**
   * Documenten splitsen in geschikte chunks (tekstfragmenten)
   * Elk chunk omzetten in vector via embedding-model
   * Vectoren en originele tekst opslaan in vectordatabase

2. **Vraagverwerkingsfase**
   * Gebruikersvraag omzetten in vector
   * Vergelijkbare content zoeken in vectoropslag
   * Gevonden relevante content als context aan LLM verstrekken

***

## **Wat is MCP (Model Context Protocol)?**

MCP is een open-source protocol dat grote taalmodellen (LLM's) op gestandaardiseerde wijze contextinformatie verschaft.

* **Analoog begrip:** Vergelijk MCP met een "USB-stick" voor AI. Net zoals USB-sticks allerlei bestanden bevatten die computers direct kunnen gebruiken, kunnen op MCP-Servers contextbiedende "plug-ins" worden aangesloten. LLM's kunnen deze plug-ins op aanvraag gebruiken voor rijkere contextinformatie.
* **Vergelijking met Function Tools:** Traditionele function tools bieden externe functionaliteit, maar MCP vertegenwoordigt een hoger abstractieniveau. Waar function tools zich richten op specifieke taken, biedt MCP een universeel, modulair contextverwervingsmechanisme.

### **Kernvoordelen van MCP**

1. **Standaardisatie:** Uniforme interfaces en dataformaten voor naadloze samenwerking
2. **Modulariteit:** Ontwikkelaars kunnen context opsplitsen in herbruikbare plug-ins
3. **Flexibiliteit:** LLM's selecteren dynamisch benodigde contextplug-ins voor intelligente interactie
4. **Schaalbaarheid:** Ontwerp ondersteunt toevoeging van nieuwe contextplug-intypen voor eindeloze uitbreidingen

***