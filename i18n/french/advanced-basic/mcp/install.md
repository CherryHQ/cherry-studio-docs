# Installation de l'environnement MCP


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




**MCP (Model Context Protocol)** est un protocole open-source conçu pour fournir des informations contextuelles aux grands modèles de langage (LLM) de manière standardisée. Pour plus d'informations sur MCP, consultez [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Utilisation de MCP dans Cherry Studio

Voici un exemple avec la fonction `fetch` démontrant comment utiliser MCP dans Cherry Studio. Les détails complets sont disponibles dans la [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Prérequis : Installation de uv et bun**

{% hint style="warning" %}
Cherry Studio utilise actuellement uniquement les versions intégrées de [uv](https://github.com/astral-sh/uv) et [bun](https://github.com/oven-sh/bun), **sans réutiliser** les installations existantes de uv et bun sur votre système.
{% endhint %}

Dans `Paramètres → Serveurs MCP`, cliquez sur le bouton `Installer` pour télécharger et installer automatiquement. Le téléchargement direct depuis GitHub peut être lent et échouer fréquemment. L'installation est réussie si les fichiers apparaissent dans les dossiers mentionnés ci-dessous.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Répertoires d'installation des exécutables :**

- Windows : `C:\Users\Nom_utilisateur\.cherrystudio\bin`
- macOS/Linux : `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Répertoire bin</p></figcaption></figure>

**En cas d'échec d'installation :**

1. Créez manuellement le répertoire s'il n'existe pas.
2. Vous pouvez soit :
   - Créer des liens symboliques vers les commandes système existantes
   - Télécharger manuellement les exécutables aux liens ci-dessous et les placer dans le répertoire :
     - Bun : [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)
     - UV : [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)