---
icon: book-open-cover
---
# Tutorial de Base de Conocimientos


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




En la versión 0.9.1, CherryStudio presenta la tan esperada función de base de conocimientos.

A continuación, proporcionaremos instrucciones detalladas paso a paso para usar CherryStudio.

## Agregar Modelo de Incrustación

1. Busque modelos en el servicio de gestión de modelos; puede hacer clic en "Modelo de Incrustación" para filtrar rápidamente;
2. Encuentre el modelo que necesita y agréguelo a Mis Modelos.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Crear Base de Conocimientos

1. Acceso a la base de conocimientos: en la barra de herramientas izquierda de CherryStudio, haga clic en el icono de base de conocimientos para ingresar a la página de gestión;
2. Agregar base de conocimientos: haga clic en Agregar para comenzar a crear una base de conocimientos;
3. Nombre: ingrese el nombre de la base de conocimientos y agregue un modelo de incrustación, tomando bge-m3 como ejemplo, para completar la creación.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Agregar Archivos y Vectorizar

1. Agregar archivos: haga clic en el botón para agregar archivos para abrir el selector de archivos;
2. Seleccionar archivos: elija entre los formatos admitidos, como pdf, docx, pptx, xlsx, txt, md, mdx, etc., y ábralos;
3. Vectorización: el sistema realizará automáticamente el procesamiento de vectorización; cuando se muestre completado (marca verde ✓), significa que la vectorización ha finalizado.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Agregar Datos de Múltiples Fuentes

CherryStudio admite múltiples formas de agregar datos:

1. Directorio de carpetas: puede agregar un directorio completo; los archivos en formatos admitidos dentro de este directorio se vectorizarán automáticamente;
2. Enlace URL: admite URL, como [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Mapa del sitio: admite mapas de sitio en formato XML, como [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Notas de texto plano: admite la entrada de contenido personalizado en texto plano.

{% hint style="info" %}
Nota:

1. Las ilustraciones en los documentos importados a la base de conocimientos aún no se pueden convertir en vectores; deben convertirse manualmente en texto.
2. Al utilizar una URL como fuente de la base de conocimientos, puede que no siempre sea exitoso. Algunos sitios web tienen mecanismos anti-rastreo estrictos (o requieren inicio de sesión, autorización, etc.), por lo que este método podría no obtener el contenido preciso. Se recomienda realizar una búsqueda de prueba después de la creación.
3. Generalmente, los sitios web proporcionan un sitemap, como el [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml) de CherryStudio. Por lo general, puede obtener la información relevante agregando `/sitemap.xml` a la dirección raíz del sitio (es decir, la URL). Por ejemplo: `aaa.com/sitemap.xml`.
4. Si el sitio web no proporciona un sitemap o las URL son demasiado complejas, puede crear manualmente un archivo XML de sitemap. Temporalmente, el archivo debe ser un enlace directo accesible públicamente; los enlaces a archivos locales no serán reconocidos.

> 1) Puede pedir a una IA que genere un archivo sitemap o que escriba una herramienta generadora de sitemap en HTML.
> 2) Para los enlaces directos, puede utilizar enlaces directos de OSS o de servicios de almacenamiento en la nube. Si no tiene una herramienta existente, puede visitar el sitio web oficial de [ocoolAI](https://one.ocoolai.com/login), iniciar sesión y utilizar la herramienta gratuita de carga de archivos en la barra superior para generar un enlace directo.
{% endhint %}

## Buscar en la Base de Conocimientos

Cuando la vectorización de archivos y materiales esté completa, puede realizar consultas:

1. Haga clic en el botón "Buscar en la base de conocimientos" en la parte inferior de la página;
2. Ingrese el contenido de la consulta;
3. Se mostrarán los resultados de la búsqueda;
4. Y se mostrará la puntuación de coincidencia de cada resultado.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Generar Respuestas Citando la Base de Conocimientos en una Conversación

1. Cree un nuevo tema; en la barra de herramientas de conversación, haga clic en "Base de Conocimientos" para expandir la lista de bases de conocimientos creadas y seleccione la que desee citar;
2. Ingrese y envíe la pregunta; el modelo devolverá una respuesta generada a partir de los resultados de la búsqueda;
3. Además, las fuentes de datos citadas se adjuntarán debajo de la respuesta para una revisión rápida del archivo fuente.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>