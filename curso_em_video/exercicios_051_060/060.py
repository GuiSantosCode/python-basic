print('------ Fatorial ------')

fatorial = int(input('Digite um número: '))
multiplicador = fatorial - 1

while multiplicador > 0:
    fatorial *= multiplicador
    multiplicador -= 1

print(fatorial)