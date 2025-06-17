
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# GitHub Copilot

Om GitHub Copilot te gebruiken, moet je eerst een GitHub-account hebben en een abonnement op de GitHub Copilot-service nemen. Het gratis abonnement is mogelijk, maar de gratis versie ondersteunt niet het nieuwste Claude 3.7-model. Raadpleeg voor details de [officiële GitHub Copilot-website](https://github.com/features/copilot).

## Device Code verkrijgen

Klik op "Aanmelden bij GitHub" om een Device Code te verkrijgen en kopieer deze.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Voorbeeldafbeelding van Device Code verkrijgen"><figcaption><p>Device Code verkrijgen</p></figcaption></figure>

## Device Code invullen en toestemming verlenen in browser

Nadat je de Device Code hebt verkregen, klik je op de link om de browser te openen. Meld je aan bij je GitHub-account in de browser, voer de Device Code in en verleen toestemming.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Voorbeeldafbeelding GitHub-toestemming"><figcaption><p>GitHub-toestemming</p></figcaption></figure>

Na succesvolle autorisatie keer je terug naar Cherry Studio en klik je op "Verbinden met GitHub". Bij succes worden je GitHub-gebruikersnaam en avatar weergegeven.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Voorbeeldafbeelding geslaagde GitHub-verbinding"><figcaption><p>GitHub-verbinding succesvol</p></figcaption></figure>

## Modelijst ophalen via "Beheren"

Klik op de knop "Beheren" hieronder. Deze haalt automatisch de lijst met momenteel ondersteunde modellen op via internet.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Voorbeeldafbeelding modelijst ophalen"><figcaption><p>Modelijst ophalen</p></figcaption></figure>

## Veelgestelde vragen

### Device Code verkrijgen mislukt, probeer opnieuw

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Voorbeeldafbeelding mislukte Device Code-verkrijging"><figcaption><p>Device Code verkrijgen mislukt</p></figcaption></figure>

Momenteel worden verzoeken gebouwd met Axios. Axios ondersteunt geen SOCKS-proxy. Gebruik een systeemproxy of HTTP-proxy, of stel helemaal geen proxy in CherryStudio in en gebruik een globale proxy. Zorg er eerst voor dat uw netwerkverbinding normaal is om mislukte Device Code-verkrijging te voorkomen.