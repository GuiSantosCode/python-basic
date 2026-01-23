print('--- Lista ordenada sem método ---')

lista = []

for i in range(5):
    valor = float(input('Digite um valor: '))
    if not lista or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor < lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1
            
print(lista)