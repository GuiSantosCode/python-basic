dicionario = {}

user_frase = str(input('Digite uma frase: ')).lower().strip()
user_lista = user_frase.split()

for palavra in user_lista:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print(dicionario)

