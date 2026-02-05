import os
print('--- Dicionário em lista ---')

# COLETA DE DADOS
lista = []
mulheres = []

for i in range(4):
    dados = {}
    dados['nome'] = str(input('Digite seu nome: ')).strip().lower()
    dados['sexo'] = str(input('Digite seu sexo [m/f]: ')).strip().lower()
    if dados['sexo'] == 'f':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Digite sua idade: '))
    lista.append(dados)
    os.system('cls')

# EXIBIÇÃO
# A) Quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(lista)} pessoas!')

# B) A média de idade do grupo
media = sum(pessoa['idade'] for pessoa in lista) / len(lista)
print(f"A idade média do grupo é {media}")

# C) Uma lista com todas as mulheres
print(f'Lista com as mulheres: {mulheres}')

# D) Uma lista com todas as pessoas com idade acima da média
acima_media = []
for pessoa in lista:
    if pessoa['idade'] > media:
        acima_media.append(pessoa['nome'])
print(f'Pessoas com idade acima da média do grupo: {acima_media}')