# PROGRAMA PRINCIPAL

from uteis import numeros

# Pode ser feito dessa forma abaixo, ai não precisa usar o uteis.
# from uteis import fatorial, dobro, triplo

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O dobro de {num} é {numeros.triplo(num)}')