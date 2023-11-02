from datetime import date
from geral import *



data_atual = date.today()


def menu_jornalista(emailusuario, materias, idmateria):
    while True:
        print("-" * 30)
        print('|          Opções:           |')
        print('| 1 - Escrever matéria       |')
        print('| 2 - Visualizar matérias    |')
        print('| 3 - Excluir matéria        |')
        print('| 4 - Editar matéria         |')
        print('| 5 - Sair                   |')
        print("-" * 30)
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            escrever_materia(emailusuario, materias, idmateria)
        elif (opcao == '2'):
            listar_noticias(emailusuario, materias)
        elif (opcao == '3'):
            excluir_materia(emailusuario, materias)
        elif (opcao == '4'):
            editar_materia(emailusuario, materias)
        elif (opcao == '5'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')


def editar_materia(emailusuario, materias):

    listar_noticias(materias)  # Mostra a lista de notícias para que o usuário veja os IDs
    id_a_editar = input('Qual id da matéria a ser editada: ')

    # Verifica se o ID é um número válido
    if not id_a_editar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_editar = int(id_a_editar)

    # Procura a matéria com base no ID
    for materia in materias:
        if materia['id'] == id_a_editar and emailusuario == materia['autor']:

            print(f'Editando matéria com ID {id_a_editar} .')
            novo_titulo = input('Digite o novo título: ')
            novo_conteudo = input('Digite o novo conteúdo: ')
            nova_data = input('Digite a nova data (no formato DD/MM/AAAA): ')

            materia['titulo'] = novo_titulo
            materia['conteudo'] = novo_conteudo
            materia['data'] = nova_data

            print(f'Matéria com ID {id_a_editar} editada com sucesso.')
            break
    else:
        print(f'Matéria com ID {id_a_editar} não encontrada')


def listar_noticias(emailusuario, materias):
    if len(materias) == 0:
        print('Não há matérias disponíveis no momento')
    else:
        print('Lista de matérias:')
        for materia in materias:
            if(materia['autor'] == emailusuario):

                print('-' * 40)
                print(f"ID: {materia['id']}")
                print(f"Título: {materia['titulo']}")
                print(f"Autor: {materia['autor']}")
                print(f"Data: {materia['data']}")
                print(f"Conteúdo: {materia['conteudo']}")


def exibirComentariosNoticia(emailusuario, materias):
    listar_noticias(emailusuario, materias)

    idnoticia = int(input('digite o ID da materia que voce quer exibir os comentarios'))

    for i in range(len(materias)):
        if materias[i]['id'] == idnoticia:
            for comentario in materias[i]['comentarios']:
                print(comentario)
                #alterar conforme a estrutura da funcao que adiciona comentarios






#---------------------------------OK-----------------------------------
def escrever_materia(email, materias, idmateria):
    titulo = input('Digite o titulo da matéria: ')
    conteudo = input('Digite o texto: ')
    data_materia = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

    idmateria[0] = idmateria[0] + 1
    materia = {
        'id': idmateria[0],
        'titulo': titulo,
        'conteudo': conteudo,
        'data': data_materia,
        'autor': email,
        'comentarios': [],
        'curtidas': 0
    }

    materias.append(materia)
    print('Matéria escrita com sucesso!')


def excluir_materia(emailusuario, materias):
    if len(materias) == 0:
        print('Não há matérias disponíveis para excluir.')
        return

    listar_noticias(emailusuario, materias)
    id_a_excluir = input('Digite o ID da notícia: ')

    # Verifica se o ID é um número válido
    if not id_a_excluir.isdigit():
        print('ID inválido. Digite um número válido')
        return
    id_a_excluir = int(id_a_excluir)

    # Procura a notícia com base no ID
    for materia in materias:
        if materia['id'] == id_a_excluir:
            if emailusuario == materia['autor']:
                materias.remove(materia)
                print(f'Noticia com ID {id_a_excluir} excluida com sucesso.')
            else:
                print('Você não tem permissão para excluir esta matéria')
            return
    print(f'Noticia com ID {id_a_excluir} não encontrada. ')


#--------------------------------OK---------------------------------------------