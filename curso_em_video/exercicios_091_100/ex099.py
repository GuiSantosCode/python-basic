print('--- Função: Maior número ---')

# Função
def maior(n):
    print(f'O maior número é: {max(n)}')
    
# Lista
qntd = int(input('Quantos números quer adicionar? '))
numeros = []

# Adicionando números a lista
for i in range(qntd):
    numero = int(input('Adicione o número que quiser: '))
    numeros.append(numero)
    
# Chamando a função
maior(numeros)