"""
-GRUPO BESOURO VERMELHO-
Naytson Pimentel da Silva
Edson Pedro da Rocha Silva
Eddie Yago Gabriel dos Santos Sátiro
Guilherme Natã Meirelles Jung
"""

from operacoesbd import *
from ouvidoria import *

conexao = criarConexao('127.0.0.1', 'root', '12345', 'ouvidoriabesourovermelhov2')

condicao = 0

print("\nBem-vindo à Ouvidoria BESOURO VERMELHO.\n")

while condicao != 6:
    print("\n|============================================|")
    print("|        OUVIDORIA - MENU DE AÇÕES           |")
    print("|============================================|")
    print("| Opção | Descrição                          |")
    print("|   1   | Listar manifestações               |")
    print("|   2   | Criar uma nova manifestação        |")
    print("|   3   | Exibir quantidade de manifestações |")
    print("|   4   | Pesquisar manifestação por código  |")
    print("|   5   | Excluir manifestação por código    |")
    print("|   6   | Sair do sistema                    |")
    print("|============================================|")

    condicao = int(input("\nDigite a ação que deseja realizar: "))

    if condicao == 1:
        escolha = 0
        while escolha != 5:
            print("\n|===================================|")
            print("|        TIPO DE MANIFESTAÇÃO       |")
            print("|===================================|")
            print("| Opção | Descrição                 |")
            print("|   1   | Elogios                   |")
            print("|   2   | Sugestões                 |")
            print("|   3   | Reclamações               |")
            print("|   4   | Todas                     |")
            print("|   5   | Voltar ao menu principal  |")
            print("|===================================|\n")

            escolha = int(input("Digite o número do tipo de manifestação: "))

            if escolha == 1:
                listarElogios(conexao)
            elif escolha == 2:
                listarSugestoes(conexao)
            elif escolha == 3:
                listarReclamacoes(conexao)
            elif escolha == 4:
                listarTodos(conexao)
            elif escolha != 5:
                print("\nOpção inválida. Por favor, digite novamente.")

    elif condicao == 2:
        print("\nVocê escolheu: Criar uma nova manifestação\n")
        condicao = 0
        while condicao != 4:
            print("|===================================|")
            print("|             MENU TIPOS            |")
            print("|===================================|")
            print("| Opção | Descrição                 |")
            print("|   1   | Elogio                    |")
            print("|   2   | Sugestão                  |")
            print("|   3   | Reclamação                |")
            print("|   4   | Voltar ao menu principal  |")
            print("|===================================|")

            condicao = int(input("Digite qual tipo de manifestação deseja adicionar: "))

            if condicao == 1:
                criarElogio(conexao)
            elif condicao == 2:
                criarSugestao(conexao)
            elif condicao == 3:
                criarReclamacao(conexao)
            elif condicao != 4:
                print("\nOpção inválida. Por favor, digite novamente.")

    elif condicao == 3:
        print("\nVocê escolheu: Exibir quantidade de manifestações")
        contadorManifestacoes(conexao)

    elif condicao == 4:
        print("\nVocê escolheu: Pesquisar manifestação por código")
        pesquisarManifestacoes(conexao)

    elif condicao == 5:
        print("\nVocê escolheu: Excluir manifestação")
        excluirManifestacao(conexao)

    elif condicao != 6:
        print("\nOpção inválida. Por favor, digite novamente.\n")

encerrarConexao(conexao)

print()
print("-----------------------------------------------------")
print("Agradecemos por utilizar a Ouvidoria BESOURO VERMELHO")
print("-----------------------------------------------------")
