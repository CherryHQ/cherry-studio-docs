---
hidden: True
icon: code
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Code Struktur

```yaml
...
├─ docs/ #Dokumentationsverzeichnis
├─ resources/ #Ressourcenverzeichnis
├─ scripts/ #Skriptverzeichnis
└─ src/ #Hauptquellcode-Verzeichnis
    ├─main/ #Hauptprozess-Code
    ├─preload/ #Preload-Skriptverzeichnis
    └─renderer/ #Renderer-Prozesscode
        ├─src/ #Quellcode des Renderers
            ├─assets/ #Ressourcen
                ├─fonts/ #Schriftdateien
                ├─images/ #Bilddateien (Avatare, etc.)
                └─styles/ #Stildateien
            ├─components/ #Komponenten
            ├─config/ #Konfiguration
            ├─context/ #Kontext
            ├─databases/ #Datenbankbezogene Dateien
            ├─hooks/ #Benutzerdefinierte Hooks
            ├─i18n/ #Internationalisierung
            ├─pages/ #Seiten
            ├─providers/ #Anbieterbezogene Konfiguration
            ├─services/ #Dienste
            ├─store/ #Zustandsmanagement
            ├─types/ #TypeScript-Typdefinitionen
            ├─utils/ #Hilfsfunktionen
            ...
        ...
    ...
...
```