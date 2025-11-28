print('------ Aumento de 15% no salário! ------')

salario = float(input('Qual o seu salário? R$'))
novo_salario = (salario) + (salario * 0.15)
#novo_salario = salario * 1.15

print(f'Seu novo salário é: R${novo_salario:.2f}')