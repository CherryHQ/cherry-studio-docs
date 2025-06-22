---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Vertex AI

## Visão Geral do Tutorial

### 1. Obter a Chave de API

* Antes de obter a chave de API do Gemini, você precisa ter um projeto no Google Cloud (se já tiver, pule esta etapa)
* Acesse o [Google Cloud](https://console.cloud.google.com/projectcreate) para criar um projeto, preencha o nome do projeto e clique em "Criar projeto"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Acesse o [console do Vertex AI](https://console.cloud.google.com/vertex-ai)
* No projeto criado, ative a [API Vertex AI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurar Permissões de Acesso à API

* Abra a página de permissões de [contas de serviço](https://console.cloud.google.com/iam-admin/serviceaccounts) e crie uma conta de serviço

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Na página de gerenciamento de contas de serviço, localize a conta recém-criada, clique em `Chaves` e crie uma nova chave no formato JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Após a criação bem-sucedida, o arquivo de chave será salvo automaticamente em seu computador no formato JSON. **Guarde-o cuidadosamente**

## 3. Configurar o Vertex AI no Cherry Studio

* Selecione o provedor Vertex AI
* Preencha os campos correspondentes com os dados do arquivo JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Clique em Adicionar [Modelo](https://console.cloud.google.com/vertex-ai/model-garden) e você já pode começar a usar!