print('------ PROGRESSÃO ARITMÉTICA: 10 primeiros termos (Resolução 2) ------')

dez_termos = []

primeiro_termo = int(input('Qual primeiro termo: '))
razao = int(input('Qual a razão? '))

nove_termos = primeiro_termo
dez_termos.append(primeiro_termo)

for i in range(9):
    nove_termos += razao
    dez_termos.append(nove_termos)
print(dez_termos)