#(if/elif/else)

print('\nRANK DE HERÓI!!!\n')

xp = int(input('Quanto de xp seu herói tem? '))

print('O seu rank de herói é: ')

if xp < 0:
    print('Erro de execução, valor inválido!')
elif xp < 1000:
    print('Ferro!')
elif xp < 2000:
    print('Bronze!')
elif xp < 5000:
    print('Prata!')
elif xp < 8000:
    print('Ouro!')
elif xp < 9000:
    print('Platina!')
elif xp < 10000:
    print('Diamante!')
else:
    print('Mestre!')