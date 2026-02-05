print('-- Impar e Par ---')

print('Digite 0 se quiser parar!')

lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break

    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

if not lista:
    print(f'Não foi adicionado nenhum número!')
else:
    print(f'Lista completa = {lista}')
    print('Nenhum par adicionado!' if not pares else f'Quantidade de pares = {len(pares)}')
    print('Nenhum impar adicionado!' if not impares else f'Quantidade de impares = {len(impares)}')
    print('Lista vazia' if not pares else f'Pares = {pares}')
    print('Lista vazia' if not impares else f'Impares = {impares}')