print('--- Brasileirao: Manipulação de tuplas')

brasileirao = ( "Flamengo", "Palmeiras", "Cruzeiro", "Mirassol",
               "Fluminense", "Botafogo", "Bahia", "São Paulo",
               "Grêmio", "Red Bull Bragantino", "Atlético-MG", "Santos",
               "Corinthians", "Vasco da Gama", "Vitória", "Internacional",
               "Ceará", "Fortaleza", "Juventude", "Sport" )

print('\nOs 5 primeiros colocados: ')
for pos, time, in enumerate(brasileirao[0:5], start=1):
    print(f'{pos}° {time}')
    
print('\nOs últimos 4 colocados: ')
for pos, time, in enumerate(brasileirao[-4:], start=17):
    print(f'{pos}° {time}')
    
print(f'\nTimes em ordem alfabética: {sorted(brasileirao)}')

print('\nEm que posição está o Fluminense? ')
for pos, time in enumerate(brasileirao, start=1):
    if time == 'Fluminense':
        print(f'{pos}° {time}')