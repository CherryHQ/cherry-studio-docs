---
icon: searchengin
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Ανάπτυξη και Διαμόρφωση SearXNG

Το CherryStudio υποστηρίζει διαδικτυακή αναζήτηση μέσω του SearXNG, ενός ανοιχτού λογισμικού που μπορεί να αναπτυχθεί τοπικά ή σε διακομιστή. Αυτός ο τρόπος διαφέρει από άλλες διαμορφώσεις που βασίζονται σε παρόχους API.

**Σύνδεσμος έργου SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Πλεονεκτήματα SearXNG

* Ανοιχτό λογισμικό και δωρεάν, χωρίς απαίτηση API
* Σχετικά υψηλότερη προστασία απορρήτου
* Υψηλός βαθμός προσαρμογής

## Τοπική Ανάπτυξη

### 1. Άμεση Ανάπτυξη με Docker

Εφόσον το SearXNG δεν απαιτεί περίπλοκες ρυθμίσεις περιβάλλοντος, μπορείτε να χρησιμοποιήσετε απευθείας το Docker αντί για docker compose. Αυτός είναι ο ταχύτερος τρόπος.

#### 1. Κατέβασμα, εγκατάσταση και ρύθμιση [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Επιλέξτε διαδρομή αποθήκευσης εικόνων μετά την εγκατάσταση:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Αναζήτηση και λήψη εικόνας SearXNG

Στο πλαίσιο αναζήτησης πληκτρολογήστε **searxng**:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Λήψη εικόνας:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Εκτέλεση εικόνας

Μετά την επιτυχή λήψη, μεταβείτε στη σελίδα **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Επιλέξτε την εικόνα και κάντε κλικ στην επιλογή εκτέλεσης:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Ανοίξτε τις ρυθμίσεις για διαμόρφωση:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Για θύρα `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Μετά την επιτυχή εκτέλεση, κάντε κλικ στον σύνδεσμο για το περιβάλλον εργασίας SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Αυτή η σελίδα δείχνει επιτυχή ανάπτυξη:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Ανάπτυξη σε Διακομιστή

### Ανάπτυξη SearXNG

Παρόμοια με τοπική ανάπτυξη, χρησιμοποιούμε Docker. Αν υποθέσουμε ότι έχετε εγκαταστήσει το Docker CE σύμφωνα με [την επίσημη τεκμηρίωση](https://docs.docker.com/engine/install), εδώ είναι εντολές για Debian:

```bash
sudo apt update
sudo apt install git -y

# Λήψη επίσημου αποθετηρίου
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Για μικρό εύρος ζώνης διακομιστή
export IMAGE_PROXY=true

# Διαμόρφωση αρχείου ρυθμίσεων
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# see https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url is defined in the SEARXNG_BASE_URL environment variable, see .env and docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # can be disabled for a private instance
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

Για αλλαγή θύρας ή χρήση υπάρχοντος Nginx, τροποποιήστε το `docker-compose.yaml`:

```yaml
version: "3.7"

services:
  # ... [παραληφμένο για σαφήνεια] ...

  searxng:
    container_name: searxng
    image: docker.io/searxng/searxng:latest
    restart: unless-stopped
    networks:
      - searxng
    ports:
      - "127.0.0.1:8080:8080"  # Αλλαγή θύρας εδώ
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

# ... [παραληφμένο] ...
```

Εκτελέστε `docker compose up -d` και `docker compose logs -f searxng` για παρακολούθηση αρχείων καταγραφής.

### Ανάπτυξη Αντίστροφου Διακομιστή και Βασικής Πιστοποίησης HTTP

Χρησιμοποιήστε Nginx για αντίστροφο διακομιστή και βασική πιστοποίηση. Για πίνακες όπως BT/1Panel, δείτε τα αντίστοιχα έγγραφα.

Δείγμα ρυθμίσεων Nginx:

```conf
server
{
    listen 443 ssl;
    server_name search.example.com;
    
    ssl_certificate    /path/to/cert/fullchain.pem;
    ssl_certificate_key    /path/to/cert/privkey.pem;
    
    location / {
        auth_basic "Εισαγάγετε τα διαπιστευτήριά σας";
        auth_basic_user_file /etc/nginx/conf.d/search.htpasswd;

        proxy_http_version 1.1;
        proxy_set_header Connection "";
        # ... [άλλες ρυθμίσεις] ...
        proxy_pass http://127.0.0.1:8000;
    }
}
```

Δημιουργία αρχείου κωδικών:

```bash
echo "όνομα_χρήστη:$(openssl passwd -5 'κωδικός')" > /etc/nginx/conf.d/search.htpasswd
```

Επαναλάβετε την εκκίνηση του Nginx.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Ρυθμίσεις Cherry Studio

Μετά την επιτυχή ανάπτυξη SearXNG, ρυθμίστε το CherryStudio.

Στη σελίδα ρυθμίσεων δικτυακής αναζήτησης, επιλέξτε Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Προσθέστε τη διεύθυνση τοπικού σας στιγμιότυπου.

### Διόρθωση Διαμόρφωσης

Για αποτυχία επικύρωσης εξαιτίας JSON:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Επεξεργαστείτε το `settings.yml` και προσθέστε JSON ως μορφή:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

Μετά την επανεκκίνηση:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Χρησιμοποιήστε `http://localhost:θύρα` ή `http://host.docker.internal:θύρα`.

### Βασική Πιστοποίηση

Για διακομιστές με ενεργοποιημένη βασική πιστοποίηση, προσθέστε τα διαπιστευτήρια:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

### Άλλες Ρυθμίσεις

Για προσαρμογές μηχανών αναζήτησης, επεξεργαστείτε το αρχείο ρυθμίσεων:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

## Συχνά Ζητήματα

### Ελλιπής Μορφή Αποτελεσμάτων

Προσθέστε JSON στις επιτρεπόμενες μορφές:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Προβλήματα Μηχανών Αναζήτησης

Για την Κίνα, χρησιμοποιήστε baidu ως μηχανή αναζήτησης:

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

### Όριο Ταχύτητας

Απενεργοποιήστε τον περιορισμό ρυθμού:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>