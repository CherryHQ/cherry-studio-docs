---
icon: cloud-check
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Provider Instellingen

Deze pagina dient alleen ter introductie van de interfacefunctionaliteiten. Voor configuratietutorials raadpleeg de [Providerconfiguratie](../../../pre-basic/providers/) tutorial in de basiscursus.

{% hint style="info" %}
* Bij gebruik van ingebouwde providers hoeft u alleen de bijbehorende sleutel in te vullen.
* Verschillende providers gebruiken mogelijk verschillende termen voor sleutels: sleutel, key, API key of token verwijzen allemaal naar hetzelfde.
{% endhint %}

### API-sleutel

In Cherry Studio ondersteunt een enkele provider meerdere sleutels voor round-robin gebruik, waarbij de volgorde van de lijst wordt gevolgd.

* Voer meerdere sleutels toe met Engelse komma's ertussen, zoals in dit voorbeeld:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Gebruik **verplicht** Engelse komma's.
{% endhint %}

### API-adres

Bij ingebouwde providers hoeft u meestal geen API-adres in te vullen. Volg bij aanpassing exact de officiële documentatie van de provider.

> Als het adres van een provider dit formaat heeft: <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark><br>
> Vul dan alleen het basisadres in (<mark style="background-color:red;">https://xxx.xxx.com</mark>).<br>
> Cherry Studio voegt automatisch het pad toe (<mark style="background-color:green;">/v1/chat/completions</mark>). Onjuiste invoer kan tot fouten leiden.

{% hint style="info" %}
**Toelichting**: De meeste providers gebruiken een uniform modelpad. Bij afwijkende paden (bv. v2/ of v3/chat/completions):
* Eindig het adres met `/` om automatisch "<mark style="background-color:green;">chat/completions</mark>" toe te voegen
* Eindig met `#` om het volledige adres handmatig te gebruiken

Voorbeeldregels:<br>
![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Modellen toevoegen

Klik op de `Beheren` knop linksonder in het providerconfiguratiescherm om alle beschikbare modellen op te halen. Voeg modellen toe door op `+` bij het gewenste model te klikken.

{% hint style="info" %}
Modellen worden pas zichtbaar in de selectielijst na toevoeging via de `+` knop in het beheerscherm.
{% endhint %}

### Connectiviteitstest

Klik op het testicoon naast het API-sleutelveld om de configuratie te controleren.

{% hint style="info" %}
De test gebruikt standaard het laatste dialoogmodel in de lijst. Controleer bij fouten of er ongeldige modellen zijn toegevoegd.
{% endhint %}

{% hint style="danger" %}
Schakel na succesvolle configuratie **verplicht** de schakelaar rechtsboven in. Zonder activering zijn de modellen niet beschikbaar.
{% endhint %}