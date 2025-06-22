---
hidden: True
icon: code
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Estructura del Código

```yaml
...
├─ docs/ # Directorio de documentación
├─ resources/ # Directorio de archivos de recursos
├─ scripts/ # Directorio de archivos de scripts
└─ src/ # Directorio principal del código fuente
    ├─main/ # Código del proceso principal
    ├─preload/ # Directorio de scripts de precarga
    └─renderer/ # Código del proceso de renderizado
        ├─src/ # Código fuente del proceso de renderizado
            ├─assets/ # Archivos de recursos
                ├─fonts/ # Archivos de fuentes
                ├─images/ # Archivos de imágenes (avatares, etc.)
                └─styles/ # Archivos de estilos
            ├─components/ # Componentes
            ├─config/ # Archivos de configuración
            ├─context/ # Contexto
            ├─databases/ # Archivos relacionados con bases de datos
            ├─hooks/ # Hooks personalizados
            ├─i18n/ # Archivos de internacionalización
            ├─pages/ # Archivos de páginas
            ├─providers/ # Configuración relacionada con proveedores
            ├─services/ # Archivos de servicios
            ├─store/ # Archivos de gestión de estado
            ├─types/ # Archivos de definición de tipos TypeScript
            ├─utils/ # Funciones de utilidad
            ...
        ...
    ...
...
```