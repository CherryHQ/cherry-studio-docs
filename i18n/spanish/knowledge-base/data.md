---
icon: database
---
# Instrucciones de almacenamiento de datos


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Los datos añadidos a la base de conocimientos de Cherry Studio se almacenan completamente en local. Durante el proceso de adición, se copia un documento en el directorio de almacenamiento de datos de Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Diagrama de flujo de procesamiento de la base de conocimientos</p></figcaption></figure>

Base de datos vectorial: [https://turso.tech/libsql](https://turso.tech/libsql)

Cuando un documento se agrega a la base de conocimientos de Cherry Studio, el archivo se divide en varios fragmentos, luego estos fragmentos se entregan al modelo de incrustación para su procesamiento.

Al utilizar modelos grandes para preguntas y respuestas, se consultan los fragmentos de texto relacionados con la pregunta y se entregan al modelo de lenguaje grande para su procesamiento.

Si existen requisitos de privacidad de datos, se recomienda utilizar una base de datos de incrustaciones local y un modelo de lenguaje grande local.