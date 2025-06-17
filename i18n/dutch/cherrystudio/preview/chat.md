---
icon: message
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Conversatie-interface

## Assistenten en onderwerpen

### Assistenten

`Assistenten` zijn gepersonaliseerde instellingen voor het gekozen model, zoals vooraf ingestelde prompts en parameters. Met deze instellingen wordt het model beter afgestemd op je verwachte werking.

`Standaard systeemassistent` bevat algemene parameters (zonder prompt). Je kunt deze direct gebruiken of op de [agentenpagina](agents.md) geschikte voorinstellingen zoeken.

### Onderwerpen

`Assistenten` zijn de hoofdgroep van `onderwerpen`. Onder één assistent kun je meerdere onderwerpen (conversaties) aanmaken. Alle `onderwerpen` delen dezelfde parameterinstellingen en promptvoorinstellingen van de assistent.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Knoppen in chatvenster

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nieuw onderwerp` - Creëert een nieuw onderwerp onder de huidige assistent.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Afbeelding of document uploaden` - Vereist modelondersteuning voor afbeeldingen. Documenten worden automatisch omgezet in tekst als context voor het model.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Webzoeken` - Vereist configuratie in instellingen. Zoekresultaten dienen als context voor het model. Zie [Onlinemodus](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` - Activeert kennisbank. Zie [Knowledge Base-tutorial](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP-server` - Activeert MCP-serverfunctionaliteit. Zie [MCP-gebruikershandleiding](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Afbeelding genereren` - Standaard verborgen. Voor modellen die afbeeldingen ondersteunen (zoals Gemini), moet je dit handmatig activeren.

{% hint style="info" %}
Vanwege technische beperkingen moet je deze knop handmatig activeren. Dit wordt verwijderd na optimalisatie.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Model selecteren` - Wisselt van model voor volgende berichten, behoudt context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Snelle frasen` - Vooraf ingestelde zinnen (configureer in instellingen), ondersteunt variabelen.

![](../../.gitbook/assets/对话界面/清空消息.png) `Berichten wissen` - Verwijdert alle inhoud in dit onderwerp.

![](../../.gitbook/assets/对话界面/展开.png) `Uitvouwen` - Vergroot het invoervak voor lange teksten.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Context wissen` - Verwijdert eerdere gesprekscontext voor het model zonder inhoud te verwijderen.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Geschatte Tokens` - Toont: `Huidige contexttokens`, `Max contexttokens` (∞ = onbeperkt), `Huidige invoertokens`, `Geschatte tokens`.

{% hint style="info" %}
Dit is slechts een schatting. Werkelijke tokens verschillen per model (raadpleeg leveranciersgegevens).
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Vertalen` - Vertaalt inhoud in invoervak naar Engels.

## Conversatie-instellingen

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Modelinstellingen

Gesynchroniseerd met `Modelinstellingen` onder assistentconfiguratie. Zie [Assistent-instellingen](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Alleen deze instelling geldt voor huidige assistent. Overige instellingen zijn globaal (bijvoorbeeld berichtstijl).
{% endhint %}

### Berichtinstellingen

#### <mark style="color:blue;">**`Berichtsplitser`**</mark>:

Scheidt berichtinhoud van actiebalk.

{% tabs %}
{% tab title="Ingeschakeld" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Uitgeschakeld" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Serif-lettertype gebruiken`**</mark>：

Wisselt lettertypestijl. Aanpasbaar via [aangepaste CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Rekennummer weergeven`**</mark>：

Toont coderegelnummers in uitvoer.

{% tabs %}
{% tab title="Uitgeschakeld" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ingeschakeld" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Codeblok vouwbaar`**</mark>：

Vouwt lange code automatisch in.

#### <mark style="color:blue;">**`Codeblok regelterugloop`**</mark>：

Activeert terugloop voor lange coderegels.

#### <mark style="color:blue;">**`Redenering automatisch vouwen`**</mark>：

Vouwt denkproces in na voltooiing (indien ondersteund).

#### <mark style="color:blue;">**`Berichtstijl`**</mark>：

Wisselt tussen bellen- of lijstweergave.

#### <mark style="color:blue;">**`Codestijl`**</mark>：

Wisselt weergavestijl codefragmenten.

#### <mark style="color:blue;">**`Wiskundeformule-engine`**</mark>：

* KaTeX - Sneller, geoptimaliseerd voor prestaties.
* MathJax - Langzamer maar uitgebreidere ondersteuning.

#### <mark style="color:blue;">**`Berichtlettergrootte`**</mark>：

Past tekstgrootte in chat aan.

### Invoerinstellingen

#### <mark style="color:blue;">**`Geschatte tokens tonen`**</mark>：

Toont geschat tokenverbruik in invoervak (indicatief, geen daadwerkelijke context).

#### <mark style="color:blue;">**`Lange tekst als bestand plakken`**</mark>：

Toont geplakte lange teksten als bestanden voor minder afleiding.

#### <mark style="color:blue;">**`Markdown weergave invoerberichten`**</mark>：

Renderen van verzonden berichten uitschakelen.

{% tabs %}
{% tab title="Uitgeschakeld" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ingeschakeld" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Driemaal spatie voor vertaling`**</mark>：

Vertaaal invoer naar Engels na driemaal spatie.

{% hint style="warning" %}
Waarschuwing: Overschrijdt originele tekst.
{% endhint %}

#### <mark style="color:blue;">**`Doeltaal`**</mark>：

Stelt doeltaal in voor vertaalknop en spatie-vertaling.

## Assistent-instellingen

Selecteer assistentnaam in assistentoverzicht → Rechtermuismenu → Instellingen

### Assistent bewerken

{% hint style="info" %}
Instellingen gelden voor alle onderwerpen onder deze assistent.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Promptinstellingen

#### <mark style="color:blue;">**`Naam`**</mark>：

Aanpasbare assistentnaam.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Promptinformatie (zie promptmethoden op agentenpagina).

#### Modelinstellingen

#### <mark style="color:blue;">**`Standaardmodel`**</mark>：

Stelt vaste standaardmodel in voor assistent. Zonder instelling wordt [globale standaardmodel](settings/default-models.md#mo-ren-zhu-shou-mo-xing) gebruikt.

{% hint style="info" %}
Prioriteit: Assistentmodel > globaal model. Ongeconfigureerd? Dan assistentmodel = globaal model.
{% endhint %}

#### <mark style="color:blue;">**`Model automatisch resetten`**</mark>：

Bij inschakeling: Na modelwissel wordt nieuw onderwerp teruggezet naar standaardmodel. Uitgeschakeld: Nieuwe onderwerpen behouden laatst gebruikte model.

> Voorbeeld (standaardmodel: gpt-3.5-turbo):
> - Met reset: Nieuw onderwerp gebruikt gpt-3.5-turbo
> - Zonder reset: Nieuw onderwerp behoudt gpt-4o

#### <mark style="color:blue;">**`Temperatuur (Temperature)`**</mark> ：

Regelt creativiteit (standaard: 0.7):
* Laag (0-0.3): Accuratere uitvoer (bv. code)
* Gemiddeld (0.4-0.7): Balans (aanbevolen voor chat)
* Hoog (0.8-1.0): Creatiever maar minder coherent

#### <mark style="color:blue;">**`Top P (Kernsteekproef)`**</mark>：

Standaard 1. Lagere waarden → voorspelbaarder, hogere waarden → diverser:
* Laag (0.1-0.3): Conservatief (bv. technische docs)
* Gemiddeld (0.4-0.6): Balans
* Hoog (0.7-1.0): Rijke expressie (bv. creatief schrijven)

{% hint style="info" %}
- Parametersonafhankelijk/combinatiebaar
- Experimenteer voor optimale instellingen
- Waardenindicatief (raadpleeg modelspecificaties)
{% endhint %}

#### <mark style="color:blue;">**`Contextvenster (Context Window)`**</mark>

Aantal berichten in context (meer tokens bij hogere waarden):
* 5-10: Standaard gesprekken
* >10: Complexe taken met lang geheugen
* Opmerking: Hogere waarden verhogen tokenverbruik

#### <mark style="color:blue;">**`Berichtlengtebeperking inschakelen (MaxToken)`**</mark>

Max tokens per antwoord. Beïnvloedt lengte en kwaliteit.

> Voorbeeld: Modelconnectiviteitstest vereist slechts 1 token.

Max limieten variëren per model (typisch 32k-64k+ tokens).

{% hint style="success" %}
Aanbevelingen:
* Chat: 500-800
* Korte tekst: 800-2000
* Code: 2000-3600
* Lange tekst: 4000+ (modelafhankelijk)
{% endhint %}

{% hint style="warning" %}
Antwoorden worden afgekapt bij MaxToken. Pas dynamisch aan bij afbreking.
{% endhint %}

#### <mark style="color:blue;">**`Streaming-uitvoer (Stream)`**</mark>

Real-time gegevensverwerking (type-machine-effect):
* Uit: Berichten in één keer verzonden
* Aan: Karakter-voor-karakter uitvoer

{% hint style="info" %}
Schakel uit voor niet-ondersteunende modellen (bv. o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Aangepaste parameters`**</mark>

Voegt extra verzoekparameters toe (bv. `presence_penalty`). Geavanceerd gebruik.

> Zie documentatie: [Klik hier](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Aangepaste parameters overschrijven standaardinstellingen
- Gebruik `<param>:undefined` om parameters uit te sluiten
- Modelleveranciers hebben unieke parameters
{% endhint %}