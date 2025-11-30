print('------ Hogwarts: Chapéu Seletor ------')

import random

continuar = (input('Aperte qualquer tecla pra continuar: '))
numero = random.randint(1, 4)

print('O chápeu decidide...')

if numero == 1:
    print(' Grifinória 🦁')
elif numero == 2:
    print('Sonserina 🐍')
elif numero == 3:
    print('Lufa-Lufa 🦡')
else:
    print('Corvinal 🦅')