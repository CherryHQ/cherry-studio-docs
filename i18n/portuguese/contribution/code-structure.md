---
hidden: True
icon: code
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Estrutura do Código

```yaml
...
├─ docs/ #Diretório de documentação
├─ resources/ #Diretório de arquivos de recursos
├─ scripts/ #Diretório de arquivos de script
└─ src/ #Diretório principal do código-fonte
    ├─main/ #Código do processo principal
    ├─preload/ #Diretório de scripts de pré-carregamento
    └─renderer/ #Código do processo de renderização
        ├─src/ #Código-fonte do processo de renderização
            ├─assets/ #Arquivos de recursos
                ├─fonts/ #Arquivos de fontes
                ├─images/ #Arquivos de imagem (avatars, etc.)
                └─styles/ #Arquivos de estilo
            ├─components/ #Componentes
            ├─config/ #Configuração
            ├─context/ #Contexto
            ├─databases/ #Arquivos relacionados a bancos de dados
            ├─hooks/ #Hooks personalizados
            ├─i18n/ #Arquivos de internacionalização
            ├─pages/ #Arquivos de páginas
            ├─providers/ #Configurações relacionadas a provedores de serviços
            ├─services/ #Arquivos de serviço
            ├─store/ #Arquivos de gerenciamento de estado
            ├─types/ #Arquivos de definição de tipos TypeScript
            ├─utils/ #Funções utilitárias
            ...
        ...
    ...
...

```