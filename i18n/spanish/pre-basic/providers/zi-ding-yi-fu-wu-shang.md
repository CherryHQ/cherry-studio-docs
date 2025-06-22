
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Proveedores personalizados

Cherry Studio no solo integra los principales servicios de modelos de IA, sino que también te brinda un poderoso control de personalización. A través de la función **Proveedores de IA personalizados**, puedes integrar fácilmente cualquier modelo de IA que necesites.

## ¿Por qué utilizar proveedores de IA personalizados?

* **Flexibilidad:** No te limites a la lista preconfigurada de proveedores, elige libremente el modelo de IA que mejor se adapte a tus necesidades.
* **Diversidad:** Prueba modelos de IA de diferentes plataformas y descubre sus ventajas únicas.
* **Control:** Administra directamente tus claves API y direcciones de acceso, garantizando seguridad y privacidad.
* **Personalización:** Integra modelos implementados de forma privada para satisfacer necesidades específicas de tu negocio.

## ¿Cómo agregar proveedores de IA personalizados?

Sigue estos simples pasos para agregar proveedores personalizados en Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Abrir configuración:** En la barra de navegación izquierda de Cherry Studio, haz clic en "Configuración" (icono de engranaje).
2. **Ir a servicios de modelos:** En la página de configuración, selecciona la pestaña "Servicios de modelos".
3. **Agregar proveedor:** En la página de servicios de modelos, verás la lista de proveedores existentes. Haz clic en el botón "+ Agregar" para abrir el cuadro emergente "Agregar proveedor".
4. **Completar información:** En el cuadro emergente, debes ingresar lo siguiente:
   * **Nombre del proveedor:** Un nombre identificable (ej: MyCustomOpenAI).
   * **Tipo de proveedor:** Selecciona el tipo en el menú desplegable. Actualmente compatibles:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Guardar configuración:** Haz clic en "Agregar" para guardar la configuración.

## Configuración de proveedores personalizados

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Después de agregarlo, configura el proveedor en la lista:

1. **Estado de activación:** El interruptor en el extremo derecho activa/desactiva el servicio personalizado.
2. **Clave API:**
   * Ingresa la clave API proporcionada por tu proveedor de IA.
   * Haz clic en el botón "Comprobar" para verificar su validez.
3. **URL de la API:**
   * Ingresa la URL base de acceso a la API.
   * Consulta siempre la documentación oficial de tu proveedor.
4.  **Gestión de modelos:**

    * Haz clic en "+ Agregar" para añadir manualmente los ID de modelos que usarás (ej: `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Si no conoces los nombres específicos, consulta la documentación oficial.
    * Haz clic en "Gestionar" para editar o eliminar modelos.

## Comenzar a utilizar

¡Después de completar la configuración, selecciona tu proveedor y modelo personalizado en el chat de Cherry Studio para comenzar!

## Usar vLLM como proveedor personalizado

vLLM es una biblioteca de inferencia LLM rápida y sencilla (similar a Ollama). Pasos para integrarlo:

1.  **Instalar vLLM:** Sigue la documentación oficial ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # si usas pip
    uv pip install vllm # si usas uv
    ```
2.  **Iniciar servicio vLLM:** Usa su interfaz compatible con OpenAI. Dos métodos principales:

    * Usando `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Usando `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

El servicio se inicia en el puerto `8000` por defecto. Puedes cambiar el puerto con `--port`.

3. **Agregar proveedor vLLM en Cherry Studio:**
   * Sigue los pasos para agregar nuevo proveedor.
   * **Nombre:** `vLLM`
   * **Tipo:** Selecciona `OpenAI`.
4. **Configurar proveedor vLLM:**
   * **Clave API:** Déjalo vacío o ingresa cualquier valor (vLLM no requiere clave).
   * **URL API:** Ingresa la URL del servicio (por defecto: `http://localhost:8000/`).
   * **Gestión de modelos:** Agrega el nombre del modelo cargado. Ej: `gpt2`.
5. **Comenzar chat:** ¡Selecciona vLLM y el modelo en Cherry Studio para interactuar!

## Consejos prácticos

* **Lee detenidamente la documentación:** Antes de agregar proveedores, revisa la documentación oficial sobre claves API, URLs y nombres de modelos.
* **Verifica las claves API:** Usa el botón "Comprobar" para evitar errores.
* **Presta atención a las URLs API:** Varían según proveedores y modelos.
* **Administra modelos eficientemente:** Agrega solo los modelos que realmente utilizarás.