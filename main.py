from art import *
from datetime import date
import geral
import jornalista
import leitor

id_materia = 1
usuario_logado = []

while True:
    tprint("Catolica News","cybermedium")

    print("-" * 30)
    print('|          Opções:           |')
    print("-" * 30)
    print('|      1. Cadastrar Usuário  |')
    print('|      2. Fazer login        |')
    print('|      3. Sair               |')
    print("-" * 30)

    opcao = input('Escolha uma opção: ')

    if (opcao == '1'):
        geral.cadastrar()

    elif (opcao == '2'):
        geral.fazer_login(usuarios_cadastrados, materias)

    elif (opcao == '3'):
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

    #if __name__ == "__main__":
    #    main()