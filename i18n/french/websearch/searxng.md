---
icon: searchengin
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Déploiement et configuration de SearXNG

Cherry Studio prend en charge la recherche Web via SearXNG. SearXNG étant un projet open-source pouvant être déployé localement ou sur un serveur, sa configuration diffère légèrement des autres fournisseurs nécessitant une API.

**Lien vers le projet SearXNG :** [SearXNG](https://github.com/searxng/searxng)

## Avantages de SearXNG

* Open source gratuit, sans API nécessaire
* Confidentialité relativement élevée
* Hautement personnalisable

## Déploiement local

### 1. Déploiement direct via Docker

Comme SearXNG ne nécessite pas de configuration d'environnement complexe et peut être déployé simplement en fournissant un port libre sans docker compose, la méthode la plus rapide est d'utiliser Docker pour récupérer et déployer directement l'image.

#### 1. Télécharger, installer et configurer [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Après l'installation, choisissez un chemin de stockage pour les images :

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Rechercher et récupérer l'image SearXNG

Entrez **searxng** dans la barre de recherche :

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Récupérer l'image :

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Exécuter l'image

Après un récupération réussie, accédez à la page **Images** :

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Sélectionnez l'image récupérée et cliquez sur Exécuter :

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Ouvrez les paramètres pour configurer :

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Prenons le port `8085` comme exemple :

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Après un démarrage réussi, cliquez sur le lien pour accéder à l'interface frontale de SearXNG :

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Cette page indique un déploiement réussi :

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Déploiement sur serveur

Étant donné que l'installation de Docker sous Windows est assez compliquée, les utilisateurs peuvent déployer SearXNG sur un serveur, ce qui permet également de le partager avec d'autres. Cependant, SearXNG ne prend pas encore en charge l'authentification nativement, ce qui permet à d'autres personnes d'accéder à votre instance via des scans techniques.

Pour cette raison, Cherry Studio prend désormais en charge la configuration de [l'authentification HTTP basique (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Si vous envisagez d'exposer votre SearXNG déployé sur Internet, veuillez **impérativement** configurer l'authentification HTTP basique via un logiciel proxy inverse comme Nginx. Voici un bref tutoriel nécessitant des connaissances de base en administration Linux.

### Déployer SearXNG

De manière similaire, utilisez Docker pour le déploiement. Supposons que vous ayez déjà installé la dernière version de Docker CE sur le serveur selon le [tutoriel officiel](https://docs.docker.com/engine/install). Voici les commandes complètes pour une nouvelle installation sous système Debian :

```bash
sudo apt update
sudo apt install git -y

# Récupérer le dépôt officiel
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Si la bande passante de votre serveur est faible, définissez sur false
export IMAGE_PROXY=true

# Modifier le fichier de configuration
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# voir https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url est défini dans la variable d'environnement SEARXNG_BASE_URL, voir .env et docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # peut être désactivé pour une instance privée
  image_proxy: $IMAGE_PROXY
ui:
  static_use_hash: true
redis:
  url: redis://redis:6379/0
search:
  formats:
    - html
    - json
EOF
```

Si vous devez modifier le port d'écoute local ou réutiliser un nginx existant, modifiez le fichier `docker-compose.yaml` comme suit :

```yaml
version: "3.7"

services:
# Si vous n'avez pas besoin de Caddy et réutilisez un Nginx local existant, supprimez la section suivante. Nous n'avons pas besoin de Caddy par défaut.
  caddy:
    container_name: caddy
    image: docker.io/library/caddy:2-alpine
    network_mode: host
    restart: unless-stopped
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy-data:/data:rw
      - caddy-config:/config:rw
    environment:
      - SEARXNG_HOSTNAME=${SEARXNG_HOSTNAME:-http://localhost}
      - SEARXNG_TLS=${LETSENCRYPT_EMAIL:-internal}
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"
# Si vous n'avez pas besoin de Caddy et réutilisez un Nginx local existant, supprimez la section ci-dessus. Nous n'avons pas besoin de Caddy par défaut.
  redis:
    container_name: redis
    image: docker.io/valkey/valkey:8-alpine
    command: valkey-server --save 30 1 --loglevel warning
    restart: unless-stopped
    networks:
      - searxng
    volumes:
      - valkey-data2:/data
    cap_drop:
      - ALL
    cap_add:
      - SETGID
      - SETUID
      - DAC_OVERRIDE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

  searxng:
    container_name: searxng
    image: docker.io/searxng/searxng:latest
    restart: unless-stopped
    networks:
      - searxng
    # Par défaut mappé sur le port 8080 de l'hôte. Si vous voulez écouter sur 8000, modifiez en "127.0.0.1:8000:8080"
    ports:
      - "127.0.0.1:8080:8080"
    volumes:
      - ./searxng:/etc/searxng:rw
    environment:
      - SEARXNG_BASE_URL=https://${SEARXNG_HOSTNAME:-localhost}/
      - UWSGI_WORKERS=${SEARXNG_UWSGI_WORKERS:-4}
      - UWSGI_THREADS=${SEARXNG_UWSGI_THREADS:-4}
    cap_drop:
      - ALL
    cap_add:
      - CHOWN
      - SETGID
      - SETUID
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

networks:
  searxng:

volumes:
# Si vous n'avez pas besoin de Caddy et réutilisez un Nginx local existant, supprimez la section suivante
  caddy-data:
  caddy-config:
# Si vous n'avez pas besoin de Caddy et réutilisez un Nginx local existant, supprimez la section ci-dessus
  valkey-data2:
```

Exécutez `docker compose up -d` pour démarrer. Utilisez `docker compose logs -f searxng` pour consulter les journaux.

### Déployer le proxy inverse Nginx et l'authentification HTTP basique

Si vous utilisez des panneaux de serveur comme Baota ou 1Panel, consultez leur documentation pour ajouter un site et configurer le proxy inverse nginx. Modifiez ensuite le fichier de configuration nginx selon l'exemple suivant :

```conf
server
{
    listen 443 ssl;

    # Ceci est votre nom d'hôte
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Si SSL est configuré, ajoutez ces deux lignes
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Par défaut, configuré via le panneau avec bloc location standard
    location / {
        # Ajoutez simplement ces deux lignes dans le bloc location, conservez le reste
        # Cet exemple suppose que vos configurations sont dans /etc/nginx/conf.d/
        auth_basic "Veuillez entrer votre nom d'utilisateur et mot de passe";
        auth_basic_user_file /etc/nginx/conf.d/search.htpasswd;

        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_protocol_addr;
        proxy_pass http://127.0.0.1:8000;
        client_max_body_size 0;
    }

    # access_log  ...;
    # error_log  ...;
}
```

En supposant que le fichier de configuration Nginx est dans `/etc/nginx/conf.d`, sauvegardez le fichier de mot de passe dans le même répertoire.

Exécutez la commande (remplacez `example_name` et `example_password` par vos identifiants) :

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Redémarrez Nginx (un rechargement de la configuration suffit).

Vous pouvez maintenant ouvrir la page web, où vous serez invité à entrer vos identifiants. Utilisez ceux définis précédemment pour vérifier si la page SearXNG s'affiche correctement.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt="Exemple d'authentification basique"><figcaption></figcaption></figure>

## Configuration dans Cherry Studio

Une fois SearXNG déployé localement ou sur serveur, procédez à la configuration dans Cherry Studio.

Accédez à la page des paramètres de recherche Web, sélectionnez Searxng :

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

En saisissant le lien local, la validation échoue initialement :

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt="Échec initial de vérification"><figcaption></figcaption></figure>

Car le type de retour JSON n'est pas configuré par défaut. Modifiez le fichier de configuration.

Retournez dans Docker, onglet Files, et localisez le dossier balisé :

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Développez jusqu'à trouver un autre dossier balisé :

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Localisez le fichier de configuration **settings.yml** :

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Ouvrez l'éditeur de fichiers :

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Ligne 78 : seul html est présent :

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Ajoutez le format json, sauvegardez et redémarrez l'image :

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Retournez dans Cherry Studio : la validation réussit :

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt="Validation réussie"><figcaption></figcaption></figure>

Utilisez soit le lien local : <http://localhost:port>  
soit l'adresse Docker : <http://host.docker.internal:port>

Si vous avez déployé sur un serveur et configuré le proxy inverse avec authentification HTTP, la validation retournera une erreur 401 :

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt="Erreur 401 d'authentification"><figcaption></figcaption></figure>

Configurez l'authentification HTTP basique dans le client :

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt="Configuration de l'authentification"><figcaption></figcaption></figure>

La validation devrait maintenant réussir.

### Autres configurations

SearXNG a désormais une capacité de recherche Web par défaut. Pour personnaliser les moteurs de recherche, une configuration supplémentaire est nécessaire.

Remarque : Les préférences ici n'affectent pas la configuration lors de l'appel par les grands modèles.

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Pour configurer les moteurs de recherche utilisés par les grands modèles, modifiez le fichier de configuration :

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Référence de configuration linguistique :

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt="Configuration linguistique"><figcaption></figcaption></figure>

Pour des modifications complexes, copiez le contenu dans un IDE local et collez-le après modification.

## Causes courantes d'échec de validation

### Format de retour JSON non ajouté

Ajoutez json dans le fichier de configuration :

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt="Configuration du format JSON"><figcaption></figcaption></figure>

### Moteurs de recherche mal configurés

Cherry Studio sélectionne par défaut les moteurs avec des catégories incluant web et general. Par défaut, Google est sélectionné, inaccessible en Chine. Ajoutez cette configuration pour forcer SearXNG à utiliser Baidu :

```
use_default_settings:
  engines:
    keep_only:
      - baidu
engines:
  - name: baidu
    engine: baidu 
    categories: 
      - web
      - general
    disabled: false
```

### Taux d'accès trop rapide

La configuration limiter de SearXNG bloque les accès API. Désactivez-la dans les paramètres :

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt="Désactivation du limiter"><figcaption></figcaption></figure>