---
icon: message
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Interface de Conversation

## Assistant et Sujets

### Assistant

`L'assistant` permet de personnaliser le modèle sélectionné via des paramètres tels que des prompts prédéfinis et des réglages de paramètres, afin de mieux répondre à vos attentes opérationnelles.

`L'assistant système par défaut` préconfigure des paramètres génériques (sans prompt). Vous pouvez l'utiliser directement ou trouver des préréglages adaptés dans la [page des agents](agents.md).

### Sujets

`L'assistant` est l'ensemble parent des `sujets`. Un assistant peut contenir plusieurs sujets (conversations). Tous les `sujets` partagent les paramètres et prompts de `l'assistant`.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Boutons de la boîte de dialogue

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nouveau sujet` Crée un nouveau sujet sous l'assistant actuel.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Télécharger une image ou un document` Nécessite un modèle prenant en charge les images. Les documents sont automatiquement convertis en texte comme contexte pour le modèle.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Recherche Web` Requiert une configuration dans les paramètres. Les résultats sont fournis au modèle comme contexte. Voir [Mode en ligne](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de connaissances` Active la base de connaissances. Voir [Tutoriel sur les bases de connaissances](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Serveur MCP` Active la fonctionnalité du serveur MCP. Voir [Tutoriel MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Générer une image` Non affiché par défaut. Pour les modèles prenant en charge la génération d'images (ex: Gemini), cliquez manuellement pour activer.

{% hint style="info" %}
Pour des raisons techniques, vous devez activer manuellement ce bouton pour générer des images. Il sera retiré après optimisation.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Choisir un modèle` Bascule vers un modèle spécifié pour la suite de la conversation, en conservant le contexte.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Phrases rapides` Définissez des phrases fréquentes dans les paramètres pour une insertion rapide, avec prise en charge des variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Effacer les messages` Supprime tous les contenus du sujet actuel.

![](../../.gitbook/assets/对话界面/展开.png) `Étendre` Agrandit la boîte de dialogue pour la saisie de textes longs.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Effacer le contexte` Réinitialise le contexte du modèle sans supprimer les contenus visibles.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimation des Tokens` Affiche : `Contexte actuel`, `Contexte maximal` (∞ = illimité), `Caractères saisis`, et `Tokens estimés`.

{% hint style="info" %}
Ceci est une estimation uniquement. Les Tokens réels varient selon les modèles.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduire` Traduit le contenu de la boîte de saisie en anglais.

## Paramètres de conversation

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Paramètres du modèle

Synchronisés avec les `Paramètres du modèle` de l'assistant. Voir [Paramètres de l'assistant](chat.md#paramètres-de-l'assistant).

{% hint style="info" %}
Seuls les paramètres du modèle s'appliquent à l'assistant actuel. Les autres paramètres sont globaux (ex: le style de messages en bulles s'applique à tous les sujets).
{% endhint %}

### Paramètres des messages

#### <mark style="color:blue;">**`Séparateur de messages`**</mark>:

Utilise une ligne pour séparer le contenu des messages des boutons d'action.

{% tabs %}
{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Utiliser des polices serif`**</mark>:

Change le style de police. Modifiable via [CSS personnalisé](../../personalization-settings/).

#### <mark style="color:blue;">**`Afficher les numéros de ligne`**</mark>:

Affiche les numéros de ligne pour les blocs de code générés.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocs de code pliables`**</mark>:

Plie automatiquement les blocs de code longs.

#### <mark style="color:blue;">**`Retour à la ligne dans les blocs de code`**</mark>:

Active le retour à la ligne automatique pour les lignes de code longues.

#### <mark style="color:blue;">**`Repli automatique des réflexions`**</mark>:

Replie automatiquement le processus de réflexion des modèles qui le supportent.

#### <mark style="color:blue;">**`Style des messages`**</mark>:

Bascule entre le style "bulles" ou "liste".

#### <mark style="color:blue;">**`Style du code`**</mark>:

Change le style d'affichage des blocs de code.

#### <mark style="color:blue;">**`Moteur de formules mathématiques`**</mark>:

* **KaTeX** : Rendu plus rapide, optimisé pour les performances.
* **MathJax** : Rendu plus lent mais prend en charge davantage de symboles et commandes.

#### <mark style="color:blue;">**`Taille de police des messages`**</mark>:

Ajuste la taille des polices dans l'interface.

### Paramètres de saisie

#### <mark style="color:blue;">**`Afficher l'estimation des Tokens`**</mark>:

Affiche les Tokens estimés pour le texte saisi (indication uniquement).

#### <mark style="color:blue;">**`Coller les longs textes comme fichiers`**</mark>:

Affiche les longs textes collés sous forme de fichiers pour réduire les interférences.

#### <mark style="color:blue;">**`Rendu Markdown des messages saisis`**</mark>:

Désactivé : Ne rend que les réponses du modèle. Activé : Rend aussi les messages envoyés.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduction par triple espace`**</mark>:

Traduit le contenu saisi en anglais après trois appuis sur la barre d'espace.

{% hint style="warning" %}
Attention : Cela remplace le texte original.
{% endhint %}

#### <mark style="color:blue;">**`Langue cible`**</mark>:

Définit la langue pour la traduction du bouton `Traduire` et du triple espace.

## Paramètres de l'assistant

Sélectionnez <mark style="background-color:yellow;">le nom de l'assistant</mark> → <mark style="background-color:yellow;">Menu contextuel</mark> → Paramètres correspondants

### Modifier l'assistant

{% hint style="info" %}
Les paramètres s'appliquent à tous les sujets sous cet assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Paramètres du prompt

#### <mark style="color:blue;">**`Nom`**</mark>:

Nom personnalisable pour identifier facilement l'assistant.

#### <mark style="color:blue;">**`Prompt`**</mark>:

Consultez les modèles dans la page des agents pour rédiger votre prompt.

#### Paramètres du modèle

#### <mark style="color:blue;">**`Modèle par défaut`**</mark>:

Définit un modèle par défaut pour l'assistant. Sinon, utilise le modèle global ([Modèle par défaut](settings/default-models.md#modèle-par-défaut)).

{% hint style="info" %}
Priorité : Modèle de l'assistant > Modèle global.
{% endhint %}

#### <mark style="color:blue;">**`Réinitialisation automatique du modèle`**</mark>:

Activé : Les nouveaux sujets utilisent le modèle par défaut de l'assistant. Désactivé : Ils conservent le modèle du dernier sujet.

> Exemple : Modèle par défaut = gpt-3.5-turbo. Pendant une conversation, bascule vers gpt-4o.
> * Activé → Nouveau sujet : gpt-3.5-turbo
> * Désactivé → Nouveau sujet : gpt-4o

#### <mark style="color:blue;">**`Température`**</mark>:

Contrôle la créativité des réponses (défaut: 0.7) :
* **Faible (0-0.3)** : Réponses précises. Idéal pour le code ou l'analyse.
* **Moyenne (0.4-0.7)** : Équilibre créativité/cohérence. Recommandé pour les discussions.
* **Élevée (0.8-1.0)** : Sorties créatives mais moins cohérentes.

#### <mark style="color:blue;">**`Top P (Noyau d'échantillonnage)`**</mark>:

Défaut: 1. Valeur basse = réponses prévisibles, haute = diversité lexicale.

Comportement :
* **Faible (0.1-0.3)** : Vocabulaire restreint. Bon pour la documentation technique.
* **Moyen (0.4-0.6)** : Équilibre diversité/précision.
* **Élevé (0.7-1.0)** : Réponses très diverses.

{% hint style="info" %}
- Ces paramètres peuvent être combinés
- Expérimentez pour trouver les réglages optimaux
- Ces plages sont indicatives. Consultez la documentation des modèles.
{% endhint %}

#### <mark style="color:blue;">**`Taille du contexte (fenêtre)`**</mark>

Nombre de messages conservés dans le contexte. Plus élevé = plus de Tokens consommés :
* **5-10** : Conversations standards
* **>10** : Tâches complexes nécessitant une mémoire étendue
* **Important** : Plus de messages = plus de Tokens

#### <mark style="color:blue;">**`Activer la limite de longueur (MaxToken)`**</mark>

Limite de Tokens par réponse. Ce paramètre impacte directement la longueur et qualité des réponses.

> Exemple : Pour tester la connectivité d'un modèle, MaxToken=1 suffit.

La plupart des modèles supportent 32k Tokens max (certains 64k+). À adapter selon les besoins :

{% hint style="success" %}
Recommandations :
* Discussions : 500-800
* Textes courts : 800-2000
* Génération de code : 2000-3600
* Textes longs : 4000+ (si modèle compatible)
{% endhint %}

{% hint style="warning" %}
Attention : Les réponses peuvent être tronquées si MaxToken est trop bas.
{% endhint %}

#### <mark style="color:blue;">**`Sortie en flux continu (Stream)`**</mark>

Envoie les réponses au fur et à mesure (effet "machine à écrire"). Désactivé : Réponse complète en une fois.

{% hint style="info" %}
Désactivez pour les modèles incompatibles (ex: o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Paramètres personnalisés`**</mark>

Ajoute des paramètres personnalisés à la requête (ex: `presence_penalty`). Documentation : [Cliquez ici](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Priorité sur les paramètres intégrés (les doublons sont écrasés)
- Utilisez `nom_paramètre:undefined` pour exclure un paramètre
- Certains fournisseurs ont des paramètres exclusifs
{% endhint %}