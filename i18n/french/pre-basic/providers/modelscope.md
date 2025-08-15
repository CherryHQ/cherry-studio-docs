# Guide d'intégration de la plateforme ModelScope (ModelScope)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Qu'est-ce que ModelScope ?
> ModelScope est une nouvelle génération de plateforme open source de Modèle en tant que Service (MaaS). Elle s'engage à fournir aux développeurs une solution de service de modèles **flexible, facile à utiliser et à faible coût**, rendant l'application des modèles plus simple !
>
> Grâce à la **capacité de service API-Inference**, la plateforme standardise les modèles open source en interfaces API appelables. Les développeurs peuvent intégrer légèrement et rapidement les capacités des modèles dans diverses applications d'IA, supportant des scénarios innovants tels que l'appel d'outils et le prototypage.

### Avantages clés
- ✅ **Quota gratuit** : Offre **2000 appels API gratuits par jour** ([règles de facturation](##règles-de-facturation-et-de-quotas))
- ✅ **Base de modèles riche** : Couvre plus de 1000 modèles open source dans les domaines NLP, CV, audio, multimodal, etc.
- ✅ **Prêt à l'emploi** : Aucun déploiement nécessaire, appel rapide via API RESTful

---

## Processus d'intégration avec Cherry Studio
### Étape 1 : Obtenir un jeton API ModelScope
1. **Connexion à la plateforme**
   - Visitez le [site officiel de ModelScope](https://modelscope.cn) → Cliquez sur **Connexion** en haut à droite → Choisissez le mode d'authentification
   ![Interface de connexion](../../.gitbook/assets/ModelScope/image.png)
2. **Créer un jeton d'accès**
   - Accédez à **[Paramètres du compte → Jetons d'accès](https://modelscope.cn/my/myaccesstoken)**
   - Cliquez sur **`Créer un jeton`** → Remplissez la description → **Copiez le jeton généré** (*voir exemple ci-dessous*)
   ![Exemple de création de jeton](../../.gitbook/assets/ModelScope/image-7.png)
   > 🔑 **Important** : La fuite du jeton compromet la sécurité du compte !

### Étape 2 : Configurer Cherry Studio
- Ouvrez **Cherry Studio** → **Paramètres → Services de modèles → ModelScope**
- Collez le jeton copié dans le champ `Clé API`
  ![Interface de configuration](../../.gitbook/assets/ModelScope/image-2.png)
- Cliquez sur **`Enregistrer`** pour terminer l'autorisation

### Étape 3 : Appeler l'API du modèle
1. **Trouver des modèles compatibles API**
   - Visitez la [bibliothèque de modèles ModelScope](https://modelscope.cn/models)
   - Filtres : **Cochez `API-Inference`** (ou identifiez l'icône `API` sur la carte du modèle)
   ![Filtrage des modèles API](../../.gitbook/assets/ModelScope/image-3.png)
   > La couverture des modèles par API-Inference est principalement déterminée par leur popularité dans la communauté (données de likes, téléchargements, etc.). Ainsi, la liste des modèles supportés évolue continuellement avec la sortie de nouvelles versions.
2. **Obtenir l'ID du modèle**
   - Accédez à la page de détails du modèle cible → Copiez le **Model ID** (format : `damo/nlp_structbert_sentiment-classification_chinese-base`)
   ![Copie du Model ID](../../.gitbook/assets/ModelScope/image-5.png)
3. **Remplir dans Cherry Studio**
   - Entrez l'ID dans le champ `ID du modèle` → Sélectionnez le type de tâche → Finalisez la configuration
   ![Saisie de l'ID du modèle](../../.gitbook/assets/ModelScope/image-6.png)

---

## Règles de facturation et de quotas
### Informations importantes
- 🎫 **Quota gratuit** : **2000 appels API par jour** par utilisateur (*sujet aux dernières règles officielles)
- 🔁 **Réinitialisation du quota** : Réinitialisation automatique quotidienne à 00:00 UTC+8, **pas de cumul ou mise à niveau inter-jours**
- 💡 **Dépassement de quota** :
  - Lorsque la limite quotidienne est atteinte, l'API retourne une `erreur 429`
  - Solutions : Basculer vers un compte secondaire / Utiliser une autre plateforme / Optimiser la fréquence d'appel

### Vérifier le quota restant
- Connectez-vous à ModelScope → Cliquez sur **`Nom d'utilisateur`** en haut à droite → **`Statut d'utilisation de l'API`**
  ![Emplacement de vérification du quota](../../.gitbook/assets/ModelScope/image-8.png)

> ⚠️ Note : L'API d'inférence Inference offre 2000 appels gratuits par jour. Pour des besoins supplémentaires, envisagez d'utiliser des services cloud comme Alibaba Cloud Bailian.