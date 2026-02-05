from datetime import datetime
dicionario = {}

# COLETA DE DADOS

# Nome
dicionario['nome'] = str(input('Digite seu nome: ')).strip()
# Idade
ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = datetime.now().year 
dicionario['idade'] = ano_atual - ano_nasc
# Carteira de trabalho
while True: 
    dicionario['ctps'] = int(input('Digite sua carteira de trabalho: '))
    if dicionario['ctps'] == 0:
        continue
    else:
        break
# Ano de contratação
while True:
    dicionario['contratacao'] = int(input('Que ano você foi contratado? '))
    if dicionario['contratacao'] < ano_nasc or dicionario['contratacao'] > ano_atual:
        print(f'Impossível você ter sido contratado neste ano!')
        print(f'Digite outro!')
        continue
    else:
        break
# Salário
while True:
    dicionario['salario'] = float(input('Digite seu salário: '))
    if dicionario['salario'] == 0:
        continue
    else:
        break
# Idade de aposentadoria
while True:
    sexo = str(input('Você é homem ou mulher [h/m]: ')).lower().strip()
    if sexo in 'hm':
        break
    else:
        print(f'Você digitou errado!')
        continue
if sexo == 'h':
    dicionario['aposentadoria'] = (dicionario['contratacao'] + 35) - ano_nasc
else:
    dicionario['aposentadoria'] = (dicionario['contratacao'] + 30) - ano_nasc

# EXIBIÇÃO
for k, v in dicionario.items():
    print(f'{k} = {v}')