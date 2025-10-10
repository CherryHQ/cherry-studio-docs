---
description: Tools
icon: code
---
# Tutorial de uso de Code Tools


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio v1.5.7 introdujo la función de Code Agent, una herramienta poderosa y fácil de usar que permite ejecutar y gestionar múltiples agentes de programación IA. Este tutorial te guiará por el proceso completo de configuración e inicio.

***

### Pasos de operación

#### 1. Actualizar Cherry Studio

Primero, asegúrate de tener Cherry Studio actualizado a **v1.5.7** o superior. Puedes descargar la última versión desde [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) o el sitio web oficial.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 2. Ajustar posición de la barra de navegación

Para facilitar el uso de las pestañas superiores, recomendamos mover la barra de navegación a la parte superior.
* Ruta: `Configuración` → `Ajustes de visualización` → `Configuración de barra de navegación`
* Establece la opción "Posición de la barra de navegación" en **`Superior`**.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Crear nueva pestaña

Haz clic en el icono "+" en la parte superior para crear una nueva pestaña en blanco.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Activar función Code Agent

En la nueva pestaña, haz clic en el icono `Code` (o `</>`) para acceder a la interfaz de configuración de Code Agent.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Seleccionar herramienta CLI

Elige una herramienta Code Agent según tus necesidades y API Key disponible. Actualmente se admiten:
* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Seleccionar modelo para el Agent

En el menú desplegable, elige un modelo compatible con tu herramienta CLI seleccionada. *(Consulta "Notas importantes" más abajo para detalles de compatibilidad)*

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Especificar directorio de trabajo

Haz clic en "Seleccionar directorio" para asignar una ubicación de trabajo al Agent. Este tendrá acceso completo a todos los archivos y subdirectorios para entender el contexto del proyecto.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configurar variables de entorno
* **Configuración automática**: Tus selecciones en los pasos 6 (modelo) y 7 (directorio) generarán automáticamente las variables correspondientes.
* **Adición personalizada**: Si tu proyecto requiere variables específicas adicionales (como `PROXY_URL`), añádelas aquí.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Opciones de actualización
* **Archivos ejecutables integrados**: Cherry Studio incluye todos los ejecutables necesarios para los Code Agents, funcionando sin conexión en la mayoría de casos.
* **Actualización automática**: Marca **`Comprobar actualizaciones e instalar última versión`** para mantener siempre actualizado el Agent.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Iniciar Agent

Tras completar la configuración, haz clic en **`Iniciar`**. Cherry Studio abrirá la Terminal de tu sistema, cargará las variables de entorno y ejecutará el Code Agent elegido. ¡Ahora podrás interactuar con el AI Agent en la ventana de terminal!

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Notas importantes

1. **Compatibilidad de modelos**:
   * **Claude Code**: Requiere modelos compatibles con formato Anthropic API Endpoint. Modelos oficialmente soportados:
     * Serie Claude
     * DeepSeek V3.1 (plataforma API oficial)
     * Kimi K2 (plataforma API oficial)
     * GLM 4.5 de Zhipu (plataforma API oficial)
     * **Nota**: Muchos proveedores externos (One API, New API) actualmente solo soportan formato OpenAI para DeepSeek/Kimi/GLM, lo que puede causar incompatibilidad.
   * **Gemini CLI**: Requiere modelos Gemini de Google.
   * **Qwen Code**: Soporta modelos con formato OpenAI Chat Completions API. Se recomienda **`Qwen3 Coder`** para máxima eficacia en generación de código.
   * **OpenAI Codex**: Compatible con modelos GPT (ej. `gpt-4o`, `gpt-5`).
   
2. **Conflictos de dependencias**:
   * Cherry Studio incluye un entorno Node.js independiente para evitar conflictos.
   * Si encuentras errores, considera **desinstalar dependencias globales conflictivas** (Node.js u otras herramientas).
   
3. **Advertencia de consumo de tokens**:
   * **Los Code Agents consumen tokens API masivamente**. Tareas complejas generan múltiples solicitudes que agotan rápidamente los tokens.
   * **Usa con moderación** según tu presupuesto API y monitorea constantemente el consumo para evitar gastos excesivos.

¡Esperamos que este tutorial te ayude a dominar la poderosa función Code Agent de Cherry Studio!