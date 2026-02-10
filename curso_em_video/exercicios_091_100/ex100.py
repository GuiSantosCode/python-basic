from random import randint

# Definindo funções
def sorteia():
    for i in range(5):
        numero = randint(1, 100)
        numeros.append(numero)

def somaPar():
    soma = 0
    lista_par = []
    for numero in numeros:
        if numero % 2 == 0:
            lista_par.append(numero)
            soma += numero
    print(f'Lista total: {numeros}')
    print(f'Lista pares: {lista_par}')
    print(f'Soma dos pares: {soma}')
    
# Criando lista
numeros = []

# Chamando as funções
sorteia()
somaPar()