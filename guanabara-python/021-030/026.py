print('------ Caracter no começo e final da frase ------')

frase = (input('Digite uma frase: '))

print(f'Quantas vezes aparece a letra "a":', frase.count('a'))
print(f'Em que posição ela aparece pela primeira vez:', frase.find('a') + 1)
print(f'Em que posição ela aparece pela última vez:', frase.rfind('a') + 1)