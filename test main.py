from datetime import date
data_atual = date.today()
data_materia = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)

print(data_materia)

for usuario in usuarios_cadastrados:
    if (usuario['email'] == email and usuario['senha'] == senha):
        print('Logado')
        usuario_logado.append(usuario)