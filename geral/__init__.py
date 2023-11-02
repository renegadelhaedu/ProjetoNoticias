from jornalista import *
from leitor import *

usuarios_cadastrados = []
TIPO_JORNALISTA = "jornalista"
TIPO_LEITOR = "leitor"


def fazer_login(materias):
    email = input('Email: ')
    senha = input('Senha: ')

    for usuario in usuarios_cadastrados:
        if (usuario['email'] == email and usuario['senha'] == senha):

            if (usuario['tipo'] == TIPO_JORNALISTA):
                menu_jornalista(email, materias)

            elif (usuario['tipo'] == TIPO_LEITOR):
                menu_leitor()

            else:
                print('Credenciais inválidas')











def curtir_noticia(usuario_logado, id_noticia_curtir, materias):
    if len(materias) == 0:
        print('No momento não há matérias disponíveis para curtir. ')
        return

    if 'curtidas' in usuario_logado and id_noticia_curtir in usuario_logado['curtidas']:
        print('Você já curtiu esta notícia anteriormente.')
        return

    if not id_noticia_curtir.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_noticia_curtir = int(id_noticia_curtir)

    for materia in materias:
        if materia['id'] == id_noticia_curtir:
            if 'curtidas' not in materia:
                materia['curtidas'] = 0
            materia['curtidas'] += 1

            if 'curtidas' not in usuario_logado:
                usuario_logado['curtidas'] = []
            usuario_logado['curtidas'].append(id_noticia_curtir)

            print('Curtida adicionada com sucesso')
            return
    print(f'Matéria com ID {id_noticia_curtir} não encontrada.')

def comentar_noticia(usuario_logado, materias, listar_noticias):
    if len(materias) == 0:
        print('No momento não há matérias disponíveis para comentar.')
        return

    listar_noticias(materias)  # Mostra a lista de notícias para que o usuário veja os IDs
    id_a_comentar = input('Digite o id da matéria que deseja comentar: ')

    if not id_a_comentar.isdigit():
        print('ID inválido. Digite um número válido.')
        return
    id_a_comentar = int(id_a_comentar)

    for materia in materias:
        if materia['id'] == id_a_comentar:
            comentario = input('Digite seu comentário: ')
            if 'comentarios' not in materia:
                materia['comentarios'] = []
            # Adicione o comentário ao campo 'comentarios' da notícia
            materia['comentarios'].append({'usuario': usuario_logado['nome'], 'comentario': comentario})

            print('Comentário adicionado com sucesso.')
            return
    print(f'Notícia com ID {id_a_comentar} não encontrada.')




#----------------------------OK--------------------------------------
def cadastrar():
    print("-" * 30)
    while True:
        nome = input('Nome: ')
        if nome.strip():  # Verifica se a string não está vazia após remover espaços em branco
            break
        else:
            print('Não pode ficar vazio tente novamente')

    while True:
        email = input('Email: ')
        if '@' in email and email.endswith('.com') and email not in usuarios_cadastrados:
            break
        elif '@' not in email:
            print('Email deve conter o caractere @. Tente novamente')
        elif not email.endswith('.com'):
            print("O email deve terminar com '.com' ")
            print('Exemplo: seu_email@dominio.com')
        else:
            print('Email já cadastrado. Informe outro')

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

    print("-" * 30)
    print('| Escolha o tipo de usuário: |')
    print('| 1. Jornalista              |')
    print('| 2. Leitor                  |')
    print("-" * 30)

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

    novo_usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'tipo': tipo_usuario,
        'curtidas': []
    }

    cadastrar_novo_usuario(novo_usuario)


def validar_senha(senha):
    if len(senha) >= 6 and any(char.isalpha() for char in senha) and any(char.isdigit() for char in senha):
        return True
    else:
        return False


def cadastrar_novo_usuario(novo_usuario):
    for usuario in usuarios_cadastrados:
        if (usuario['email'] == novo_usuario['email']):
            print('email existente')
            return

    usuarios_cadastrados.append(novo_usuario)
    print('Usuário cadastrado')

#-------------------------------OK--------------------------------
