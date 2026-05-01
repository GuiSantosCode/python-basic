import time
import random
# FUNÇÃO

def acertos(a, e):
    '''
    Parâmetro a: Quantidade de acertos
    Parâmetro e: Quantidade de erros
    Retorno: taxa de acertos
    '''
    taxa = a * 20
    
    print('\nGerando Relatório', end='')
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(0.50)
    print('\n')
    return taxa

def jogo(a):
    '''
    Parâmetro a: Acertos
    Retorna: Jogo sorteado ou nenhum jogo
    '''
    jogos = [
    "Resident Evil 2 (Remake)",
    "Resident Evil 3 (Remake)",
    "Resident Evil 4 (Remake)",
    "Resident Evil 7: Biohazard",
    "Resident Evil Village",
    "Resident Evil Re:Verse",
    "Resident Evil Gold Edition"
    ]
    if a > 2:
        sorteado = random.choice(jogos)
        return sorteado
    else: 
        return 'Você não é fã e não vai ganhar nada!'
    