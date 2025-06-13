---
icon: searchengin
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# نشر وتكوين SearXNG

يدعم Cherry Studio البحث على الإنترنت عبر SearXNG، وهو مشروع مفتوح المصدر يمكن نشره محليًا أو على الخادم، لذلك يختلف قليلاً عن طرق التكوين الأخرى التي تتطلب موفر واجهة برمجة تطبيقات (API).

**رابط مشروع SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## مزايا SearXNG

* مفتوح المصدر ومجاني، لا يحتاج إلى واجهة برمجة تطبيقات (API)
* خصوصية أعلى نسبيًا
* قابل للتخصيص بدرجة كبيرة

## النشر المحلي

### أولاً: النشر المباشر باستخدام Docker

نظراً لأن SearXNG لا يحتاج إلى تهيئة بيئة معقدة ولا يتطلب استخدام docker compose، ويكفي فقط توفير منفذ خالٍ للنشر، فإن أسرع طريقة هي سحب صورة Docker ونشرها مباشرة.

#### 1. تنزيل وتثبيت وتكوين [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

بعد التثبيت، اختر مسارًا لتخزين الصور:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. البحث عن صورة SearXNG وسحبها

اكتب **searxng** في شريط البحث:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

سحب الصورة:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. تشغيل الصورة

بعد السحب بنجاح، انتقل إلى صفحة **الصور (images)**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

اختر الصورة المسحوبة وانقر على "تشغيل (Run)":

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

افتح إعدادات التكوين:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

على سبيل المثال باستخدام منفذ `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

بعد التشغيل بنجاح، انقر على الرابط لفتح واجهة SearXNG الأمامية:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

ظهور هذه الصفحة يشير إلى نجاح النشر:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## النشر على الخادم

نظراً لأن تثبيت Docker على Windows يمثل تحدياً، يمكن للمستخدمين نشر SearXNG على خادم ومشاركته مع الآخرين. ولكن للأسف، SearXNG نفسه لا يدعم حالياً المصادقة، مما يسمح للآخرين بمسح المثيل وإساءة استخدامه.

لهذا السبب، يدعم Cherry Studio الآن تكوين [المصادقة الأساسية عبر HTTP (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). إذا كنت تنوي نشر SearXNG الخاص بك على شبكة عامة، يرجى **الضرورة** تكوين المصادقة الأساسية عبر HTTP باستخدام برامج وكيل عكسي مثل Nginx. فيما يلي دليل موجز، يتطلب منك معرفة أساسية بصيانة Linux.

### نشر SearXNG

بشكل مماثل، لا يزال يتم استخدام Docker للنشر. لنفترض أنك قمت بتثبيت أحدث إصدار من Docker CE على الخادم وفقاً للدليل الرسمي، إليك أوامر متكاملة مناسبة للتثبيت الجديد على نظام Debian:

```bash
sudo apt update
sudo apt install git -y

# سحب المستودع الرسمي
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# إذا كانت سرعة خادمك بطيئة، يمكنك تعيين هذه القيمة على false
export IMAGE_PROXY=true

# تعديل ملف التكوين
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# انظر https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url معرف في متغير البيئة SEARXNG_BASE_URL، انظر .env و docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # يمكن تعطيله لمثيل خاص
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

إذا كنت بحاجة إلى تعديل منفذ الاستماع المحلي أو إعادة استخدام nginx موجود مسبقاً، يمكنك تعديل ملف `docker-compose.yaml` كما يلي:

```yaml
version: "3.7"

services:
# إذا لم تكن بحاجة إلى Caddy وأعدت استخدام Nginx المحلي الموجود، فاحذف القسم التالي. لا نستخدم Caddy افتراضياً.
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
# إذا لم تكن بحاجة إلى Caddy وأعدت استخدام Nginx المحلي الموجود، فاحذف القسم السابق. لا نستخدم Caddy افتراضياً.
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
    # افتراضياً، يُعرّض على منفذ 8080 على الجهاز المضيف. إذا أردت الاستماع على 8000، فغيّر إلى "127.0.0.1:8000:8080"
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
# إذا لم تكن بحاجة إلى Caddy وأعدت استخدام Nginx المحلي الموجود، فاحذف القسم التالي
  caddy-data:
  caddy-config:
# إذا لم تكن بحاجة إلى Caddy وأعدت استخدام Nginx المحلي الموجود، فاحذف القسم السابق
  valkey-data2:
```

نفّذ الأمر `docker compose up -d` للبدء. استخدم `docker compose logs -f searxng` لعرض السجلات.

### نشر وكيل عكسي Nginx والمصادقة الأساسية عبر HTTP

إذا كنت تستخدم لوحات تحكم مثل BaoTa أو 1Panel، فراجع وثائقها لإضافة موقع وتكوين وكيل عكسي لـ nginx. ثم ابحث عن مكان تعديل ملف تكوين nginx وقم بالتعديل وفقاً للمثال التالي:

```conf
server
{
    listen 443 ssl;

    # اسم المضيف الخاص بك
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # إذا قمت بتكوين SSL، يجب أن يظهر هذان السطران
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # تكوين وكيل عكسي افتراضيًا، تظل كتلة location كما هي
    location / {
        # فقط أضف السطرين التاليين في كتلة location، واحتفظ بالباقي كما هو
        # افترض أن ملف التكوين محفوظ في /etc/nginx/conf.d/
        # في BaoTa، يجب أن يكون محفوظاً في /www أو مشابه، انتبه لذلك
        auth_basic "الرجاء إدخال اسم المستخدم وكلمة المرور";
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

افترض أن ملف تكوين Nginx محفوظ في `/etc/nginx/conf.d`، سنحفظ ملف كلمات المرور في نفس الدليل.

نفّذ الأمر (استبدل `example_name` و `example_password` باسم المستخدم وكلمة المرور اللذين تختارهما):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

أعد تشغيل Nginx (أو أعد تحميل التكوين).

يمكنك الآن فتح صفحة الويب، يجب أن تظهر مطالبة بإدخال اسم المستخدم وكلمة المرور. أدخل ما حددته سابقاً للتحقق من إمكانية الدخول بنجاح إلى صفحة بحث SearXNG والتحقق من صحة التكوين.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## التكوين ذو الصلة بـ Cherry Studio

بعد نشر SearXNG محلياً أو على الخادم بنجاح، انتقل إلى تكوين Cherry Studio.

انتقل إلى صفحة إعدادات البحث على الإنترنت واختر Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

عند إدخال رابط النشر المحلي مباشرة، ستلاحظ فشل التحقق، لا تقلق:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

لأن التكوين الافتراضي بعد النشر المباشر لا يتضمن نوع إرجاع json، لذا لا يمكن الحصول على البيانات. يجب تعديل ملف التكوين.

ارجع إلى Docker، انتقل إلى علامة التبويب "ملفات" وابحث عن المجلد الموسوم داخل الصور:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

بعد التوسيع، استمر في التمرير لأسفل للعثور على مجلد موسوم آخر:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

استمر في التوسيع للعثور على ملف التكوين **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

انقر لفتح محرر الملفات:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

ابحث عن السطر 78، ستلاحظ أن النوع هو html فقط:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

أضف نوع json واحفظ، ثم أعد تشغيل الصورة:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

ارجع إلى Cherry Studio وأعد التحقق، يجب أن ينجح التحقق الآن:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

يمكنك إدخال العنوان المحلي: <http://localhost>:رقم_المنفذ
أو عنوان docker: <http://host.docker.internal>:رقم_المنفذ

إذا اتبعت المثال السابق وقمت بنشر SearXNG على الخادم وقمت بتكوين وكيل عكسي بشكل صحيح، وتم تمكين نوع إرجاع json. عند إدخال العنوان وإجراء التحقق، ولأنك قمت بتكوين المصادقة الأساسية لوكيلك العكسي، يجب أن يعيد رمز الخطأ 401:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

قم بتكوين المصادقة الأساسية عبر HTTP في العميل، وأدخل اسم المستخدم وكلمة المرور اللذين قمت بتعيينهما:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

أعد التحقق، يجب أن ينجح التحقق.

### تكوينات أخرى

أصبح SearXNG الآن قادراً على البحث الافتراضي على الإنترنت. إذا كنت بحاجة إلى تخصيص محركات البحث، يجب أن تقوم بالتكوين بنفسك.

انتبه: التفضيلات هنا لا تؤثر على التكوين المستخدم عند استدعاء النموذج الكبير:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

لضبط محركات البحث المستخدمة عند استدعاء النموذج الكبير، يجب التحديد في ملف التكوين:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

مرجع لغة التكوين:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

إذا كان المحتوى طويلاً جداً ويصعب تعديله مباشرة، انسخه إلى بيئة التطوير المحلية، عدله ثم ألصقه مرة أخرى في ملف التكوين.

## الأسباب الشائعة لفشل التحقق

### عدم إضافة تنسيق الإرجاع json

في ملف التكوين، أضف تنسيق json إلى تنسيقات الإرجاع:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### عدم تكوين محرك البحث بشكل صحيح

يختار Cherry Studio افتراضياً محركات البحث التي تشمل الفئة web general. افتراضياً، سيتم تحديد محركات مثل Google، ولأن الوصول إلى Google غير مباشر في البر الرئيسي للصين، يؤدي إلى الفشل. أضف التكوين التالي لإجبار SearXNG على استخدام محرك Baidu لحل المشكلة:

```yaml
use_default