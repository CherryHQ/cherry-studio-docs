---
icon: book-open-cover
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Tutorial de Base de Conocimientos

En la versión 0.9.1, CherryStudio presenta la tan esperada función de bases de conocimientos.

A continuación, se presenta una guía detallada paso a paso para usar CherryStudio.

## Añadir modelos de embedding

1. En el servicio de gestión de modelos, busque modelos. Puede hacer clic en "Modelos de embedding" para filtrar rápidamente;
2. Encuentre el modelo que necesite y añádalo a "Mis modelos".

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Crear una base de conocimientos

1. Acceso a base de conocimientos: En la barra de herramientas izquierda de CherryStudio, haga clic en el icono de base de conocimientos para entrar a la página de gestión;
2. Añadir base de conocimientos: Haga clic en "Añadir" para comenzar a crear una base de conocimientos;
3. Nombre: Ingrese el nombre de la base de conocimientos y añada un modelo de embedding. Tomando bge-m3 como ejemplo, se completará la creación.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Añadir archivos y vectorizar

1. Añadir archivo: Haga clic en el botón "Añadir archivo" para abrir el selector de archivos;
2. Seleccionar archivo: Elija formatos compatibles como pdf, docx, pptx, xlsx, txt, md, mdx, etc., y ábralos;
3. Vectorización: El sistema realizará automáticamente la vectorización. Cuando muestre "Completado" (✓ verde), la vectorización ha finalizado.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Añadir datos de múltiples fuentes

CherryStudio admite varias formas de añadir datos:

1. Directorios: Puede añadir carpetas completas. Los archivos con formatos compatibles se vectorizarán automáticamente;
2. Enlaces web: Admite URLs como [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Mapa del sitio: Admite mapas de sitio en formato XML, como [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Notas de texto: Admite contenido personalizado en texto plano.

{% hint style="info" %}
Notas:

1. Las ilustraciones en documentos importados aún no pueden convertirse en vectores, necesita convertirlas manualmente a texto;
2. Usar URLs como fuente no siempre funciona. Algunos sitios tienen mecanismos anti-scraping estrictos (o requieren inicio de sesión/autorización), por lo que este método podría no obtener contenido exacto. Se recomienda verificar mediante búsqueda después de crearlo;
3. La mayoría de sitios proporcionan sitemap, como el de CherryStudio: [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). Normalmente puede acceder agregando `/sitemap.xml` a la URL principal, ej. `aaa.com/sitemap.xml`;
4. Si un sitio no proporciona sitemap o tiene URLs complejas, puede crear manualmente un archivo XML. El archivo debe ser accesible públicamente mediante enlace directo. Los enlaces locales no se reconocerán.

> 1) Puede pedir a una IA que genere el archivo sitemap o cree una herramienta generadora de sitemap HTML;
> 2) Use enlaces directos de OSS o servicios de almacenamiento en la nube. Si no tiene herramientas, visite [ocoolAI](https://one.ocoolai.com/login), inicie sesión y utilice la herramienta gratuita de subida de archivos en la barra superior para generar enlaces directos.
{% endhint %}

## Buscar en la base de conocimientos

Cuando los archivos están vectorizados, puede consultar:

1. Haga clic en el botón "Buscar en base de conocimientos" al final de la página;
2. Ingrese el contenido de la consulta;
3. Aparecerán los resultados de búsqueda;
4. Se mostrará la puntuación de coincidencia de cada resultado.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Usar la base de conocimientos para generar respuestas en conversaciones

1. Cree un nuevo tema. En la barra de herramientas de conversación, haga clic en "Base de conocimientos" para mostrar las bases existentes. Seleccione la que necesite;
2. Ingrese y envíe su pregunta. El modelo generará una respuesta utilizando los resultados de búsqueda;
3. Las fuentes de datos citadas aparecerán debajo de la respuesta para acceso rápido.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>