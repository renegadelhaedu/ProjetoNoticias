def menu_leitor(usuario_logado):
    while True:

        print("-" * 30)
        print('|          Opções:           |')
        print("-" * 30)
        print('| 1 - Visualizar matérias    |')
        print('| 2 - Comentar notícia       |')
        print('| 3 - Curtir notícia         |')
        print('| 4 - Sair                   |')
        print("-" * 30)
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            listar_noticias(materias)
        elif (opcao == '2'):
            comentar_noticia(usuario_logado)
        elif (opcao == '3'):
            id_noticia_curtir = input('Digite o ID da notícia que deseja curtir: ')
            curtir_noticia(usuario_logado, id_noticia_curtir)
        elif (opcao == '4'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')
