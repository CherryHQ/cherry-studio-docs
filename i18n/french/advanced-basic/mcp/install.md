
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Installation de l'environnement MCP

**MCP (Model Context Protocol)** est un protocole open source conçu pour fournir des informations contextuelles aux modèles de langage à grande échelle (LLM) de manière standardisée. Pour plus de détails sur le MCP, consultez [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Utilisation de MCP dans Cherry Studio

Voici un exemple avec la fonction `fetch` pour illustrer l'utilisation de MCP dans Cherry Studio. Les détails complets sont disponibles dans la [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Préparation : installation d'uv et bun**

{% hint style="warning" %}
Cherry Studio utilise actuellement exclusivement [uv](https://github.com/astral-sh/uv) et [bun](https://github.com/oven-sh/bun) intégrés, **sans réutiliser** les versions déjà installées sur votre système.
{% endhint %}

Dans `Paramètres > Serveur MCP`, cliquez sur le bouton `Installer` pour télécharger et installer automatiquement. Comme le téléchargement s'effectue directement depuis GitHub, il peut être lent et présente un risque élevé d'échec. L'installation réussie est confirmée par la présence de fichiers dans les répertoires mentionnés ci-dessous.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Répertoires d'installation des exécutables :**

Windows: `C:\Users\<nom_utilisateur>\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Répertoire bin</p></figcaption></figure>

**En cas d'échec d'installation :**

Vous pouvez créer des liens symboliques (soft links) vers les commandes correspondantes de votre système dans ce répertoire. Si le répertoire n'existe pas, créez-le manuellement. Vous pouvez également télécharger manuellement les exécutables :

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)