print('Exercício 5: Verifique se o primeiro e o último número de uma lista são iguais.')

def primeiro_e_ultimo_numero(lista):
    return lista[0] == lista[-1]
    
list = [10, 20, 30, 40, 10]

print(primeiro_e_ultimo_numero(list))

list = [75, 65, 25, 75, 30]

print(primeiro_e_ultimo_numero(list))