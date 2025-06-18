# 🐞 Ouvidoria BESOURO VERMELHO

Este projeto é uma aplicação simples de ouvidoria desenvolvida em Python com integração a banco de dados MySQL. O sistema permite registrar, listar, buscar e excluir manifestações do tipo **elogio**, **sugestão** e **reclamação**.

## 📁 Estrutura de Arquivos

- `menu.py` - Arquivo principal que exibe o menu de opções e gerencia a navegação do sistema.
- `ouvidoria.py` - Contém todas as funções responsáveis pelas operações da ouvidoria (CRUD).
- `operacoesbd.py` - Lida com operações genéricas no banco de dados (não detalhado neste README).

---

## 📄 menu.py

Este é o ponto de entrada da aplicação. Suas principais funcionalidades são:

- Estabelece a conexão com o banco de dados MySQL.
- Apresenta um menu principal com 6 opções:
  1. **Listar manifestações**: Permite visualizar apenas elogios, sugestões, reclamações ou todas.
  2. **Criar uma nova manifestação**: Permite cadastrar uma nova entrada, selecionando o tipo.
  3. **Exibir quantidade de manifestações**: Mostra o total de registros na tabela.
  4. **Pesquisar manifestação por código**: Busca uma manifestação específica pelo ID.
  5. **Excluir manifestação por código**: Remove uma manifestação do sistema.
  6. **Sair do sistema**: Encerra a aplicação e a conexão com o banco.

Todas as ações chamam funções contidas no módulo `ouvidoria.py`, utilizando uma variável de conexão criada via `operacoesbd.py`.

---

## 📄 ouvidoria.py

Este módulo contém a lógica de negócios da aplicação, incluindo todas as funcionalidades que manipulam os dados no banco:

### 📝 Criação de manifestações

- `criarElogio(conexao)`
- `criarSugestao(conexao)`
- `criarReclamacao(conexao)`

Essas funções inserem dados na tabela `ouvidoria` com o tipo de manifestação correspondente (1 = Elogio, 2 = Sugestão, 3 = Reclamação).

### 📋 Listagem de manifestações

- `listarElogios(conexao)`
- `listarSugestoes(conexao)`
- `listarReclamacoes(conexao)`
- `listarTodos(conexao)`

Permitem visualizar as manifestações com filtros ou sem filtro (todas).

### 🔍 Pesquisa e Exclusão

- `pesquisarManifestacoes(conexao)`  
  Permite buscar uma manifestação pelo código (ID).

- `excluirManifestacao(conexao)`  
  Permite excluir uma manifestação existente informando seu código.

### 📊 Contagem

- `contadorManifestacoes(conexao)`  
  Exibe a quantidade total de manifestações registradas no sistema.

---

## ✅ Pré-requisitos

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python`

Instalação do conector:
```bash
pip install mysql-connector-python
