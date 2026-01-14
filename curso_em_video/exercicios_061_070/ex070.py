print('------ Calculo de gastos ------')

total_gasto = 0
mais_de_mil = 0
menor_preco = float('inf')
nome_menor_preco = ''

while True:
    print('-'*50)
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: '))
     
    if preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_menor_preco = nome_produto
        
    if preco_produto > 1000:
        mais_de_mil += 1    
            
    total_gasto += preco_produto
    
    continuar = input('Quer continuar? s/n: ').lower()
    if not continuar == 's':
        break

print('-'*50)
print(f'\nTotal gasto: {total_gasto}')
print(f'Custa mais de mil: {mais_de_mil}')
print(f'Produto mais barato: {nome_menor_preco}')