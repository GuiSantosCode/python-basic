print('------ Menu aritmético ------')

escolha_menu = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print('''
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
''')

while escolha_menu != 5:
    escolha_menu = int(input('Escolha uma opção: '))
    if escolha_menu == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif escolha_menu == 2:
        multiplicacao = num1 * num2
        print(f'{num1} X {num2} = {multiplicacao}')
    elif escolha_menu == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else: 
            print(f'{num2} é maior que {num1}')
    elif escolha_menu == 4:
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite outro novo número: '))
    elif escolha_menu == 5: 
        print('Programa encerrado!')
    else: 
        print('Valor inválido')