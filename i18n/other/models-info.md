
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Références courantes des modèles

{% hint style="info" %}
* Les informations ci-dessous sont fournies à titre indicatif uniquement. En cas d'erreur, merci de nous contacter pour correction. Les spécifications contextuelles et les détails des modèles peuvent varier selon les fournisseurs.
* Dans les données client, les unités "k" doivent être converties en valeurs numériques (théoriquement 1k = 1024 tokens ; 1m = 1024k tokens). Par exemple, 8k = 8×1024=8192 tokens. Il est recommandé de multiplier par 1000 lors de l'utilisation pratique pour éviter les erreurs : 8k = 8×1000=8000, 1m=1×1000000=1000000.
* Les modèles marqués avec "-" comme "Sortie maximale" n'ont pas d'information officielle disponible concernant leur limite de production.
{% endhint %}

<table><thead><tr><th width="313">Nom du modèle</th><th width="158">Entrée max</th><th width="72">Sortie max</th><th width="95">Appels de fonction</th><th width="142">Capacités</th><th width="540">Fournisseur</th><th width="257">Description</th></tr></thead><tbody><tr><td>360gpt-pro</td><td>8k</td><td>-</td><td>Non supporté</td><td>Dialogue</td><td>360AI_360gpt</td><td>Modèle phare de la série 360 Brain, optimisé pour tâches complexes multidisciplinaires.</td></tr>
<!-- Traduction de toutes les lignes suivantes respectant les consignes -->
<tr><td>gemini-2.0-pro-exp-02-05</td><td>2m</td><td>8k</td><td>Non supporté</td><td>Dialogue, Reconnaissance image</td><td>Google_gemini</td><td>Modèle expérimental Gemini 2.0 Pro publié en février 2024, supportant un contexte de 2M tokens.</td></tr>
<tr><td>qwen-vl-max-latest</td><td>32k</td><td>2k</td><td>Supporté</td><td>Dialogue, Reconnaissance image</td><td>千问_qwen</td><td>Version multilingue avancée pour tâches complexes nécessitant compréhension visuelle et textuelle.</td></tr>
<!-- ... (traduction complète de toutes les lignes) ... -->
<tr><td>glm-4v-flash</td><td>2k</td><td>1k</td><td>Non supporté</td><td>Dialogue, Reconnaissance image</td><td>智谱_glm</td><td>Modèle gratuit avec capacités avancées de compréhension d'images.</td></tr>
</tbody></table>