numero = int(input('Numero: '))


def multiplicar(numero):
    resultado = numero * numero
    return resultado


print(multiplicar(numero))


def soma(a, b):
    return a + b


print(soma(10, 30))


def loucura(c, d, palavra):
    resultado = ((c ** 2) + (d ** 3)) * palavra
    return resultado


print(loucura(2, 3, 'Rola '))


nome = input('Insira um nome: ')
sobrenome = input('Insira seu sobrenome: ')


def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'


print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(nome='Carla', sobrenome='da Silva'))
print(nome_completo(sobrenome='das Galaxias', nome='Pica'))


