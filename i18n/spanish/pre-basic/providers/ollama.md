
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Ollama

Ollama es una excelente herramienta de código abierto que te permite ejecutar y administrar fácilmente varios modelos de lenguaje grandes (LLMs) localmente. ¡Cherry Studio ahora soporta integración con Ollama, permitiéndote interactuar directamente con LLMs implementados localmente en una interfaz familiar, sin depender de servicios en la nube!

## ¿Qué es Ollama?

Ollama es una herramienta que simplifica la implementación y uso de modelos de lenguaje grandes (LLMs). Tiene las siguientes características:

* **Ejecución local:** Los modelos funcionan completamente en tu computadora local, sin necesidad de conexión a Internet, protegiendo tu privacidad y seguridad de datos.
* **Sencillo y fácil de usar:** Con simples comandos de terminal, puedes descargar, ejecutar y administrar varios LLMs.
* **Amplia variedad de modelos:** Soporta modelos populares de código abierto como Llama 2, Deepseek, Mistral, Gemma y otros.
* **Multiplataforma:** Compatible con macOS, Windows y Linux.
* **API abierta:** Soporta interfaces compatibles con OpenAI, permitiendo integración con otras herramientas.

## ¿Por qué usar Ollama en Cherry Studio?

* **Sin servicios en la nube:** Libre de limitaciones de cuotas y costos de API en la nube, disfruta plenamente de las potentes funciones de LLMs locales.
* **Privacidad de datos:** Todas tus conversaciones permanecen localmente, sin preocupaciones por fugas de privacidad.
* **Funcionalidad offline:** Interactúa con LLMs incluso sin conexión a Internet.
* **Personalización:** Selecciona y configura el LLM que mejor se adapte a tus necesidades.

## Configurar Ollama en Cherry Studio

### **1. Instalar y ejecutar Ollama**

Primero, necesitas instalar y ejecutar Ollama en tu computadora. Sigue estos pasos:

*   **Descargar Ollama:** Visita el sitio oficial de Ollama ([https://ollama.com/](https://ollama.com/)) y descarga el paquete de instalación según tu sistema operativo.\
    En Linux, puedes instalar Ollama directamente ejecutando:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Instalar Ollama:** Sigue las instrucciones del instalador para completar la instalación.
*   **Descargar modelos:** Abre la terminal (o símbolo del sistema) y usa el comando `ollama run` para descargar el modelo que deseas usar. Por ejemplo, para descargar el modelo Llama 2, ejecuta:

    ```sh
    ollama run llama3.2
    ```

    Ollama descargará y ejecutará automáticamente el modelo.
* **Mantener Ollama en ejecución:** Asegúrate de que Ollama permanezca activo mientras uses Cherry Studio para interactuar con los modelos.

### **2. Añadir Ollama como proveedor en Cherry Studio**

Ahora, añade Ollama como proveedor personalizado de servicios de IA en Cherry Studio:

* **Abrir configuración:** En la barra de navegación izquierda de Cherry Studio, haz clic en "Settings" (icono de engranaje).
* **Acceder a servicios de modelos:** En la página de configuración, selecciona la pestaña "Model Services".
* **Añadir proveedor:** Haz clic en "Ollama" en la lista.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configurar el proveedor Ollama**

En la lista de proveedores, localiza Ollama y configura los detalles:

1. **Estado de activación:**
   * Asegúrate de que el interruptor a la derecha de Ollama esté activado (ON).
2. **Clave de API:**
   * Ollama **no requiere** clave API por defecto. Deja este campo vacío o ingresa cualquier valor.
3. **Dirección API:**
   *    Ingresa la dirección API local de Ollama. Normalmente es:

       ```
       http://localhost:11434/
       ```

       Si cambiaste el puerto, ajústalo según corresponda.
4. **Tiempo de mantenimiento activo:** Configura la duración de la sesión (en minutos). Si no hay nuevas interacciones durante este tiempo, Cherry Studio desconectará automáticamente Ollama para liberar recursos.
5. **Gestión de modelos:**
   * Haz clic en "+ Add" para añadir manualmente los nombres de los modelos que ya descargaste en Ollama.
   * Por ejemplo, si descargaste `llama3.2` con `ollama run llama3.2`, ingresa `llama3.2`.
   * Usa el botón "Manage" para editar o eliminar modelos añadidos.

## Comenzar a usar

¡Después de completar esta configuración, podrás seleccionar el proveedor Ollama y tus modelos descargados en la interfaz de chat de Cherry Studio para conversar con tus LLMs locales!

## Consejos y sugerencias

* **Primera ejecución de modelos:** Ollama descargará los archivos del modelo durante la primera ejecución, lo que puede tomar tiempo. Sé paciente.
* **Ver modelos disponibles:** Ejecuta `ollama list` en la terminal para ver los modelos de Ollama que has descargado.
* **Requisitos de hardware:** Ejecutar modelos grandes requiere recursos considerables (CPU, RAM, GPU). Asegúrate que tu equipo cumpla con los requisitos.
* **Documentación de Ollama:** Haz clic en `View Ollama Docs & Models` en la página de configuración para acceder rápidamente a la documentación oficial.