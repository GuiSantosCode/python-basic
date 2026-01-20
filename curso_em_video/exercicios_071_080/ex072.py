print('--- Contagem de 0 à 20 ---')

print('Contagem de 0 à 20: ')

lista = ('um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito',
         'nove', 'dez','onze', 'doze',
         'treze', 'quatorze', 'quinze',
         'dezeseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))

if 0 <= num <= 20:
    print(lista[num - 1])
    
else:
    print('Número inválido!')