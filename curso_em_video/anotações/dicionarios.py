# =================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# Aula 19: Dicionários
# =================================================================

# 1. CONCEITO BÁSICO
# Diferente das listas (índices numéricos), dicionários permitem 
# usar índices literais (chaves/keys).
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

# 2. ACESSANDO DADOS
# Utilizamos as chaves para retornar os valores correspondentes.
# Nota: Use aspas diferentes (simples/duplas) para não dar erro no print.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# 3. VALORES, CHAVES E ITENS
print(pessoas.values()) # Retorna apenas os valores
print(pessoas.keys())   # Retorna apenas as chaves
print(pessoas.items())  # Retorna a composição (chave, valor)

# 4. ITERAÇÃO (FOR)
# Usamos o método .items() para desempacotar chave (k) e valor (v).
for k, v in pessoas.items():
    print(f'{k} = {v}')

# 5. MANIPULAÇÃO
# Adicionar elementos: Não precisa de .append(), basta criar a nova chave.
pessoas['peso'] = 98.5

# Remover elementos:
del pessoas['sexo']

# Modificar valores:
pessoas['nome'] = 'Leandro'

# 6. DICIONÁRIOS DENTRO DE LISTAS
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf']) # Rio de Janeiro

# 7. CÓPIA DE DICIONÁRIOS
# IMPORTANTE: Para copiar um dicionário para uma lista sem criar ligação,
# não usamos [:] (fatiamento de listas), usamos o método .copy()
estado = dict()
brasil_novo = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil_novo.append(estado.copy()) # Cria uma cópia real do dicionário

# =================================================================
# TROFÉUS DA AULA (Exercícios para praticar)
# Faça Agora: 090, 091, 092, 093
# Deixe para a Segunda Run (Complexidade maior): 094, 095
# =================================================================