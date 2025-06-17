---
icon: trash-xmark
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Очистка настроек CSS



{% hint style="warning" %}
Используйте этот метод, когда заданы некорректные стили CSS или после установки CSS вы не можете войти в интерфейс настроек.
{% endhint %}

* Откройте консоль, нажмите на окно CherryStudio и введите комбинацию клавиш <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (для MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* В появившемся окне консоли нажмите вкладку `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Затем вручную введите команду `document.getElementById('user-defined-custom-css').remove()` — копирование и вставка могут не сработать.
* После ввода нажмите Enter для подтверждения, чтобы очистить настройки CSS. Затем снова войдите в настройки отображения CherryStudio и удалите проблемный CSS-код.