# Loop for

# Python
# for item in interavel:

# String: nome = 'Roubalheira'
# Lista: nomes = ['A', 'B', 'C', '...']
# Range: numeros = range(1, 10)

nome = 'Roubalheiranobrasiléverdadeirarapaziadabrasileira'
nomes = ['Carlos', 'Izaias', 'Jouseppe', 'Ramilson']
numeros = range(1,10)

#String
for letra in nome:
    print(letra)  # print de cada letra em uma linha

#Lista
for pessoa in nomes:
    print(pessoa)

#range
for numero in range(1,10):
    print(numero)

#   enumerate is useful for obtaining an indexed list:
#      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)


# Algoritmo de soma em for

soma = 0
vezes = int(input(f'Vezes pra rodar: '))

for n in range(1, vezes+1):
    num = int(input(f'Informe o {n}/{vezes} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

for n in range(1, vezes+1):
    soma = soma + 1
    print(f'{soma}')


#  Mostrando String em quantidade controlada
vezes = int(input(f'Quantidade de vezes: '))

for indice in range(0, vezes):
    print(nome[indice], end='')

# For com controle de range
nome0 = 'Truly '
nome1 = 'Geeky '

vezes = int(input(f'Input: '))

for num in range(0, vezes+1):
    print(f'{(nome0*num)+(nome1*(vezes-num))}')
