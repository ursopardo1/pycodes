login = ['pimpidpimpoda', 'deisebaz', 'l']
senha = ['levi1020', 'barboza0', '1']
cores = {'Branco': 'de arrombado', 'Azul': 'control', 'Preto': 'mono-black', 'Vermelho': 'burn', 'Verde': 'elves'}


def input_login(nome, password):
    if (nome == nome in login) and (password in senha):
        print(f'\nBem vindo {nome}\n')
        return True
    else:
        print('\nLogin ou senha incorretos, tente novamente...')
        return False


def atividade_1():
    deck_input = input(f'Escreva o nome do deck que pretende adicionar: ')
    deck_input1 = input(f'Descreva o deck: ')
    cores[deck_input] = deck_input1
    print(f'Deck adicionado com sucesso!\n')
    print(f'Decks disponíveis: {cores}\n')
    return


def atividade_2():
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
    return


logado = False
ativo = False

while True:

    while logado is False:
        login_input = input(f'\nInsira seu login: ')
        senha_input = input(f'Insira sua senha: ')
        logado = input_login(login_input, senha_input)

    if logado:
        ativo = True
        while ativo:
            print('Escolha uma das atividades abaixo:')
            print('1. Adicionar nome de decks a lista;')
            print('2. Escolher um deck e começar o duelo;')
            print('3. Voltar para tela de login;')
            print('4. Sair do programa "exit()";\n')
            # print(f'{ativo},{logado}')

            opcao_input = input('Insira uma atividade: ')

            if opcao_input == '1':
                atividade_1()
            elif opcao_input == '2':
                atividade_2()
            elif opcao_input == '3':
                ativo = False
                logado = False
                # print(f'{ativo},{logado}')
            elif opcao_input == '4':
                exit()
            else:
                print('Escolha uma atividade da lista!\n')
