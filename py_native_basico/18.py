print('Exercício 18: Verifique se um determinado ano é bissexto.')

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('É bisexto!')
        else: 
            print()
    else: 
        print('É bisexto!')