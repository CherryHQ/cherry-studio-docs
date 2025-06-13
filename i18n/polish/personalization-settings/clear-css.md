---
icon: trash-xmark
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Usuwanie ustawień CSS

{% hint style="warning" %}
Użyj tej metody, aby wyczyścić ustawienia CSS, gdy zostały ustawione błędne reguły CSS lub gdy po ustawieniu CSS nie można wejść do interfejsu ustawień.
{% endhint %}

* Otwórz konsolę deweloperską, kliknij w okno CherryStudio i naciśnij skrót klawiszowy <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* W wyskakującym oknie konsoli kliknij zakładkę `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Następnie ręcznie wprowadź `document.getElementById('user-defined-custom-css').remove()` - kopiowanie i wklejanie prawdopodobnie nie zadziała.
* Po wprowadzeniu naciśnij Enter, aby potwierdzić i wyczyścić ustawienia CSS, a następnie ponownie wejdź w ustawienia wyświetlania CherryStudio, aby usunąć problematyczny kod CSS.