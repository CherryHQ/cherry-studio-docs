---
icon: trash-xmark
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Borrar configuración CSS

{% hint style="warning" %}
Utilice este método para borrar la configuración CSS cuando haya configurado CSS incorrecto o no pueda acceder a la interfaz de configuración después de aplicar CSS.
{% endhint %}

* Abra la consola, haga clic en la ventana de CherryStudio y presione el atajo de teclado <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* En la ventana de consola emergente, haga clic en `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Luego ingrese manualmente `document.getElementById('user-defined-custom-css').remove()` - copiar y pegar probablemente no funcionará.
* Después de ingresar, presione Enter para confirmar y borrar la configuración CSS, luego vuelva a la configuración de visualización de CherryStudio y elimine el código CSS problemático.