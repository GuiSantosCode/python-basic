# PROGRAMA PRINCIPAL    
import moeda

numero = float(input('Digite um número até 999 para fazermos operações: '))

print('OPERAÇÕES')
print('1 - Aumentar')
print('2 - Diminuir')
print('3 - Dobro')
print('4 - Metade')

resposta = str(input('Qual dessas operações você quer realizar? ')).lower().strip()

if resposta in '1234':
    if resposta == '1':
        print(f'{moeda.aumentar(numero)}')
    elif resposta == '2':
        print(f'{moeda.diminuir(numero)}')
    elif resposta == '3':
        print(f'{moeda.dobro(numero)}')
    elif resposta == '4':
        print(f'{moeda.metade(numero)}')
    print('Programa encerrado!')
else:
    print('Você digitou um valor errado e o programa irá encerrar!')