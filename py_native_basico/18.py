print('Exercício 18: Verifique se um determinado ano é bissexto.')

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bisexto!')
        else: 
            print(f'O ano {ano} não é bisexto!')
    else: 
        print(f'O ano {ano} é bisexto!')
else: 
    print(f'O ano {ano} não é bisexto!')