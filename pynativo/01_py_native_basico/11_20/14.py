print('Exercício 14: Imprima um padrão de meia pirâmide de estrelas voltada para baixo.')
for i in range(6, 1, -1):
    for j in range(0, i - 1):
        print('*', end = ' ')
    print(' ')