# Escolha de produtos:

produto1 = {'Nome': 'Dildo 3 ways', 'Quantidade': 69, 'Preço': 69.00}
produto2 = {'Nome': 'Enxaguante bucal', 'Quantidade': 6, 'Preço': 300.000}
produto3 = {'Nome': 'Controle remoto', 'Quantidade': 200, 'Preço': 2.00}

estante = [produto1,
           produto2,
           produto3]

print('Produtos disponíveis na loja')
print(estante)

carrinho = []

for n in range(3):
    escolha = input(f'Esolha um produto da estante: ')
    carrinho.append(escolha)

print(f'Suas escolhas: {carrinho}')
print(carrinho[0])
print(carrinho[1])
print(carrinho[2])

print(f'Sua escolha 1: {(produto1).get("Nome")}')
print(f'Sua escolha 2: {(produto2).get("Nome")}')
print(f'Sua escolha 3: {(produto3).get("Nome")}')


