preco = float(input('Qual o preço do produto: '))

print('''
Condições de pagamento:
1 - À vista (pix/dinheiro)
2 - Cartão de Débito
3 - Cartão de Crédito
''')
opcao = int(input('Escolha uma opção: '))

preco_novo = preco

if opcao == 1: 
    preco_novo -= preco * 0.10
elif opcao == 2:
    preco_novo -= preco * 0.5
elif opcao == 3:
    vezes = int(input('Em quantas vezes? '))
    if vezes <= 2:
        preco_novo = preco
    else:
        preco_novo += preco * 0.20
    print(f'\nAs parcelas ficaram {vezes}x de {preco_novo / vezes:.2f}!')
    
print(f'\nO preço do produto com juros ficou: {preco_novo:.2f}')