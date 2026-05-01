import time

def efeito_cyberpunk(frase, velocidade):
    '''
    Exibe o texto caractere por caractere com atraso.
    '''
    for c in frase: 
        print(c, end='', flush=True)
        time.sleep(velocidade)
    print('')