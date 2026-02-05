print('--- Dicionário: Aproveitamento do jogador ---')

import os
# Entrada de dados
lista = []

qntd = int(input('Quantos jogadores você quer adicionar? '))
for i in range(qntd):
    player = {}
    player['nome'] = str(input('Nome: '))
    player['partidas'] = int(input('Quantidade de partidas: '))
    player['gols'] = 0
    print(f'Digite a quantidade de gols por partida!')
    for c in range(player['partidas']):
        player['gols'] += int(input(f'{c + 1}° partida: '))
    lista.append(player.copy())
    os.system('cls')

# Exibição de dados 
print('-' * 80)
print(f"{'NOME':<13} {'PARTIDAS':<13} {'GOLS':<13} {'MÉDIA DE GOLS POR PARTIDA':<13}")
print('-' * 80)
for player in lista:
    print(f'{player['nome']:<13} {player['partidas']:<13} {player['gols']:<13} {player['gols'] / player['partidas']:<13.2f}')