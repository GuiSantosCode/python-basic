print('------ Os maiores e menor de idade ------')

from datetime import datetime

ano_atual = (datetime.now().year)
maiores_de_idade = 0
menores_de_idade = 0

for i in range(7):
    ano_nascimento = int(input('Em que ano você nasceu? '))
    
    if ano_atual - ano_nascimento > 18: 
        maiores_de_idade += 1
    else: 
        menores_de_idade += 1

print(f'Maiores de idade: {maiores_de_idade}')
print(f'Menores de idade: {menores_de_idade}')