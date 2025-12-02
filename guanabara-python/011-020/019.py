print('------ Sorteio ------')

import random

aluno1 = (input('Digite seu nome: '))
aluno2 = (input('Digite seu nome: '))
aluno3 = (input('Digite seu nome: '))
aluno4 = (input('Digite seu nome: '))

escolha = random.randint(1, 4)

print('O aluno escolhido foi: ')

if escolha == 1:
    print(aluno1)
elif escolha == 2:
    print(aluno2)
elif escolha == 3:
    print(aluno3)
else:
    print(aluno4)
    
#import random
#alunos = ['Ruan', 'Guilherme', 'Luiza', 'Isis']
#escolha = random.choice(alunos)
#print(escolha)