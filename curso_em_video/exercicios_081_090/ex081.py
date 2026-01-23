print('--- Listas: Decrescente, tamanho, encontrando valores ---')
print('Digite 0 para parar')

lista = []

while True:
    numero = float(input('Digite um número: '))
    if numero == 0:
        break
    lista.append(numero)

#lista_decrescente = sorted(lista, reverse=True), para guardar em uma váriavel
lista.sort(reverse=True)

print(f'Quantos números foram digitados: {len(lista)}')
print(f'Lista decrescente: {lista}')
if 5 in lista: 
    print('Tem o número 5 na lista!')
else:
    print('Não tem o número 5 na lista!')