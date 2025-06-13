---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Spraakfuncties

```
Cherry Studio Spraakfuncties Gebruikershandleiding

1. Overzicht van spraakfuncties

Cherry Studio biedt drie belangrijke spraakfunctiemodules: TTS (Text-To-Speech), ASR (Automatic Speech Recognition) en spraakgesprekken. Deze functies stellen u in staat om natuurlijke interactie met AI te hebben via spraak, wat de gebruikservaring verbetert.

- TTS (Text-To-Speech): Zet tekst van AI-reacties om in spraakuitvoer
- ASR (Automatic Speech Recognition): Zet uw spraak om in tekstinvoer
- Spraakgesprekken: Combineert TTS en ASR voor een ChatGPT-achtige spraakgesprekservaring

2. TTS (Text-To-Speech) Functie

1. Ondersteunde servicetypen

Cherry Studio ondersteunt vier TTS-servicetypen:

- OpenAI: Gebruikt OpenAI's TTS API, vereist API-sleutel
- Browser TTS: Gebruikt ingebouwde browser-spraaksynthese, gratis en zonder configuratie
- Siliconflow: Gebruikt Siliconflow's TTS-service, vereist API-sleutel
- Gratis online TTS: Gebruikt gratis online TTS-service, geen API-sleutel nodig

2. Instellingsmethode

1) Ga naar instellingenpagina, selecteer tabblad "Spraakfuncties"
2) In "TTS" subtabblad:
   - Schakel TTS in (zet schakelaar aan)
   - Selecteer TTS-servicetype
   - Configureer parameters per servicetype:
     - OpenAI: Vul API-sleutel, API-adres, selecteer stem en model
     - Browser TTS: Selecteer stem
     - Siliconflow: Vul API-sleutel, API-adres, selecteer stem, model, responsformaat en spreeksnelheid
     - Gratis online TTS: Selecteer stem en uitvoerformaat
3) Configureer TTS-filteropties (optioneel):
   - Filter denkprocessen
   - Filter Markdown-tags
   - Filter codeblokken
4) Stel in of TTS-voortgangsbalk getoond moet worden
5) Klik op "Test TTS" knop om configuratie te controleren

3. Gebruiksmethode

- Na activering wordt AI's reactie automatisch omgezet in spraak
- Onder elke AI-reactie in chatvenster wordt TTS-afspeelknop getoond
- Klik om spraak af te spelen/pauzeren
- Als voortgangsbalk is ingeschakeld, wordt deze onder tekst getoond
- Lange teksten worden automatisch gesegmenteerd en samenvallend afgespeeld

3. ASR (Automatic Speech Recognition) Functie

1. Ondersteunde servicetypen

Cherry Studio ondersteunt drie ASR-servicetypen:

- OpenAI: Gebruikt OpenAI's Whisper-model, vereist API-sleutel
- Browser: Gebruikt ingebouwde browser-spraakherkenning, gratis en zonder configuratie
- Lokale server: Maakt verbinding met lokale WebSocket-server voor spraakherkenning

2. Instellingsmethode

1) Ga naar instellingenpagina, selecteer tabblad "Spraakfuncties"
2) In "ASR" subtabblad:
   - Schakel ASR in (zet schakelaar aan)
   - Selecteer ASR-servicetype
   - Configureer parameters per servicetype:
     - OpenAI: Vul API-sleutel, API-adres, selecteer model
     - Browser: Geen extra configuratie nodig
     - Lokale server: Kan instellen of ASR-server automatisch start bij opstarten
   - Selecteer spraakherkenningsstaal (standaard Chinees)
3) Klik op "Test ASR" knop om configuratie te controleren

3. Gebruiksmethode

- Na activering wordt spraakherkenningsknop naast invoerveld getoond
- Klik om opname te starten
- Spraak wordt omgezet in tekst in invoerveld
- Klik opnieuw om opname te stoppen
- Ondersteunt continue herkenning met cumulatief modus

4. Spraakgesprekken Functie

1. Functiekenmerken

- Combineert TTS en ASR voor ChatGPT-achtige spraakgesprekken
- Gebruik zwevend venster met sleepfunctionaliteit
- Ondersteunt "knop ingedrukt houden om te spreken"
- Ondersteunt aanpasbare sneltoetsen
- Ondersteunt venstervouwing
- Kan gespecialiseerde spraakgesprekkenmodel selecteren
- Ondersteunt aanpasbare prompts

2. Instellingsmethode

1) Ga naar instellingenpagina, selecteer tabblad "Spraakfuncties"
2) In "Gespreksfunctie" subtabblad:
   - Schakel spraakgesprekken in (zet schakelaar aan)
   - Klik op "Selecteer model", kies AI-model voor spraakgesprekken
   - Pas spraakgesprekken-prompt aan in tekstveld (optioneel)
   - Klik op "Opslaan" om prompt te bewaren, of "Reset" voor standaardprompt

3. Gebruiksmethode

1) Klik op spraakgesprekkenknop (telefoonicoon) naast invoerveld
2) Spraakgespreksvenster opent en speelt welkomstbericht af
3) Houd "Houd ingedrukt om te spreken" knop ingedrukt om opname te starten
4) Laat knop los om opname te stoppen en naar AI te sturen
5) AI genereert reactie en speelt af via TTS
6) Gebruik bedieningsknoppen:
   - Dempen/opheffen: Controleert TTS-output
   - Pauze/Doorgaan: Pauzeert of hervat gesprek
   - Instellingen: Configureert sneltoetsen
   - Samenvouwen: Vouwt venster samen
7) Klik op sluitknop om gesprek te beëindigen

4. Sneltoetsinstellingen

1) Klik op instellingenknop in spraakgespreksvenster
2) In instellingenpaneel, klik op sneltoetsknop
3) Druk op gewenste toets (bijv. spatiebalk, Shift, etc.)
4) Klik op "Opslaan" om instellingen te bewaren
5) Gebruik: Houd sneltoets ingedrukt om opname te starten, loslaten om te stoppen

5. Veelvoorkomende problemen en oplossingen

1. TTS-gerelateerde problemen

- Probleem: TTS produceert geen geluid
  Oplossing: Controleer of TTS is ingeschakeld, juiste servicetype en benodigde parameters

- Probleem: Slechte TTS-kwaliteit
  Oplossing: Probeer ander servicetype of stem

- Probleem: Foutmelding tijdens TTS-afspelen
  Oplossing: Controleer API-sleutel en netwerkverbinding

2. ASR-gerelateerde problemen

- Probleem: ASR herkent spraak niet
  Oplossing: Controleer of ASR is ingeschakeld en juiste configuratie

- Probleem: Lage herkenningsnauwkeurigheid
  Oplossing: Probeer ander servicetype of pas microfoonpositie aan

- Probleem: ASR-serververbinding mislukt
  Oplossing: Controleer lokale server of herstart applicatie

3. Spraakgesprekproblemen

- Probleem: Gespreksvenster opent niet
  Oplossing: Controleer of spraakgesprekken is ingeschakeld en TTS/ASR correct geconfigureerd

- Probleem: "Knop ingedrukt houden" reageert niet
  Oplossing: Controleer microfoontoestemmingen of herstart gesprek

- Probleem: Geen spraak bij AI-reacties
  Oplossing: Controleer of TTS is ingeschakeld en niet gedempt

6. Geavanceerde instellingen en aanpassingsopties

1. Geavanceerde TTS-instellingen

- Filteropties: Filtert denkprocessen, Markdown-tags en codeblokken
- Voortgangsbalk: Toont voortgangsbalk tijdens afspelen
- Aanpasbare stemmen en modellen: Voeg aangepaste stemmen toe

2. Geavanceerde ASR-instellingen

- Automatisch starten: Start ASR-server bij opstarten applicatie
- Taalselectie: Kies verschillende spraakherkenningsstalen

3. Geavanceerde spraakgesprekinstellingen

- Aanpasbare prompts: Definieer prompts voor AI-reacties
- Gespecialiseerd model: Selecteer apart model voor spraakgesprekken
- Sneltoetsaanpassing: Stel aangepaste opnametoets in

7. Gebruiksaanbevelingen

1. Kies geschikt TTS-servicetype:
   - Voor hoge kwaliteit: Gebruik OpenAI of Siliconflow
   - Zonder API-configuratie: Gebruik Browser TTS of Gratis online TTS

2. Kies geschikt ASR-servicetype:
   - Voor hoge nauwkeurigheid: Gebruik OpenAI
   - Zonder API-configuratie: Gebruik browserherkenning

3. Optimaliseer spraakgesprekservaring:
   - Gebruik koptelefoon om echo te voorkomen
   - Gebruik in stille omgeving voor betere herkenning
   - Gebruik aangepaste prompts voor spraakvriendelijke reacties

4. Pas instellingen aan:
   - Voor tekstinteractie: Schakel alleen TTS in
   - Voor spraakinvoer: Schakel alleen ASR in
   - Voor volledige spraakgesprekken: Schakel spraakgesprekken in

Hopelijk helpt deze handleiding u om optimaal gebruik te maken van Cherry Studio's spraakfuncties voor natuurlijke en gebruiksvriendelijke AI-interactie!
```