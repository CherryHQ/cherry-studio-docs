---
icon: trash-xmark
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# CSS-Einstellungen zurücksetzen

{% hint style="warning" %}
Verwenden Sie diese Methode, wenn falsche CSS-Einstellungen vorgenommen wurden oder der Zugriff auf die Einstellungsseite nach CSS-Änderungen nicht möglich ist.
{% endhint %}

*   Öffnen Sie die Konsole durch Klicken auf das CherryStudio-Fenster und Drücken von <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
*   Klicken Sie im daraufhin angezeigten Konsolenfenster auf `Console`.

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

*   Geben Sie manuell `document.getElementById('user-defined-custom-css').remove()` ein (Kopieren/Einfügen führt meist nicht zur Ausführung).
*   Bestätigen Sie mit der Eingabetaste, um CSS-Einstellungen zurückzusetzen. Anschließend können Sie problematischen CSS-Code in CherryStudios Anzeigeeinstellungen entfernen.