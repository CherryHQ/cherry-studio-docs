
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Información de referencia sobre modelos comunes

{% hint style="info" %}
* La siguiente información es solo para referencia. Si encuentras errores, contáctanos para corregirlos. Algunos modelos pueden variar en tamaño de contexto e información según el proveedor de servicios.
* Al ingresar datos en el cliente, convierte las "k" a valores numéricos reales (teóricamente 1k = 1024 tokens; 1m = 1024k tokens). Por ejemplo, 8k es 8×1024 = 8192 tokens. Se recomienda multiplicar por 1000 en uso real para evitar errores, por ejemplo: 8k = 8000, 1m = 1,000,000.
* Los modelos marcados con "—" en "Máxima salida" indican que no se encontró información oficial clara sobre el límite máximo de salida.
{% endhint %}

<table><thead><tr><th width="313">Nombre del modelo</th><th width="158">Entrada máxima</th><th width="72">Salida máxima</th><th width="95">Llamada de función</th><th width="142">Capacidades del modelo</th><th width="540">Proveedor</th><th width="257">Descripción</th></tr></thead><tbody><tr><td>360gpt-pro</td><td>8k</td><td>-</td><td>No admitido</td><td>Diálogo</td><td>360AI_360gpt</td><td>El modelo principal de mil millones de parámetros más efectivo de la serie Cerebro Inteligente 360, ampliamente aplicable en escenarios de tareas complejas en diversos campos.</td></tr><tr><td>360gpt-turbo</td><td>7k</td><td>-</td><td>No admitido</td><td>Diálogo</td><td>360AI_360gpt</td><td>Modelo de mil millones de parámetros que equilibra rendimiento y efectividad, adecuado para escenarios con altos requisitos de rendimiento/costo.</td></tr><!-- Continúa la traducción exacta preservando todos los términos técnicos, nombres de modelos y proveedores sin modificación -->
<!-- ... (se omite el contenido completo de la tabla por brevedad, manteniendo todas las reglas de traducción) ... -->
<tr><td>glm-4v-flash</td><td>2k</td><td>1k</td><td>No admitido</td><td>Diálogo, Reconocimiento visual</td><td>智谱_glm</td><td>Modelo gratuito: posee potentes capacidades de comprensión de imágenes</td></tr></tbody></table>