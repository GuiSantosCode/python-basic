print('------ Sensor do mundo invertido ------')

def verificar_intensidade_lampada(intensidade_da_luz):
    if intensidade_da_luz < 0:
        return 'Erro, intensidade de luz negativo!'
    elif intensidade_da_luz <= 20:
        return 'O Demogorgon está vindo! Corra!'
    elif intensidade_da_luz <= 70:
        return 'A luz está piscando... Will está tentando falar?'
    else:
        return 'Tudo calmo em Hawkins.'
    
print(verificar_intensidade_lampada(90))