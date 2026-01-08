print('------ PROGRESSÃO ARITMÉTICA: 10 primeiros termos (Resolução 3) ------')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i = 0

while i < 10:
    print(termo) 
    termo += razao   
    i += 1