---
icon: trash-xmark
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Limpar configurações de CSS

{% hint style="warning" %}
Use este método quando configurações CSS incorretas forem aplicadas ou quando não for possível acessar a interface de configurações após definir o CSS.
{% endhint %}

* Abra o console. Clique na janela do CherryStudio e pressione o atalho <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* Na janela do console que aparece, clique em `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Insira manualmente `document.getElementById('user-defined-custom-css').remove()` – copiar e colar provavelmente não funcionará.
* Após inserir o comando, pressione Enter para limpar as configurações de CSS. Você poderá então acessar novamente as configurações de exibição do CherryStudio para remover o código CSS problemático.