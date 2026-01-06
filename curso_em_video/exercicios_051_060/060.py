print('------ Fatorial ------')

numero = int(input('Digite um número: '))
fatorial = numero
multiplicador = numero - 1

while multiplicador > 0:
    fatorial *= multiplicador
    multiplicador -= 1

print(fatorial)