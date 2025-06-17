
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# PPIO PiOu Cloud

## Cherry Studio Integración con PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#overview-del-tutorial)Resumen del Tutorial <a href="#overview-del-tutorial" id="overview-del-tutorial"></a>

Cherry Studio es un cliente de escritorio multimodelo que actualmente admite paquetes de instalación para Windows, Linux y macOS. Agrega modelos LLM principales y ofrece asistencia para múltiples escenarios. Los usuarios pueden mejorar la productividad mediante gestión de conversaciones inteligentes, personalización de código abierto e interfaces multitema.

Cherry Studio ahora está profundamente integrado con el **canal API de alto rendimiento de PPIO**. Garantiza potencia computacional empresarial, **respuesta ultrarrápida de DeepSeek-R1/V3** y **disponibilidad del 99.9%**, brindándote una experiencia fluida.

El tutorial a continuación incluye una solución completa de integración (con configuración de claves). Activa el modo avanzado "Cherry Studio + API de alto rendimiento de PPIO" en solo 3 minutos.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-acceder-a-cherrystudio-a%C3%B1adir-ppio-como-proveedor-de-modelo)1. Accede a CherryStudio y añade "PPIO" como proveedor de modelo <a href="#1-acceder-a-cherrystudio-añadir-ppio-como-proveedor-de-modelo" id="1-acceder-a-cherrystudio-añadir-ppio-como-proveedor-de-modelo"></a>

Primero, descarga Cherry Studio desde la web oficial: [https://cherry-ai.com/download](https://cherry-ai.com/download) (Si no accedes, usa este enlace alternativo de Quark: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Haz clic en "Configuración" abajo a la izquierda. Define el nombre del proveedor como: `PPIO`. Haz clic en "Aceptar".

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Accede a la [Gestión de claves API de PPIO](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio). Haz clic en el **icono de usuario → "Gestión de claves API"**.

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Haz clic en **"+ Crear"** para generar una nueva clave API. Asigna un nombre personalizado. **¡Copia y guarda la clave inmediatamente! Solo es visible durante la generación.**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) En CherryStudio, pega la clave: Ve a Configuración → Selecciona **"PPIO 派欧云"** → Ingresa la clave API → Haz clic en **"Comprobar"**.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Selecciona el modelo: Por ejemplo, `deepseek/deepseek-r1/community`. Puedes cambiarlo según necesidades.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 y V3 community son versiones gratuitas de parámetros completos. Para uso intensivo, **debes recargar saldo y cambiar a versión no community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-configuraci%C3%B3n-del-modelo)2. Configuración de uso del modelo <a href="#2-configuración-del-modelo" id="2-configuración-del-modelo"></a>

(1) Tras clicar "Comprobar", verifica la conexión exitosa.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Finalmente, haz clic en **"@"** → Selecciona el modelo **DeepSeek R1** bajo PPIO → ¡Comienza a chatear!

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

*Fuente parcial: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)*

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-videotutorial-de-ppio--cherry-studio)3. Video-tutorial de PPIO × Cherry Studio <a href="#3-videotutorial-de-ppio-cherry-studio" id="3-videotutorial-de-ppio-cherry-studio"></a>

Si prefieres aprendizaje visual, visita nuestro tutorial en Bilibili. Configura "API PPIO + Cherry Studio" fácilmente:  
[《¡¿Desesperado con DeepSeek cargando?! PPIO + DeepSeek full power = ¡Sin congestión, máxima velocidad!》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

*Material de video: [sola]*