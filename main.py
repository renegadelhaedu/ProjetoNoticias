menu = int('00')
user = []
adm = []

while (menu != '0'):
    print('1 - Cadastrar Usuário')
    print('2 - Login')
    print('0 - Sair')
    menu = int(input('Escolha a opção desejada: '))

    if (menu == 1):
        print('\nNessa tela voce realizará seu cadastro\n')
        user = input('Digite seu login: ')
        print(user)


    elif (menu == 2):
        print('\nInforme seu usuário e senha')

    elif (menu == 99):
        print('\nCrie seu usário SuperAdmin')

    elif (menu == 0):
        print('\nObrigado por usar nosso sistema!')
        break

    else:
        print('Opção Invalida. Tente novamente')

