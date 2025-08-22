# Installation de l'environnement MCP


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




**MCP (Model Context Protocol)** est un protocole open source conçu pour fournir des informations contextuelles aux grands modèles de langage (LLM) de manière standardisée. Pour plus d'informations sur MCP, voir [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Utilisation de MCP dans Cherry Studio

Prenons l'exemple de la fonction `fetch` pour démontrer comment utiliser MCP dans Cherry Studio. Les détails sont disponibles dans la [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Préparation : installation d'uv et bun**

{% hint style="warning" %}
Cherry Studio utilise exclusivement [uv](https://github.com/astral-sh/uv) et [bun](https://github.com/oven-sh/bun) intégrés, **sans réutiliser** les versions préinstallées sur le système.
{% endhint %}

Dans `Paramètres → Serveur MCP`, cliquez sur `Installer` pour télécharger et installer automatiquement. Comme le téléchargement s'effectue directement depuis GitHub, la vitesse peut être lente et des échecs sont probables. La réussite de l'installation se vérifie par la présence de fichiers dans les dossiers mentionnés ci-dessous.

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Répertoire d'installation des exécutables :**  
Windows : `C:\Users\Nom_utilisateur\.cherrystudio\bin`  
macOS/Linux : `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Répertoire bin</p></figcaption></figure>

**En cas d'échec d'installation :**  
Vous pouvez créer des liens symboliques vers les commandes système dans ce répertoire. Si le dossier n'existe pas, créez-le manuellement. Vous pouvez également télécharger manuellement les exécutables :  
Bun : [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)  
UV : [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)