print('--- Tupla, valores, e parâmetros ---')

valores = ()

for i in range(4):
    valor = int(input('Digite um valor: '))
    valores += (valor,)

print(f'\nQuantas vezes apareceu o número 9: {valores.count(9)}')

print(f'\nEm que posição foi digitado o primeiro valor 3: {valores.index(3) + 1}° posição!')

print(f'\nQuais foram os números pares: ', end='')
for item in valores:
    if item % 2 == 0:
        print(item, end = ' | ')