print('------ O Alarme do WILL! ------')

def verificar_distancia_demogorgon(distancia):
    if distancia < 10:
        return 'CORRA WILL!'
    elif distancia < 50:
        return 'SHH, FIQUE EM SILÊNCIO!'
    else: 
        return 'VOCÊ ESTÁ SEGURO, POR ENQUANTO!'


distancia_input = float(input('A quantos metros o Will está do Demogorgon? '))

print(verificar_distancia_demogorgon(distancia_input))