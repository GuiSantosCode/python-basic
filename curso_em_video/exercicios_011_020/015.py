print('------ Aluguel de carros ------')

km = float(input('Quantos km você percorreu? '))
diaria = int(input('Quantos dias? '))
preco_total = (km * 0.15) + (diaria * 60)

print(f'Ficou R${preco_total:.2f}, qual a forma de pagamento? ')