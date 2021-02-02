paises = {'br': 'brasil', 'py': 'paraguai', 'ru': 'russia'}
print(paises)

paises_input = input('escolha um pais: ')
pais_get = paises.get((paises_input), 'pais não encontrado')

if pais_get == None:
    print('erro!')
    print(pais_get)
else:
    print(pais_get)


# exemplo mercado:

carrinho1 = []

produto1 = {'Nome': 'Dildo 3 ways', 'Quantidade': 69, 'Preço': 69.00}
produto2 = {'Nome': 'Enxaguante bucal', 'Quantidade': 6, 'Preço': 300.000}
produto3 = {'Nome': 'Controle remoto', 'Quantidade': 200, 'Preço': 2.00}

carrinho1.append(produto1)
carrinho1.append(produto2)

print(carrinho1)