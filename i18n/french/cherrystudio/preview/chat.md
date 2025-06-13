---
icon: message
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

---
icon: cherries
---

# Interface de conversation

## Assistants et sujets

### Assistant

L'`assistant` personnalise les paramètres du modèle sélectionné (comme les préréglages de prompts et de paramètres) pour adapter le modèle à vos tâches spécifiques.

L'`assistant par défaut du système` dispose de paramètres génériques (sans prompt). Vous pouvez l'utiliser directement ou trouver des préréglages sur la [page Agents](agents.md).

### Sujet

L'`assistant` est un ensemble parent des `sujets`. Un même assistant peut créer plusieurs sujets (conversations), tous partageant les mêmes paramètres et préréglages (prompts) de l'assistant.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Boutons de la boîte de dialogue

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nouveau sujet` Crée un nouveau sujet sous l'assistant actuel.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Importer image ou document` Les images nécessitent un modèle compatible. Les documents sont automatiquement analysés en texte comme contexte pour le modèle.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Recherche web` Nécessite une configuration préalable. Les résultats sont fournis comme contexte au modèle. Voir [Mode connecté](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de connaissances` Active la base de connaissances. Voir [Tutoriel base de connaissances](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Serveur MCP` Active la fonction de serveur MCP. Voir [Tutoriel MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Générer des images` Masqué par défaut. Pour les modèles compatibles (ex: Gemini), doit être activé manuellement.

{% hint style="info" %}
Pour des raisons techniques, vous devez l'activer manuellement. Ce bouton sera supprimé après optimisation.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Sélectionner un modèle` Change le modèle pour les réponses suivantes en conservant le contexte.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Phrases rapides` Utilise des phrases prédéfinies dans les paramètres. Prend en charge les variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Effacer les messages` Supprime tout le contenu du sujet.

![](../../.gitbook/assets/对话界面/展开.png) `Développer` Agrandit la zone de saisie pour les longs textes.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Effacer le contexte` Limite le contexte visible par le modèle sans supprimer l'historique.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimation de Tokens` Affiche : `Contexte actuel`, `Contexte max` (∞ = illimité), `Messages en cours`, `Tokens estimés`.

{% hint style="info" %}
Estimation indicative. Les Tokens réels varient selon les modèles. Consultez les données du fournisseur.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduire` Traduit le contenu actuel en anglais.

## Paramètres de conversation

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Paramètres du modèle

Synchronisés avec `Paramètres du modèle` dans les paramètres d'assistant. Voir [Éditer l'assistant](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Ici, seul le paramètre de modèle s'applique à l'assistant actuel. Les autres sont globaux (ex: le style de message reste identique partout).
{% endhint %}

### Paramètres des messages

#### <mark style="color:blue;">**`Ligne de séparation des messages`**</mark> :

Ajoute un séparateur entre le contenu et les options.

{% tabs %}
{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Police sérif`**</mark> :
Change le style de police. Modifiable via [CSS personnalisé](../../personalization-settings/).

#### <mark style="color:blue;">**`Numérotation des lignes dans le code`**</mark> :
Affiche les numéros de ligne dans les blocs de code.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocs de code repliables`**</mark> :
Replie automatiquement les longs blocs de code.

#### <mark style="color:blue;">**`Retour à la ligne dans le code`**</mark> :
Revient à la ligne dans les longues lignes de code.

#### <mark style="color:blue;">**`Repli automatique du raisonnement`**</mark> :
Replie automatiquement les étapes de réflexion des modèles.

#### <mark style="color:blue;">**`Style des messages`**</mark> :
Bulles ou liste.

#### <mark style="color:blue;">**`Style de code`**</mark> :
Change l'apparence des blocs de code.

#### <mark style="color:blue;">**`Moteur de formules mathématiques`**</mark> :
* **KaTeX** : Plus rapide, optimisé pour la performance.
* **MathJax** : Plus complet mais plus lent, supporte plus de symboles.

#### <mark style="color:blue;">**`Taille de la police`**</mark> :
Ajuste la taille du texte dans l'interface.

### Paramètres de saisie

#### <mark style="color:blue;">**`Afficher l'estimation de Tokens`**</mark> :
Montre les Tokens estimés pour le texte saisi (indicatif uniquement).

#### <mark style="color:blue;">**`Coller les longs textes en tant que fichiers`**</mark> :
Transforme les longs textes collés en fichier pour éviter les interférences.

#### <mark style="color:blue;">**`Rendu Markdown des messages entrants`**</mark> :
Désactivé = rendu Markdown uniquement pour les réponses du modèle.

{% tabs %}
{% tab title="Désactivé" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activé" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduction par triple espace`**</mark> :
Traduit le texte après trois espaces consécutifs.

{% hint style="warning" %}
Attention : Remplace le texte original.
{% endhint %}

#### <mark style="color:blue;">**`Langue cible`**</mark> :
Définit la langue pour le bouton de traduction et la triple espace.

## Paramètres de l'assistant

Cliquez sur <mark style="background-color:yellow;">le nom de l'assistant</mark> → <mark style="background-color:yellow;">Menu contextuel</mark> → Paramètres.

### Modifier l'assistant

{% hint style="info" %}
S'applique à tous les sujets de cet assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Paramètres de prompt

#### <mark style="color:blue;">**`Nom`**</mark> :
Nom personnalisé pour identifier l'assistant.

#### <mark style="color:blue;">**`Prompt`**</mark> :
Consultez la page Agents pour des exemples de rédaction.

#### Paramètres du modèle

#### <mark style="color:blue;">**`Modèle par défaut`**</mark> :
Modèle fixe pour cet assistant. Si non défini, utilise le modèle global ([Modèle par défaut](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
Priorité : Modèle de l'assistant > Modèle global.
{% endhint %}

#### <mark style="color:blue;">**`Réinitialisation automatique du modèle`**</mark> :
Activé = les nouveaux sujets utilisent le modèle par défaut de l'assistant. Désactivé = réutilise le dernier modèle utilisé.

> **Exemple** :  
> Modèle par défaut : gpt-3.5-turbo  
> Dans un sujet, vous passez à gpt-4o.  
> - Activé : Nouveau sujet → gpt-3.5-turbo  
> - Désactivé : Nouveau sujet → gpt-4o

#### <mark style="color:blue;">**`Température (Temperature)`**</mark> :
Contrôle la créativité (défaut : 0.7) :
* **0-0.3** : Réponses prévisibles (ex: code, analyse)
* **0.4-0.7** : Équilibre (recommandé pour les chatbots)
* **0.8-1.0** : Hautement créatif (ex: écriture)

#### <mark style="color:blue;">**`Top P (échantillonnage par noyau)`**</mark> :
Diversité lexicale (défaut : 1) :
* **0.1-0.3** : Vocabulaire restreint (ex: docs techniques)
* **0.4-0.6** : Équilibre
* **0.7-1.0** : Vocabulaire large (ex: création)

{% hint style="info" %}
- Utilisez ces paramètres indépendamment ou ensemble
- Testez pour trouver les valeurs optimales
- Les plages sont indicatives (consultez la documentation des modèles)
{% endhint %}

#### <mark style="color:blue;">**`Fenêtre de contexte`**</mark>
Nombre de messages conservés :
* **5-10** : Discussions simples
* **>10** : Tâches complexes (ex: rédaction longue)
* ⚠ Plus de messages = plus de Tokens consommés

#### <mark style="color:blue;">**`Activer la limite de longueur (MaxToken)`**</mark>
Tokens maximum par réponse. Affecte directement la qualité et la longueur.

> Ex : Test de connexion → MaxToken=1 suffit.

Limites courantes : 32k Tokens (certains modèles jusqu'à 64k).

**Recommandations** :
{% hint style="success" %}
* Discussion normale : 500-800
* Texte court : 800-2000
* Génération de code : 2000-3600
* Texte long : ≥4000 (modèles compatibles requis)
{% endhint %}

{% hint style="warning" %}
Une limite trop basse peut tronquer les réponses (ex: code incomplet).
{% endhint %}

#### <mark style="color:blue;">**`Sortie en flux continu (Stream)`**</mark>
Mode "machine à écrire" (défaut activé) :
* **Activé** : Réponse progressive caractère par caractère
* **Désactivé** : Réponse complète en une fois

{% hint style="info" %}
Désactivez pour les modèles incompatibles (ex: o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Paramètres personnalisés`**</mark>
Ajoutez des paramètres supplémentaires (ex: `presence_penalty`) au corps de la requête. Utilisation avancée.

> Exemples inclus : top-p, maxtokens, stream.  
> Documentation : [Cliquez ici](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Priorité : Paramètres personnalisés > Paramètres intégrés
  > Ex : `"model":"gpt-4o"` ignorera toute sélection de modèle
- Utilisez `<kbd>nom_paramètre:undefined</kbd>` pour exclure un paramètre
- Consultez la documentation spécifique des fournisseurs
{% endhint %}