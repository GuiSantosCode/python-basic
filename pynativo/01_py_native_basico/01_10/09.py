print('Exercise 9: Check Palindrome Number')

numero = int(input('Digite um número: '))
numero_convertido = str(numero)

if numero_convertido == numero_convertido[::-1]:
    print('Sim, o número fornecido é um número palíndromo!')
else: 
    print('Não, o número fornecido não é um número palíndromo!')