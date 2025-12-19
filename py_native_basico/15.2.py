print('Exercício 15: Obtenha um valor inteiro de base elevado à potência do expoente.')

def expoente(base, expoente):
    num = base
    resultado = 1
    while expoente > 0:
        resultado *= base
        expoente -= 1
    return resultado

print(expoente(5,4))