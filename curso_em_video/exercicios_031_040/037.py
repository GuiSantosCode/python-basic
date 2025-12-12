numero_input = input('Digite um número qualquer: ')

if not numero_input.isdigit(): 
    print('isso não é um número inteiro! PROGRAMA FINALIZADO!')
    exit()

numero = int(numero_input)

print('''Qual será a Base de Conversão: 
1 = Binário
2 = Octal
3 = Hexadecimal''')

escolha = int(input('Escolha a opção que você quer converter: '))

if escolha == 1:
    print(f'{numero} em Binário é:', bin(numero)[2:])
elif escolha == 2:
    print(f'{numero} em Octal é:', oct(numero)[2:])
elif escolha == 3:
    print(f'{numero} em hexadecimal é:', hex(numero)[2:])
else: 
    print('Escolha inválida, não existe a opção escolha {escolha}}!')