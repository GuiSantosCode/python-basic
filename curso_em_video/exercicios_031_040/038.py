print('------ Número maior, menor ou igual! ------')

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

print(f'Suas escolhas foram subsequentemente, {num1} e {num2}.')

if num1 > num2:
    print(f'E obviamente o {num1} é maior!')
elif num1 < num2:
    print(f'E obviamente o {num2} é maior!')
else:
    print(f'E obviamente não tem número maior!')