---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Tutorial de Configuração do Obsidian

O Cherry Studio oferece integração com o Obsidian para exportar conversas completas ou mensagens individuais para sua biblioteca do Obsidian.

{% hint style="warning" %}
Este processo não requer instalação de plugins adicionais do Obsidian. Contudo, como o mecanismo de exportação para o Obsidian usa princípios similares ao Obsidian Web Clipper, recomendamos atualizar o Obsidian para a versão mais recente (versão mínima **1.7.2** ou superior) para evitar [falhas de importação com conversas longas](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Tutorial Atual

{% hint style="info" %}
Em comparação com a versão anterior, o novo recurso de exportação para o Obsidian seleciona automaticamente o caminho da biblioteca, eliminando a necessidade de inserção manual do nome da biblioteca ou pasta.
{% endhint %}

### Passo 1: Configurar o Cherry Studio

Acesse _Configurações_ →  _Configurações de Dados_ → Menu _Configuração do Obsidian_. Os nomes das bibliotecas do Obsidian abertas localmente aparecerão automaticamente. Selecione sua biblioteca alvo:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Passo 2: Exportar Conversas

#### Exportar Conversa Completa

Na interface de conversas do Cherry Studio, clique com o botão direito em uma conversa, selecione _Exportar_ e clique em _Exportar para Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Uma janela será aberta para configurar as **Propriedades** da nota exportada, **localização da pasta** no Obsidian e **método de processamento**:

* **Cofre**: Menu suspenso para selecionar outra biblioteca do Obsidian
* **Caminho**: Menu suspenso para escolher a pasta de destino
* Propriedades da nota:
  * Etiquetas (tags)
  * Data de criação (created)
  * Origem (source)
* **Métodos de processamento**:
  * **Novo (substituir se existir)**: Cria nova nota na pasta especificada, substituindo notas existentes com mesmo nome
  * **Preceder**: Adiciona conteúdo ao início de notas existentes com mesmo nome
  * **Anexar**: Adiciona conteúdo ao final de notas existentes com mesmo nome

{% hint style="info" %}
Apenas o primeiro método inclui as propriedades. Os métodos subsequentes preservam apenas o conteúdo.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Configurar propriedades da nota</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Selecionar caminho</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Escolher método de processamento</p></figcaption></figure>

Após configurar todas as opções, clique em confirmar para exportar a conversa completa para a pasta especificada.

#### Exportar Mensagem Individual

Para mensagens individuais, clique no _menu de três linhas_ abaixo da mensagem, selecione _Exportar_ e clique em _Exportar para Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Exportar mensagem individual</p></figcaption></figure>

A mesma janela de configuração de **propriedades** e **método de processamento** será exibida. Configure conforme o [tutorial de exportação completa acima](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Exportação Bem-sucedida

🎉 Parabéns! Você concluiu toda a integração entre Cherry Studio e Obsidian. Desfrute!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exportado para o Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Verificar resultado da exportação</p></figcaption></figure>

***

## Tutorial Antigo (para Cherry Studio < v1.1.13)

### Passo 1: Preparar o Obsidian

Abra sua biblioteca do Obsidian e crie uma _pasta_ para armazenar as conversas exportadas (exemplo: "Cherry Studio"):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Anote o nome do _cofre_ (destacado no canto inferior esquerdo).

### Passo 2: Configurar o Cherry Studio

Em _Configurações_ →  _Configurações de Dados_ → Menu _Configuração do Obsidian_, insira o nome do _cofre_ e da _pasta_ obtidos no [Passo 1](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

A opção _Etiquetas Globais_ (etiquetas aplicadas a todas as notas exportadas) é opcional.

### Passo 3: Exportar Conversas

#### Exportar Conversa Completa

Na interface de conversas, clique com o botão direito na conversa, selecione _Exportar_ e clique em _Exportar para Obsidian_:

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Exportar conversa completa</p></figcaption></figure>

Configure as **propriedades** da nota e escolha entre estes **métodos de processamento**:
* **Novo (substituir se existir)**: Cria nova nota na pasta configurada
* **Preceder**: Adiciona conteúdo ao início de notas existentes
* **Anexar**: Adiciona conteúdo ao final de notas existentes

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Configurar propriedades da nota</p></figcaption></figure>

{% hint style="info" %}
Apenas o primeiro método inclui propriedades. Os demais preservam apenas conteúdo.
{% endhint %}

#### Exportar Mensagem Individual

Clique no _menu de três linhas_ abaixo da mensagem, selecione _Exportar_ e clique em _Exportar para Obsidian_:

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Exportar mensagem individual</p></figcaption></figure>

Configure conforme o [tutorial de exportação completa acima](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Exportação Bem-sucedida

🎉 Parabéns! Você concluiu toda a integração entre Cherry Studio e Obsidian. Desfrute!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exportado para o Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Verificar resultado da exportação</p></figcaption></figure>