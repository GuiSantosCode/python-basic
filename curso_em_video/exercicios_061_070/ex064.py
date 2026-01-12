print('------ Flag: ex01 ------')

numero = 0
qntd_numeros = 0
soma_numeros = 0

while not numero == 999:
    qntd_numeros += 1    
    soma_numeros += numero
    numero = int(input('Digite um número: '))
    
print(f'A soma dos números é {soma_numeros}')