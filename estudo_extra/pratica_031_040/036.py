'''
Exercício 1 – Dicionários em Python

Objetivo:
Praticar a criação e manipulação de dicionários usando chaves e valores.

O programa:
- Cria um dicionário com dados pessoais
- Acessa e percorre chaves e valores
- Atualiza e adiciona informações
- Permite buscar uma chave informada pelo usuário
'''

# Step 1
dicionario = {
    'nome':'Guilherme',
    'idade': 23,
    'cidade': 'Florianópolis'
}

print(dicionario['nome'])
for k in dicionario.keys():
    print(f'Chaves = {k}')
for v in dicionario.values():
    print(f'Valores = {v}')

# Step 2 
dicionario['idade'] = 26
dicionario['profissao'] = 'Preparador'
for k,v in dicionario.items():
    print(f'{k} = {v}')

# Step 3
usuario = str(input('Digite um nome de chave para procurar: ')).strip()
if usuario in dicionario:
    print(dicionario[usuario])
else:
    print('Chave não encontrada')