print('Exercício 1: Calcule a multiplicação e a soma de dois números.')

def multiplicacao_ou_soma(dado1, dado2):
    produto = dado1 * dado2
    if produto <= 1000:
        return produto
    else: 
        soma = dado1 + dado2
        return soma
        
resultado = multiplicacao_ou_soma(20, 30)
print(resultado)

resultado = multiplicacao_ou_soma(30,40)
print(resultado)