print('------ O Tesouro Perdido do Pirata 🏴‍☠️  ------')

continuar = (input('Aperte qualquer tecla para continuar: '))

import random 

mapa = ['Caverna', 'Praia', 'Floresta', 'Montanha', 'Cachoeira']
numero_secreto = random.randint(1, 5)
tesouro_encontrado = False
tentativas = 0

print(f'''\n1 = Caverna | 2 = Praia | 3 = Floresta | 4 = Montanha | 5 = Cachoeira''')

print('\nVocê tem 2 tentativas!')

while tentativas < 2:
    numero_usuario = int(input('Escolha um local: '))
    if numero_usuario == numero_secreto:
        numero_secreto -= 1
        print(f'\nVocê encontrou o tesouro na {mapa[numero_secreto]}! Parabéns!')
        tesouro_encontrado = True
        tentativas += 2
    else: print('\nÚltima tentativa!')
    tentativas += 1

if tesouro_encontrado == False:
    print('\nVocê não é pirata, está mais pra papagaio! 🦜')
else:
    print('Você é um verdadeiro pirata! ☠️')

