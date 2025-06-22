---
icon: book-bookmark
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Divulgación de Conocimientos

## ¿Qué son los tokens?

Los tokens son la unidad básica que los modelos de IA utilizan para procesar texto, y pueden entenderse como la unidad mínima de "pensamiento" del modelo. No son equivalentes exactos a caracteres o palabras como los entendemos los humanos, sino una forma especial de segmentación de texto propia del modelo.

#### 1. Segmentación de texto en chino
* Un carácter chino típicamente se codifica en 1-2 tokens
* Ejemplo: `"你好"` ≈ 2-4 tokens

#### 2. Segmentación de texto en inglés
* Las palabras comunes generalmente son 1 token
* Palabras largas o poco comunes se dividen en múltiples tokens
* Ejemplo:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caracteres especiales
* Los espacios, signos de puntuación también consumen tokens
* Un salto de línea suele ser 1 token

{% hint style="info" %}
Los Tokenizers varían entre proveedores de servicios, e incluso entre diferentes modelos del mismo proveedor. Este conocimiento solo sirve para comprender el concepto de token.
{% endhint %}

***

## ¿Qué es un Tokenizer?

El Tokenizer (segmentador de texto) es la herramienta que convierte texto en tokens para que los modelos de IA puedan procesarlo. Determina cómo dividir el texto de entrada en unidades mínimas comprensibles para el modelo.

### ¿Por qué los tokenizadores difieren entre modelos?

#### 1. Datos de entrenamiento diferentes
* Corpus diferentes conducen a enfoques de optimización distintos
* Grados variables de soporte multilingüe
* Optimizaciones específicas para dominios (médico, legal, etc.)

#### 2. Algoritmos de tokenización diferentes
* BPE (Byte Pair Encoding) - usado en la serie GPT de OpenAI
* WordPiece - usado en BERT de Google
* SentencePiece - adecuado para escenarios multilingües

#### 3. Objetivos de optimización diferentes
* Algunos priorizan eficiencia de compresión
* Otros enfatizan la preservación semántica
* Algunos optimizan velocidad de procesamiento

### Impacto práctico

El mismo texto puede tener diferentes recuentos de tokens en distintos modelos:

```
输入："Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## ¿Qué es un Modelo de Incrustación (Embedding Model)?

**Concepto básico:** Técnica que convierte datos discretos de alta dimensión (texto, imágenes) en vectores continuos de baja dimensión, permitiendo a las máquinas comprender y procesar mejor información compleja. Funciona como un "traductor" en el ecosistema de IA, transformando información humana a formato numérico procesable.

**Funcionamiento:** En procesamiento de lenguaje natural, mapea palabras a posiciones específicas en espacios vectoriales donde términos semánticamente similares se agrupan automáticamente. Por ejemplo:
* "rey" y "reina" tienen vectores cercanos
* "gato" y "perro" (como palabras de mascotas) también están próximos
* "coche" y "pan" (semánticamente no relacionados) están distantes

**Aplicaciones principales:**
* Análisis de texto: clasificación documental, análisis de sentimientos
* Sistemas de recomendación: contenido personalizado
* Procesamiento de imágenes: búsqueda de imágenes similares
* Motores de búsqueda: optimización semántica

**Ventajas clave:**
1. Reducción dimensional: simplifica datos complejos a vectores manejables
2. Preservación semántica: mantiene relaciones semánticas críticas
3. Eficiencia computacional: mejora entrenamiento e inferencia de modelos

**Valor técnico:** Componente fundamental de sistemas modernos de IA que proporciona representaciones de datos de alta calidad para tareas de aprendizaje automático, clave en avances de PNL y visión computacional.

***

## Funcionamiento de Embeddings en Recuperación de Conocimiento

**Flujo básico:**

1. **Preprocesamiento del repositorio**
* Segmentación de documentos en chunks (fragmentos)
* Conversión de cada chunk a vector mediante embedding
* Almacenamiento de vectores y texto en base de datos vectorial

2. **Procesamiento de consultas**
* Conversión de preguntas de usuario a vectores
* Recuperación de contenido similar en el almacén vectorial
* Suministro de contexto relevante al LLM (Large Language Model)

***

## ¿Qué es MCP (Model Context Protocol)?

Protocolo de código abierto que proporciona contexto a LLMs mediante un enfoque estandarizado.

* **Analogía:** MCP funciona como una "unidad USB" para IA: almacena módulos de contexto ("archivos") que los LLMs pueden "conectar" según necesidad para enriquecer capacidades.
* **Comparación con Herramientas de Función:** Mientras estas ofrecen funcionalidades específicas, MCP constituye una abstracción de mayor nivel para adquisición modular de contexto.

### Ventajas clave de MCP

1. **Estandarización:** Interfaz unificada para colaboración fluida entre LLMs y proveedores de contexto
2. **Modularidad:** Contexto organizado en componentes independientes (plugins) para gestión y reutilización
3. **Flexibilidad:** Selección dinámica de módulos según necesidades específicas de interacción
4. **Escalabilidad:** Diseño extensible que admite nuevos tipos de plugins para ampliar capacidades de LLMs sin límites