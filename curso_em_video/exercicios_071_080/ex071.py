print('------ Caixa Eletrônico ------')

qntd_saque = int(input('Digite quanto quer sacar: '))
cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

while True: 
    if qntd_saque >= 50:
        qntd_saque -= 50
        cedula_50 += 1   
        
    elif qntd_saque > 20:
        qntd_saque -= 20
        cedula_20 += 1
        
    elif qntd_saque > 10:
        qntd_saque -= 10
        cedula_10 += 1
    
    elif qntd_saque >= 1:
        qntd_saque -= 1
        cedula_1 += 1
    
    else:
        break 
    
print(f'Notas de 50: {cedula_50}')
print(f'Notas de 20: {cedula_20}')
print(f'Notas de 10: {cedula_10}')
print(f'Notas de 1: {cedula_1}') 