print('----- TABOADA -----')

multiplicador = int(input('Digite o número que você quer a taboada: '))

for i in range(1,11):
    print(f'{multiplicador} x {i:2} = {multiplicador * i:2}')