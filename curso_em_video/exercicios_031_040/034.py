print('------ Aumento Salárial -----')

salario = float(input('Qual o salário do seu funcionário? '))

if salario > 1250:
    aumento = salario * 0.10
else: 
    aumento = salario * 0.15
    
salario_atual = salario + aumento
    
print(f'O aumento é de {aumento:.2f}R$')
print(f'O salário agora é {salario_atual:.2f}R$')