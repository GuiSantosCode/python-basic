print('Exercício 2: Imprima a soma do número atual com um número anterior.')

for i in range(1,10):
    numero_atual = i
    numero_anterior = i - 1
    soma = numero_atual + numero_anterior
    print(f'Número atual: {numero_atual} | Número anterior: {numero_anterior} | Soma: {soma}')