---
icon: trash-xmark
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Очистка настроек CSS

{% hint style="warning" %}
Этот метод очистки настроек CSS следует использовать при установке некорректного CSS или если после настройки CSS невозможно войти в интерфейс настроек.
{% endhint %}

* Откройте консоль разработчика: в окне CherryStudio нажмите комбинацию клавиш <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (для MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* В открывшейся консоли перейдите на вкладку `Console` (Консоль).

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Вручную введите команду `document.getElementById('user-defined-custom-css').remove()` - копирование и вставка скорее всего не сработают.
* После ввода нажмите Enter для выполнения команды. Это очистит настройки CSS, после чего вы сможете снова войти в настройки отображения CherryStudio и удалить проблемный CSS-код.