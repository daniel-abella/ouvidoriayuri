from operacoesbd import *


# Função para excluir uma manifestação pelo código informado
def excluirManifestacao(conexao):
    codigoExcluir = int(input("Digite o código da manifestação que deseja excluir: "))
    excluir = 'delete from ouvidoria where codigo = (%s)'
    lista = [codigoExcluir]
    conexao = excluirBancoDados(conexao, excluir, lista)

    if conexao == 1:
        print("\nA manifestação foi excluída com sucesso.")
    elif conexao == 0:
        print("\nNão há manifestações com este código para serem apagadas.")


# Função para pesquisar uma manifestação específica pelo código
def pesquisarManifestacoes(conexao):
    consulta = int(input("Digite o código da manifestação que deseja visualizar: "))
    pesquisar = 'select * from ouvidoria where codigo = %s'
    lista = [consulta]
    conexao = listarBancoDados(conexao, pesquisar, lista)

    if len(conexao) == 0:
        print("\nNão há manifestações disponíveis com este código.\n")
    else:
        print("\nCódigo:", conexao[0][0], "| Nome:", conexao[0][1])
        print("Manifestação:", conexao[0][3])
        print()


# Função para exibir a quantidade total de manifestações
def contadorManifestacoes(conexao):
    contador = 'select count(*) from ouvidoria'
    conexao = listarBancoDados(conexao, contador)
    print("\nA quantidade de manifestações disponíveis é:", conexao[0][0])
    print()


# Função para criar um elogio
def criarElogio(conexao):
    nome = input("Digite seu nome: ")
    manifestacao = input("Descreva sua manifestação: ")
    tipo = 1
    sql = 'insert into ouvidoria(nomeusuario, tipomanifestacao, manifestacao) values (%s, %s, %s)'
    dados = [nome, tipo, manifestacao]
    insertNoBancoDados(conexao, sql, dados)
    print("\nElogio adicionado com sucesso!\n")


# Função para criar uma sugestão
def criarSugestao(conexao):
    nome = input("Digite seu nome: ")
    manifestacao = input("Descreva sua manifestação: ")
    tipo = 2
    sql = 'insert into ouvidoria(nomeusuario, tipomanifestacao, manifestacao) values (%s, %s, %s)'
    dados = [nome, tipo, manifestacao]
    insertNoBancoDados(conexao, sql, dados)
    print("\nSugestão adicionada com sucesso!\n")


# Função para criar uma reclamação
def criarReclamacao(conexao):
    nome = input("Digite seu nome: ")
    manifestacao = input("Descreva sua manifestação: ")
    tipo = 3
    sql = 'insert into ouvidoria(nomeusuario, tipomanifestacao, manifestacao) values (%s, %s, %s)'
    dados = [nome, tipo, manifestacao]
    insertNoBancoDados(conexao, sql, dados)
    print("\nReclamação adicionada com sucesso!\n")


# Função para listar todas as manifestações
def listarTodos(conexao):
    sql = 'select * from ouvidoria'
    resultados = listarBancoDados(conexao, sql)

    if len(resultados) == 0:
        print("\nNão há manifestações a serem exibidas.\n")
    else:
        print("\nTodas as manifestações:\n")
        for item in resultados:
            print(item[0], "|", item[1])
        print()


# Função para listar apenas os elogios
def listarElogios(conexao):
    sql = 'select * from ouvidoria where tipomanifestacao = 1'
    resultados = listarBancoDados(conexao, sql)

    if len(resultados) == 0:
        print("\nNão há manifestações de elogio a serem exibidas.\n")
    else:
        print("\nManifestações - Elogios:\n")
        for item in resultados:
            print(item[0], "|", item[1])
        print()


# Função para listar apenas as sugestões
def listarSugestoes(conexao):
    sql = 'select * from ouvidoria where tipomanifestacao = 2'
    resultados = listarBancoDados(conexao, sql)

    if len(resultados) == 0:
        print("\nNão há sugestões a serem exibidas.\n")
    else:
        print("\nManifestações - Sugestões:\n")
        for item in resultados:
            print(item[0], "|", item[1])
        print()


# Função para listar apenas as reclamações
def listarReclamacoes(conexao):
    sql = 'select * from ouvidoria where tipomanifestacao = 3'
    resultados = listarBancoDados(conexao, sql)

    if len(resultados) == 0:
        print("\nNão há reclamações a serem exibidas.\n")
    else:
        print("\nManifestações - Reclamações:\n")
        for item in resultados:
            print(item[0], "|", item[1])
        print()
