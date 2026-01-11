print('Exercício 16: Verificar Número Palíndromo')

def palindromo(num):
    if str(num) == str(num)[::-1]:
        return 'É palíndromo!'
    else:
        return 'Não é palíndromo!'

print(palindromo(122))
print(palindromo(121))