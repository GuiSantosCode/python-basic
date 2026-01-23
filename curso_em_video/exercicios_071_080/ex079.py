print('--- Lista ordenada com números únicos ---')
print('Digite o número "0" quando quiser parar.')

lista = []

while True:
    numero = float(input('Digite um número: '))
    
    if numero == 0:
        break
    
    if numero in lista:
        continue
    else: 
        lista.append(numero)
        
lista.sort()
print(lista)