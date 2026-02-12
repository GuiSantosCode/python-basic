print('--- Função 2: Voto ---')
from datetime import datetime

def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'Negado!'
    elif idade < 18:
        return 'Opcional!'
    else:
        return 'Obrigatório!'


# Programa principal
ano = int(input('Que ano você nasceu? '))
print(voto(ano))