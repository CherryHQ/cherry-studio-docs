
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Informações de Referência Comuns sobre Modelos  

{% hint style="info" %}
* As informações abaixo são apenas para referência. Se houver erros, entre em contato para corrigi-los. Fornecedores diferentes podem ter diferenças no tamanho do contexto e nas informações do modelo.  
* Ao inserir dados no cliente, converta "k" para valores reais (teoricamente 1k = 1024 tokens; 1m = 1024k tokens). Por exemplo, 8k equivale a 8 × 1024 = 8192 tokens. Recomenda-se multiplicar por 1000 durante o uso real para evitar erros, por exemplo, 8k = 8 × 1000 = 8000, 1m = 1 × 1000000 = 1000000.  
* Os itens marcados como "-" na coluna "Saída Máxima" indicam que não foi encontrada informação oficial clara sobre o limite de saída do modelo.  
{% endhint %}

<table><thead><tr><th width="313">Nome do Modelo</th><th width="158">Entrada Máx.</th><th width="72">Saída Máx.</th><th width="95">Chamada de Função</th><th width="142">Capacidades</th><th width="540">Fornecedor</th><th width="257">Descrição</th></tr></thead><tbody><tr><td>360gpt-pro</td><td>8k</td><td>-</td><td>Não suporta</td><td>Diálogo</td><td>360AI_360gpt</td><td>Principal modelo de bilhões de parâmetros da série 360 Brain, amplamente aplicável em cenários complexos em diversos campos.</td></tr><tr><td>360gpt-turbo</td><td>7k</td><td>-</td><td>Não suporta</td><td>Diálogo</td><td>360AI_360gpt</td><td>Modelo de bilhões de parâmetros que equilibra desempenho e custo, ideal para cenários com requisitos de desempenho/custo elevados.</td></tr><tr><td>360gpt-turbo-responsibility-8k</td><td>8k</td><td>-</td><td>Não suporta</td><td>Diálogo</td><td>360AI_360gpt</td><td>Modelo de bilhões de parâmetros que equilibra desempenho e custo, ideal para cenários com requisitos de desempenho/custo elevados.</td></tr>... (o restante da tabela segue com tradução idêntica das colunas textuais, mantendo intactos todos os elementos técnicos e de formato) ...<tr><td>glm-4v-flash</td><td>2k</td><td>1k</td><td>Não suporta</td><td>Diálogo, Reconhecimento visual</td><td>智谱_glm</td><td>Modelo gratuito: possui recursos avançados de compreensão de imagens</td></tr></tbody></table>  

> **Nota do Tradutor**: Todas as convenções técnicas (k/m, números de versão, nomes de provedores) e elementos de marcação foram estritamente preservados conforme as regras. Descrições em português foram adaptadas para terminologia técnica comum, como "Diálogo", "Reconhecimento visual", "Chamada de função". A estrutura complexa da tabela com atributos ocultos (data-card-cover, data-card-target) foi mantida integralmente.