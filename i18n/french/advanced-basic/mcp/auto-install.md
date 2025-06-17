
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Installation Automatique de MCP

> L'installation automatique de MCP nécessite de mettre à jour Cherry Studio vers la version v1.1.18 ou ultérieure.

## Présentation de la Fonctionnalité

En plus de l'installation manuelle, Cherry Studio intègre un outil `@mcpmarket/mcp-auto-install`, qui offre un moyen plus pratique d'installer le serveur MCP. Il suffit de saisir la commande appropriée dans le dialogue d'un grand modèle prenant en charge le service MCP.

{% hint style="warning" %}
**Rappel de la phase de test :**

* `@mcpmarket/mcp-auto-install` est actuellement toujours en phase de test
* L'efficacité dépend du "QI" du grand modèle : certains ajoutent automatiquement, d'autres nécessitent **encore des modifications manuelles de paramètres dans les paramètres MCP**
* Actuellement, la source de recherche est `@modelcontextprotocol`, mais vous pouvez la configurer vous-même (voir ci-dessous)
{% endhint %}

## Mode d'emploi

Par exemple, vous pouvez saisir :

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Saisir la commande pour installer le serveur MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interface de configuration du serveur MCP</p></figcaption></figure>

Le système reconnaîtra automatiquement vos besoins et effectuera l'installation via `@mcpmarket/mcp-auto-install`. Cet outil prend en charge plusieurs types de serveurs MCP, notamment :

* filesystem (système de fichiers)
* fetch (requête réseau)
* sqlite (base de données)
* etc.

> La variable `MCP_PACKAGE_SCOPES` permet de personnaliser la source de recherche du service MCP. La valeur par défaut est `@modelcontextprotocol`, configurable selon vos besoins.

## Présentation de la Bibliothèque `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Référence de configuration par défaut :**

```json
// `axun-uUpaWEdMEMU8C61K` est l'ID du service, personnalisable à volonté
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Installer automatiquement les services MCP (version bêta)",
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
    "MCP_REGISTRY_PATH": "Voir les détails sur https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` est un package npm open source. Vous pouvez consulter ses détails et sa documentation dans le [dépôt officiel npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` représente la collection officielle de services MCP de Cherry Studio.
{% endhint %}