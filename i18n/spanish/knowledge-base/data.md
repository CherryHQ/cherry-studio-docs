---
icon: database
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instrucciones de almacenamiento de datos

Los datos añadidos a la base de conocimiento de Cherry Studio se almacenan completamente en local. Durante el proceso de adición, se copia un documento en el directorio de almacenamiento de datos de Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Diagrama de flujo del procesamiento de la base de conocimiento</p></figcaption></figure>

Base de datos vectoriales: [https://turso.tech/libsql](https://turso.tech/libsql)

Una vez que un documento se añade a la base de conocimiento de Cherry Studio, el archivo se divide en varios fragmentos. Estos fragmentos luego se procesan mediante un modelo de incrustación.

Cuando se utiliza un modelo grande para preguntas y respuestas, se consultan los fragmentos de texto relacionados con la pregunta y se envían juntos al modelo de lenguaje grande para su procesamiento.

Si tiene requisitos de privacidad de datos, se recomienda utilizar una base de datos de incrustaciones local y un modelo de lenguaje grande local.