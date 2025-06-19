---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Vertex AI

## Resumen del Tutorial

### 1. Obtener la clave API

*   Para obtener la clave API de Gemini, primero necesitas tener un proyecto de Google Cloud (puedes omitir este paso si ya tienes uno)
*   Crea un proyecto en [Google Cloud](https://console.cloud.google.com/projectcreate), completa el nombre del proyecto y haz clic en "Crear proyecto"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   Accede a la [consola de Vertex AI](https://console.cloud.google.com/vertex-ai)
*   Habilita [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) en el proyecto creado

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurar permisos de acceso a la API

*   Abre la página de permisos de [cuentas de servicio](https://console.cloud.google.com/iam-admin/serviceaccounts) y crea una cuenta de servicio

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   En la página de gestión de cuentas de servicio, localiza la cuenta recién creada, haz clic en `Claves` y crea una nueva clave en formato JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   Después de crearse correctamente, el archivo de clave se guardará automáticamente en formato JSON en tu computadora. **Consérvalo adecuadamente**

## 3. Configurar Vertex AI en Cherry Studio

*   Selecciona el proveedor de servicios Vertex AI
*   Completa los campos correspondientes con los datos del archivo JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

¡Haz clic para agregar [modelos](https://console.cloud.google.com/vertex-ai/model-garden) y podrás comenzar a usarlo con gusto!\