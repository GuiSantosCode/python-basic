import os
from random import randint
from time import sleep

jogo = {}

# Criando dicionário de jogadas
for i in range(4):
    input('Aperte enter pra jogar o dado: ')
    jogada = randint(1,20)
    for j in range(3):
        print('tuc')
        sleep(0.5)
    print(jogada)
    jogo[f'jogador{i+1}'] = jogada
    sleep(0.5)
    os.system('cls')
  
# Ordenando o dicionário
ranking = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))

# Exibindo jogadas ordenadas como ranking
print('--- Ranking ---')
for key, value in ranking.items():
    print(f'{key} = {value}')

# Jogada vencedora
print(f'\nA jogada vencedora foi: {max(ranking.values())}')