print('--- Números aleatórios em tupla ---')

from random import randint

lista_num = ()

while len(lista_num) < 5:
    num = randint(1, 100)
    lista_num += (num,) # Quando colocamos a virgula cria-se a tupla, com um valor, nesse caso o 'num'
    
print(lista_num)
print(min(lista_num))
print(max(lista_num))