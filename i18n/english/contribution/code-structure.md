---
hidden: True
icon: code
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Code Structure

```yaml
...
├─ docs/ #Documentation directory
├─ resources/ #Resource file directory
├─ scripts/ #Script file directory
└─ src/ #Main source code directory
    ├─main/ #Main process code
    ├─preload/ #Preload script directory
    └─renderer/ #Renderer process code
        ├─src/ #Renderer process source code
            ├─assets/ #Resource files
                ├─fonts/ #Font files
                ├─images/ #Image files such as avatars
                └─styles/ #Style files
            ├─components/ #Components
            ├─config/ #Configuration files
            ├─context/ #Context
            ├─databases/ #Database related files
            ├─hooks/ #Custom Hooks
            ├─i18n/ #Internationalization files
            ├─pages/ #Page files
            ├─providers/ #Provider related configurations
            ├─services/ #Service files
            ├─store/ #State management files
            ├─types/ #TypeScript type definition files
            ├─utils/ #Utility functions
            ...
        ...
    ...
...

```