print('--- Divisão Segura ---')

def divisao_segura():
    while True:
        try:
            a = float(input('Digite um número: '))
            b = float(input('Digite outro número: '))
            resultado = a / b
        except ValueError:
            print('Você precisa digitar um número!')
        except ZeroDivisionError:
            print('Um número não pode ser divido por zero!')
        else:
            return resultado

print(divisao_segura())