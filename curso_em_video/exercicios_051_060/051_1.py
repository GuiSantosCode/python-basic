print('------ PROGRESSÃO ARITMÉTICA: 10 primeiros termos (Resolução 1) ------')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range(10):
    print(termo) 
    termo += razao   