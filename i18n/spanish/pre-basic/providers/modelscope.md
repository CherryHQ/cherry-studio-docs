# Guía de Integración con la Plataforma ModelScope  


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}



## ¿Qué es ModelScope?  
> ModelScope es una nueva plataforma de código abierto para compartir modelos como servicio (MaaS). Está dedicada a proporcionar a los desarrolladores de IA una solución de **flexible, fácil de usar y de bajo costo** para servicios de modelos integrados, haciendo que la aplicación de modelos sea más simple.  
>  
> A través de la capacidad de **servicio de inferencia API**, la plataforma estandariza modelos de código abierto como interfaces API invocables. Los desarrolladores pueden integrar capacidades de modelos en diversas aplicaciones de IA de manera ligera y rápida, admitiendo escenarios innovadores como llamadas de herramientas y desarrollo de prototipos.  

### Ventajas Clave  
- ✅ **Cupo Gratuito**: Proporciona **2000 llamadas API gratuitas diarias** ([Reglas de Facturación](#Facturación-y-Reglas-de-Cupo))  
- ✅ **Biblioteca de Modelos Rica**: Cubre más de 1000 modelos de código abierto en NLP, CV, voz, multimodal, etc.  
- ✅ **Listo para Usar**: Sin necesidad de implementación, llama rápidamente mediante API RESTful  

---  

## Proceso de Integración con Cherry Studio  
### Paso 1: Obtener Token de API de ModelScope  
1. **Iniciar Sesión en la Plataforma**  
   - Visita el [sitio oficial de ModelScope](https://modelscope.cn) → Haz clic en **Iniciar Sesión** en la esquina superior derecha → Selecciona método de autenticación  
   ![Interfaz de Inicio de Sesión](../../.gitbook/assets/ModelScope/image.png)  
2. **Crear Token de Acceso**  
   - Ve a **[Configuración de Cuenta → Tokens de Acceso](https://modelscope.cn/my/myaccesstoken)**  
   - Haz clic en **`Crear Nuevo Token`** → Completa la descripción → **Copia el token generado** (*ejemplo en la imagen*)  
   ![Ejemplo de Creación de Token](../../.gitbook/assets/ModelScope/image-7.png)  
   > 🔑 **Importante**: ¡La exposición del token compromete la seguridad de la cuenta!  

### Paso 2: Configurar Cherry Studio  
- Abre **Cherry Studio** → **Configuración → Servicio de Modelos → ModelScope**  
- Pega el token copiado en el campo `Clave API`  
  ![Interfaz de Configuración](../../.gitbook/assets/ModelScope/image-2.png)  
- Haz clic en **`Guardar`** para completar la autorización  

### Paso 3: Llamar a la API del Modelo  
1. **Buscar Modelos Compatibles con API**  
   - Visita el [Repositorio de Modelos de ModelScope](https://modelscope.cn/models)  
   - Filtro: **Marca `API-Inferencia`** (o busca el ícono `API` en la tarjeta del modelo)  
   ![Filtrado de Modelos API](../../.gitbook/assets/ModelScope/image-3.png)  
   > El alcance de los modelos cubiertos por API-Inferencia se determina principalmente por el nivel de atención del modelo en la comunidad (considerando datos como "me gusta" y descargas). Por lo tanto, la lista de modelos admitidos se actualizará continuamente según los nuevos modelos de código abierto más potentes.  
2. **Obtener el ID del Modelo**  
   - Ve a la página de detalles del modelo objetivo → Copia el **Model ID** (formato como `damo/nlp_structbert_sentiment-classification_chinese-base`)  
   ![Copiar Model ID](../../.gitbook/assets/ModelScope/image-5.png)  
3. **Introducir en Cherry Studio**  
   - Ingresa el ID en el campo `ID del Modelo` de la página de configuración → Selecciona el tipo de tarea → Completa la configuración  
   ![Ingresar el ID del Modelo](../../.gitbook/assets/ModelScope/image-6.png)  

---  

## Facturación y Reglas de Cupo  
### Notas Importantes  
- 🎫 **Cupo Gratuito**: Cada usuario tiene **2000 llamadas API diarias** (*sujeto a las últimas reglas del sitio oficial*)  
- 🔁 **Reinicio del Cupo**: Se reinicia automáticamente diariamente a las 00:00 UTC+8, **no es acumulable ni mejorable**  
- 💡 **Exceder el Cupo**:  
  - Al alcanzar el límite diario, la API devolverá `Error 429`  
  - Solución: Cambiar a cuenta alternativa / Usar otras plataformas / Optimizar frecuencia de llamadas  

### Ver Cupo Restante  
- Inicia sesión en ModelScope → Haz clic en el **`nombre de usuario`** superior derecho → **`Uso de API`**  
  ![Ubicación para Ver Cupo](../../.gitbook/assets/ModelScope/image-8.png)  

> ⚠️ Atención: La API de inferencia API-Inference tiene un cupo diario gratuito de 2000 llamadas. Para mayores necesidades, considera usar servicios en la nube como Alibaba Cloud Bailian.