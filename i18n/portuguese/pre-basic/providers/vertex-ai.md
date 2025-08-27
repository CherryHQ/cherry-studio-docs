---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Visão Geral do Tutorial

### 1. Obter Chave da API

*   Antes de obter a chave da API do Gemini, você precisa ter um projeto do Google Cloud (pule esta etapa se já tiver um)
*   Acesse o [Google Cloud](https://console.cloud.google.com/projectcreate) para criar seu projeto, preencha o nome do projeto e clique em "Criar projeto"

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

*   Acesse o [Console do Vertex AI](https://console.cloud.google.com/vertex-ai)
*   Ative a [API Vertex AI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) no projeto criado

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurar Permissões de Acesso à API

*   Abra a página de permissões de [contas de serviço](https://console.cloud.google.com/iam-admin/serviceaccounts) e crie uma conta de serviço

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   Na página de gerenciamento de contas de serviço, localize a conta recém-criada, clique em `Chaves` e crie uma nova chave no formato JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   Após a criação bem-sucedida, o arquivo de chave será salvo automaticamente em seu computador no formato JSON - **guarde-o com segurança**

## 3. Configurar o Vertex AI no Cherry Studio

*   Selecione o provedor de serviços Vertex AI
*   Preencha os campos correspondentes com os dados do arquivo JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Clique para adicionar [modelos](https://console.cloud.google.com/vertex-ai/model-garden) e comece a usar com prazer!