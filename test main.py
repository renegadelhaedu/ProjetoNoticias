cadastro_user = []

while (True):
    print('1 - Cadastrar Usuário')
    print('2 - Login')
    print('0 - Sair')
    menu = int(input('Escolha a opção desejada: '))

    if (menu == 1):
        print('\nNessa tela voce realizará seu cadastro\n')
        login = input('Digite seu login: ')
        senha = input('Digite uma senha: ')
        cadastro_user.append([login, senha])




    if (menu == 2):

        login_auth = input('Login: ')
        senha_auth = input('Senha: ')

        logar = [login_auth, senha_auth]

        for user in cadastro_user:
            if(user == logar):
                print('Logado')
            else:
                print('usuáio não cadastrado')