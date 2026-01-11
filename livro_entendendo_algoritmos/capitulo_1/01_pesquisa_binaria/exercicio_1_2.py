print('''
EXERCÍCIO: 1.2
Suponha que você duplique o tamanho da lista. Qual seria o número máximo de 
etapas que você levaria para encontrar o nome desejado?   
Resposta: 8  
''')

lista_nomes = 128 * 2 # Duplicando a lista para resolução do exercício
etapas = 0

while lista_nomes > 1: # Se for 1, você achou o item.
    lista_nomes = lista_nomes // 2
    etapas += 1

print(f'No máximo {etapas} etapas.')