print('--- Matriz: Versão 2 ---')

lista_matriz = [[],[],[]]

# Preenchimento
for linha in range(3):
    for valores in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {valores}]: '))
        lista_matriz[linha].append(valor)
print('-=' * 25)

# Exibição  
for linha in lista_matriz:
    for valores in linha:
        print(f'[ {valores} ]', end='')
    print()
print('-=' * 25)

# A soma dos valores pares
pares = []
for linha in lista_matriz:
    for valores in linha: 
        if valores % 2 == 0:
            pares.append(valores)
print(f'A soma dos valores pares é: {sum(pares)}')
print('-=' * 25)
            
# A soma dos valores da terceira coluna
terceira_coluna = []
for linha in lista_matriz:
    terceira_coluna.append(linha[2])
print(f'A soma dos valores da terceira coluna é: {sum(terceira_coluna)}')
print('-=' * 25)

# O maior valor da segunda linha
print(f'O maior valor da segunda linha é: {max(lista_matriz[1])}')
print('-=' * 25)