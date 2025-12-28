frase = str(input('Digite uma frase: ')).replace(' ','').lower()

if frase[::-1] == frase:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')