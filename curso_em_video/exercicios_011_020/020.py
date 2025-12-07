import random 

alunos = ['Ruan', 'Guilherme', 'Mari', 'Isis']
print(alunos)

i = 0

while i < 4:
    escolha = random.choice(alunos)
    print(escolha)
    alunos.remove(escolha)
    i += 1
    
''' 
import random
alunos = ['Ruan', 'Guilherme', 'Luiza', 'Isis']
apresentacao = random.sample(alunos, 4) 
print(apresentacao) 
'''