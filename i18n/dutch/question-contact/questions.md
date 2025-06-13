---
icon: seal-question
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Veelgestelde Vragen

## Veelvoorkomende foutcodes

* **4xx (Clientfout-statuscodes)**: Doorgaans fouten in verzoekopmaak, authenticatiefalen of autorisatiefalen waardoor het verzoek niet kan worden voltooid.
* **5xx (Serverfout-statuscodes)**: Doorgaans serverfouten zoals serveruitval of time-outs tijdens verwerkingsverzoeken.

| Foutcode          | Mogelijke situaties                                                   | Oplossing                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4> | Ongeldige verzoekbodyopmaak                                                       | <p>Controleer de foutinhoud teruggekeerd door de dialoog of bekijk de foutmelding in de <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a>, volg de aanwijzingen.</p><p><mark style="color:purple;">【Veelvoorkomend geval 1】</mark>: Voor Gemini-modellen kan koppeling van een kaart nodig zijn;<br><mark style="color:purple;">【Veelvoorkomend geval 2】</mark>: Data-overmaat, vooral bij visuele modellen - afbeeldingen overschreden maximale limiet;<br><mark style="color:purple;">【Veelvoorkomend geval 3】</mark>: Niet-ondersteunde parameters of foutieve parameters. Test met een nieuwe assistent;<br><mark style="color:purple;">【Veelvoorkomend geval 4】</mark>: Context overschrijdt limiet - wis context of start nieuwe dialoog.</p> |
| <h4>401</h4> | Authenticatiefalen: model niet ondersteund of account geblokkeerd                             | Neem contact op met provider of controleer accountstatus                                                                                                                                                                                                                                                                                                                                                                                               |
| <h4>403</h4> | Geen machtiging voor verzoekactie                                              | Volg foutmelding in dialoog of [console](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                                                                               |
| <h4>404</h4> | Gevraagde bron niet gevonden                                                  | Controleer verzoekpad                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <h4>422</h4> | Correct formaat maar semantische fout                                          | Server kan verzoek parseren maar niet verwerken. Vaak JSON-fouten (bijv. null, getal i.p.v. string).                                                                                                                                                                                                                                                                                                                                          |
| <h4>429</h4> | Verzoeksnelheidslimiet bereikt                                                | TPM/RPM-limiet overschreden. Wacht even                                                                                                                                                                                                                                                                                                                                                                                                             |
| <h4>500</h4> | Interne serverfout, verzoek niet voltooid                                         | Bij aanhoudende fouten provider contacteren                                                                                                                                                                                                                                                                                                                                                                                                           |
| <h4>501</h4> | Functie niet geïmplementeerd door server                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>502</h4> | Ongeldig antwoord van upstream-server bij gateway/proxy                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>503</h4> | Server tijdelijk overbelast/in onderhoud. Zie Retry-After header                     |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>504</h4> | Gateway/proxy ontving geen tijdig antwoord van upstream-server                             |                                                                                                                                                                                                                                                                                                                                                                                                                                            |

***

## Hoe consolefouten te bekijken

* Klik op Cherry Studio-clientvenster en druk op <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Cherry Studio-clientvenster moet actief zijn om console te openen;
- Open console vóórdat je test/dialoog start om aanvraaginformatie te verzamelen.
{% endhint %}

* Klik in console op <mark style="color:blue;">`Network`</mark> → Zoek de laatste rode <mark style="color:red;">`✗`</mark> bij <mark style="color:red;">`completions`</mark>_(dialoog/vertaling/modelchecks)_ of <mark style="color:red;">`generations`</mark>_(beeldgeneratie-fouten)_ → Klik op <mark style="color:blue;">`Response`</mark> voor volledige inhoud (gebied ④ in afbeelding).

> Kun je de oorzaak niet vinden? Deel een screenshot in de [officiële groep](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Deze methode werkt voor alle functies: dialogen, modeltests, kennisbasistoepassing, beeldcreatie. Open altijd eerst debugvenster vóór acties.

{% hint style="info" %}
Naamkolom (②) varieert per scenario:

Dialoog/vertaling/modelchecks: <mark style="color:red;">`completions`</mark>  
Beeldcreatie: <mark style="color:red;">`generations`</mark>  
Kennisbasecreatie: <mark style="color:red;">`embeddings`</mark>  
{% endhint %}

***

## Formule niet gerenderd/formulerenderfout

* Formulecode wordt getoond? Controleer op afbakeningskarakters:

> **Afbakeningsgebruik**  
> 
> _Inline formules_  
> 
> * Enkele dollar: `$formule$`  
> * Of `\(formule\)`
> 
> 
> 
> _Zelfstandige formuleblokken_  
> 
> * Dubbele dollars: `$$formule$$`  
> * Of `\[formule\]`  
> * Voorbeeld: `$$\sum_{i=1}^n x_i$$`  
>   $$\sum_{i=1}^n x_i$$

* Renderfouten/rommel bij Chinese inhoud? Schakel engine om naar KaTeX.

***

## Kennisbase niet aanmaakbaar/fout bij inbeddimensies

1. Modelstatus onbeschikbaar

> Controleer of model beschikbaar/ondersteund is bij provider.

2. Niet-inbedmodel gebruikt

***

## Model herkent afbeelding niet/afbeelding niet uploadbaar

Controleer eerst of model afbeeldingen ondersteunt: zoek naar oog-icoon na modelnaam in Cherry Studio.

Modelleer met afbeeldingsondersteuning laten uploaden. Onjuiste matching? Ga naar providerlijst → modelinstellingen → activeer "Afbeelding".

Modeldetails vind je bij provider. Net als inbedmodellen: afbeeldsoptie activeren heeft geen effect bij niet-visuele modellen.