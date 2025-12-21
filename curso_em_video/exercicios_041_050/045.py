import random

print('------ Pedra, papel e tesoura! ------')

choices = ['pedra', 'papel', 'tesoura']
print('0 = pedra | 1 = papel | 2 = tesoura')

maq_index = random.randint(0, 2)
maq_choice = choices[maq_index]

user_index = int(input('Escolha uma opção: '))
user_choice = choices[user_index]

print(f'Você escolheu: {user_choice}')
print(f'A máquina escolheu: {maq_choice}')

if user_choice == maq_choice:
    print('EMPATE!!!')
elif ((user_choice == 'pedra' and maq_choice == 'tesoura') or
      (user_choice == 'papel' and maq_choice == 'pedra') or
      (user_choice == 'tesoura' and maq_choice == 'papel')):
    print('VOCÊ VENCEU!')
else: 
    print('A MÁQUINA VENCEU!')