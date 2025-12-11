print('------ Calculadora Básica +-*/ ------')

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print('''\n1 = Soma
2 = Subtração
3 = Multiplicação
4 = Divisão
Escolha outro número pra encerrar o programa!
''')

while True:

    escolha = int(input('Escolha uma opção: '))

    if escolha >= 1 and escolha <= 4:
        num1 = float(input('Escolha o primeiro número: '))
        num2 = float(input('Escolha outro número: '))

        if escolha == 1:    
            print(f'{num1} + {num2} =', soma(num1, num2))
        elif escolha == 2:
            print(f'{num1} - {num2} =', subtracao(num1, num2))
        elif escolha == 3:
            print(f'{num1} * {num2} =' , multiplicacao(num1, num2))
        elif escolha == 4:
            print(f'{num1} / {num2} =', divisao(num1, num2))
        else:
            print('Número inválido!')
    else:
        print('Programa finalizado!')
        break