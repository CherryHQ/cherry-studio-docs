---
icon: book-open-cover
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Tutorial de Base de Conhecimento

Na versão 0.9.1, o CherryStudio introduziu a tão aguardada funcionalidade de base de conhecimento.

Abaixo apresentaremos instruções detalhadas de uso passo a passo do CherryStudio.

## Adicionar Modelos de Embedding

1. Busque modelos no serviço de gerenciamento de modelos - você pode clicar em "Embedding Models" para filtragem rápida;
2. Encontre o modelo necessário e adicione-o aos "Meus Modelos".

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Criar Base de Conhecimento

1. Acesso à base de conhecimento: Na barra lateral esquerda do CherryStudio, clique no ícone da base de conhecimento para acessar a página de gerenciamento;
2. Adicionar base de conhecimento: Clique em "Adicionar" para começar a criar uma base;
3. Nomeação: Digite o nome da base de conhecimento e adicione um modelo de embedding, como bge-m3, para concluir a criação.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Adicionar Arquivos e Vetorização

1. Adicionar arquivo: Clique no botão de adicionar arquivo para abrir a seleção de arquivos;
2. Selecionar arquivo: Escolha formatos suportados como pdf, docx, pptx, xlsx, txt, md, mdx etc., e abra;
3. Vetorização: O sistema realizará automaticamente o processamento de vetorização. Quando mostrar "Concluído" (✓ verde), indica que a vetorização foi finalizada.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Adicionar Dados de Múltiplas Fontes

O CherryStudio suporta várias formas de adicionar dados:

1. Diretório de pastas: Você pode adicionar todo um diretório - os arquivos em formatos suportados serão vetorizados automaticamente;
2. URL: Suporta links de sites como [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Mapa do site: Suporta mapas de site em formato XML, como [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Notas de texto: Suporta entrada de conteúdo personalizado em texto puro.

{% hint style="info" %}
Nota:

1. Ilustrações em documentos importados para a base de conhecimento ainda não suportam conversão para vetores - precisam ser convertidas manualmente para texto;
2. Usar URLs como fonte pode não funcionar sempre devido a mecanismos anti-raspagem rigorosos em alguns sites (ou requisitos de login/autorização). Recomenda-se testar com uma pesquisa após criar;
3. Sites geralmente oferecem sitemaps, como o do CherryStudio: [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). Normalmente, adicione `/sitemap.xml` à URL raiz para acessar (ex: `aaa.com/sitemap.xml`);
4. Caso o site não forneça sitemap ou tenha URLs complexas, você pode criar um arquivo XML manualmente. O arquivo precisa ter um link direto publicamente acessível - links locais não funcionam.

> 1) Peça à IA para gerar um sitemap ou criar uma ferramenta geradora;
> 2) Use links diretos OSS ou de nuvem. Sem ferramentas, visite [ocoolAI](https://one.ocoolai.com/login), faça login e use o serviço gratuito de upload na barra superior para gerar links diretos.
{% endhint %}

## Procurar na Base de Conhecimento

Após a vetorização dos materiais, você pode pesquisar:

1. Clique no botão "Buscar na base de conhecimento" abaixo da página;
2. Insira o termo de busca;
3. Visualize os resultados;
4. Veja a pontuação de correspondência de cada resultado.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Gerar Respostas Citando a Base de Conhecimento

1. Crie uma nova conversa. Na barra de ferramentas, clique em "Base de Conhecimento" para ver a lista de bases criadas e selecione a desejada;
2. Digite e envie sua pergunta - o modelo retornará uma resposta gerada a partir dos resultados da pesquisa;
3. Fontes citadas aparecem abaixo da resposta para visualização rápida.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>