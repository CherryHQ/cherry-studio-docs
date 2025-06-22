
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# PPIO 派欧云

## Intégration de PPIO LLM API à Cherry Studio

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Aperçu du tutoriel <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio est un client desktop multi-modèles, compatible actuellement avec Windows, Linux et macOS. Il agrège les principaux modèles LLM et offre une assistance multi-scénarios. Les utilisateurs peuvent améliorer leur productivité grâce à une gestion intelligente des conversations, une personnalisation open source et des interfaces multi-thèmes.

Cherry Studio est désormais entièrement compatible avec les **canaux API hautes performances de PPIO** – en assurant une puissance de calcul professionnelle pour offrir des **réponses rapides DeepSeek-R1/V3** et une **disponibilité de service de 99,9%**, vous garantissant une expérience fluide.

Le tutoriel ci-dessous contient la procédure complète d'intégration (incluant la configuration des clés), vous permettant d'activer le mode avancé « Cherry Studio + API hautes performances PPIO » en 3 minutes.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Accéder à CherryStudio et ajouter "PPIO" comme fournisseur de modèles <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Commencez par télécharger Cherry Studio sur le site officiel : [https://cherry-ai.com/download](https://cherry-ai.com/download) (si le lien ne fonctionne pas, vous pouvez utiliser ce lien alternatif Quark : [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Cliquez d'abord sur l'icône des paramètres en bas à gauche, définissez le nom du fournisseur sur : `PPIO`, puis cliquez sur "Confirmer"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Rendez-vous sur la [gestion des clés API de PPIO](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), cliquez sur 【Avatar】→【Gestion des clés API】 pour accéder au panneau de contrôle

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Cliquez sur le bouton 【+ Créer】 pour générer une nouvelle clé API. Attribuez-lui un nom personnalisé. **La clé n'est visible qu'au moment de sa création : copiez-la impérativement et sauvegardez-la, sous peine de compromettre son utilisation ultérieure.**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Dans CherryStudio, collez la clé Cliquez sur les paramètres, sélectionnez 【PPIO 派欧云】, saisissez la clé API générée sur le site, puis cliquez sur 【Vérifier】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Sélectionnez un modèle : prenons l'exemple de deepseek/deepseek-r1/community. Pour en changer, remplacez simplement le nom.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

Les versions DeepSeek R1 et V3 community sont fournies à titre exploratoire. Ce sont des modèles complets et non limités, avec une stabilité et des performances identiques. Pour des appels intensifs, **rechargez votre compte et basculez vers une version non-community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Configuration d'utilisation des modèles <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Une fois la 【vérification】 réussie, l'utilisation normale est possible

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Enfin, cliquez sur 【@】 et sélectionnez le modèle DeepSeek R1 nouvellement ajouté sous le fournisseur PPIO pour démarrer une conversation !

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Source partielle du matériel : [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Tutoriel vidéo PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Pour un apprentissage visuel, nous proposons un tutoriel vidéo sur Bilibili. Ce guide pas à pas vous permettra de maîtriser rapidement la configuration « PPIO API + Cherry Studio ». Cliquez sur le lien ci-dessous pour accéder à la vidéo et démarrer une expérience de développement fluide → [《 Vous en avez marre des délais d'attente DeepSeek ? PPIO + DeepSeek full-speed = ? Fini les congestions, démarrage immédiat 》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Source vidéo : sola】