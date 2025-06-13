
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Installation automatique de MCP

> L'installation automatique de MCP nécessite Cherry Studio version v1.1.18 ou supérieure.

## Présentation des fonctionnalités

En plus de l'installation manuelle, Cherry Studio inclut l'outil `@mcpmarket/mcp-auto-install`, une méthode plus pratique pour installer le serveur MCP. Il vous suffit de saisir la commande appropriée dans le dialogue avec un modèle prenant en charge les services MCP.

{% hint style="warning" %}
**Rappel de phase de test :**

* `@mcpmarket/mcp-auto-install` est actuellement en phase de test
* L'efficacité dépend de "l'intelligence" du grand modèle : certains s'installent automatiquement, d'autres nécessitent **des ajustements manuels de paramètres dans les réglages MCP**
* Actuellement, la source de recherche est @modelcontextprotocol, configurable par l'utilisateur (détails ci-dessous)
{% endhint %}

## Mode d'emploi

Par exemple, vous pouvez saisir :

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Saisie de commande pour installer le serveur MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interface de configuration du serveur MCP</p></figcaption></figure>

Le système identifiera automatiquement vos besoins et effectuera l'installation via `@mcpmarket/mcp-auto-install`. Cet outil prend en charge différents types de serveurs MCP, notamment :

* filesystem (système de fichiers)
* fetch (requêtes réseau)
* sqlite (base de données)
* etc.

> La variable MCP_PACKAGE_SCOPES permet de personnaliser la source de recherche des services MCP. Valeur par défaut : `@modelcontextprotocol`.

## Présentation de la bibliothèque `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Référence de configuration par défaut :**

```json
// 'axun-uUpaWEdMEMU8C61K' est l'ID du service, personnalisez-le comme vous le souhaitez
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Installation automatique des services MCP (version bêta)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Voir https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` est un package npm open source. Consultez les détails et la documentation dans le [dépôt npm officiel](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` représente la collection officielle de services MCP de Cherry Studio.
{% endhint %}