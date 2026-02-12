print('--- Fatorial ---')

def fatorial(numero, mostrar):
    if mostrar == 's':
        f = 1
        for i in range(numero, 0, -1):
            print(f'{f} x {i} =' , end=' ')
            f *= i
            print(f)
    else:
        f = 1
        for i in range(numero, 0, -1):
            f *= i
        print(f)
    

number = int(input('Quer fazer o fatorial de qual número? '))
show = str(input('Quer mostrar o preocesso de calculo [s/n]? ')).strip().lower()

fatorial(number, show)