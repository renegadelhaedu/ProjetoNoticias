from art import *

# Cria um dicionário vazio para armazenar os usuários
usuarios = {}

# Cria uma lista vazia para armazenar as matérias
materias = []

# Define um contador de IDs para atribuir IDs únicos a cada matéria
id_materia = 1

# Define as constantes para os tipos de usuário
TIPO_JORNALISTA = "jornalista"
TIPO_LEITOR = "leitor"

usuario_logado = None


def cadastrar():
    # Solicita informações do usuário
    print("-" * 30)  # linha superior
    while True:
        nome = input('Nome: ')
        if nome.strip(): # Verifica se a string não está vazia após remover espaços em branco
            break
        else:
            print('Não pode ficar vazio tente novamente')



    # Solicita o email do usuário e realiza a verificação
    while True:
        email = input('Email: ')
        if '@' in email and email.endswith('.com') and email not in usuarios:
            break
        elif '@' not in email:
            print('Email deve conter o caractere @. Tente novamente')
        elif not email.endswith('.com'):
            print("O email deve terminar com '.com' ")
            print('Exemplo: seu_email@dominio.com')
        else:
            print('Email já cadastrado. Informe outro')

    # Solicita a senha do usuário e realiza a validação
    senha = None
    while True:
        print('Informe uma senha que contenha 6 caracteres (letras e números)')
        senha = input('Senha: ')
        if validar_senha(senha):
            break
        else:
            print('Senha não atende aos critérios.')
    confirmacao_senha = None
    while True:
        confirmacao_senha = input('Confirme a senha: ')
        if senha == confirmacao_senha:
            break
        else:
            print('As senhas não coincidem. Tente novamente')

        # Solicita o tipo de usuário (comum ou administrador)
    print("-" * 30)  # linha superior
    print('| Escolha o tipo de usuário: |')
    print('| 1. Jornalista              |')
    print('| 2. Leitor                  |')
    print("-" * 30)  # linha inferior
    # Valida o tipo de usuario
    while True:
        tipo_usuario = input("Digite o número correspondente ao tipo de usuário: ")
        if tipo_usuario == '1':
            tipo_usuario = TIPO_JORNALISTA
            break
        elif tipo_usuario == '2':
            tipo_usuario = TIPO_LEITOR
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Cria um novo usuário com as informações fornecidas
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'tipo': tipo_usuario,
        'curtidas': []  # Inicialmente vazio
    }

    # Adiciona o usuário ao dicionário de usuários
    usuarios[email] = usuario
    print('Usuário cadastrado com sucesso')

def escrever_materia(usuario):
    global id_materia

    if usuario['tipo'] == TIPO_JORNALISTA:
        titulo = input('Digite o titulo da matéria: ')
        conteudo = input('Digite o texto: ')
        # Obtém a data atual
        data_materia = input('Digite a data da matéria (no formato DD/MM/AAAA): ')

        materia = {
            'id': id_materia,
            'titulo': titulo,
            'conteudo': conteudo,
            'data': data_materia,
            'autor': usuario['nome']  # Adiciona o email do autor
        }
        # Incrementa o contador de IDs para a próxima matéria
        id_materia += 1

        materias.append(materia)
        print('Matéria escrita com sucesso!')
    else:
        print('Você não tem permissão para escrever matéria')

def fazer_login():
    # Solicita o email do usuário a ser buscado
    global usuario_logado  # Indica que estamos usando a variável global
    email = input('Email: ')
    senha = input('Senha: ')

    # Verifica se o email está no dicionário de usuários
    if email in usuarios and usuarios[email]['senha'] == senha:
        print("-" * 30)  # linha superior
        print('| Login feito com sucesso    |')
        print('| Bem vindo', usuarios[email]['nome'], '            |')
        print("-" * 30)  # linha inferior
        usuario_logado = usuarios[email]  # Define o usuário logado
        return True
    else:
        print('Credenciais inválidas')
        return False

def validar_senha(senha):
    # Valida a senha com base em regras específicas
    if len(senha) >= 6 and any(char.isalpha() for char in senha) and any(char.isdigit() for char in senha):
        return True
    else:
        return False

def excluir_noticia():
    if len(materias) == 0:
        print('Não há matérias disponíveis para excluir.')
        return

    listar_noticias(materias)  # Mostra a lista de notícias para que o usuário veja os IDs
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

def editar_materia():
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
            print(f'\nEditando matéria com ID {id_a_editar}.')
            novo_titulo = input('Digite o novo título: ')
            novo_conteudo = input('Digite o novo conteúdo: ')
            nova_data = input('Digite a nova data (no formato DD/MM/AAAA): ')

            materia['titulo'] = novo_titulo
            materia['conteudo'] = novo_conteudo
            materia['data'] = nova_data

            print(f'Matéria com ID {id_a_editar} editada com sucesso.')
            return
    print(f'Matéria com ID {id_a_editar} não encontrada')

def menu_jornalista(usuario):
    while True:
        print("-" * 30)  # linha superior
        print('|          Opções:           |')
        print('| 1 - Escrever matéria       |')
        print('| 2 - Visualizar matérias    |')
        print('| 3 - Excluir matéria        |')
        print('| 4 - Editar matéria         |')
        print('| 5 - Sair                   |')
        print("-" * 30)  # linha inferior
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            escrever_materia(usuario)
        if (opcao == '2'):
            listar_noticias(materias)
        elif (opcao == '3'):
            excluir_noticia()  # Chamando a função para excluir notícias
        elif (opcao == '4'):
            editar_materia()
        elif (opcao == '5'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')

def curtir_noticia(usuario_logado, id_noticia_curtir):
    if len(materias) == 0:
        print('No momento não há matérias disponíveis para curtir. ')
        return

    # Verifique se o usuário já curtiu esta notícia
    if 'curtidas' in usuario_logado and id_noticia_curtir in usuario_logado['curtidas']:
        print('Você já curtiu esta notícia anteriormente.')
        return

    # Verifica se o ID é um número válido
    if not id_noticia_curtir.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_noticia_curtir = int(id_noticia_curtir)

    # Procura a notícia com base no ID
    for materia in materias:
        if materia['id'] == id_noticia_curtir:
            # Incrementa o número de curtidas na matéria
            if 'curtidas' not in materia:
                materia['curtidas'] = 0
            materia['curtidas'] += 1

            # Adicione o ID da notícia às curtidas do usuário
            if 'curtidas' not in usuario_logado:
                usuario_logado['curtidas'] = []
            usuario_logado['curtidas'].append(id_noticia_curtir)

            print('Curtida adicionada com sucesso')
            return
    print(f'Matéria com ID {id_noticia_curtir} não encontrada.')

def comentar_noticia(usuario_logado):
    if len(materias) == 0:
        print('No momento não há matérias disponíveis para comentar.')
        return

    listar_noticias(materias)  # Mostra a lista de notícias para que o usuário veja os IDs
    id_a_comentar = input('Digite o id da matéria que deseja comentar: ')

    # Verifica se o ID é um número válido
    if not id_a_comentar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_comentar = int(id_a_comentar)

    # Procura a notícia com base no ID
    for materia in materias:
        if materia['id'] == id_a_comentar:
            comentario = input('Digite seu comentário: ')
            # Crie uma chave 'comentarios' na notícia se ainda não existir
            if 'comentarios' not in materia:
                materia['comentarios'] = []
            # Adicione o comentário ao campo 'comentarios' da notícia
            materia['comentarios'].append({'usuario': usuario_logado['nome'], 'comentario': comentario})

            print('Comentário adicionado com sucesso.')
            return
    print(f'Notícia com ID {id_a_comentar} não encontrada.')

def listar_noticias(materias):
    if len(materias) == 0:
        print('Não há matérias disponíveis no momento')
    else:
        print('Lista de matérias:')
        for materia in materias:
            print('-' * 40)  # Linha de hifens para separar as matérias
            print(f"ID: {materia['id']}")
            print(f"Título: {materia['titulo']}")
            print(f"Autor: {materia['autor']}")  # Exibe o autor da matéria
            print(f"Data: {materia['data']}")
            print(f"Conteúdo: {materia['conteudo']}")

            # Verifica se há comentários na matéria
            if 'comentarios' in materia and len(materia['comentarios']) > 0:
                print('-' * 40)  # Linha de hifens para separar os comentários
                print('Comentários:')
                for comentario in materia['comentarios']:
                    print(f'Usuário: {comentario["usuario"]}')
                    print(f'Comentário: {comentario["comentario"]}')
                    print('-' * 40)  # Linha de hifens para separar os comentários

            # Verifica se há curtidas na matéria
            if 'curtidas' in materia:
                print(f'Curtidas: {materia["curtidas"]}')

            print('-' * 40)  # Linha de hifens para separar os comentários

def menu_leitor(usuario_logado):
    while True:

        print("-" * 30)  # linha superior
        print('|          Opções:           |')
        print("-" * 30)  # linha inferior
        print('| 1 - Visualizar matérias    |')
        print('| 2 - Comentar notícia       |')
        print('| 3 - Curtir notícia         |')
        print('| 4 - Sair                   |')
        print("-" * 30)  # Linha inferior
        opcao = input('Digite uma opção: ')

        if (opcao == '1'):
            listar_noticias(materias)
        elif (opcao == '2'):
            comentar_noticia(usuario_logado)
        elif (opcao == '3'):
            id_noticia_curtir = input('Digite o ID da notícia que deseja curtir: ')
            curtir_noticia(usuario_logado, id_noticia_curtir)  # Passe o ID da notícia como argumento
        elif (opcao == '4'):
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Selecione novamente')

def main():
    global usuario_logado

    while True:
        tprint("Catolica News","cybermedium")
        print("-" * 30)  # linha superior
        print('|          Opções:           |')
        print("-" * 30)  # cabecalho
        print('|      1. Cadastrar Usuário  |')
        print('|      2. Fazer login        |')
        print('|      3. Sair               |')
        print("-" * 30)  # Linha inferior
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            if fazer_login():
                if usuario_logado['tipo'] == TIPO_JORNALISTA:
                    menu_jornalista(usuario_logado)
                else:
                    menu_leitor(usuario_logado)

        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()