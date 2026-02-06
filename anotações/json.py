# ============================================================
# BASE DE ESTUDO — BIBLIOTECA JSON EM PYTHON
# ============================================================
# Este arquivo serve como DOCUMENTAÇÃO e GUIA
# para o desafio de cadastro usando JSON.
#
# O objetivo do JSON é:
# - Salvar dados (listas e dicionários) em arquivo
# - Ler esses dados depois
# - Simular um "banco de dados simples"
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTANDO A BIBLIOTECA JSON
# ------------------------------------------------------------
# A biblioteca json já vem instalada no Python (biblioteca padrão)
# Ela permite converter:
# - Dicionários e listas do Python -> arquivo .json
# - Arquivo .json -> dicionários e listas do Python

import json


# ------------------------------------------------------------
# 2. ESTRUTURAS QUE O JSON SUPORTA
# ------------------------------------------------------------
# O JSON aceita APENAS tipos simples:
#
# ✔ dict      -> dicionário
# ✔ list      -> lista
# ✔ str       -> texto
# ✔ int       -> número inteiro
# ✔ float     -> número decimal
# ✔ bool      -> True / False
#
# ❌ NÃO aceita:
# - funções
# - classes
# - objetos complexos
#
# Por isso usamos lista + dicionário no desafio.


# ------------------------------------------------------------
# 3. EXEMPLO DE DADOS QUE SERÃO SALVOS
# ------------------------------------------------------------
# Exemplo de estrutura válida para JSON:

series = [
    {
        "nome": "Dark",
        "temporadas": 3,
        "nota": 9.5
    },
    {
        "nome": "Breaking Bad",
        "temporadas": 5,
        "nota": 9.8
    }
]


# ------------------------------------------------------------
# 4. SALVANDO DADOS EM UM ARQUIVO JSON
# ------------------------------------------------------------
# json.dump() é usado para SALVAR dados em um arquivo
#
# Sintaxe:
# json.dump(dados, arquivo)
#
# IMPORTANTE:
# - O arquivo deve estar aberto em modo 'w' (write)
# - Usar with open garante que o arquivo feche corretamente

with open("series.json", "w") as arquivo:
    json.dump(series, arquivo)

# Após isso:
# - Um arquivo chamado "series.json" será criado
# - Os dados da lista 'series' serão gravados nele


# ------------------------------------------------------------
# 5. LENDO DADOS DE UM ARQUIVO JSON
# ------------------------------------------------------------
# json.load() é usado para LER dados de um arquivo JSON
#
# Sintaxe:
# dados = json.load(arquivo)
#
# IMPORTANTE:
# - O arquivo deve estar aberto em modo 'r' (read)

with open("series.json", "r") as arquivo:
    dados_lidos = json.load(arquivo)

# Agora:
# - dados_lidos volta a ser uma LISTA de DICIONÁRIOS
# - Pode ser usada normalmente no Python
... (36 linhas)