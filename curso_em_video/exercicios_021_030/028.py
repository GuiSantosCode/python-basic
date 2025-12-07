nome_receita = (input('É receita do que? '))
ingredientes = int(input('Quantos ingredientes vai usar? '))

receita = f'''
========================================================
            Receita de {nome_receita}
========================================================
'''

i = 0
while i < ingredientes:
    receita += '\n'
    receita += (input('Digite um ingrediente: '))
    i += 1 

print(receita)
print('')
