
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuration MCP intégrée

### @cherry/mcp-auto-install

Installation automatique du service MCP (version bêta)

### @cherry/memory

Implémentation de base de mémoire persistante basée sur un graphe de connaissances local. Cela permet au modèle de mémoriser les informations pertinentes de l'utilisateur entre différentes conversations.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Implémentation d'un serveur MCP fournissant des outils pour la résolution dynamique et réflexive de problèmes grâce à un processus de pensée structuré.

### @cherry/brave-search

Implémentation d'un serveur MCP intégrant l'API de recherche Brave, offrant une double fonctionnalité de recherche web et locale.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Serveur MCP pour récupérer le contenu de pages web via URL.

### @cherry/filesystem

Serveur Node.js implémentant le protocole de contexte de modèle (MCP) pour les opérations sur le système de fichiers.