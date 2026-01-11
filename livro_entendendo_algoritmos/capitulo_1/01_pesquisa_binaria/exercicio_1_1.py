print('''
EXERCÍCIO: 1.1
Suponha que você tenha uma lista com 128 nomes e esteja
fazendo uma pesquisa binária. Qual seria o número máximo de
etapas que você levaria para encontrar o nome desejado?    
Resposta: 7  
''')

lista_nomes = 128
etapas = 0

while lista_nomes > 1: # Se for 1, você achou o item.
    lista_nomes = lista_nomes // 2
    etapas += 1

print(f'No máximo {etapas} etapas.')