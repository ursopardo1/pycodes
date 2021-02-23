"""
List Comprehension

- É possível gerar novas listas com dados processados a partir de outro interável

# Sintaxe:

[ dado for dado in interável ]
"""

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


def sum(num1, num2):
    return num1 + num2


res2 = [sum(numeros[1], numeros[2]) for numero in numeros]
print(res2)


numeros_dobrados = []
print([numero * 2 for numero in [1, 2, 3, 4, 5]])


amigos = ['jef', 'carlos', 'tésio']


print([amigo.title() for amigo in amigos])
