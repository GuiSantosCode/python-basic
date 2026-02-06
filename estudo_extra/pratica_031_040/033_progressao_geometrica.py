print('------ Dobrando o salario todo dia, durante 31 dias ------')

dias = 1
salario = 1

while dias < 31:
    salario = salario * 2
    dias = dias + 1
    
print(f'Partindo de 1 real, o seu salário diário no fim do contrato seria {salario}')