---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Tutorial de Configuración de Obsidian

Cherry Studio admite la integración con Obsidian para exportar conversaciones completas o mensajes individuales a una biblioteca de Obsidian.

{% hint style="warning" %}
Este proceso no requiere instalar complementos adicionales de Obsidian. Sin embargo, dado que el método de importación de Cherry Studio a Obsidian es similar a Obsidian Web Clipper, se recomienda actualizar Obsidian a la versión más reciente (la versión actual debe ser superior a **1.7.2**) para evitar [fallos de importación en conversaciones largas](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Tutorial Actualizado

{% hint style="info" %}
Comparado con la versión anterior, la nueva función de exportación a Obsidian selecciona automáticamente la ruta de la biblioteca, eliminando la necesidad de ingresar manualmente nombres de biblioteca o carpetas.
{% endhint %}

### Paso 1: Configurar Cherry Studio

En Cherry Studio, abre _Ajustes_ → _Configuración de datos_ → Menú _Configuración de Obsidian_. Los nombres de las bibliotecas de Obsidian abiertas localmente aparecerán automáticamente en el menú desplegable. Selecciona tu biblioteca de Obsidian objetivo:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Paso 2: Exportar Conversación

#### Exportar Conversación Completa

En la interfaz de conversación de Cherry Studio, haz clic derecho en la conversación, selecciona _Exportar_, luego haz clic en _Exportar a Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Se abrirá una ventana para configurar las **Properties (propiedades)** de la nota exportada, la **ubicación de la carpeta** en Obsidian y el **modo de procesamiento**:

* **Biblioteca**: Selecciona otra biblioteca de Obsidian en el menú desplegable
* **Ruta**: Selecciona la carpeta de destino en el menú desplegable
* Propiedades de Obsidian:
  * Etiquetas (tags)
  * Fecha de creación (created)
  * Fuente (source)
* **Modos de procesamiento disponibles**:
  * **Nuevo (sobrescribir si existe)**: Crea una nueva nota en la carpeta especificada, sobrescribiendo notas existentes con el mismo nombre
  * **Prepend**: Agrega el contenido al inicio de una nota existente con el mismo nombre
  * **Añadir**: Agrega el contenido al final de una nota existente con el mismo nombre

{% hint style="info" %}
Solo el primer modo incluye Properties; los otros dos no incluyen propiedades.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Configurar propiedades de la nota</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Seleccionar ruta</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Seleccionar modo de procesamiento</p></figcaption></figure>

Tras configurar todas las opciones, haz clic en "Aceptar" para exportar la conversación completa a la carpeta especificada de tu biblioteca de Obsidian.

#### Exportar Mensaje Individual

Para exportar un mensaje individual, haz clic en el _menú de tres líneas_ bajo el mensaje, selecciona _Exportar_, luego haz clic en _Exportar a Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Exportar mensaje individual</p></figcaption></figure>

Aparecerá la misma ventana de configuración de **propiedades de la nota** y **modo de procesamiento**, que debes completar siguiendo el [tutorial anterior](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Exportación Exitosa

🎉 ¡Felicidades! Has completado toda la configuración de integración entre Cherry Studio y Obsidian. ¡Disfrútala!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exportar a Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Ver resultados de la exportación</p></figcaption></figure>

***

## Tutorial Antiguo (para Cherry Studio <v1.1.13)

### Paso 1: Preparar Obsidian

Abre tu biblioteca de Obsidian y crea una `carpeta` para guardar las conversaciones exportadas (ejemplo: carpeta "Cherry Studio"):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Recuerda el nombre de la `Biblioteca` resaltado en la esquina inferior izquierda.

### Paso 2: Configurar Cherry Studio

En Cherry Studio, ve a _Ajustes_ → _Configuración de datos_ → Menú _Configuración de Obsidian_. Ingresa el nombre de la `Biblioteca` y `carpeta` obtenidos en el [Paso 1](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

El campo `Etiquetas globales` es opcional y permite definir etiquetas para todas las notas exportadas.

### Paso 3: Exportar Conversación

#### Exportar Conversación Completa

En la interfaz de conversación de Cherry Studio, haz clic derecho en la conversación, selecciona _Exportar_, luego haz clic en _Exportar a Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Exportar conversación completa</p></figcaption></figure>

Configura las **Properties (propiedades)** y el **modo de procesamiento** en la ventana emergente. Los modos disponibles son:

* **Nuevo (sobrescribir si existe)**: Crea una nueva nota en la `carpeta` configurada
* **Prepend**: Agrega el contenido al inicio de una nota existente
* **Añadir**: Agrega el contenido al final de una nota existente

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Configurar propiedades de la nota</p></figcaption></figure>

{% hint style="info" %}
Solo el primer modo incluye Properties; los otros dos no incluyen propiedades.
{% endhint %}

#### Exportar Mensaje Individual

Para mensajes individuales, haz clic en el _menú de tres líneas_ bajo el mensaje, selecciona _Exportar_, luego _Exportar a Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Exportar mensaje individual</p></figcaption></figure>

Completa la configuración siguiendo el [tutorial previo](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Exportación Exitosa

🎉 ¡Felicidades! Has completado la configuración de integración entre Cherry Studio y Obsidian. ¡Disfrútala!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exportar a Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Ver resultados de la exportación</p></figcaption></figure>