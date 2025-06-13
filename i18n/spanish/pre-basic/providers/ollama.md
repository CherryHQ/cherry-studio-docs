
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Ollama

Ollama es una excelente herramienta de código abierto que le permite ejecutar y gestionar fácilmente diversos Modelos de Lenguaje Grande (LLMs) de forma local. ¡Cherry Studio ahora es compatible con la integración de Ollama, lo que le permite interactuar directamente con LLMs implementados localmente en una interfaz familiar, sin depender de servicios en la nube!

## ¿Qué es Ollama?

Ollama es una herramienta que simplifica la implementación y el uso de Modelos de Lenguaje Grande (LLMs). Ofrece las siguientes características:

* **Ejecución local:** Los modelos se ejecutan completamente en su computadora local, sin necesidad de conexión a Internet, protegiendo su privacidad y seguridad de datos.
* **Simple y fácil de usar:** Mediante simples comandos de terminal, puede descargar, ejecutar y administrar diversos LLMs.
* **Amplia variedad de modelos:** Admite múltiples modelos de código abierto populares como Llama 2, Deepseek, Mistral, Gemma, entre otros.
* **Multiplataforma:** Compatible con sistemas macOS, Windows y Linux.
* **API abierta:** Admite una interfaz compatible con OpenAI, permitiendo su integración con otras herramientas.

## ¿Por qué usar Ollama en Cherry Studio?

* **Sin necesidad de servicios en la nube:** Elimina las limitaciones de cuotas y costos de APIs en la nube, permitiéndole disfrutar plenamente de las poderosas funciones de los LLMs locales.
* **Privacidad de datos:** Todos sus datos de conversación permanecen locales, sin preocupaciones sobre fugas de privacidad.
* **Funcionalidad sin conexión:** Puede continuar interactuando con LLMs incluso sin conexión a Internet.
* **Personalización:** Puede seleccionar y configurar el LLM que mejor se adapte a sus necesidades.

## Configurar Ollama en Cherry Studio

### **1. Instalar y ejecutar Ollama**

Primero, debe instalar y ejecutar Ollama en su computadora. Siga estos pasos:

*   **Descargar Ollama:** Visite el sitio oficial de Ollama ([https://ollama.com/](https://ollama.com/)) y descargue el paquete de instalación correspondiente a su sistema operativo.\
    En Linux, puede instalar ollama directamente con este comando:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Instalar Ollama:** Complete la instalación siguiendo las instrucciones del programa de instalación.
*   **Descargar modelos:** Abra la terminal (o Símbolo del sistema) y use el comando `ollama run` para descargar el modelo que desee utilizar. Por ejemplo, para descargar el modelo Llama 2, ejecute:

    ```sh
    ollama run llama3.2
    ```

    Ollama descargará y ejecutará automáticamente el modelo.
* **Mantener Ollama en ejecución:** Asegúrese de que Ollama permanezca en ejecución mientras utiliza Cherry Studio para interactuar con los modelos.

### **2. Agregar Ollama como proveedor en Cherry Studio**

A continuación, agregue Ollama como proveedor de IA personalizado en Cherry Studio:

* **Abrir configuración:** En la barra de navegación izquierda de Cherry Studio, haga clic en "Configuración" (icono de engranaje).
* **Ir a servicios de modelos:** En la página de configuración, seleccione la pestaña "Servicios de modelos".
* **Agregar proveedor:** Haga clic en Ollama en la lista.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configurar el proveedor Ollama**

Localice Ollama en la lista de proveedores y realice la configuración detallada:

1. **Estado de activación:**
   * Asegúrese de que el interruptor de la derecha esté activado, lo que indica que el servicio está habilitado.
2. **Clave API:**
   * Ollama **no requiere** clave API por defecto. Puede dejar este campo vacío o ingresar cualquier texto.
3. **Dirección API:**
   *    Ingrese la dirección API local proporcionada por Ollama. Normalmente es:

       ```
       http://localhost:11434/
       ```

       Si cambió el puerto, modifíquela aquí.
4. **Tiempo de mantenimiento activo:** Esto configura la duración de la sesión en minutos. Si no hay nuevos diálogos durante este tiempo, Cherry Studio cerrará la conexión con Ollama automáticamente para liberar recursos.
5. **Gestión de modelos:**
   * Haga clic en "+ Agregar" para añadir manualmente los nombres de los modelos descargados en Ollama.
   * Por ejemplo, si descargó `llama3.2` con `ollama run llama3.2`, ingrese aquí `llama3.2`.
   * Utilice el botón "Gestionar" para editar o eliminar modelos añadidos.

## Comenzar a utilizar

¡Una vez completada esta configuración, podrá seleccionar el proveedor Ollama y sus modelos descargados en la interfaz de chat de Cherry Studio para empezar a conversar con LLMs locales!

## Consejos y sugerencias

* **Primera ejecución del modelo:** Durante la primera ejecución de un modelo, Ollama descarga los archivos necesarios, lo que puede tardar bastante tiempo. Por favor, sea paciente.
* **Ver modelos disponibles:** Ejecute `ollama list` en la terminal para ver su lista de modelos descargados.
* **Requisitos de hardware:** Ejecutar modelos grandes requiere recursos computacionales (CPU, memoria, GPU). Asegúrese de que su computadora cumpla con los requisitos.
* **Documentación de Ollama:** Haga clic en `Ver documentación y modelos de Ollama` en la página de configuración para acceder rápidamente a la documentación oficial.