---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

---
icon: cherries
---

# Configuración de acceso a Internet de Volcano Engine

### 1. Iniciar sesión/Registrar una cuenta en Volcano Engine <a href="#rclz7" id="rclz7"></a>

Visite el sitio web oficial: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Sitio web oficial de Volcano Engine</p></figcaption></figure>

### 2. Crear una "Mi aplicación" con capacidad de acceso a Internet <a href="#gvzaa" id="gvzaa"></a>

2.1. Inicie sesión en Volcano Engine y acceda a la página de **Volcano Ark**: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Haga clic secuencialmente en:** <mark style="color:red;">**"Mi aplicación" → "Crear aplicación" → "Código cero" → "Chat individual"**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Complete la información y publique la aplicación <a href="#zzdfe" id="zzdfe"></a>

**Nombre de la aplicación**: Asigne cualquier nombre que cumpla con los requisitos (campos marcados con <mark style="color:red;">**\* son obligatorios**</mark>, los demás son opcionales).

<mark style="color:red;">**Punto clave: Active el plugin de acceso a Internet (requiere habilitación previa)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Habilitar la función del plugin de acceso a Internet (preste atención a los costos y usos gratuitos) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Haga clic en "Comprar ahora" y siga los pasos hasta que aparezca la siguiente interfaz, lo que indica que se ha habilitado correctamente.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Verifique el estado: habililitación completada</p></figcaption></figure>

Regrese a la interfaz de "Completar información de la aplicación" para continuar.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Explicación de la "Configuración avanzada" para búsqueda en Internet <a href="#sp6uz" id="sp6uz"></a>

Seleccione según sus necesidades reales. Recomendaciones personales:

* Para control preciso de entradas/salidas: use **Llamada personalizada**;
* Si prefiere simplicidad: use **Llamada automática** (valor predeterminado);
* Si requiere máxima actualización y no le importa el costo: **Forzar activación**.

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publicar la aplicación <a href="#fe1gf" id="fe1gf"></a>

Haga clic en el botón "Publicar" en la esquina superior derecha para completar la creación de la aplicación.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtener la API Key <a href="#jtqlu" id="jtqlu"></a>

Haga clic secuencialmente: **"Guía de llamada API" → "Seleccionar API Key y copiar" → "Ver y seleccionar"**

Copie la API Key y luego péguela en Cherry Studio (detalles operativos en la interfaz inferior).

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

**Nota**: Si no hay API Key, haga clic en **"Crear API Key"** en la esquina superior derecha del cuadro emergente, luego cópiela.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Usar la API Key en Cherry Studio para acceder a deepseek-R1 con Internet <a href="#lrefj" id="lrefj"></a>

#### 5.1. Abra Cherry Studio → "Configuración" → "Asignar nombre arbitrario" → "Tipo: OpenAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configure la URL y la Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Nota: Si no encuentra la dirección o no usa el nodo de Beijing, localice la dirección específica aquí. ¡No olvide "/" al final!</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Agregar el nombre del modelo <a href="#qmh3i" id="qmh3i"></a>

**Importante**: Copie el texto en letras pequeñas como nombre del modelo, de lo contrario ocurrirán errores.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Vista previa del efecto <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>