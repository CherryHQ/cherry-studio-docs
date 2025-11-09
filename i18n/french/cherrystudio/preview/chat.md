---
icon: message
---
# Interface de conversation


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Assistants et conversations

### Assistant

Un `assistant` permet de configurer des paramètres personnalisés pour le modèle sélectionné, tels que des prompts prédéfinis et des paramètres prédéfinis. Ces configurations permettent au modèle sélectionné de fonctionner conformément à vos attentes.

L'`assistant par défaut du système` propose des paramètres généraux prédéfinis (sans prompt). Vous pouvez l'utiliser directement ou rechercher les préréglages nécessaires dans la [page des agents](agents.md).

### Conversation

Un `assistant` est l'ensemble parent d'une `conversation`. Sous un assistant unique, vous pouvez créer plusieurs conversations (c'est-à-dire des dialogues). Toutes les `conversations` partagent les paramètres de l'`assistant`, les prompts prédéfinis et autres configurations du modèle.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Boutons dans la zone de dialogue

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nouvelle conversation` Crée une nouvelle conversation sous l'assistant actuel.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Télécharger une image ou un document` Le téléchargement d'images nécessite un modèle compatible. Le téléchargement de documents est automatiquement analysé en texte pour fournir le contexte au modèle.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Recherche web` Doit être configurée dans les paramètres. Les résultats de recherche sont renvoyés au modèle comme contexte. Voir [Mode connecté](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de connaissances` Active la base de connaissances. Voir [Tutoriel de la base de connaissances](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Serveur MCP` Active la fonctionnalité du serveur MCP. Voir [Tutoriel d'utilisation de MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Générer une image` Affiché uniquement lorsque le **modèle de conversation** sélectionné prend en charge la génération d'images. (Pour les modèles de génération d'images non conversationnels, rendez-vous sur [Dessin](./drawing.md))

![](../../.gitbook/assets/对话界面/选择模型.png) `Sélectionner un modèle` Permet de basculer vers le modèle spécifié pour les prochains dialogues, en conservant le contexte.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Phrases rapides` Doivent être prédéfinies dans les paramètres. Permet de les appeler directement dans le champ de saisie avec prise en charge des variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Effacer les messages` Supprime tout le contenu de cette conversation.

![](../../.gitbook/assets/对话界面/展开.png) `Développer` Agrandit la zone de dialogue pour faciliter la saisie de longs textes.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Effacer le contexte` Coupe le contexte accessible au modèle sans supprimer le contenu, ce qui signifie que le modèle "oubliera" les dialogues précédents.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Nombre estimé de tokens` Affiche le nombre estimé de tokens. Les quatre valeurs correspondent respectivement à : `Nombre de tokens actuel dans le contexte`, `Nombre maximum de tokens dans le contexte` (∞ signifie contexte illimité), `Nombre de caractères dans le champ de saisie actuel`, `Nombre estimé de tokens`.

{% hint style="info" %}
Cette fonctionnalité est uniquement une estimation. Le nombre réel de tokens varie selon les modèles. Consultez les données fournies par le fournisseur du modèle.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduire` Traduit le contenu actuel du champ de saisie en anglais.

## Paramètres de conversation

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Paramètres du modèle

Les paramètres du modèle sont synchronisés avec les paramètres `Paramètres du modèle` de l'assistant. Voir [Paramètres de l'assistant](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Dans les paramètres de conversation, seul ce paramètre du modèle s'applique à l'assistant actuel, tandis que les autres paramètres sont globaux. Par exemple, après avoir défini le style des messages en bulles, tous les assistants et conversations utiliseront ce style.
{% endhint %}

### Paramètres des messages

#### <mark style="color:blue;">**`Séparateur de messages`**</mark> :

Utilise un séparateur pour distinguer le corps du message de la barre d'actions.

{% tabs %}
{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Utiliser des polices à sérif`**</mark> :

Permet de basculer entre les styles de police. Vous pouvez également changer la police via [CSS personnalisée](../../personalization-settings/).

#### <mark style="color:blue;">**`Afficher les numéros de ligne`**</mark> :

Affiche les numéros de ligne lorsque le modèle génère des fragments de code.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocs de code repliables`**</mark> :

Lorsque cette option est activée, les blocs de code longs sont automatiquement repliés.

#### <mark style="color:blue;">**`Retour à la ligne dans les blocs de code`**</mark> :

Lorsque cette option est activée, les lignes de code dépassant la fenêtre sont automatiquement renvoyées à la ligne.

#### <mark style="color:blue;">**`Contenu de réflexion repliable`**</mark> :

Lorsque cette option est activée, les modèles prenant en charge la réflexion replient automatiquement le processus de réflexion après sa complétion.

#### <mark style="color:blue;">**`Style des messages`**</mark> :

Permet de basculer entre le style bulle et le style liste pour l'interface de conversation.

#### <mark style="color:blue;">**`Style des blocs de code`**</mark> :

Permet de modifier le style d'affichage des fragments de code.

#### <mark style="color:blue;">**`Moteur de formules mathématiques`**</mark> :

* KaTeX est plus rapide car conçu pour des performances optimisées.
* MathJax est plus lent mais offre plus de fonctionnalités et supporte davantage de symboles et commandes mathématiques.

#### <mark style="color:blue;">**`Taille de la police des messages`**</mark> :

Ajuste la taille de la police dans l'interface de conversation.

### Paramètres de saisie

#### <mark style="color:blue;">**`Afficher le nombre estimé de tokens`**</mark> :

Affiche dans le champ de saisie le nombre estimé de tokens consommés par le texte saisi (non indicatif du nombre réel de tokens du contexte).

#### <mark style="color:blue;">**`Coller les longs textes comme fichiers`**</mark> :

Lorsque des textes longs sont copiés depuis d'autres sources et collés dans le champ de saisie, ils s'affichent sous forme de fichier pour réduire les interférences avec les saisies ultérieures.

#### <mark style="color:blue;">**`Rendu Markdown des messages envoyés`**</mark> :

Lorsque désactivé, seul le rendu des réponses du modèle est appliqué, pas celui des messages envoyés.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Appuyer 3 fois sur espace pour traduire`**</mark> :

Après avoir saisi un message dans le champ de dialogue, appuyez rapidement 3 fois sur la barre d'espacement pour traduire le contenu en anglais.

{% hint style="warning" %}
Attention : cette opération écrasera le texte d'origine.
{% endhint %}

#### <mark style="color:blue;">**`Langue cible`**</mark> :

Définit la langue cible pour le bouton de traduction et pour l'option "appuyer 3 fois sur espace".

## Paramètres de l'assistant

Sélectionnez le nom de l'<mark style="background-color:yellow;">assistant</mark> à configurer dans l'interface de l'assistant → Sélectionnez les paramètres correspondants dans le <mark style="background-color:yellow;">menu contextuel</mark>.

### Modifier l'assistant

{% hint style="info" %}
Les paramètres de l'assistant s'appliquent à toutes les conversations sous cet assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Paramètres du prompt

#### <mark style="color:blue;">**`Nom`**</mark> :

Permet de définir un nom personnalisé pour identifier facilement l'assistant.

#### <mark style="color:blue;">**`Prompt`**</mark> :

Correspond au prompt. Vous pouvez vous inspirer des exemples de prompts sur la page des agents pour rédiger le contenu.

#### Paramètres du modèle

#### <mark style="color:blue;">**`Modèle par défaut`**</mark> :

Permet de fixer un modèle par défaut pour cet assistant. Lors de l'ajout depuis la page des agents ou de la copie d'un assistant, le modèle initial sera celui-ci. Si non défini, le modèle initial sera le modèle initial global (c'est-à-dire le [modèle par défaut de l'assistant](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
Il existe deux types de modèles par défaut pour l'assistant : le [modèle de conversation par défaut global](settings/default-models.md#mo-ren-zhu-shou-mo-xing) et le modèle par défaut de l'assistant. Le modèle par défaut de l'assistant a une priorité supérieure au modèle de conversation par défaut global. Lorsque le modèle par défaut de l'assistant n'est pas défini, il équivaut au modèle de conversation par défaut global.
{% endhint %}

#### <mark style="color:blue;">**`Réinitialiser automatiquement le modèle`**</mark> :

Activé : Lors de l'utilisation d'un autre modèle pendant cette conversation, la création d'une nouvelle conversation réinitialisera le modèle à celui par défaut de l'assistant. Désactivé : Le modèle de la nouvelle conversation suivra le modèle utilisé dans la conversation précédente.

> Exemple : Si le modèle par défaut de l'assistant est gpt-3.5-turbo, que je crée une conversation 1 sous cet assistant et que je bascule vers gpt-4o pendant la conversation :
>
> Si la réinitialisation automatique est activée : En créant une conversation 2, le modèle sélectionné par défaut sera gpt-3.5-turbo.
>
> Si la réinitialisation automatique est désactivée : En créant une conversation 2, le modèle sélectionné par défaut sera gpt-4o.

#### <mark style="color:blue;">**`Température (Temperature)`**</mark> :

Contrôle le niveau de créativité et d'aléatoire dans la génération du texte (valeur par défaut : 0,7). Se manifeste par :

* Valeurs basses (0-0,3) :
  * Sortie plus déterministe et concentrée
  * Adapté à la génération de code, à l'analyse de données, etc.
  * Privilégie les mots les plus probables
* Valeurs moyennes (0,4-0,7) :
  * Équilibre créativité et cohérence
  * Adapté aux dialogues quotidiens, rédaction générale
  * Recommandé pour les chatbots (autour de 0,5)
* Valeurs élevées (0,8-1,0) :
  * Sortie plus créative et diversifiée
  * Adapté à l'écriture créative, brainstorming, etc.
  * Peut réduire la cohérence du texte

#### <mark style="color:blue;">**`Top P (échantillonnage nucléaire)`**</mark> :

Valeur par défaut : 1. Une valeur plus petite rend le contenu généré plus monotone mais plus compréhensible ; une valeur plus grande élargit le vocabulaire utilisé par l'IA.

L'échantillonnage nucléaire influence la sortie via le seuil de probabilité de sélection des mots :

* Valeurs faibles (0,1-0,3) :
  * Ne considère que les mots de probabilité la plus élevée
  * Sortie plus conservatrice et contrôlée
  * Adapté aux commentaires de code, documentation technique, etc.
* Valeurs moyennes (0,4-0,6) :
  * Équilibre diversité et précision
  * Adapté aux dialogues et tâches d'écriture générales
* Valeurs élevées (0,7-1,0) :
  * Considère un éventail plus large de choix lexicaux
  * Génère du contenu plus riche et diversifié
  * Adapté à l'écriture créative nécessitant une expression variée

{% hint style="info" %}
- Ces deux paramètres peuvent être utilisés indépendamment ou combinés
- Choisissez les valeurs appropriées selon le type de tâche
- Testez pour trouver la combinaison optimale pour votre cas d'usage
- Les plages de valeurs données sont indicatives et peuvent ne pas convenir à tous les modèles. Référez-vous aux documents du modèle.
{% endhint %}

#### <mark style="color:blue;">**`Nombre de messages dans le contexte (Context Window)`**</mark>

Nombre de messages à conserver dans le contexte. Une valeur plus élevée signifie un contexte plus long et une consommation accrue de tokens :

* 5-10 : Adapté aux conversations ordinaires
* >10 : Tâches complexes nécessitant une mémoire plus longue (ex. : génération progressive de textes longs selon un plan, pour assurer la cohérence logique)
* > Remarque : Plus le nombre de messages est élevé, plus la consommation de tokens est importante

#### <mark style="color:blue;">**`Activer la limite de longueur des messages (MaxToken)`**</mark>

Nombre maximal de [tokens](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) pour une réponse. Dans les grands modèles linguistiques, max token est un paramètre clé influençant directement la qualité et la longueur des réponses.

> Exemple : Lors du test de connectivité d'un modèle dans CherryStudio après avoir saisi la clé, si vous souhaitez simplement vérifier si le modèle renvoie un message correct sans contenu spécifique, définissez MaxToken sur 1.

La plupart des modèles ont une limite MaxToken de 32k tokens, bien que certains atteignent 64k ou plus. Consultez la page de description du modèle pour plus de détails.

Le réglage dépend de vos besoins. Vous pouvez suivre ces suggestions :

{% hint style="success" %}
Suggestions :

* Conversation ordinaire : 500-800
* Génération de textes courts : 800-2000
* Génération de code : 2000-3600
* Génération de textes longs : 4000+ (nécessite un modèle compatible)
{% endhint %}

{% hint style="warning" %}
Normalement, les réponses générées par le modèle sont limitées à la valeur MaxToken. Cependant, des troncatures (comme lors de la rédaction de longs codes) ou des réponses incomplètes peuvent survenir. Ajustez selon les besoins.
{% endhint %}

#### <mark style="color:blue;">**`Sortie en streaming (Stream)`**</mark>

La sortie en streaming est une méthode de traitement de données permettant la transmission et le traitement continu plutôt qu'envoyer toutes les données d'un coup. Cela permet un traitement immédiat dès la génération des données, améliorant considérablement le temps réel et l'efficacité.

Dans CherryStudio et des environnements similaires, cela correspond à l'effet machine à écrire.

Désactivé (non streaming) : Le modèle génère l'ensemble du message avant de l'afficher (comme un message reçu sur WeChat).

Activé : Affichage caractère par caractère, comme si le modèle envoyait chaque caractère dès sa génération.

{% hint style="info" %}
Désactivez ce paramètre pour les modèles ne prenant pas en charge le streaming, comme **initialement** o1-mini.
{% endhint %}

#### <mark style="color:blue;">**`Paramètres personnalisés`**</mark>

Ajoute des paramètres supplémentaires dans le corps de la requête (body), comme les champs `presence_penalty`, etc. Rarement utilisés par les utilisateurs standard.

> Les paramètres mentionnés ci-dessus (top-p, maxtokens, stream, etc.) font partie de ces paramètres.

Format : Nom du paramètre — Type de paramètre (texte, nombre, etc.) — Valeur. Référence : [Cliquez ici](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Les fournisseurs de modèles ont souvent des paramètres spécifiques. Consultez leur documentation pour savoir comment les utiliser.
{% endhint %}

{% hint style="info" %}
* Les paramètres personnalisés ont une priorité supérieure aux paramètres intégrés. Si un paramètre personnalisé entre en conflit avec un paramètre intégré, il le remplace.

> Exemple : Si vous définissez `model` sur `gpt-4o` dans les paramètres personnalisés, le modèle `gpt-4o` sera utilisé quelle que soit le modèle sélectionné en conversation.

* Utilisez le format <kbd>Nom du paramètre:undefined</kbd> pour exclure un paramètre.
{% endhint %}