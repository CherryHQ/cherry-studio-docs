---
icon: book-open-cover
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Tutorial de Base de Conhecimento

Na versão 0.9.1, o CherryStudio introduziu a tão esperada funcionalidade de Base de Conhecimento.

A seguir, apresentaremos o guia detalhado de utilização do CherryStudio passo a passo.

## Adicionar Modelos de Embedding

1. Busque modelos no serviço de gerenciamento de modelos - é possível filtrar rapidamente clicando em "Modelos de Embedding";
2. Encontre o modelo desejado e adicione-o aos meus modelos.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Criar Base de Conhecimento

1. Acesso à Base de Conhecimento: Na barra de ferramentas à esquerda do CherryStudio, clique no ícone da Base de Conhecimento para acessar a página de gerenciamento;
2. Adicionar Base de Conhecimento: Clique em "Adicionar" para começar a criar sua base de conhecimento;
3. Nomeação: Insira o nome da base de conhecimento e adicione um modelo de embedding, usando bge-m3 como exemplo, para finalizar a criação.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Adicionar Arquivos e Vetorizar

1. Adicionar arquivos: Clique no botão de adicionar arquivos para abrir a seleção;
2. Selecionar arquivos: Escolha entre formatos suportados como pdf, docx, pptx, xlsx, txt, md, mdx etc.;
3. Vetorização: O sistema realizará automaticamente o processo de vetorização. Quando mostrar "Concluído" (verde ✓), significa que a vetorização está completa.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Adicionar Dados de Múltiplas Fontes

O CherryStudio suporta diversos métodos de adição de dados:

1. Diretório de pastas: Adicione uma pasta inteira - os arquivos suportados serão vetorizados automaticamente;
2. URL: Suporta links como [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Mapa do site: Suporta sitemaps em formato XML como [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Notas de texto: Permite inserir conteúdo personalizado em texto puro.

{% hint style="info" %}
Dicas:
1. Ilustrações em documentos importados não são convertidas em vetores automaticamente – é necessário convertê-las manualmente em texto;
2. URLs como fonte podem falhar devido a políticas antifraude rigorosas, login obrigatório ou autorização. Recomenda-se testar após a criação;
3. Sites geralmente possuem sitemaps (ex: [sitemap do CherryStudio](https://docs.cherry-ai.com/sitemap-pages.xml)). Normalmente localizados em `domínio.com/sitemap.xml`;
4. Se o site não tiver sitemap, crie um arquivo XML manualmente usando URLs públicas:
   > 1) Use IA para gerar sitemaps ou ferramentas geradoras;
   > 2) Utilize links diretos de OSS (Object Storage Service) ou armazenamento em nuvem. Ferramenta gratuita disponível em: [ocoolAI](https://one.ocoolai.com/login).
{% endhint %}

## Pesquisar na Base de Conhecimento

Após a vetorização, é possível realizar consultas:

1. Clique no botão "Pesquisar Base de Conhecimento" no rodapé da página;
2. Insira o conteúdo da consulta;
3. Visualize os resultados da pesquisa;
4. Verifique a pontuação de correspondência para cada resultado.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Gerar Respostas com Base de Conhecimento em Diálogos

1. Crie um novo tópico. Na barra de ferramentas, clique em "Base de Conhecimento" para ver a lista e selecione uma base;
2. Envie sua pergunta – o modelo retornará respostas geradas a partir dos resultados da pesquisa;
3. As fontes de dados utilizadas aparecerão abaixo da resposta para acesso rápido.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>