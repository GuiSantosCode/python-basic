print('Exercício 23: Crie um cronômetro de contagem regressiva simples usando um whileloop.')

from time import sleep

def contagem_regressiva(segundos):
    while segundos > 0:
        print(f'Tempo restante: {segundos} segundo(s)')
        sleep(1)
        segundos -= 1
    print('Tempo esgotado!')

segundos_input = int(input('A partir de qual segundo quer regredir a contagem? '))

contagem_regressiva(segundos_input)