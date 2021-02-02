ativo = False
logado = False
login = ['pimpidpimpoda', 'deisebaz']
senha = ['levi1020', 'barboza0']
# cores = ['Branco', 'Preto', 'Vermelho', 'Verde']
cores = {'Branco': 'de arrombado', 'Azul': 'control', 'Preto': 'mono-black', 'Vermelho': 'burn', 'Verde': 'elves'}

login_input = input(f'Insira seu login: ')
senha_input = input(f'Insira sua senha: ')
cores_input = 'null'

if login_input in login:
    logado = True
else:
    print(f'Usuário inexsistente no sistema.\n')

if senha_input in senha:
    ativo = True
    print(f'Usuário logado com sucesso!\n ')
else:
    logado = False
    ativo = False
    cores_input = 'null'
    print(f'Senha ou Usuário incorretos.\n')

print(f'{logado}, {ativo}')

if logado:

    while ativo:
        print(f'Inicializando o sistema...\n')
        print('Escolha uma das atividades abaixo:')
        print('1. Adicionar nome de decks a lista;')
        print('2. Escolher um deck e começar o duelo;')
        print('3. Sair do programa "exit()";\n')

        opcao_input = input('Insira uma atividade: ')

        if opcao_input == '1':
            deck_input = input(f'Escreva o nome do deck que pretende adicionar: ')
            deck_input1 = input(f'Descreva o deck: ')
            cores[deck_input] = deck_input1
            print(f'Deck adicionado com sucesso!\n')
            print(f'Decks disponíveis: {cores}\n')

        elif opcao_input == '2':
            print('Esses são os decks disponíveis: \n')
            print(f'{cores}')
            cores_input = input(f'Insira um dos seus decks: ')
            cores_get = cores.get(cores_input, 'Você não possui esse deck')

            if cores_get is not None:
                print(f'O deck "{cores_get}" foi selecionado da sua pool!')
                print('Procurando um desafiante para inicializar o duelo!\n')
            else:
                print(cores_get)
                print(f'Amigo, tá na hora de comprar uns boosters e montar uns decks novos\n')

        elif opcao_input == '3':
            break
    else:
        print('Escolha uma atividade da lista!')
        print('Por favor, relogue no sistema...\n')
else:
    print('Login falhou...')
