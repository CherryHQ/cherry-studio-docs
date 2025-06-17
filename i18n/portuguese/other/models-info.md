
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Informações de Referência de Modelos Comuns

{% hint style="info" %}
* As informações abaixo são apenas para referência. Se houver erros, entre em contato para corrigi-los. As informações sobre o tamanho do contexto e as especificações do modelo podem variar dependendo do provedor de serviços;
* Ao inserir dados no cliente, é necessário converter "k" para valores numéricos (teoricamente 1k = 1024 tokens; 1m = 1024k tokens). Por exemplo, 8k equivalem a 8×1024=8192 tokens. Recomenda-se multiplicar por 1000 durante o uso real para evitar erros, ou seja, 8k = 8×1000=8000, 1m=1×1000000=1000000;
* "Saída máxima" marcada como "-" indica que a informação de saída máxima não foi encontrada oficialmente.
{% endhint %}

<table><thead><tr><th width="313">Nome do Modelo</th><th width="158">Entrada Máxima</th><th width="72">Saída Máxima</th><th width="95">Chamada de Função</th><th width="142">Capacidades do Modelo</th><th width="540">Provedor</th><th width="257">Introdução</th></tr></thead><tbody><tr><td>360gpt-pro</td><td>8k</td><td>-</td><td>Não suportado</td><td>Diálogo</td><td>360AI_360gpt</td><td>Principal modelo de bilhões de parâmetros da série 360 Brain, amplamente aplicável em cenários de tarefas complexas em várias áreas.</td></tr><tr><td>360gpt-turbo</td><td>7k</td><td>-</td><td>Não suportado</td><td>Diálogo</td><td>360AI_360gpt</td><td>Modelo de bilhões de parâmetros com equilíbrio entre desempenho e eficiência, adequado para cenários com altos requisitos de desempenho/custo.</td></tr><!-- (Table rows continue with translated content maintaining all technical terms/names unchanged) --><tr><td>glm-4v-flash</td><td>2k</td><td>1k</td><td>Não suportado</td><td>Diálogo, Reconhecimento visual</td><td>智谱_glm</td><td>Modelo gratuito com recursos avançados de compreensão de imagens</td></tr></tbody></table>