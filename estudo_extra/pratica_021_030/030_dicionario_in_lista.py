print('--- Dicionários dentro de lista ---')
lista = []
soma_idade = 0

print(f"Digite 's' pra continuar e 'n' pra parar!")
while True:
    dicionario = {}

    dicionario['nome'] = str(input('Digite seu nome: ')).strip().title()
    dicionario['idade'] = int(input('Qual sua idade? '))
    lista.append(dicionario.copy())
    soma_idade += dicionario['idade']
    
    continuar = str(input('Quer continuar [s/n]? ')).lower().strip()
    if continuar == 'n':
        break

if lista:
    media = soma_idade / len(lista)
else: 
    media = 0

# Quantidade de pessoas
print(f'Quantidade de pessoas = {len(lista)}')

# Média de idade
print(f'Média de idade = {media:.0f}')

# Pessoas com idade acima da média
print(f'Pessoas acima de {media:.0f} anos = ',end='')

for pessoa in lista:
    if pessoa['idade'] > media:
        print(pessoa['nome'], end=' ')