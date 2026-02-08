print('--- Cadastro de restaurantes ---')
import os

def tabela(txt):
    print()
    print()
    print('-' * 130)
    print(txt)
    print('-' * 130)

restaurantes = []

qntd = int(input('Digite quantos restaurantes quer cadastrar: '))
os.system('cls')

for i in range(qntd):
    restaurante = {}
    # Nome do restaurante
    restaurante['nome'] = str(input('Digite o nome do restaurante: '))
    
    # Tipo de comida
    restaurante['tipo'] = str(input('Digite o tipo da comida (Italiana, Japonesa..): '))
    
    # Pratos
    qntd_prato = int(input('Quantos pratos você quer cadastrar? '))
    pratos = []
    for j in range(qntd_prato):
        prato = str(input(f'Digite o nome do {j + 1}° prato: '))
        pratos.append(prato)
    os.system('cls')
    restaurante['lista de pratos'] = pratos
    restaurantes.append(restaurante.copy())

tabela(f"{'RESTAURANTE':<25} {'TIPO DE COMIDA':<25} {'CARDÁPIO':<25}")

# Restaurantes cadastrados
for restaurante in restaurantes:
    pratos = ', '.join(restaurante['lista de pratos'])
    print(f"{restaurante['nome']:<25} {restaurante['tipo']:<25} {pratos:<25}")