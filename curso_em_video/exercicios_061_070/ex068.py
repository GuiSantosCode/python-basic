print('------ PAR ou ÍMPAR ------')

from random import randint 

print('Vamos jogar PAR ou IMPAR!!!')

vitorias = 0

while True:
    numero_computador = randint(1, 5)
    escolha_jogador = str(input('Você quer impar ou par? '))
    numero_jogador = int(input('Digite um número de 1 a 5: '))
    
    if (numero_computador + numero_jogador) % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    
    if resultado == escolha_jogador:
        print(f'Deu {resultado}, você venceu!')
        vitorias += 1
    else:
        print(f'Deu {resultado}, você perdeu!')
        break

print(f'Você venceu {vitorias} vezes consecutivas.')