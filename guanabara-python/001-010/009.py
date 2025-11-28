print('----- TABOADA -----')
num_multiplicado = int(input('Qual número você quer a taboada? '))

for i in range(1, 11):
    resultado = num_multiplicado * i
    print(f'{num_multiplicado} X {i} = {resultado}')