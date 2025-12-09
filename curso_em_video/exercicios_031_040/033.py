print('------ Menor e Maior Número ------')

num = int(input('Digite um número: '))
num_maior = num
num_menor = num

i = 1
while i < 5:
    num = int(input('Digite um número: '))
    if num > num_maior:
        num_maior = num
    if num < num_menor:
        num_menor = num
    i += 1

print(f'Menor número digitado: {num_menor}')
print(f'Maior número digitado: {num_maior}')