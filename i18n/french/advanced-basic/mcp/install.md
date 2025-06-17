
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Installation de l'environnement MCP

**MCP (Model Context Protocol)** est un protocole open source conçu pour fournir des informations contextuelles aux grands modèles de langage (LLM) de manière standardisée. Pour plus d'informations sur MCP, consultez [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Utilisation de MCP dans Cherry Studio

L'exemple suivant utilise la fonction `fetch` pour démontrer comment utiliser MCP dans Cherry Studio. Pour plus de détails, consultez la [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Préparation : installation de uv et bun**

{% hint style="warning" %}
Actuellement, Cherry Studio n'utilise que [uv](https://github.com/astral-sh/uv) et [bun](https://github.com/oven-sh/bun) intégrés, **sans réutiliser** les versions déjà installées sur votre système.
{% endhint %}

Dans `Paramètres → Serveur MCP`, cliquez sur le bouton `Installer` pour un téléchargement et une installation automatiques. Étant donné que le téléchargement se fait directement depuis GitHub, il peut être lent et présenter un taux d'échec élevé. Le succès de l'installation dépend de la présence de fichiers dans les répertoires mentionnés ci-dessous.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Répertoire d'installation des exécutables :**

Windows: `C:\Users\Nom d'utilisateur\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Répertoire bin</p></figcaption></figure>

**Si l'installation échoue :**

Créez des liens symboliques des commandes système vers ces répertoires. Si les répertoires n'existent pas, créez-les manuellement. Vous pouvez également télécharger manuellement les exécutables :

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)