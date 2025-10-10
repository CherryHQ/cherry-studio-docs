# PPIO Pi Ouyun


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Cherry Studio Acceso a la API LLM de PPIO

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Resumen del tutorial <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio es un cliente de escritorio multmodelo que actualmente admite paquetes de instalación para equipos Windows, Linux y MacOS. Agrega modelos LLM principales para brindar asistencia en múltiples escenarios. Los usuarios pueden mejorar su productividad mediante gestión inteligente de conversaciones, personalización de código abierto e interfaces multitema.

Cherry Studio ahora está profundamente integrado con el **canal API de alto rendimiento de PPIO**, ofreciendo **respuesta ultrarrápida con DeepSeek-R1/V3** y **99.9% de disponibilidad** mediante infraestructura empresarial, garantizando una experiencia fluida.

El siguiente tutorial incluye la solución completa de integración (con configuración de claves), permitiéndote activar el modo avanzado "Cherry Studio + API de alto rendimiento de PPIO" en solo 3 minutos.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Ingresa a Cherry Studio y agrega "PPIO" como proveedor de modelos <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Primero descarga Cherry Studio desde el sitio oficial: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (Si no puedes acceder, usa este enlace alternativo de Quark: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Haz clic en Configuración (inferior izquierdo), personaliza el nombre del proveedor como: `PPIO`, luego haz clic en "Aceptar"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Visita [Gestión de claves API de PPIO](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), haz clic en el 【avatar de usuario】→【Gestión de claves API】para entrar al panel.

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Haz clic en【+ Crear】para generar una nueva clave API. Asigna un nombre personalizado. **La clave solo se muestra al generarse; cópiala y guárdala en un documento para evitar problemas futuros.**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) En Cherry Studio, ingresa la clave: Ve a Configuración, selecciona【PPIO Pi Ouyun】, ingresa la clave API generada y haz clic en【Verificar】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Selecciona el modelo: Ejemplo deepseek/deepseek-r1/community. Para cambiar a otro modelo, selecciónalo directamente.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

Las versiones community de DeepSeek R1 y V3 son para pruebas gratuitas (modelos completos sin recortes). Para uso intensivo, **recarga tu saldo y cambia a versión no community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Configuración del modelo <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Tras hacer clic en【Verificar】y ver "Conectado", el modelo está listo.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Finalmente haz clic en【@】, selecciona el modelo DeepSeek R1 bajo el proveedor PPIO e inicia el chat.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

[Fuente parcial: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)]

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Video tutorial PPIO×Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Para aprendizaje visual, tenemos un tutorial en Bilibili. Te guiamos paso a paso para configurar "API PPIO + Cherry Studio". Haz clic en el enlace: [《¿Frustrado con DeepSeek? PPIO + DeepSeek Full Power = Sin congestión, máximo rendimiento》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

[Fuente del video: sola]