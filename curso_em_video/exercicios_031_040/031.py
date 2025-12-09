print('------ Preço por distância ------')

distancia_viagem = int(input('Qual a distância da sua viagem? '))

if distancia_viagem <= 200:
    preco_passagem = distancia_viagem * 0.50
else: 
    preco_passagem = distancia_viagem * 0.45

print(f'Sua passagem vai lhe custar R${preco_passagem:.2f}!')