---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Modo en línea

{% hint style="info" %}
Ejemplos de escenarios que requieren conexión a Internet:

* Información de actualidad: como el precio del oro de hoy/esta semana/recientemente, etc.
* Datos en tiempo real: como el clima, tipos de cambio y otros valores dinámicos.
* Conocimientos emergentes: como nuevas cosas, nuevos conceptos, nuevas tecnologías, etc.
{% endhint %}

### I. Cómo activar el modo en línea

En la ventana de preguntas de Cherry Studio, haz clic en el icono del 【Globo terráqueo】 para activar el modo en línea.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Haz clic en el icono del globo - Activar conexión</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indicador de conexión activada</p></figcaption></figure>

### II. Presta atención: existen dos modos de conexión

#### Modo 1: Modelos con capacidad nativa de conexión

Algunos proveedores de modelos ya incluyen funciones de conexión integradas. Al activarlo, podrás usar el servicio directamente de forma sencilla.

{% hint style="warning" %}
Verifica si el nombre del modelo muestra un ícono de mapa pequeño detrás para identificar rápidamente si soporta conexión.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

En la página de gestión de modelos, este método también te ayuda a identificar rápidamente qué modelos son compatibles.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Proveedores compatibles actualmente en Cherry Studio**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (todos los modelos)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian, etc.</mark>

{% hint style="danger" %}
Excepción importante:  
Algunos modelos sin ícono de globo también pueden conectarse, como se explica en esta guía:
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Modo 2: Conexión mediante Tavily

Al usar modelos sin capacidad de conexión (sin ícono de globo), pero necesitando procesar información en tiempo real, usa el servicio de búsqueda Tavily.

**Primer uso de Tavily**:  
Aparecerá una ventana para configurar los datos. ¡Sigue las instrucciones! Es sencillo.

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Haz clic: Configurar</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Obtén la clave</p></figcaption></figure>

Al hacer clic, se abrirá **tavily.com**. Regístrate, crea una API key y cópiala en Cherry Studio.

{% hint style="danger" %}
¿Problemas con el registro? Consulta la guía de Tavily en este directorio.
{% endhint %}

**Documento de referencia:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Esta pantalla confirma el registro exitoso:

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copia la clave</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Pega la clave - ¡Configuración completada!</p></figcaption></figure>

Verifica el funcionamiento. Los resultados muestran búsquedas exitosas (valor predeterminado: 5 fuentes).

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
¡Atención! Tavily tiene límites mensuales gratuitos. El exceso requiere pago.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PD: Si encuentras errores, contáctanos.