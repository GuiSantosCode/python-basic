"""
Exercício 4 – Percorrendo dicionários

Objetivo:
Praticar o uso de laços para percorrer dicionários.

O programa:
- Cria um dicionário com informações de um produto
- Percorre o dicionário exibindo cada chave e seu valor
"""
print('--- Prática dicionário: 4 ---')
produto = {
    'nome': 'Mouse',
    'preco': 150,
    'estoque': 20
}

for k, v in produto.items():
    print(f'{k} -> {v}')    