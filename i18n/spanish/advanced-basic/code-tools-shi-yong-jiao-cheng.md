---
description: Tools
icon: code
---
# Tutorial de uso de Code Tools


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio v1.5.7 introdujo la potente función Code Agent, de operación sencilla, que permite iniciar y gestionar múltiples agentes de programación AI. Este tutorial le guiará a través del proceso completo de configuración e inicio.

***

### Pasos de operación

#### 1. Actualizar Cherry Studio

Primero, asegúrese de que su Cherry Studio esté actualizado a la versión **v1.5.7** o superior. Puede descargar la última versión en [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) o en el sitio web oficial.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. Ajustar posición de la barra de navegación

Para facilitar el uso de las pestañas superiores, recomendamos mover la barra de navegación a la parte superior.

* Ruta de operación: `Configuración` → `Configuración de visualización` → `Configuración de barra de navegación`
* Establezca la opción "Posición de barra de navegación" en **`Superior`**.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Crear nueva pestaña

Haga clic en el icono "+" en la parte superior de la interfaz para crear una nueva pestaña en blanco.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Activar función Code Agent

En la nueva pestaña, haga clic en el icono `Code` (o `</>`) para acceder a la interfaz de configuración de Code Agent.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Seleccionar herramienta CLI

Según sus necesidades y las API Key disponibles, seleccione una herramienta Code Agent. Actualmente se admiten las siguientes:

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Seleccionar modelo para el Agent

En el menú desplegable de modelos, seleccione uno compatible con su herramienta CLI. _(Para detalles de compatibilidad, consulte "Notas importantes" más abajo)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Especificar directorio de trabajo

Haga clic en "Seleccionar directorio" para asignar un directorio de trabajo al Agent. Este tendrá acceso a todos los archivos y subdirectorios dentro de esta ruta para comprender el contexto del proyecto.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configurar variables de entorno

* **Configuración automática**: Sus selecciones en los pasos 6 (modelo) y 7 (directorio) generarán automáticamente las variables correspondientes.
* **Adición personalizada**: Si su Agent o proyecto requiere variables específicas adicionales (ej. `PROXY_URL`), puede agregarlas manualmente aquí.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Opciones de actualización

* **Ejecutables integrados**: Cherry Studio incluye ejecutables preinstalados para todos los Code Agent mencionados, permitiendo su uso offline en la mayoría de casos.
* **Actualización automática**: Si desea mantener siempre la última versión del Agent, active la opción **`Comprobar actualizaciones e instalar última versión`**. Al activarla, el programa verificará y actualizará el Agent en cada inicio.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Iniciar Agent

Tras completar la configuración, haga clic en **`Iniciar`**. Cherry Studio llamará automáticamente a la herramienta Terminal de su sistema, cargará las variables de entorno y ejecutará el Code Agent seleccionado. Ahora puede interactuar con el AI Agent en la ventana de terminal.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Notas importantes

1. **Compatibilidad de modelos**:
   * **Claude Code**: Requiere modelos compatibles con el formato Anthropic API Endpoint. Modelos oficialmente soportados:
     * Serie Claude
     * DeepSeek V3.1 (plataforma API oficial)
     * Kimi K2 (plataforma API oficial)
     * GLM 4.5 de Zhipu (plataforma API oficial)
     * **Nota**: Muchos proveedores terceros (ej. One API, New API) para DeepSeek/Kimi/GLM solo soportan formato OpenAI Chat Completions, pudiendo ser incompatibles con Claude Code actualmente.
   * **Gemini CLI**: Requiere modelos de la serie Gemini de Google.
   * **Qwen Code**: Soporta modelos con formato OpenAI Chat Completions API. Se recomienda usar modelos **`Qwen3 Coder`** para óptima generación de código.
   * **OpenAI Codex**: Soporta modelos GPT (ej. `gpt-4o`, `gpt-5`).
2. **Conflictos de dependencias**:
   * Cherry Studio incluye un entorno Node.js independiente, ejecutables de Code Agent y configuración de variables para un entorno limpio listo para usar.
   * Si encuentra conflictos o errores al iniciar, considere **desinstalar o desactivar dependencias globales** (ej. Node.js instalado globalmente) para resolver conflictos.
3. **Advertencia sobre consumo de tokens**:
   * **Code Agent consume enormes cantidades de tokens API**. Tareas complejas generan múltiples solicitudes que agotan rápidamente los tokens.
   * Monitoree cuidadosamente el uso de tokens según su presupuesto API para evitar sobrecostes.

¡Esperamos que este tutorial le ayude a dominar rápidamente la potente función Code Agent de Cherry Studio!