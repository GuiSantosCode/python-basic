print('------ Lançamento de Foguete! ------')

import time

tempo = 10
voo = 10
lancar = (input('Aperte qualquer tecla para lançar: '))

while tempo > 0:
    print(f'{tempo}')
    tempo -= 1
    time.sleep(1)

print('Lançamento! ')

