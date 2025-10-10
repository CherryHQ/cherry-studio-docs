---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---
# Conexión a Volc Engine


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




### 1. Iniciar sesión/Registrar cuenta en «Volc Engine» <a href="#rclz7" id="rclz7"></a>

Acceda al sitio web oficial: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Sitio web oficial de Volc Engine</p></figcaption></figure>

### 2. Crear «Mi aplicación» con capacidad de conexión a Internet <a href="#gvzaa" id="gvzaa"></a>

2.1. Inicie sesión en Volc Engine y acceda a la página «Volc Ark»: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Haga clic en secuencia:** <mark style="color:red;">**«Mi aplicación» → «Crear aplicación» → «Cero código» → «Chat individual»**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Rellenar información y publicar la aplicación <a href="#zzdfe" id="zzdfe"></a>

**Nombre de la aplicación**: Asigne cualquier nombre según los requisitos (<mark style="color:red;">**\*obligatorio**</mark>, otros campos opcionales).

<mark style="color:red;">**Clave: Active el complemento de conexión a Internet (requiere activación previa)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Activar función de complemento de Internet (note costos y usos gratuitos) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Haga clic en "Comprar ahora" y complete los pasos hasta ver esta interfaz, indicando activación exitosa</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Verifique el estado: activación completada</p></figcaption></figure>

Regrese a la interfaz de información de aplicación para continuar.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Configuración avanzada de búsqueda en línea <a href="#sp6uz" id="sp6uz"></a>

Recomendaciones según necesidades:
* Para control preciso de entrada/salida: usar **«Llamada personalizada»**
* Para simplicidad: **«Llamada automática»** (valor predeterminado)
* Para máxima actualización de información (con costo): **«Forzar activación»**

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publicar aplicación <a href="#fe1gf" id="fe1gf"></a>

Haga clic en «Publicar» (esquina superior derecha) para crear la aplicación.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtener clave API <a href="#jtqlu" id="jtqlu"></a>

Siga: **«Guía de llamadas API» → «Seleccionar y copiar clave API» → «Ver y seleccionar»**

Copie la clave API y péguela en Cherry Studio (detalles abajo):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Nota: Si no existe clave API, haga clic en **«Crear clave API»** (esquina superior derecha del cuadro emergente).

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Usar clave API en Cherry Studio para acceso en línea a deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Abrir Cherry Studio → «Configuración» → «Nombre arbitrario» → «Tipo: OpenAI» <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configurar URL y clave <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Nota: Si no encuentra la dirección o no es nodo de Beijing, localice la dirección exacta aquí (no olvide "/"):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Añadir nombre del modelo <a href="#qmh3i" id="qmh3i"></a>

Importante: Copie el texto pequeño inferior como nombre del modelo, de lo contrario generará error.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Vista previa del resultado <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>