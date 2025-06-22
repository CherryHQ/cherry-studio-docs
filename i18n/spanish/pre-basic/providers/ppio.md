
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

---
icon: cherries
---

# PPIO Cloud

## Cherry Studio integra la API de LLM de PPIO

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Descripción general del tutorial <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio es un cliente de escritorio multi-modelo, compatible actualmente con Windows, Linux y MacOS. Combina modelos LLM líderes para brindar asistencia en múltiples escenarios. Los usuarios pueden mejorar su eficiencia mediante gestión inteligente de conversaciones, personalización de código abierto e interfaces multitema.

Cherry Studio está totalmente adaptado al **canal API de alto rendimiento de PPIO**—gracias a su infraestructura empresarial, garantiza **respuestas ultrarrápidas de DeepSeek-R1/V3** y **99.9% de disponibilidad**, ofreciéndote una experiencia fluida y veloz.

El siguiente tutorial contiene el proceso completo de integración (incluyendo configuración de claves), permitiéndote activar en 3 minutos el modo avanzado de "Cherry Studio + API de alto rendimiento PPIO".

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Accede a CherryStudio y añade "PPIO" como proveedor de modelos <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Primero descarga Cherry Studio desde el sitio oficial: [https://cherry-ai.com/download](https://cherry-ai.com/download) (si no se puede acceder, usa este enlace alternativo de Quark: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Haz clic en el icono de configuración inferior izquierdo, establece el nombre del proveedor como: `PPIO` y confirma

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Dirígete a [Gestión de claves API de PPIO Cloud](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), haz clic en el 【avatar】→【API Key Management】para acceder al panel

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Haz clic en 【+ Create】 para generar una nueva clave API. Asigna un nombre personalizado. **La clave solo se muestra durante la generación: copia y guarda el valor en un documento para uso futuro**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Introduce la clave en CherryStudio. En configuración, selecciona 【PPIO Cloud】, pega la clave API y haz clic en 【Check】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Selecciona modelo: Ej. deepseek/deepseek-r1/community. Si necesitas otros modelos, cámbialos directamente.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1/V3 community son versiones completas gratuitas para pruebas. Tienen la misma estabilidad y rendimiento que las versiones estándar. Para uso intensivo, **recarga y cambia a la versión no comunitaria**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Configuración de uso del modelo <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Tras verificación exitosa (【Check】), el modelo está listo para usarse

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Finalmente, haz clic en 【@】 para seleccionar el modelo DeepSeek R1 bajo el proveedor PPIO. ¡Comienza a chatear!

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Material de referencia: [ Chen En ](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Tutorial en video: PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Si prefieres aprendizaje visual, hemos preparado un tutorial en Bilibili. Te guiaremos paso a paso para configurar "API PPIO + Cherry Studio". Accede al video con este enlace para una experiencia de desarrollo fluida → [《¿Cansado de que DeepSeek se congele? PPIO Cloud + DeepSeek Full Version = ¡Sin retrasos, respuesta instantánea!》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Material de video: sola】