print('--- Tupla tabulada ---')

produtos = ('Coca-cola', 10.5, 
            'Chocolate', 5.50, 
            'Salgadinho', 8.90,
            'Pão de queijo', 10.90)

produto = 'Produto'

print(f'{produto:<30}Preço') # Delimita 30 casas a direita.
print(f'-' * 40)

for pos, item in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{produtos[pos]:<30}', end='')
    else:
        print(produtos[pos])