---
icon: book-bookmark
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Conocimiento Científico

## ¿Qué son los tokens?

Los tokens son la unidad básica que utilizan los modelos de IA para procesar texto. Pueden entenderse como la unidad mínima de "pensamiento" del modelo. No equivalen exactamente a caracteres o palabras tal como los entendemos, sino que representan una forma especial de segmentación de texto propia del modelo.

#### 1. Segmentación de textos en chino

* Un carácter chino suele codificarse en 1-2 tokens
* Ejemplo: `"你好"` ≈ 2-4 tokens

#### 2. Segmentación de textos en inglés

* Las palabras comunes suelen ser 1 token
* Palabras largas o poco comunes se descomponen en múltiples tokens
* Ejemplo:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caracteres especiales

* Los espacios, signos de puntuación también consumen tokens
* El salto de línea suele ser 1 token

{% hint style="info" %}
El Tokenizer es diferente en cada proveedor de servicios, e incluso varía entre modelos del mismo proveedor. Este conocimiento solo tiene como objetivo aclarar el concepto de token.
{% endhint %}

***

## ¿Qué es un Tokenizer?

El Tokenizer (segmentador) es la herramienta que convierte texto en tokens para los modelos de IA. Determina cómo dividir el texto de entrada en las unidades mínimas que el modelo puede entender.

### ¿Por qué el Tokenizer es diferente en cada modelo?

#### 1. Datos de entrenamiento diferentes

* Distintos corpus conducen a diferentes optimizaciones
* Niveles variables de soporte multilingüe
* Optimizaciones específicas para áreas como medicina, derecho, etc.

#### 2. Algoritmos de segmentación diferentes

* BPE (Byte Pair Encoding) - Serie GPT de OpenAI
* WordPiece - Google BERT
* SentencePiece - Adecuado para escenarios multilingües

#### 3. Objetivos de optimización diferentes

* Algunos enfocados en eficiencia de compresión
* Otros en preservación semántica
* Otros en velocidad de procesamiento

### Impacto práctico

El mismo texto puede tener diferente número de tokens en distintos modelos:

```
Entrada: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## ¿Qué son los modelos de incrustación (Embedding Model)?

**Concepto básico:** Los modelos de incrustación transforman datos discretos de alta dimensión (texto, imágenes) en vectores continuos de baja dimensión, permitiendo a las máquinas comprender y procesar mejor datos complejos. Imagine convertir un puzle complejo en un punto de coordenadas simple que mantiene las características clave. En el ecosistema de modelos grandes, actúan como "traductores" que convierten información comprensible para humanos a formato numérico calculable por IA.

**Funcionamiento:** En procesamiento del lenguaje natural, estos modelos mapean palabras a posiciones específicas en espacios vectoriales. En este espacio, palabras semánticamente cercanas se agrupan naturalmente. Por ejemplo:

* Los vectores de "rey" y "reina" estarán próximos
* Palabras de mascotas como "gato" y "perro" estarán cercanas
* Palabras no relacionadas como "coche" y "pan" estarán distantes

**Principales aplicaciones:**

* Análisis de texto: Clasificación de documentos, análisis de sentimientos
* Sistemas de recomendación: Recomendaciones de contenido personalizado
* Procesamiento de imágenes: Búsqueda de imágenes similares
* Motores de búsqueda: Optimización de búsqueda semántica

**Ventajas clave:**

1. Reducción dimensional: Simplificación de datos complejos en vectores manejables
2. Preservación semántica: Mantiene información semántica crítica de datos originales
3. Eficiencia computacional: Mejora significativa en entrenamiento e inferencia de modelos

**Valor técnico:** Estos modelos son componentes fundamentales de sistemas modernos de IA, proporcionando representaciones de datos de alta calidad para tareas de aprendizaje automático, siendo una tecnología clave en campos como PLN y visión computacional.

***

## Funcionamiento de Embedding en recuperación de conocimiento

**Flujo básico de trabajo:**

1. **Fase de preprocesamiento del conocimiento**
   
* Divide documentos en fragmentos (chunks) de tamaño adecuado
* Convierte cada fragmento en vector usando embedding
* Almacena vectores y texto original en base de datos vectorial

2. **Fase de procesamiento de consultas**
   
* Convierte preguntas de usuarios en vectores
* Recupera contenido similar en la base vectorial
* Proporciona el contexto recuperado al modelo de lenguaje (LLM)

***

## ¿Qué es MCP (Model Context Protocol)?

MCP es un protocolo open-source que proporciona información contextual a modelos de lenguaje (LLM) de forma estandarizada.

* **Analogía:** Imagine MCP como una "memoria USB" para IA. Así como la USB almacena archivos que se usan al conectarse, el servidor MCP puede "conectar" varios "plugins" contextuales que los LLM solicitan según necesidad, obteniendo contexto enriquecido para mejorar sus capacidades.
* **Comparación con Function Tool:** Las herramientas tradicionales (Function Tool) ofrecen funcionalidad externa, pero MCP es una abstracción superior. Mientras Function Tool es específico, MCP ofrece un mecanismo contextual modular y universal.

### Ventajas clave de MCP

1. **Estandarización:** Interface y formato de datos unificados para colaboración entre distintos LLM y proveedores de contexto
2. **Modularidad:** Permite dividir información contextual en módulos (plugins) independientes
3. **Flexibilidad:** LLM pueden seleccionar dinámicamente plugins según necesidades
4. **Escalabilidad:** Diseñado para incorporar nuevos tipos de plugins contextuales