import random

numero_sorteado = random.randint(0, 3)

numero_tentado = int(input('Tente um número de 0 a 3: '))

if numero_tentado == numero_sorteado:
    print('You Win!!!')
else:
    print(f'You Lose!!!')

print(f'O computador escolheu {numero_sorteado}!')