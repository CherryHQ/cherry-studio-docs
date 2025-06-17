
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuration MCP Intégrée

### @cherry/mcp-auto-install  
Installation automatique du service MCP (version bêta)

### @cherry/memory  
Implémentation de base de mémoire persistante basée sur des graphes de connaissances locaux. Permet au modèle de retenir les informations utilisateur entre différentes conversations.

```typescript
MEMORY_FILE_PATH=/chemin/vers/votre/fichier.json
```

### @cherry/sequentialthinking  
Implémentation d'un serveur MCP fournissant des outils pour la résolution dynamique et réflexive de problèmes via des processus de pensée structurés.

### @cherry/brave-search  
Implémentation d'un serveur MCP intégrant l'API de recherche Brave, offrant une double fonctionnalité de recherche web et locale.

```typescript
BRAVE_API_KEY=VOTRE_CLÉ_API
```

### @cherry/fetch  
Serveur MCP pour récupérer le contenu de pages web via des URL.

### @cherry/filesystem  
Serveur Node.js implémentant le protocole de contexte de modèle (MCP) pour les opérations de système de fichiers.