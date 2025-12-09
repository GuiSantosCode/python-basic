print('Exercício 3: Imprima os caracteres presentes em um número de índice par.')

algo = input('Escreva algo: ')
tamanho = len(algo)

print(f'''
Escreveu: {algo}
Quantidade de letras: {tamanho}
''')

for i in algo[0::2]: 
    print(i)