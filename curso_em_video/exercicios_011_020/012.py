print('------ Promocão 5% de desconto! ------')

preco = float(input('Quanto custa o produto? R$'))
preco_desconto = (preco) - (preco * 0.05)
#preco_desconto = preco * 0.95

print(f'O preço com desconto fica: R${preco_desconto:.2f}')