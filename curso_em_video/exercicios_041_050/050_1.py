print('------ Soma de 6 números (Resolução 1) ------')

soma = 0
for i in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num 
print(f'A soma dos números pares digitados é: {soma}')

    