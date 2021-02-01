
while True:
    cntrl = input(f'Escreva um número de 1 à 10: ')

    if cntrl != '5':
        for num in range(10, 0, -1):
            print(num)

        for num in range(0, 10):
            print(num)
    else:

        print('Falow rapaziada!')
        break
