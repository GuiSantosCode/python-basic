print('--- ---')

lista = []
lista_par = []
lista_impar = []

for i in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

for item in lista:
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)

lista.sort()
lista_par.sort()
lista_impar.sort()

print(lista)
print(lista_par)
print(lista_impar)