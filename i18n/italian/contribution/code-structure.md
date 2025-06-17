---
hidden: True
icon: code
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Struttura del Codice

```yaml
...
├─ docs/ # directory della documentazione
├─ resources/ # directory dei file di risorse
├─ scripts/ # directory degli script
└─ src/ # directory principale del codice sorgente
    ├─main/ # codice del processo principale
    ├─preload/ # directory degli script di precaricamento
    └─renderer/ # codice del processo di rendering
        ├─src/ # codice sorgente del processo di rendering
            ├─assets/ # file di risorse
                ├─fonts/ # file dei font
                ├─images/ # file di immagini (avatar, ecc.)
                └─styles/ # file di stile
            ├─components/ # componenti
            ├─config/ # file di configurazione
            ├─context/ # contesto
            ├─databases/ # file relativi al database
            ├─hooks/ # hooks personalizzati
            ├─i18n/ # file di internazionalizzazione
            ├─pages/ # file delle pagine
            ├─providers/ # configurazione relativa ai provider
            ├─services/ # file dei servizi
            ├─store/ # file di gestione dello stato
            ├─types/ # file di definizione dei tipi TypeScript
            ├─utils/ # funzioni di utilità
            ...
        ...
    ...
...
```