print('--- Lista: Análise de peso ---')

galera = []
dado = []
maior = 0
menor = 0

for i in range(4):
    nome = str(input('Digite seu nome: '))
    dado.append(nome)
    peso = float(input('Digite seu peso: '))
    if len(galera) == 0:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    dado.append(peso)
    galera.append(dado[:])
    dado.clear()

print(f'Tem {len(galera)} pessoas cadastradas!')

print('Pessoas pesadas: ', end='')
for pessoa in galera:
    if pessoa[1] == maior:
        print(f'{pessoa}', end='')

print('\nPessoas leves: ', end='')
for pessoa in galera:
    if pessoa[1] == menor: 
        print(f'{pessoa}', end='')