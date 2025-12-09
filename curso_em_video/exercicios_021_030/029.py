print('=======')
print(' RADAR')
print('=======')

vel_carro = int(input('Qual a velocidade do carro? '))

if vel_carro > 80:
    km_excedido = vel_carro - 80
    preco_km_excedido = 7
    multa = km_excedido * preco_km_excedido
    print(f'Carro passou a {vel_carro}Km/h, MULTADO!')
    print(f'O carro excedeu {km_excedido}km/h, a multa vai ser de {multa}R$!')
else:
    print(f'Carro liberado!')
  
  
'''
velocidade = int(input('Qual velocidade você passou? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'Você foi multado, e o valor é {multa}R$(7R$ para cada Km a partir de 80Km). ')
else:
    print('Ficha limpa.')
'''