print('------ Maior e menor peso ------')

lista_de_pesos = []

for i in range(5):
    peso = float(input(f'Digite o {i + 1}º peso: '))
    lista_de_pesos.append(peso)

print(f'Os pesos apontados foram: {lista_de_pesos}')
print(f'Sendo o maior: {max(lista_de_pesos)}')
print(f'E o menor: {min(lista_de_pesos)}')