#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = []

for num in range(0, 10):
    input_num = int(input(print('Insira um número para lista: ')))
    lista.append(input_num)
print(lista)
print('\n')


def count_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 !=0:
            total = total + 1
    return total


print(f'Total de números ímpares na lista: {count_impares(lista)}')
