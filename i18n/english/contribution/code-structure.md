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
├─ docs/ # Documentation directory
├─ resources/ # Resource files directory
├─ scripts/ # Script files directory
└─ src/ # Main source code directory
    ├─main/ # Main process code
    ├─preload/ # Preload scripts directory
    └─renderer/ # Renderer process code
        ├─src/ # Renderer process source code
            ├─assets/ # Asset files
                ├─fonts/ # Font files
                ├─images/ # Avatar and image files
                └─styles/ # Style files
            ├─components/ # Components
            ├─config/ # Configuration files
            ├─context/ # Context
            ├─databases/ # Database-related files
            ├─hooks/ # Custom Hooks
            ├─i18n/ # Internationalization files
            ├─pages/ # Page files
            ├─providers/ # Provider configurations
            ├─services/ # Service files
            ├─store/ # State management files
            ├─types/ # TypeScript type definitions
            ├─utils/ # Utility functions
            ...
        ...
    ...
...
```