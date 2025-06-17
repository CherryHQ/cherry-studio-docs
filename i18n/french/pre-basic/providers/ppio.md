
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# PPIO Cloud

## Intégration de Cherry Studio à l'API LLM de PPIO

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Aperçu du tutoriel <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio est un client de bureau multi-modèles prenant actuellement en charge les systèmes Windows, Linux et macOS. Il regroupe les principaux modèles LLM et fournit une assistance pour plusieurs scénarios. Les utilisateurs peuvent améliorer leur productivité grâce à la gestion intelligente des conversations, la personnalisation open source et une interface multi-thèmes.

Cherry Studio est désormais parfaitement compatible avec **le canal API haute performance de PPIO** – grâce à une garantie de puissance de calcul de niveau entreprise, il offre **des réponses ultra-rapides pour DeepSeek-R1/V3** et **99,9% de disponibilité du service**, vous offrant une expérience fluide et réactive.

Le tutoriel ci-dessous contient la solution d'intégration complète (incluant la configuration des clés) pour activer en 3 minutes le mode avancé « Orchestration intelligente de Cherry Studio + API haute performance PPIO ».

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Accéder à CherryStudio et ajouter « PPIO » comme fournisseur de modèles <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Commencez par télécharger Cherry Studio sur le site officiel : [https://cherry-ai.com/download](https://cherry-ai.com/download) (si inaccessible, utilisez le lien alternatif Quark : [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Cliquez sur les paramètres en bas à gauche, définissez le nom du fournisseur comme : `PPIO`, puis validez avec « OK »

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Accédez à la [gestion des clés API PPIO Cloud](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio) via 【Avatar】→【Gestion des clés API】

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Cliquez sur 【+ Créer】 pour générer une nouvelle clé API. Nommez-la et **copiez-la immédiatement lors de la génération (elle n’est affichée qu’une fois), et sauvegardez-la pour éviter tout problème d’utilisation future**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Dans CherryStudio, collez la clé : allez dans les paramètres, sélectionnez 【PPIO Cloud】, saisissez la clé API générée, puis cliquez sur 【Vérifier】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Sélectionnez un modèle : par exemple `deepseek/deepseek-r1/community`. Pour changer de modèle, modifiez directement cette valeur.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

Les versions communautaires DeepSeek R1 et V3 sont des démonstrations complètes et stables. Pour une utilisation intensive, **rechargez votre compte et passez à une version non-communautaire**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Configuration d'utilisation du modèle <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Une fois 【Vérifier】 affiché comme réussi, le modèle est opérationnel

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Cliquez enfin sur 【@】, sélectionnez le modèle DeepSeek R1 sous le fournisseur PPIO, et commencez à discuter !

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Source partielle : [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Tutoriel vidéo PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Pour un apprentissage visuel, un tutoriel vidéo est disponible sur Bilibili. Grâce à ce guide pas-à-pas, maîtrisez rapidement la configuration « API PPIO + Cherry Studio » en cliquant sur le lien : → [《【Vous en avez assez de voir DeepSeek tourner en rond ?】PPIO Cloud + DeepSeek version complète = ? Plus de congestion, décollage immédiat》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Source vidéo : sola】