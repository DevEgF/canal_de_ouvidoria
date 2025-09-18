# Sistema de Ouvidoria 🎧

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

Este é um projeto de um sistema de Ouvidoria desenvolvido em Python. A aplicação funciona via terminal (CLI) e permite que os usuários gerenciem manifestações (reclamações, sugestões e elogios), interagindo diretamente com um banco de dados MySQL para persistência dos dados.

## 🌟 Funcionalidades Principais

O sistema oferece um menu interativo com as seguintes opções:

* **Listar todas as manifestações** 📋: Exibe todas as reclamações, sugestões e elogios cadastrados no banco de dados.
* **Adicionar uma nova manifestação** ✨: Permite ao usuário registrar uma nova manifestação, escolhendo o tipo e preenchendo os detalhes.
* **Pesquisar por código** 🔎: Busca e exibe uma manifestação específica a partir do seu código único.
* **Pesquisar por tipo** 🗂️: Filtra e mostra todas as manifestações de um determinado tipo (Reclamação, Sugestão ou Elogio).
* **Remover uma manifestação** 🗑️: Deleta um registro do banco de dados utilizando seu código.
* **Contar manifestações** 📊: Informa o número total de manifestações registradas no sistema.
* **Sair do programa** 🚪: Encerra a conexão com o banco de dados e finaliza a aplicação.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Banco de Dados:** MySQL Server
* **Conector Python-MySQL:** `mysql-connector-python`

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local.

1.  **Pré-requisitos**

    Antes de começar, você precisa ter instalado:
    * [Python 3](https://www.python.org/downloads/)
    * [MySQL Server](https://dev.mysql.com/downloads/mysql/)

2.  **Configuração do Banco de Dados**

    A aplicação precisa de um banco de dados e uma tabela para funcionar. Execute os seguintes comandos SQL no seu terminal MySQL ou em um cliente de banco de dados (como DataGrip ou MySQL Workbench).

    * **Passo A: Crie o Banco de Dados**
        ```sql
        CREATE SCHEMA feedback;
        ```
    * **Passo B: Use o Banco de Dados**
        ```sql
        USE feedback;
        ```
    * **Passo C: Crie a Tabela `claims`**
        ```sql
        CREATE TABLE claims (
            cod int AUTO_INCREMENT,
            title varchar(50),
            description varchar(300),
            author varchar(50),
            respondent varchar(50),
            type varchar(50),
        );
        ```

3.  **Instalação das Dependências**

    Este projeto requer a biblioteca `mysql-connector-python` para se comunicar com o MySQL. Para instalá-la, basta baixar o raw e adicionar o arquivo `operacoesdb.py` na raiz do projeto:
    
    [Operações DB](https://github.com/daniel-abella/operacoesbd/blob/main/operacoesbd.py)
    

4.  **Configuração da Conexão**

    ⚠️ **Ponto Crítico:** Verifique no seu código a linha que cria a conexão. Os dados precisam ser iguais aos do seu ambiente MySQL local.

    A linha deve se parecer com esta:
    ```python
    connection = createConnection('localhost', 'root', 'senha', 'feedback')
    ```
    Ajuste o `host`, `usuário`, `senha` e `banco de dados` conforme necessário.

5.  **Executando a Aplicação**

    Com tudo pronto, navegue até a pasta do seu projeto pelo terminal e inicie o programa com o comando:
    ```bash
    python main.py
    ```
    O menu interativo da Ouvidoria irá aparecer, pronto para uso!

## 👨‍💻 Autor

Feito por **[José do Egito]**
