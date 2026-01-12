print('------ Flag: ex04 ------')

while True:
    multiplicador = 1
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    
    print('-' * 20)
    while multiplicador <= 10:
        print(f'{numero:2} X {multiplicador:2} = {numero*multiplicador:3}')
        multiplicador += 1    
    print('-' * 20)
    
print('Números negativos encerram o programa!')