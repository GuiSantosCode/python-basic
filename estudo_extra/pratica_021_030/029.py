numeros = [[],[]]

while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
    
print(f'Números = {numeros}')
print(f'Pares = {numeros[0]}')
print(f'Impares = {numeros[1]}')