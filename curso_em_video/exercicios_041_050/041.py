print('------ Categoria de natação! ------')

import datetime

ano_atual = (datetime.datetime.now().year)

ano_nascimento = int(input('Que ano você nasceu? '))

idade = ano_atual - ano_nascimento 

if idade < 9:
    print('MIRIM')
elif idade < 14: 
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 20:
    print('SÊNIOR')
else: 
    print('MASTER')