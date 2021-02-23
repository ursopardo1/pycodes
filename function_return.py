from random import random


def moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(moeda())


def par_ou_impar():
    numero = random()
    if numero % 2 != 0:
        return 'Ímpar!'
    return 'É par...'


print(par_ou_impar())
