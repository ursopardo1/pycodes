# Escolha de produtos:

produto1 = {'Nome': 'Dildo 3 ways', 'Quantidade': 69, 'Preço': 69.00}
produto2 = {'Nome': 'Enxaguante bucal', 'Quantidade': 6, 'Preço': 300.00}
produto3 = {'Nome': 'Controle remoto', 'Quantidade': 200, 'Preço': 2.00}

estante = [produto1,
           produto2,
           produto3]

print('Produtos disponíveis na loja:')
print(f'* {produto1["Nome"]}, Quantidade: {produto1["Quantidade"]}, Preço: {produto1["Preço"]} reais')
print(f'* {produto2["Nome"]}, Quantidade: {produto2["Quantidade"]}, Preço: {produto2["Preço"]} reais')
print(f'* {produto3["Nome"]}, Quantidade: {produto3["Quantidade"]}, Preço: {produto3["Preço"]} reais')
print("\n")

carrinho = {'1': '', '2': '', '3': ''}
espaco1 = {'Espaço1': '', 'Espaço2': '', 'Espaço3': ''}
espaco2 = {'Espaço1': '', 'Espaço2': '', 'Espaço3': ''}
espaco3 = {'Espaço1': '', 'Espaço2': '', 'Espaço3': ''}


for n in range(3):
    escolha = input(f'Esolha um produto da estante: ')

    if escolha == '1':
        quant_1esc = input(f'Informe a quantidade desejada: ')
        quant_1 = int(quant_1esc)
        quant_estoque1 = int(produto1.get('Quantidade'))

        quant_restante1 = (quant_estoque1 - quant_1)
        produto1['Quantidade'] = quant_restante1
        confirmar1 = input(print(f'Você escolheu {quant_1} x {produto1.get("Nome")}, correto? '))

        if confirmar1 == 'sim':
            espaco1['Espaço1'] = produto1.get("Nome")
            espaco1['Espaço2'] = quant_1
            preco1 = produto1.get('Preço')
            valor1 = (quant_1 * preco1)
            espaco1['Espaço3'] = valor1
            print(f'{espaco1}\n')
            carrinho['1'] = espaco1
        else:
            print("Voltando para seleção\n")

    elif escolha == '2':
        quant_2esc = input(f'Informe a quantidade desejada: ')
        quant_2 = int(quant_2esc)
        quant_estoque2 = int(produto2.get('Quantidade'))

        quant_restante2 = (quant_estoque2 - quant_2)
        produto2['Quantidade'] = quant_restante2
        confirmar2 = input(print(f'Você escolheu {quant_2} x {produto2.get("Nome")}, correto? '))

        if confirmar2 == 'sim':
            espaco2['Espaço1'] = produto2.get("Nome")
            espaco2['Espaço2'] = quant_2
            preco2 = produto2.get('Preço')
            valor2 = (quant_2 * preco2)
            espaco2['Espaço3'] = valor2
            print(f'{espaco2}\n')
            carrinho['2'] = espaco2
        else:
            print("Voltando para seleção\n")

    elif escolha == '3':
        quant_3esc = input(f'Informe a quantidade desejada: ')
        quant_3 = int(quant_3esc)
        quant_estoque3 = int(produto2.get('Quantidade'))
        quant_restante3 = (quant_estoque3 - quant_3)
        produto3['Quantidade'] = quant_restante3

        confirmar3 = input(print(f'Você escolheu {quant_3} x {produto3.get("Nome")}, correto?'))
        if confirmar3 == 'sim':
            espaco3['Espaço1'] = produto3.get("Nome")
            espaco3['Espaço2'] = quant_3
            preco3 = produto3.get('Preço')
            valor3 = (quant_3 * preco3)
            espaco3['Espaço3'] = valor3
            print(f'{espaco3}\n')
            carrinho['3'] = espaco3
        else:
            print("Voltando para seleção\n")
