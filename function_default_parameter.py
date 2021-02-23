def exponencial (numero, potencia=2):  # Valor padrão é dois, caso não seja informado
    return numero ** potencia          # ele ainda executará o programa

# OBS: Em funcções Python, os parâmetros com valores default devem sempre estar no final da declaração

ativo = False
logado = False
login = ['pimpidpimpoda', 'deisebaz']
senha = ['levi1020', 'barboza0']



def input_login(nome='usuário', logado=False ):
    if nome == 'Rolludo' and instrutor:
        return 'Bem vindo, pica das galaxias!'
    elif nome == 'Rolludo':
        return 'Bem vindo professor...'
    else:
        return f'Olá aluno {nome}'

