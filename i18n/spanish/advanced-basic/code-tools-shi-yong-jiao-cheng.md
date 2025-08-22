---
description: Tools
icon: code
---
# Tutorial de uso de Code Tools


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




La versión Cherry Studio v1.5.7 presenta la potente función de Code Agent, que permite iniciar y gestionar diversos agentes de programación con IA. Este tutorial le guiará a través del proceso completo de configuración e inicio.

***

### Pasos de operación

#### 1. Actualizar Cherry Studio

Primero, asegúrese de tener Cherry Studio actualizado a la versión **v1.5.7** o superior. Puede descargar la última versión desde [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) o el sitio web oficial.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### 2. Ajustar posición de la barra de navegación

Para facilitar el uso de las pestañas superiores, recomendamos posicionar la barra de navegación en la parte superior.

* Ruta de configuración: `Ajustes` -> `Configuración de visualización` -> `Configuración de barra de navegación`
* Establezca la opción "Posición de barra de navegación" en **`Superior`**.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Crear nueva pestaña

Haga clic en el icono "+" en la parte superior de la interfaz para crear una nueva pestaña en blanco.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 4. Activar función Code Agent

En la nueva pestaña, haga clic en el icono `Code` (o `</>`) para acceder a la interfaz de configuración de Code Agent.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Seleccionar herramienta CLI

Elija una herramienta Code Agent según sus necesidades y las claves API disponibles. Actualmente se admiten:

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Seleccionar modelo para el agente

En el menú desplegable de modelos, seleccione uno compatible con su herramienta CLI elegida. _(Para detalles de compatibilidad, consulte "Notas importantes" más abajo)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Especificar directorio de trabajo

Haga clic en "Seleccionar directorio" para asignar un directorio de trabajo al agente. El agente tendrá acceso a todos los archivos y subdirectorios en esta ubicación para comprender el contexto del proyecto.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configurar variables de entorno

* **Configuración automática**: Sus selecciones en los pasos 6 (modelo) y 7 (directorio) generarán automáticamente variables de entorno correspondientes.
* **Adición personalizada**: Si su agente o proyecto requiere variables específicas adicionales (ej. `PROXY_URL`), puede agregarlas manualmente aquí.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Actualizar opciones

* **Ejecutables integrados**: Cherry Studio incluye ejecutables listos para usar para todos los Code Agents mencionados. En la mayoría de casos, podrá usarlos sin conexión a internet.
* **Actualización automática**: Si desea que el agente siempre tenga la última versión, marque la opción **`Comprobar actualizaciones e instalar la última versión`**. Al activarla, el programa verificará y actualizará el agente automáticamente al iniciar.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Iniciar el agente

Tras completar la configuración, haga clic en el botón **`Iniciar`**. Cherry Studio ejecutará automáticamente la Terminal de su sistema, cargará las variables de entorno y ejecutará el Code Agent seleccionado. Ya puede interactuar con el agente IA en la ventana de terminal.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Notas importantes

1. **Compatibilidad de modelos**:
   * **Claude Code**: Requiere modelos compatibles con formato Anthropic API Endpoint. Modelos oficialmente soportados:
     * Serie Claude
     * DeepSeek V3.1 (plataforma API oficial)
     * Kimi K2 (plataforma API oficial)
     * GLM 4.5 de Zhipu (plataforma API oficial)
     * **Nota**: Actualmente, muchos proveedores de servicios de terceros (ej. One API, New API) solo admiten formato OpenAI Chat Completions para DeepSeek, Kimi y GLM, pudiendo no ser compatibles con Claude Code hasta futuras adaptaciones.
   * **Gemini CLI**: Requiere modelos de la serie Gemini de Google.
   * **Qwen Code**: Modelos compatibles con formato OpenAI Chat Completions API. Se recomienda encarecidamente la serie **`Qwen3 Coder`** para óptimos resultados en generación de código.
   * **OpenAI Codex**: Modelos de la serie GPT (ej. `gpt-4o`, `gpt-5`).
2. **Dependencias y conflictos de entorno**:
   * Cherry Studio integra de forma independiente entornos Node.js, ejecutables de Code Agent y configuraciones de entorno para ofrecer una experiencia plug-and-play.
   * Si encuentra conflictos de dependencias al iniciar, considere **desinstalar o deshabilitar dependencias relacionadas instaladas globalmente** en su sistema (ej. Node.js global o herramientas específicas).
3. **Advertencia sobre consumo de tokens API**:
   * **Code Agent consume grandes cantidades de tokens API**. Tareas complejas pueden generar múltiples solicitudes para planificación y generación de código, agotando tokens rápidamente.
   * **Administre cuidadosamente** según su cuota y presupuesto API para evitar sobrecostes.

¡Esperamos que este tutorial le ayude a dominar la potente función Code Agent de Cherry Studio!