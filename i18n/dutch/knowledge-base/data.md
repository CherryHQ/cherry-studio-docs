---
icon: database
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Dataopslagtoelichting

De gegevens die aan de Cherry Studio-kennisbank worden toegevoegd, worden volledig lokaal opgeslagen. Tijdens het toevoegen wordt een kopie van het document in de Cherry Studio-dataopslagmap geplaatst.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Stroomdiagram kennisbankverwerking</p></figcaption></figure>

Vectordatabase: [https://turso.tech/libsql](https://turso.tech/libsql)

Wanneer een document aan de Cherry Studio-kennisbank is toegevoegd, wordt het bestand opgesplitst in een aantal fragmenten. Deze fragmenten worden vervolgens door de embedding-model verwerkt.

Tijdens vraag-antwoordsessies met grote modellen worden relevante tekstfragmenten opgezocht en samen met de vraag aan het grote taalmodel doorgegeven.

Voor gevallen met strenge privacy-eisen wordt aanbevolen een lokale embedded database en lokaal groot taalmodel te gebruiken.