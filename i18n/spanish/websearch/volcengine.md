---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Conexión a Internet de Volcano Engine

### 1. Iniciar sesión/Registrar una cuenta en Volcano Engine <a href="#rclz7" id="rclz7"></a>

Visite el sitio web oficial: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Sitio web oficial de Volcano Engine</p></figcaption></figure>

### 2. Crear "Mi aplicación" con capacidad de conexión a Internet <a href="#gvzaa" id="gvzaa"></a>

2.1. Inicie sesión en Volcano Engine y acceda a la página "Volcano Ark": [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Haga clic secuencialmente en:**<mark style="color:red;">**"Mi aplicación" → "Crear aplicación" → "Cero código" → "Chat individual"**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Completar la información y publicar la aplicación <a href="#zzdfe" id="zzdfe"></a>

**Nombre de la aplicación**: Cualquier nombre que cumpla con los requisitos (los campos con <mark style="color:red;">**\* son obligatorios**</mark>, los demás son opcionales)

<mark style="color:red;">**Importante: Active el complemento de conexión a Internet (debe habilitarlo primero)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Habilitar la función de complemento de conexión a Internet (preste atención a los costos y usos gratuitos) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Haga clic en "Comprar ahora" y siga los pasos hasta ver la siguiente interfaz, lo que indica que la habilitación fue exitosa.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Verifique el estado; en este punto, la habilitación fue exitosa</p></figcaption></figure>

Luego regrese a la interfaz "Completar información de la aplicación" para continuar.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Explicación de "Configuración avanzada" para búsquedas en Internet <a href="#sp6uz" id="sp6uz"></a>

Recomendaciones según necesidades:

* Para control preciso de entrada/salida: usar conexión a Internet mediante <mark style="color:red;">**"Llamada personalizada"**</mark>
* Para mayor simplicidad: usar valor predeterminado <mark style="color:red;">**"Llamada automática"**</mark>
* Para alta prioridad en actualización de información: <mark style="color:red;">**"Forzar activación"**</mark> (considerar costos)

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publicar la aplicación <a href="#fe1gf" id="fe1gf"></a>

Haga clic en el botón "Publicar" en la esquina superior derecha para crear la aplicación exitosamente.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtener la API Key <a href="#jtqlu" id="jtqlu"></a>

Haga clic secuencialmente en: <mark style="color:red;">**"Guía de uso de API" → "Seleccionar y copiar API Key" → "Ver y seleccionar"**</mark>

Copie la API Key para usarla en Cherry Studio (detalles en capturas):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Si no tiene API Key: haga clic en <mark style="color:red;">**"Crear API Key"**</mark> en la esquina superior derecha del cuadro emergente, luego cópiela.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Usar API Key en Cherry Studio para acceder a deepseek-R1 con conexión a Internet <a href="#lrefj" id="lrefj"></a>

#### 5.1. Abrir Cherry Studio → "Configuración" → "Ingresar nombre" → "Tipo: openAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configurar URL y clave <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Nota: Si no encuentra la dirección o no es un nodo de Beijing, puede ubicar la dirección específica aquí (¡no olvide "/"!):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Agregar nombre del modelo <a href="#qmh3i" id="qmh3i"></a>

¡Importante! Copie el nombre del modelo indicado en texto pequeño, de lo contrario generará errores.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Vista previa del resultado <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>