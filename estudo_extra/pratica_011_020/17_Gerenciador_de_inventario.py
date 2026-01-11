bau = [{'trigo': 0,
        'madeira': 0,
        'pedra': 0,
        'tocha': 0}]

continuar = ''

# Para acessar um item do dicionário, precisamos utilizar bau[0] para acessar o dicionário,
#       depois [item] para encontra-lo. ex: bau[0]['trigo], no nosso algoritmo o 'trigo' está
#               dentro da váriavel 'item', a lista poderia ter mais dicionários, e ai sim
#                       utilizariamos a lógica do índice obrigatóriamente.
while continuar != 'sair':
        item = input('Digite um item pra adicionar ao baú: ')
        if item in bau[0]:
                bau[0][item] += 1
        else:
                print('Não temos esse item no baú, digite outro!')
        continuar = input('Digite "sair" ou dê ENTER pra continuar: ').lower()

print(bau)
                