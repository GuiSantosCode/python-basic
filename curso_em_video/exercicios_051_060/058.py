print('------ Sorteio melhorado ------')

from random import randint

computador = randint(0, 10)
chute = 0
tentativas = 0

while True:
    try:
        while chute != computador: 
            chute = int(input('Chute um número de 0 a 10: '))
            tentativas += 1
            
            if chute != computador:
                print('Você errou, tente novamente!')
            if chute > 10: 
                print('Só de 0 a 10!')

        print('Você acertou, parabéns!')
        print(f'A quantidade de tentativas foi: {tentativas}')
        break

    except ValueError:
        print('O programa aceita apenas números inteiros!')