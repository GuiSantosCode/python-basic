print('Exercício 10: Combine duas listas usando a seguinte condição.')

def lista_final(list1, list2):
    lista_impar = []
    for num in list1:
        if num % 2 == 1:
            lista_impar.append(num)
    for num in list2:
        if num % 2 == 1:
            lista_impar.append(num)
    return lista_impar

lista_usuario_1 = [10, 20, 25, 30, 35]
lista_usuario_2 = [40, 45, 60, 75, 90]

print(lista_final(lista_usuario_1, lista_usuario_2))
