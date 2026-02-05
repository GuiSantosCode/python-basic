print('--- Dicionário: Aproveitamento do jogador ---')

player = {}

# Entrada de dados
player['nome'] = str(input('Nome: '))
player['partidas'] = int(input('Quantidade de partidas: '))
player['gols'] = 0
print(f'Digite a quantidade de gols por partida!')
for c in range(player['partidas']):
    player['gols'] += int(input(f'{c + 1}° partida: '))

# Exibição de dados
for k, v in player.items():
    print(f'{k} = {v}')