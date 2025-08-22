---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Visão Geral do Tutorial

### 1. Obter Chave de API

* Antes de obter a chave de API do Gemini, você precisa ter um projeto no Google Cloud (se já tiver um, esta etapa pode ser ignorada)
* Acesse [Google Cloud](https://console.cloud.google.com/projectcreate) para criar um projeto, preencha o nome do projeto e clique em "Criar projeto"

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Acesse o [Console do Vertex AI](https://console.cloud.google.com/vertex-ai)
* No projeto criado, ative a [API Vertex AI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurar Permissões de Acesso à API

* Abra a página de permissões de [Contas de Serviço](https://console.cloud.google.com/iam-admin/serviceaccounts) e crie uma conta de serviço

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Na página de gerenciamento de contas de serviço, localize a conta recém-criada, clique em `Chaves` e crie uma nova chave no formato JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Após a criação bem-sucedida, o arquivo de chave será salvo automaticamente no seu computador em formato JSON - **armazene-o com segurança**

## 3. Configurar Vertex AI no Cherry Studio

* Selecione o provedor de serviços Vertex AI
* Preencha os campos correspondentes com os dados do arquivo JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Clique em adicionar [modelo](https://console.cloud.google.com/vertex-ai/model-garden) e comece a usar!