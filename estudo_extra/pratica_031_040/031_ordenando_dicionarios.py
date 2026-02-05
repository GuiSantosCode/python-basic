print('--- Ordenando Dicionários ---')


lista = []

for i in range(3):
    jogo = {}
    jogo['nome'] = str(input('Digite o nome do jogo: '))
    jogo['ano'] = int(input('Digite o ano de lançamento: '))
    jogo['nota'] = float(input('Que nota você da pra esse jogo? '))
    lista.append(jogo)
    
# Ordem de lançamento
ano_lancamento = [jogo['ano'] for jogo in lista]
ano_lancamento.sort()

print('--- Ordem de lançamento ---')
for pos, ano in enumerate(ano_lancamento, start=1):
    print(f'{pos}° - {ano}')
    

# Ordem de nota
notas = [jogo['nota'] for jogo in lista]
notas.sort()

print('--- Ordem das Notas ---')
for pos, nota in enumerate(notas, start=1):
    print(f'{pos}° - {nota}')


# Ordem de nomes
nomes = [jogo['nome'] for jogo in lista]
nomes.sort()

print('--- Ordem dos nomes ---')
for pos, nome in enumerate(nomes, start=1):
    print(f'{pos}° - {nome}')

