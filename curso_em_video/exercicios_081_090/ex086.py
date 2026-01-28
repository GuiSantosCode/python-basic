print('--- Matriz: Versão 1 ---')

lista_matriz = [[],[],[]]

# Preenchimento
for linha in range(3):
    for valores in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {valores}]: '))
        lista_matriz[linha].append(valor)

print('-=' * 20)

# Exibição  
for linha in lista_matriz:
    for valores in linha:
        print(f'[ {valores} ]', end='')
    print()