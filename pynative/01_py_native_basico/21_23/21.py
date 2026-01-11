print('Exercício 21: Verifique se uma string inserida pelo usuário contém dígitos usando um laço for.')

def contem_digito(frase):
    for i in range(0, 9 + 1):
        for letra in frase:
            if letra == str(i): 
                return True
    return False

frase_input = input('Digite uma frase: ')

print(contem_digito(frase_input))