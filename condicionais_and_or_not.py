ativo = True
logado = True
login = 'pimpidpimpoda'
senha = 'levi1020'

login_input = input(f'Insira seu login: ')
senha_input = input(f'Insira sua senha: ')

if login_input == login:
    logado = True
elif senha_input == senha:
    ativo = True
    print(f'Usuário logado com sucesso!')
else:
    logado = False
    ativo = False
    print(f'Senha ou Usuário incorretos.')

'''
if ativo:
    print('Usuário ativo no sistema.')
else:
    print('Usuário offline, verifique.')
'''