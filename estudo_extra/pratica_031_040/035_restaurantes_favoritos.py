print('--- Cadastro de restaurantes ---')
import os

def tabela(txt):
    print()
    print()
    print('-' * 100)
    print(txt)
    print('-' * 100)

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

tabela(f"{'RESTAURANTE':<25} {'QUANTIDADE DE PRATOS':<25} {'CARDÁPIO':<25}")

# Restaurantes cadastrados
for restaurante in restaurantes:
    print(f"{restaurante['nome']:<25} {len(restaurante['lista de pratos']):<25} {str(restaurante['lista de pratos']):<25}")