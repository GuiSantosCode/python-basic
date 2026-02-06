def lin(txt):
    print()
    print()
    print('-' * 60)
    print(txt)
    print('-' * 60)

# Coleta de dados
lista = [[],[]]

qntd = int(input('Quantos jogos você quer listar? '))
for i in range(qntd):
    jogo = {}
    jogo['nome'] = str(input('Nome: '))
    jogo['lanc'] = int(input('Ano de lançamento: '))
    status = str(input('Já iniciou esse jogo [s/n]? ')).lower().strip()
    if status == 's':
        jogo['status'] = 'Iniciado'
    else: 
        jogo['status'] = 'Pendente'
    jogo['expec'] = str(input('Expectativa (ex: 60%): '))
    lista.append(jogo.copy())
    if jogo['status'] == 'Iniciado':
        lista[0].append(jogo.copy())
    else:
        lista[1].append(jogo.copy())

# Exibição

# Iniciados
lin(f'{'NOME':<13} {'LANÇAMENTO':<13} {'STATUS':<13} {'EXPECTATIVA':<13} ')
for jogo in lista[0]:
    print(f'{jogo['nome']:<13} {jogo['lanc']:<13} {jogo['status']:<13} {jogo['expec']:<13}')

# Pendentes
lin(f'{'NOME':<13} {'LANÇAMENTO':<13} {'STATUS':<13} {'EXPECTATIVA':<13} ')
for jogo in lista[1]:
    print(f'{jogo['nome']:<13} {jogo['lanc']:<13} {jogo['status']:<13} {jogo['expec']:<13}')