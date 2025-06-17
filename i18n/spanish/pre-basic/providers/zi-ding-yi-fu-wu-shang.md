
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Proveedores Personalizados

Cherry Studio no solo integra los principales servicios de modelos de IA, sino que también te brinda potentes capacidades de personalización. A través de la función **Proveedores de IA personalizados**, puedes conectar fácilmente cualquier modelo de IA que necesites.

## ¿Por qué usar proveedores de IA personalizados?

* **Flexibilidad:** Sin limitarte a la lista predefinida de proveedores, eliges libremente el modelo de IA que mejor se adapte a tus necesidades.
* **Diversidad:** Prueba modelos de IA de diversas plataformas para descubrir sus ventajas únicas.
* **Control:** Gestiona directamente tus claves API y direcciones de acceso, garantizando seguridad y privacidad.
* **Personalización:** Conecta modelos implementados de forma privada para satisfacer necesidades específicas de negocio.

## ¿Cómo agregar un proveedor de IA personalizado?

En solo unos pasos puedes agregar tu proveedor de IA personalizado en Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Abrir configuración:** En la barra de navegación izquierda de Cherry Studio, haz clic en "Configuración" (icono de engranaje).
2. **Acceder a servicios de modelos:** En la página de configuración, selecciona la pestaña "Servicios de modelos".
3. **Agregar proveedor:** En la página "Servicios de modelos", verás la lista de proveedores existentes. Haz clic en el botón "+ Agregar" para abrir la ventana emergente "Agregar proveedor".
4. **Completar información:** En la ventana emergente, completa estos campos:
   * **Nombre del proveedor:** Asigna un nombre reconocible (ej: MyCustomOpenAI).
   * **Tipo de proveedor:** Selecciona del menú desplegable. Actualmente soportados:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Guardar configuración:** Haz clic en "Agregar" para guardar.

## Configurar proveedores de IA personalizados

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Tras agregarlo, configura tu proveedor en la lista:

1. **Estado de activación:** En el extremo derecho encontrarás un interruptor; actívalo para habilitar el servicio.
2. **Clave API:**
   * Ingresa la clave API proporcionada por tu proveedor.
   * Usa el botón "Verificar" para validarla.
3. **Dirección API:**
   * Ingresa la URL base de acceso al servicio.
   * Consulta siempre la documentación oficial para obtenerla correctamente.
4. **Gestión de modelos:**
   * Haz clic en "+ Agregar" para añadir manualmente los IDs de modelos (ej: `gpt-3.5-turbo`, `gemini-pro`).
   
    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>
   
   * Consulta la documentación oficial si desconoces los nombres específicos.
   * Usa "Gestionar" para editar o eliminar modelos existentes.

## Comenzar a usar

¡Tras completar la configuración, podrás seleccionar tu proveedor y modelo personalizados en el chat de Cherry Studio para conversar con la IA!

## Usar vLLM como proveedor de IA personalizado

vLLM es una biblioteca de inferencia LLM rápida y fácil de usar, similar a Ollama. Pasos para integrarlo con Cherry Studio:

1. **Instalar vLLM:** Sigue la documentación oficial ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # si usas pip
    uv pip install vllm # si usas uv
    ```
2. **Iniciar servicio vLLM:** Activa el servicio con interfaz compatible OpenAI. Dos métodos principales:

    * Usando `vllm.entrypoints.openai.api_server`:
    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Usando `uvicorn`:
    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

    El servicio se ejecuta en el puerto `8000` por defecto. Usa `--port` para especificar otro puerto.

3. **Agregar vLLM en Cherry Studio:**
   * Sigue los pasos anteriores para agregar un nuevo proveedor.
   * **Nombre del proveedor:** `vLLM`
   * **Tipo de proveedor:** Selecciona `OpenAI`.
4. **Configurar vLLM:**
   * **Clave API:** Déjala vacía o ingresa cualquier valor (vLLM no requiere clave).
   * **Dirección API:** Usa `http://localhost:8000/` (ajusta si cambiaste el puerto).
   * **Gestión de modelos:** Ingresa el nombre del modelo cargado en vLLM. Por ejemplo, si ejecutaste `--model gpt2`, ingresa `gpt2`.
5. **Iniciar conversación:** ¡Selecciona el proveedor vLLM y el modelo `gpt2` para dialogar con el LLM impulsado por vLLM!

## Consejos y trucos

* **Documentación:** Siempre consulta la documentación oficial del proveedor para claves API, direcciones y nombres de modelos.
* **Verificar clave:** Usa el botón "Verificar" para evitar errores por claves inválidas.
* **Dirección API exacta:** Las direcciones varían según proveedores y modelos; ingrésalas correctamente.
* **Modelos necesarios:** Agrega solo los modelos que realmente usarás, evitando saturar la lista.