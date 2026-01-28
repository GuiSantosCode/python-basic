print('--- Lista única: Pares e Impares ---')

lista_unica = [[],[]]

for i in range(7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista_unica[0].append(valor)
    else:
        lista_unica[1].append(valor)
    
lista_unica[0].sort()
lista_unica[1].sort()

print(lista_unica)