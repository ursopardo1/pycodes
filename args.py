"""
O parâmetro *args utilizado em uma função, coloca os
valores extras informados como entrada
em uma tupla.

É bom usar em funções para atender os pre-requisitos das funções

def soma_total(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(soma_total(1, 2, 3, 4, 5, 6))

"""

lista = []
tupla = ()


def soma_total(*args):
    return sum(args)


def convert(lista):
    return *lista,



for num in range(5):
    entrada = int(input(f'Insira um numero: '))
    lista.append(entrada)


lista_output = convert(lista)
print(lista_output)
#print(soma_total(lista))
