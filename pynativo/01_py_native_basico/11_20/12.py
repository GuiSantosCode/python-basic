print('Exercício 12: Calcule o imposto de renda')

renda = float(input('Qual sua renda: '))

if renda < 10000:
    print('TAXA DE IMPOSTO = 0')
elif renda < 20000:
    imposto = (renda - 10000) * 0.10
    print(f'TAXA DE IMPOSTO = {imposto}')
else:
    imposto = (10000 * 0.10) + (renda - 20000) * 0.20
    print(f'TAXA DE IMPOSTO = {imposto}')