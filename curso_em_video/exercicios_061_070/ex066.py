print('------ Flag: ex03 ------')

qntd_numeros = 0
soma_numeros = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    qntd_numeros += 1
    soma_numeros += numero
    
print(f'Quantidade de números: {qntd_numeros}')
print(f'Soma dos números: {soma_numeros}')