'''
vezes = int(input('Input: '))

for num in range(0, vezes+1):
    print(('\U0001F60A' * num) + ('\U0001F60D' * (vezes-num)))

    if num == int(vezes/2):
        print(('\U0001F60C' * num) + ('\U0001F60D' * (vezes-num)))
'''

# For com controle de range
nome0 = 'Split '
nome1 = 'Geeky '

vezes = int(input(f'Input: '))

# Aumentar o número de repetições do laço
for _ in range(3):
    for num in range(0, vezes+1):
        print(f'{(nome0*num)+(nome1*(vezes-num))}')

        if num == int(vezes / 2):
            print(('XxxxX ' * (num*2)))
