---
icon: message
---
# Interface de conversation


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Assistants et sujets

### Assistant

L'**Assistant** permet de personnaliser les paramètres du modèle sélectionné pour l'utiliser, comme les préréglages de prompts et de paramètres. Ces réglages permettent d'aligner le modèle sur vos attentes de travail.

L'**Assistant par défaut du système** contient des paramètres génériques (sans prompt). Vous pouvez l'utiliser directement ou chercher des préréglages adaptés dans la [page des agents](agents.md).

### Sujets

L'**Assistant** est le parent des **Sujets**. Un assistant unique peut créer plusieurs sujets (conversations). Tous les sujets partagent les mêmes paramètres et prompts de l'assistant.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Boutons de la zone de dialogue

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) **Nouveau sujet** Crée un nouveau sujet dans l'assistant actuel.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) **Importer image ou document**  
- Images : nécessitent une prise en charge par le modèle  
- Documents : analysés automatiquement en texte comme contexte pour le modèle.

![](../../.gitbook/assets/对话界面/网络搜索.png) **Recherche web** Configurez d'abord les paramètres dans les réglages. Les résultats alimentent le contexte du modèle. Voir [Mode connecté](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) **Base de connaissances** Active la base de connaissances. Voir [Tutoriel base de connaissances](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) **Serveur MCP** Active la fonctionnalité de serveur MCP. Voir [Guide MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) **Générer une image** Non affiché par défaut. Pour les modèles compatibles (ex : Gemini), activez manuellement pour générer des images.

{% hint style="info" %}
Pour des raisons techniques, vous devez activer manuellement ce bouton pour générer des images. Il sera retiré après optimisation.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) **Choisir un modèle** Change le modèle pour les réponses suivantes tout en conservant le contexte.

![](../../.gitbook/assets/对话界面/快捷短语.png) **Phrases rapides** Utilisez des phrases prédéfinies dans les réglages. Supporte les variables.

![](../../.gitbook/assets/对话界面/清空消息.png) **Effacer les messages** Supprime tout le contenu du sujet actuel.

![](../../.gitbook/assets/对话界面/展开.png) **Agrandir** Agrandit la zone de dialogue pour les longs textes.

![](../../.gitbook/assets/对话界面/清除上下文.png) **Effacer le contexte** Réinitialise le contexte du modèle sans supprimer le contenu ("oubli" des conversations précédentes).

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) **Estimation Tokens** Affiche :  
- `Contexte actuel`  
- `Contexte max` (∞ = illimité)  
- `Caractères saisis`  
- `Tokens estimés`

{% hint style="info" %}
Cette estimation est indicative. Les Tokens réels varient selon les modèles. Consultez les données du fournisseur.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) **Traduire** Traduit le contenu actuel en anglais.

## Paramètres de conversation

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Paramètres du modèle

Synchronisés avec les `Paramètres du modèle` des paramètres de l'assistant. Voir [Édition de l'assistant](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Seuls ces paramètres de modèle s'appliquent à l'assistant actuel. Les autres paramètres sont globaux (ex : style de bulles appliqué à tous les sujets).
{% endhint %}

### Paramètres des messages

#### <mark style="color:blue;">**`Séparateur de messages`**</mark> :

Ajoute une ligne de séparation entre le contenu et les actions.

{% tabs %}
{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Utiliser les polices serif`**</mark> :

Change le style de police. Personnalisation via [CSS personnalisé](../../personalization-settings/).

#### <mark style="color:blue;">**`Afficher les numéros de ligne des blocs de code`**</mark> :

Affiche les numéros de ligne pour les extraits de code.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocs de code repliables`**</mark> :

Replie automatiquement les blocs de code longs.

#### <mark style="color:blue;">**`Retour à la ligne dans les blocs de code`**</mark> :

Retourne à la ligne automatiquement pour les longues lignes de code.

#### <mark style="color:blue;">**`Repli automatique des processus de réflexion`**</mark> :

Replie automatiquement le raisonnement des modèles après réflexion.

#### <mark style="color:blue;">**`Style des messages`**</mark> :

Bulle de discussion ou style liste.

#### <mark style="color:blue;">**`Thème des blocs de code`**</mark> :

Change le style d'affichage des extraits de code.

#### <mark style="color:blue;">**`Moteur de formules mathématiques`**</mark> :

* **KaTeX** : Rendu rapide (optimisé performance)
* **MathJax** : Rendu lent mais complet (plus de symboles)

#### <mark style="color:blue;">**`Taille de police des messages`**</mark> :

Ajuste la taille du texte.

### Paramètres de saisie

#### <mark style="color:blue;">**`Afficher l'estimation de Tokens`**</mark> :

Affiche les Tokens estimés pour le texte saisi (indicatif).

#### <mark style="color:blue;">**`Coller les longs textes en tant que fichier`**</mark> :

Transforme les longs textes collés en fichiers pour éviter les interférences.

#### <mark style="color:blue;">**`Rendu Markdown pour les messages entrants`**</mark> :

Désactivé : Ne rend que les réponses du modèle.  
Activé : Rend aussi les messages envoyés.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure