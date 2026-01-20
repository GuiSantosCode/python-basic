print('--- Tuplas: Encontre vogais ---')

tupla = ('orar', 'cagar', 'computador', 'faculdade',
         'videogame', 'java', 'python', 'felicidade')

for palavra in tupla:
    print(palavra, end=': ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' | ')
    print('')