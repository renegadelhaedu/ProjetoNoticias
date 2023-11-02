from datetime import date
from geral import *

data_atual = date.today()
materias = []

def menu_jornalista(usuario, materias):
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
            escrever_materia(usuario)
        if (opcao == '2'):
            listar_noticias(materias)
        elif (opcao == '3'):
            excluir_noticia()
        elif (opcao == '4'):
            editar_materia()
        elif (opcao == '5'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')


def escrever_materia(usuario):
    global id_materia

    if usuario['tipo'] == TIPO_JORNALISTA:
        titulo = input('Digite o titulo da matéria: ')
        conteudo = input('Digite o texto: ')
        data_materia = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)

        materia = {
            'id': id_materia,
            'titulo': titulo,
            'conteudo': conteudo,
            'data': data_materia,
            'autor': usuario['nome']
        }
        id_materia += 1

        materias.append(materia)
        print('Matéria escrita com sucesso!')
    else:
        print('Você não tem permissão para escrever matéria')

def excluir_noticia(usuario_logado):
    if len(materias) == 0:
        print('Não há matérias disponíveis para excluir.')
        return

    listar_noticias(materias)
    id_a_excluir = input('Digite o ID da notícia: ')

    # Verifica se o ID é um número válido
    if not id_a_excluir.isdigit():
        print('ID inválido. Digite um número válido')
        return
    id_a_excluir = int(id_a_excluir)

    # Procura a notícia com base no ID
    for materia in materias:
        if materia['id'] == id_a_excluir:
            if usuario_logado['email'] == materia['autor']:
                materias.remove(materia)
                print(f'Noticia com ID {id_a_excluir} excluida com sucesso.')
            else:
                print('Você não tem permissão para excluir esta matéria')
            return
    print(f'Noticia com ID {id_a_excluir} não encontrada. ')

def editar_materia(usuario_logado):
    global id_materia

    if usuario_logado['tipo'] != TIPO_JORNALISTA:
        print('Você não tem permissão para editar matérias. ')
        return
    if len(materias) == 0:
        print('Não há matérias disponíveis para editar. ')
        return

    listar_noticias(materias)  # Mostra a lista de notícias para que o usuário veja os IDs
    id_a_editar = input('Qual id da matéria a ser editada: ')

    # Verifica se o ID é um número válido
    if not id_a_editar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_editar = int(id_a_editar)

    # Procura a matéria com base no ID
    for materia in materias:
        if materia['id'] == id_a_editar:
            if usuario_logado['email'] == materia['autor']:
                materias.remove(materia)
                print(f'Noticia com ID {id_a_editar} excluida com sucesso.')
            else:
                print('Apenas os autores tem permissão para fazer edições')
            return

            print(f'Editando matéria com ID {id_a_editar} .')
            novo_titulo = input('Digite o novo título: ')
            novo_conteudo = input('Digite o novo conteúdo: ')
            nova_data = input('Digite a nova data (no formato DD/MM/AAAA): ')

            materia['titulo'] = novo_titulo
            materia['conteudo'] = novo_conteudo
            materia['data'] = nova_data

            print(f'Matéria com ID {id_a_editar} editada com sucesso.')
            return
    print(f'Matéria com ID {id_a_editar} não encontrada')


def listar_noticias(materias):
    if len(materias) == 0:
        print('Não há matérias disponíveis no momento')
    else:
        print('Lista de matérias:')
        for materia in materias:
            print('-' * 40)
            print(f"ID: {materia['id']}")
            print(f"Título: {materia['titulo']}")
            print(f"Autor: {materia['autor']}")
            print(f"Data: {materia['data']}")
            print(f"Conteúdo: {materia['conteudo']}")

            # Verifica se há comentários na matéria
            if 'comentarios' in materia and len(materia['comentarios']) > 0:
                print('-' * 40)
                print('Comentários:')
                for comentario in materia['comentarios']:
                    print(f'Usuário: {comentario["usuario"]}')
                    print(f'Comentário: {comentario["comentario"]}')
                    print('-' * 40)

            if 'curtidas' in materia:
                print(f'Curtidas: {materia["curtidas"]}')

            print('-' * 40)