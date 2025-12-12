valor_da_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos_pagamento = int(input('Em quantos anos quer pagar? '))

meses_pagamento = anos_pagamento * 12
prestacao = valor_da_casa / meses_pagamento

if (prestacao) > salario * 0.30:
    print('EMPRÉSTIMO NEGADO! \nA prestação excedeu 30% do seu salário!')
else: 
    print(f'EMPRÉSTIMO APROVADO! \nVocê vai pagar {prestacao:.2f}R$ todo mês! Por {anos_pagamento} anos!')