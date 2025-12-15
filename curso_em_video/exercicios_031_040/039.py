print('------ Alistamento! ------')

import datetime

ano_nascimento = int(input('Que ano você nasceu? '))

ano_atual = int(datetime.datetime.now().year)
idade =  ano_atual - ano_nascimento 

tempo_falta = 18 - idade
tempo_passou = idade - 18


if idade < 18:
    print('Você ainda vai se alistar!')
    print(f'Faltam {tempo_falta} anos!')
elif idade == 18:
    print('Você está na hora de se alistar!')
else: 
    print('Já passou o tempo de se alistar!')
    print(f'Passou {tempo_passou} anos!')