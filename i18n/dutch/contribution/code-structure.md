---
hidden: True
icon: code
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Code Structuur

```yaml
...
├─ docs/ #documentatiemap
├─ resources/ #resourcebestandenmap
├─ scripts/ #scriptbestandenmap
└─ src/ #hoofdbroncodemap
    ├─main/ #hoofdprocescode
    ├─preload/ #preloadscriptmap
    └─renderer/ #renderprocescode
        ├─src/ #broncode van renderproces
            ├─assets/ #resourcebestanden
                ├─fonts/ #lettertypebestanden
                ├─images/ #afbeeldingsbestanden (zoals avatars)
                └─styles/ #stijlbestanden
            ├─components/ #componenten
            ├─config/ #configuratiebestanden
            ├─context/ #context
            ├─databases/ #databasegerelateerde bestanden
            ├─hooks/ #aangepaste Hooks
            ├─i18n/ #internationaliseringsbestanden
            ├─pages/ #paginabestanden
            ├─providers/ #providergerelateerde configuratie
            ├─services/ #servicebestanden
            ├─store/ #statushanteringsbestanden
            ├─types/ #TypeScript typedefinitiebestanden
            ├─utils/ #hulpfuncties
            ...
        ...
    ...
...
...
```